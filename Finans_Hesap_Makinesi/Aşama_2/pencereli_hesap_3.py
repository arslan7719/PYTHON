""" Bu sürümde temizleme butonları eklenmiştir. """

# pencere oluşturma ve düzenleme.
from tkinter import *
import tkinter as tk 
pencere_1=tk.Tk()
pencere_1.geometry('550x400')#Bu kod Pencere boyuru ayarlıyor.
pencere_1.title("Finans Hesap aracı")# pencere başlığını değiştiriyor.

#komut fonksiyonları
def basitI(): 
        s1=float(Anapara.get())
        s2=float(Faiz_oranı.get())
        s3=float(Süre.get())
        sonuc.configure(text=str(s1*(1+(s2*s3)))) 

def bilesikI():
        s1=float(Anapara.get())
        s2=float(Faiz_oranı.get())
        s3=float(Süre.get())
        sonuc.configure(text=str(s1*((1+s2)**s3)))

def basit_tahmin():
        s1=float(Anapara.get())
        s2=float(Faiz_oranı.get())
        s3=float(Süre.get())
        sonuc.configure(text=str(s1/(1+(s2*s3))))

def bilesik_tahmin():
        s1=float(Anapara.get())
        s2=float(Faiz_oranı.get())
        s3=float(Süre.get())
        sonuc.configure(text=str(s1/((1+s2)**s3)))

def Temizle_1 ():
        Anapara.delete(0,END)
def Temizle_2 ():
        Faiz_oranı.delete(0,END)
def Temizle_3 ():
        Süre.delete(0,END)
        


#Sonuç Çıkışı
sonuc = tk.Label(pencere_1,text="sonuc",font="Courier 16 bold",width=30,justify="center")
sonuc.place(x=50,y=20) # label'in pencere üzerinde göstemesini sağlar.

#Etiketler
ANAPARA= tk.Label(pencere_1,text="Anapara / Birikim ",font="Courier 14 bold")
ANAPARA.place(x=40,y=50)
FAIZ_ORANI=tk.Label(pencere_1,text="Faiz oranı",font="Courier 14 bold")
FAIZ_ORANI.place(x=70,y=85)
SURE=tk.Label(pencere_1,text="Süre",font="Courier 16 bold")
SURE.place(x=95,y=120)
# veri girişi
Anapara=tk.Entry(pencere_1,font="Courier 16 bold",width=15,justify="right")# veri girişi için label açar.
Anapara.place(x=250,y=50)
Faiz_oranı=tk.Entry(pencere_1,font="Courier 16 bold",width=15,justify="right")
Faiz_oranı.place(x=250,y=85)
Süre=tk.Entry(pencere_1,font="Courier 16 bold",width=15,justify="right")
Süre.place(x=250,y=120)


# buton oluşturma
btn=Button(pencere_1,text="Basit Faiz",width=10,height=7,background="#bfdc88",bd=2,command=basitI)
btn.place(x=120,y=170)#butonun pencerede gözükmesini sağlıyor.

btn2=Button(pencere_1,text="Bileşik Faiz",width=10,height=7,background="#88badc",bd=2,command=bilesikI)
btn2.place(x=220,y=170) 

btn3= Button(pencere_1,text="Basit Tahmin",width=10,height=3,background="red",bd=2,command=basit_tahmin)
btn3.place(x=320,y=170)

btn4=Button(pencere_1,text="Bileşik Tahmin",width=10,height=3,background="lightblue",bd=2,command=bilesik_tahmin)
btn4.place(x=320,y=230)

Tem_btn=Button(pencere_1,text="Temizle",command=Temizle_1,font="Courier 10 bold")
Tem_btn.place(x=460,y=50)
Tem_btn1=Button(pencere_1,text="Temizle",command=Temizle_2,font="Courier 10 bold")
Tem_btn1.place(x=460,y=85)
Tem_btn2=Button(pencere_1,text="Temizle",command=Temizle_3,font="Courier 10 bold")
Tem_btn2.place(x=460,y=120)

# mainloop hep en sonda dönmesi gerekiyor.
pencere_1.mainloop()