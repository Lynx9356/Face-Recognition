import csv
import datetime
import time
import Yüz_Yakala
import Egitme
import Tanıma_tanımlama
import tkinter
from tkinter import messagebox as messbox, ttk


def Cikis():
    if messbox.askyesno("Önemli", "Çıkış yapmak istediğinize emin misiniz?"):
        tk.destroy()

def Yuz_Yakala():
    x=line.get()
    y=line2.get()
    Yüz_Yakala.fotoAl(x,y)
    messbox.showinfo('Mesaj','Kaydetme Tamalandı')

def Yuz_Egit():
    Egitme.fotoEgitme()
    messbox.showinfo('Mesaj','Eğitme Tamalandı')

def Yuz_tanimla():
    Tanıma_tanımlama.ogrenci_tani()
    ts = time.time()
    gun = datetime.datetime.fromtimestamp(ts).strftime('%d-%m-%Y')
    i=0
    with open("C:/Users/celil/Desktop/Notlar ve Belgeler/Bitirme Projesi/Ogrenci/Ogrenci_"+ gun + ".csv", 'r') as csvFile1:
        reader1 = csv.reader(csvFile1)
        for lines in reader1:
            i = i + 1
            if (i > 1):
                if (i % 2 != 0):
                    iidd = str(lines[0]) + '   '
                    tb.insert('', 0, text=iidd, values=(str(lines[1]), str(lines[2]), str(lines[3])))
    csvFile1.close()


tk=tkinter.Tk()
tk.title("Yüz Tanıma Sistemi")
tk.geometry("1280x650")
tk.configure(background='#696969')




#Sol bölme----------------------------
bolme1=tkinter.Frame(tk,bg="white")
bolme1.place(relx=0.1,rely=0.1,relwidth=0.39,relheight=0.80)
#Sağ bölme-----------------------------
bolme2=tkinter.Frame(tk,bg="white")
bolme2.place(relx=0.51, rely=0.1, relwidth=0.39, relheight=0.80)

#Sol bölme başlık--------------------------------
bol_baslik1=tkinter.Label(bolme1,text="Yeni Öğrenci Ekleme",fg="red",bg="yellow",font=('times',17,'bold'))
bol_baslik1.place(x=0,y=0,relwidth=1)
#sağ bölme başlık-------------------------------
bol_baslik2=tkinter.Label(bolme2,text="Öğrenci Tanımlama",fg="red",bg="yellow",font=('times',17,'bold'))
bol_baslik2.place(x=0,y=0,relwidth=1)

#Yazı Yazma Yerleri(Sol)----------------------------------
label=tkinter.Label(bolme1,text="Numara",width=15,height=1,fg="black",bg="white",font=('times',17,'bold'))
label.place(x=0,y=55)

line=tkinter.Entry(bolme1,width=32,fg="black",bg="#e1f2f2",highlightcolor="red",highlightthickness=3,font=('times',15,'bold'))
line.place(x=55,y=88,relwidth=0.75)

label2=tkinter.Label(bolme1,text="İsim",width=12,fg="black",bg="white",font=('times',17,'bold'))
label2.place(x=0,y=140)

line2=tkinter.Entry(bolme1,width=32,fg="black",bg="#e1f2f2",highlightcolor="red",highlightthickness=3,font=('times',15,'bold'))
line2.place(x=55,y=173,relwidth=0.75)

#Butonlar---------------------------------------------
fotoAl=tkinter.Button(bolme1,text="Yeni kişi",command=Yuz_Yakala,fg="black",bg="#00aeff",width=34,height=1,activebackground="white",font=('times',16,'bold'))
fotoAl.place(x=30,y=280,relwidth=0.89)

fotoEgit=tkinter.Button(bolme1,text="Eğit Ve Kaydet",command=Yuz_Egit,fg="black",bg="#00aeff",width=34,height=1,activebackground="white",font=('times',16,'bold'))
fotoEgit.place(x=30,y=380,relwidth=0.89)

fotoEgit2=tkinter.Button(bolme2,text="Öğrenci Giriş",command=Yuz_tanimla,fg="black",bg="#00aeff",width=34,height=1,activebackground="white",font=('times',16,'bold'))
fotoEgit2.place(x=30,y=60,relwidth=0.89)

#Tablo---------------------------------------------------
style=ttk.Style()
style.configure("mystyle.Treeview",highlightthickness=0,bd=0,font=('Calibri',11))
style.configure("mystyle.Treeview.Heading",font=('times',13,'bold'))
style.layout("mystyle.Treeview",[('mystyle.Treeview.treearea',{'sticky':'nswe'})])
tb=ttk.Treeview(bolme2,height=13,columns=('name','date','time'),style="mystyle.Treeview")
tb.column('#0',width=82)
tb.column('name',width=130)
tb.column('date',width=133)
tb.column('time',width=133)
tb.grid(row=2,column=0,padx=(0,0),pady=(150,0),columnspan=4)
tb.heading('#0',text ='Numara')
tb.heading('name',text ='İsim')
tb.heading('date',text ='Gün')
tb.heading('time',text ='Zaman')

scroll=ttk.Scrollbar(bolme2,orient='vertical',command=tb.yview)
scroll.grid(row=2,column=4,padx=(0,100),pady=(150,0),sticky='ns')
tb.configure(yscrollcommand=scroll.set)


tk.protocol("WM_DELETE_WINDOW",Cikis)
tk.mainloop()

