import datetime
import os
import time
import cv2
import pandas as pd


def ogrenci_tani():
    tespit=cv2.face.LBPHFaceRecognizer_create()
    tespit.read("FotolarLabel"+os.sep+"Trainner.yml")
    harcascadeYol="haarcascade_frontalface_default.xml"
    faceCascade=cv2.CascadeClassifier(harcascadeYol)
    df=pd.read_csv("OgrenciDetay"+os.sep+"OgrenciDetay.csv")
    font=cv2.FONT_HERSHEY_SIMPLEX
    col_isim=['Numara','Isim','Gun','Zaman']
    ogrenci=pd.DataFrame(columns=col_isim)

    # canlı görüntü yakala işlemi
    cam=cv2.VideoCapture(0,cv2.CAP_DSHOW)
    cam.set(10,800)
    cam.set(10,600)
    #Tanınan yüz için pencere boyutu ayarlama
    minW=0.5*cam.get(10)
    minH=0.5*cam.get(10)

    while True: #Video akışındaki her kare işlemeyi gerçekleştirmek için sonsuz bir döngü başlatır
        ret,im=cam.read()
        gray=cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
        # facecascade nesnesini kullanıp tüz tespiti eder ve detectmultiscale kullanarak yapılır
        yuzler=faceCascade.detectMultiScale(gray,1.2,5,minSize=(int(minW),int(minH)),flags=cv2.CASCADE_SCALE_IMAGE)
        for(x,y,w,h) in yuzler:
            h+=50
            # tespit edilen her yüz için dikdörtgen çizer ve recognizer nesnesini kullanarak kimliğini tahmin eder
            cv2.rectangle(im,(x,y),(x+w,y+h),(10,255,255),2)
            Id,conf=tespit.predict(gray[y:y+h, x:x+w])
            # tahmini yüzdesi hesaplama
            if conf<100:    #conf değeri tahmin yüzdesidir ne kadar düşük değer gelirse o kadar iyi tahmin eder
                aa=df.loc[df['numara'] == Id]['isim'].values #aa ise isimi numaradan ayırıp kaydedilen değişken
                confstr="{0}%".format(round(100 - conf))  #ekrana yazılabilmesi için yüzdelik değere dönüştürülüyor
                tt=str(Id)+"-"+aa  ##tt ise ekrandaki çerçevenin üstünde bulunan numara ve isim göstermek için birleştirilen değişken
            else:
                Id='Tanımadı'
                tt = str(Id)
                confstr="{0}%".format(round(100 - conf))
            # tahmin yüzdesi %75 den yüksekse kişinin bilgileri ve tarih ve devam zamanını içeren girdi attendance içine yüklenir
            if (100-conf)>50:
                ts=time.time()
                gun=datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d')
                timeStamp=datetime.datetime.fromtimestamp(ts).strftime('%H:%M:%S')
                aa=str(aa)[2:-2] #baştaki ve sondaki 2 şeyi çıkartıp içerideki veriyi temizlemek için kullanılır
                ogrenci.loc[len(ogrenci)]=[str(Id),aa,str(gun),str(timeStamp)]


            # tespit edilen yüzlerle birlikte kareyi gösterir isimlerinin yanına doğruluk scorlarını yazar
            tt=str(tt)[2:-2]
            if(100-conf)>75:
                tt=tt+"[Tanimli]"
                cv2.putText(im,str(tt),(x+10,y-10),font,1,(255,255,255),2)
            else:
                cv2.putText(im,str(tt),(x+10,y-10),font,1,(255,255,255),2)

            if (100-conf)>75:
                cv2.putText(im,str(confstr),(x+10,y+h-5),font,1,(0,255,0),1)
            elif (100-conf)>60:
                cv2.putText(im,str(confstr),(x+10,y+h-5),font,1,(0,255,255),1)
            else:
                cv2.putText(im,str(confstr),(x+10,y+h-5),font,1,(0,0,255),1)

        ogrenci=ogrenci.drop_duplicates(subset=['Id'], keep='first')
        cv2.imshow('Ogrenci',im)
        if (cv2.waitKey(1) == ord('q')):
            break
    # geçerli zamanı kaydetme
    ts=time.time()
    gun=datetime.datetime.fromtimestamp(ts).strftime('%d-%m-%Y')# yıl ay gün
    #csv dosyasına kaydetme
    dosyaAdi="Ogrenci"+os.sep+"Ogrenci_"+gun+".csv"
    ogrenci.to_csv(dosyaAdi, index=False)
    cam.release()
    cv2.destroyAllWindows()