#Herkese Merhaba 4. kod bloğumuzda finans hesap makinemiz üzerinde sadece tasarımsal değişiklik yapılmıştır.
#tasarımı bilgisayar sistemine entegre haline getirerek daha yumuşak hatlara sahip olmasını sağlamış oldum.
#kodları çalıştırmadan önce cmd'yi açın ve konsola -pip install customtkinter yazın ve enter'layın bu komut indirme işlemi başlatacaktır,
#daha sonra aynı yere -pip install Pillow yazın ve enter'layın bu kütüphane indikten sonra kodları çalıştırabilirsiniz.

#(.exe uzantılı dosya haline getirildiğinde program hata veriyor bir sonraki adımda bu sorunu ortadan kaldırmaya çalışacağım.)

# pencere oluşturma ve düzenleme.
from tkinter import *
import tkinter as tk 
import customtkinter 
from PIL import Image,ImageTk

customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("dark-blue")


pencere_1=customtkinter.CTk()
pencere_1.geometry('450x300')#Bu kod Pencere boyuru ayarlıyor.
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
sonuc=customtkinter.CTkLabel(master=pencere_1,text="Sonuç",
                             font=customtkinter.CTkFont(family="Courier bold",size=26),width=30,
                             anchor="center") 
sonuc.place(x=220,y=15) # label'in pencere üzerinde göstemesini sağlar.
#Customurtkinter bize panel taasrımı sağlıyor aslında sistem ile aynı tasarıma geçiyor.

#Etiketler
ANAPARA=customtkinter.CTkLabel(master=pencere_1,text="Anapara / Birikim",
                               font=customtkinter.CTkFont(family="Courier bold",size=16))
ANAPARA.place(x=40,y=50)
FAIZ_ORANI=customtkinter.CTkLabel(master=pencere_1,text="Faiz oranı",
                                  font=customtkinter.CTkFont(family="Courier bold",size=16))
FAIZ_ORANI.place(x=70,y=85)
SURE=customtkinter.CTkLabel(master=pencere_1,text="Süre",
                            font=customtkinter.CTkFont(family="Courier bold",size=16))
SURE.place(x=95,y=120)
# veri girişi
Anapara=customtkinter.CTkEntry(master=pencere_1,width=100,height=10,
                               font=customtkinter.CTkFont(family="Courier bold",size=16))
# veri girişi için label açar.
Anapara.place(x=180,y=50)
Faiz_oranı=customtkinter.CTkEntry(master=pencere_1,width=100,height=10,
                                  font=customtkinter.CTkFont(family="Courier bold",size=16))
Faiz_oranı.place(x=180,y=85)
Süre=customtkinter.CTkEntry(master=pencere_1,width=100,height=10,
                            font=customtkinter.CTkFont(family="Courier bold",size=16))
Süre.place(x=180,y=120)


# buton oluşturma
Btn=customtkinter.CTkButton(master=pencere_1,text="Basit Faiz",width=90,height=7,compound="left",
                                  command=basitI)
Btn.place(x=120,y=170)#butonun pencerede gözükmesini sağlıyor.
btn2=customtkinter.CTkButton(master=pencere_1,text="Bileşik Faiz",width=90,height=7,compound="right",
                             command=bilesikI)
btn2.place(x=120,y=200) 
btn3=customtkinter.CTkButton(master=pencere_1,text="Basit tahmin",width=90,height=3,
                             command=basit_tahmin)
btn3.place(x=220,y=170)
btn4=customtkinter.CTkButton(master=pencere_1,text="Bileşik Tahmin",width=90,height=3,
                             command=bilesik_tahmin)
btn4.place(x=220,y=200)

Tem_btn=customtkinter.CTkButton(master=pencere_1,text="Temizle",width=90,height=7,command=Temizle_1)
Tem_btn.place(x=290,y=50)
Tem_btn1=customtkinter.CTkButton(master=pencere_1,text="Temizle",width=90,height=7,command=Temizle_2)
Tem_btn1.place(x=290,y=85)
Tem_btn2=customtkinter.CTkButton(master=pencere_1,text="Temizle",width=90,height=7,command=Temizle_3)
Tem_btn2.place(x=290,y=120)

# mainloop hep en sonda dönmesi gerekiyor.
pencere_1.mainloop()