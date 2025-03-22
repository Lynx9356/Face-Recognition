import os
import cv2
import numpy as np
from PIL import Image
from threading import Thread


def fotoAl(yol): #Klasordeki tüm dosyaları al
    fotoYol=[os.path.join(yol, f) for f in os.listdir(yol)]
    yuz=[]
    ids=[]
    for imageYol in fotoYol: #tüm görüntü yollarında loop yaparak kimlik ve görüntüleri yüklüyor
        pilFoto=Image.open(imageYol).convert('L') #"PIL" modülü, görüntülerin okunması, işlenmesi ve kaydedilmesi için kullanılan popüler bir Python kütüphanesidir
        fotoNp=np.array(pilFoto,'uint8') #numpy dizisine dönüştürülüyor uint8 ise fotoğraf piksellerinin 8 bitlik tamsayıları ifade eder(0 ile 255)
        id=int(os.path.split(imageYol)[-1].split(".")[1]) #bir görüntü yolundan dosya adını alır, dosya uzantısını ayırır ve
        # ardından uzantıyı tamsayıya dönüştürerek bir "id" değeri oluşturur.Bu "id" değeri, görüntüyle ilişkili bir kimlik veya indeks olarak kullanılır
        yuz.append(fotoNp)
        ids.append(id)
    return yuz,ids


def fotoEgitme():
    tanima=cv2.face_LBPHFaceRecognizer.create()
    harcascadeYol="haarcascade_frontalface_default.xml"
    tespit=cv2.CascadeClassifier(harcascadeYol)
    yuzler,id=fotoAl("Fotolar")
    Thread(target=tanima.train(yuzler,np.array(id))).start()# train işlemi başlama yeri
    #print("Tüm Fotolar Egitildi")
    tanima.save("FotolarLabel"+os.sep+"Trainner.yml")#.yml dosyası içinde yukarıdan gelen array sayıları var ve eğitilmiş yüzlerin verileri bulunuyor


