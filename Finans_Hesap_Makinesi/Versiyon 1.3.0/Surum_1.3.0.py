# pencere oluşturma ve düzenleme.
from tkinter import *
import tkinter as tk 
pencere_1=tk.Tk()
pencere_1.geometry('450x300')#Bu kod Pencere boyuru ayarlıyor.
pencere_1.title("Finans Hesap aracı")# pencere başlığını değiştiriyor.
pencere_1.configure(background="#85bfcd")
bg=PhotoImage(file="stat.png")
png=Label(pencere_1,image=bg,background="#85bfcd")
png.place(x=40,y=150)

#komut fonksiyonları
def aclis_1():
        pencere_2=Toplevel()
        pencere_2.geometry("450x300")

        def basitI(): 
                s1=float(Anapara.get())
                s2=float(Faiz_oranı.get())
                s3=float(Süre.get())
                sonuc.configure(text=str(s1*(1+(s2*s3)))) 
             
        def basit_tahmin():
                s1=float(Anapara.get())
                s2=float(Faiz_oranı.get())
                s3=float(Süre.get())
                sonuc.configure(text=str(s1/(1+(s2*s3))))
                
        def Temizle_1 ():
                Anapara.delete(0,END)
        def Temizle_2 ():
                Faiz_oranı.delete(0,END)
        def Temizle_3 ():
                Süre.delete(0,END)
        
        #sonuç etiketi
        sonuc = tk.Label(pencere_2,text="sonuc",font="Courier 16 bold",width=30,justify="center")
        sonuc.place(x=50,y=20) # label'in pencere üzerinde göstemesini sağlar.

        #etiket
        ANAPARA= tk.Label(pencere_2,text="Anapara / Birikim ",font="Courier 10 bold")
        ANAPARA.place(x=40,y=50)
        FAIZ_ORANI=tk.Label(pencere_2,text="Faiz oranı",font="Courier 10 bold")
        FAIZ_ORANI.place(x=70,y=85)
        SURE=tk.Label(pencere_2,text="Süre",font="Courier 12 bold")
        SURE.place(x=85,y=120)
        """ DEPOSİTO=tk.Label(pencere_2,text="Depozito",font="Courier 12 bold")
        DEPOSİTO.place(x=210,y=120) """

        #veri girişi
        Anapara=tk.Entry(pencere_2,font="Courier 16 bold",width=8,justify="right")# veri girişi için label açar.
        Anapara.place(x=200,y=50)
        Faiz_oranı=tk.Entry(pencere_2,font="Courier 16 bold",width=8,justify="right")
        Faiz_oranı.place(x=200,y=85)
        Süre=tk.Entry(pencere_2,font="Courier 16 bold",width=8,justify="right")
        Süre.place(x=200,y=120)

        #butonlar
        btn=Button(pencere_2,text="Basit Faiz",width=10,height=7,background="#bfdc88",bd=2,command=basitI)
        btn.place(x=120,y=170)#butonun pencerede gözükmesini sağlıyor.

        btn3= Button(pencere_2,text="Basit Tahmin",width=10,height=7,background="red",bd=2,command=basit_tahmin)
        btn3.place(x=220,y=170)

        #temizlik butonları
        Tem_btn=Button(pencere_2,text="Temizle",command=Temizle_1,font="Courier 10 bold")
        Tem_btn.place(x=320,y=50)
        Tem_btn1=Button(pencere_2,text="Temizle",command=Temizle_2,font="Courier 10 bold")
        Tem_btn1.place(x=320,y=85)
        Tem_btn2=Button(pencere_2,text="Temizle",command=Temizle_3,font="Courier 10 bold")
        Tem_btn2.place(x=320,y=120)
      

def acilis_2():
        pencere_3=Toplevel()
        pencere_3.geometry("450x300")
        
        def bilesikI():
                s1=float(Anapara.get())
                s2=float(Faiz_oranı.get())
                s3=float(Süre.get())
                sonuc.configure(text=str(s1*((1+s2)**s3)))

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

        #sonuç etiketi
        sonuc = tk.Label(pencere_3,text="sonuc",font="Courier 16 bold",width=30,justify="center")
        sonuc.place(x=50,y=20) # label'in pencere üzerinde göstemesini sağlar.

        #etiket
        ANAPARA= tk.Label(pencere_3,text="Anapara / Birikim ",font="Courier 10 bold")
        ANAPARA.place(x=40,y=50)
        FAIZ_ORANI=tk.Label(pencere_3,text="Faiz oranı",font="Courier 10 bold")
        FAIZ_ORANI.place(x=70,y=85)
        SURE=tk.Label(pencere_3,text="Süre",font="Courier 12 bold")
        SURE.place(x=85,y=120)
        """ DEPOSİTO=tk.Label(pencere_2,text="Depozito",font="Courier 12 bold")
        DEPOSİTO.place(x=210,y=120) """

        #veri girişi
        Anapara=tk.Entry(pencere_3,font="Courier 16 bold",width=8,justify="right")# veri girişi için label açar.
        Anapara.place(x=200,y=50)
        Faiz_oranı=tk.Entry(pencere_3,font="Courier 16 bold",width=8,justify="right")
        Faiz_oranı.place(x=200,y=85)
        Süre=tk.Entry(pencere_3,font="Courier 16 bold",width=8,justify="right")
        Süre.place(x=200,y=120)
        """ Deposit=tk.Entry(pencere_1,font="Courier 16 bold",width=4,justify="right")
        Deposit.place(x=320,y=120)"""

        #butonlar
        btn2=Button(pencere_3,text="Bileşik Faiz",width=10,height=7,background="#88badc",bd=2,command=bilesikI)
        btn2.place(x=220,y=170) 

        btn4=Button(pencere_3,text="Bileşik Tahmin",width=10,height=7,background="lightblue",bd=2,command=bilesik_tahmin)
        btn4.place(x=320,y=170)

        #temizlik butonları
        Tem_btn=Button(pencere_3,text="Temizle",command=Temizle_1,font="Courier 10 bold")
        Tem_btn.place(x=320,y=50)
        Tem_btn1=Button(pencere_3,text="Temizle",command=Temizle_2,font="Courier 10 bold")
        Tem_btn1.place(x=320,y=85)
        Tem_btn2=Button(pencere_3,text="Temizle",command=Temizle_3,font="Courier 10 bold")
        Tem_btn2.place(x=320,y=120)
 
#Ana pencere etkileşimi
#etiketler
baslik=tk.Label(pencere_1,text="Yapmak istediğiniz işlemi seçiniz.",background="#85bfcd",font="Courier 14 bold")
baslik.place(x=40,y=50)
#butınlar
btn_k=Button(pencere_1,text="Birikim işlemleri",width=15,height=3,command=aclis_1 )
btn_k.place(x=100,y=80)

btn_k2=Button(pencere_1,text="Peşinat işlemleri",width=15,height=3,command=acilis_2)
btn_k2.place(x=220,y=80)


# mainloop hep en sonda dönmesi gerekiyor.
pencere_1.mainloop()