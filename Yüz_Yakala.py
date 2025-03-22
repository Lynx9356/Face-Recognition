import os
import cv2
import csv


def fotoAl(id,name):
    cam=cv2.VideoCapture(0)
    harcascadeYol="haarcascade_frontalface_default.xml"
    tespit=cv2.CascadeClassifier(harcascadeYol)
    ornekNum=0



    while True: #kamera tespit
        ret,img=cam.read()
        gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) # görüntü grileştirme
        yuzler=tespit.detectMultiScale(gray,1.3,5,minSize=(50,50),flags=cv2.CASCADE_SCALE_IMAGE) #yüz tespit
        for (x,y,w,h) in yuzler:
            cv2.rectangle(img,(x,y),(x+w,y+h),(10,255,255),2)
            ornekNum=ornekNum+1 #numara arttırma
            cv2.imwrite("Fotolar"+os.sep+name+"."+id+'.'+str(ornekNum)+".jpg",gray[y:y+h,x:x+w]) # foto katdetme
        cv2.imshow('frame',img) # ekrana gösterme
        if cv2.waitKey(100)&0xFF==ord('q'):
            break
        elif ornekNum>=300: #sample number 300 den büyük olunca durdur
            break

    cam.release()
    cv2.destroyAllWindows()
    Aa=[id,name]
    with open("OgrenciDetay"+os.sep+"OgrenciDetay.csv",'a+') as csvFile: #csv file kaydetme
        writer=csv.writer(csvFile)
        writer.writerow(Aa)
    csvFile.close()


