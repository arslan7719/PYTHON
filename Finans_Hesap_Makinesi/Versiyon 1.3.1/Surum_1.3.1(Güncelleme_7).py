# pencere oluşturma ve düzenleme.
from tkinter import *
import tkinter as tk 
import customtkinter
from customtkinter import *
from tkinter import messagebox # değerlendirilecek
from dash import dcc #?

customtkinter.set_appearance_mode("system")
customtkinter.set_default_color_theme("dark-blue")

pencere_1=tk.Tk()
pencere_1.geometry('450x300')#Bu kod Pencere boyuru ayarlıyor.
pencere_1.title("Finans Hesap aracı")# pencere başlığını değiştiriyor.
pencere_1.configure(background="#85bfcd")
bg=PhotoImage(file="stat.png")
png=Label(pencere_1,image=bg,background="#85bfcd")
png.place(x=40,y=150)


#komut fonksiyonları
def aclis_1(): # bu pencereler başlangıç pencereleri idi düzenleme yapılacak.
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

        def iskonto():
                s1=float(Anapara.get())
                s4=float(iskont.get())
                s3=float(Süre.get())
                sonuc.configure(text=str(s1*((1-s4)**(1/s3))))
                
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
        iskont=tk.Entry(pencere_2,font="Courier 16 bold",width=8,justify="right")
        iskont.place(x=330,y=50)

        #butonlar
        btn=Button(pencere_2,text="Basit Faiz",width=10,height=7,background="#bfdc88",bd=2,command=basitI)
        btn.place(x=120,y=170)#butonun pencerede gözükmesini sağlıyor.

        btn3= Button(pencere_2,text="Basit Tahmin",width=10,height=7,background="red",bd=2,command=basit_tahmin)
        btn3.place(x=220,y=170)

        btn4=Button(pencere_2,text="İskonto bul",width=10,height=7,bd=2,command=iskonto)
        btn4.place(x=320,y=170)

        #temizlik butonları
        """ Tem_btn=Button(pencere_2,text="Temizle",command=Temizle_1,font="Courier 10 bold")
        Tem_btn.place(x=320,y=50)
        Tem_btn1=Button(pencere_2,text="Temizle",command=Temizle_2,font="Courier 10 bold")
        Tem_btn1.place(x=320,y=85)
        Tem_btn2=Button(pencere_2,text="Temizle",command=Temizle_3,font="Courier 10 bold")
        Tem_btn2.place(x=320,y=120)
       """

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

def Basit_faizlendirme_peşinat(): # Aklımdaki Tasarım Tam Anlamı ile gerçekleşti Yavaş yavaş kodlayıp github'a atıcağım.
        pencere_4=Toplevel()
        pencere_4.geometry("450x300")
        pencere_4.title("Basit Faizlendirme İşlemi")
        pencere_4.configure(background="#85bfcd")

        # Fonksiyon tanımlama 
        def Basit_Fazilendirme():
                s1=float(Birikim.get())
                s2=float(Zaman.get())
                s3=float(Faiz_Orani.get())
                sonuc.configure(text=str(s1*((1+s2*s3)**(-1))))
        
        def temizle():
                Birikim.delete(0,END)
                Zaman.delete(0,END)
                Faiz_Orani.delete(0,END)
                
        #Çıktı etiketi hazırlancak
        sonuc = tk.Label(pencere_4,text="Sonuç",font="Courier 16 bold",bg="#85bfcd",width=30,justify="center")
        sonuc.place(x=30,y=200)

        #Etiketler hazırlancak
        etiket_Birikim=tk.Label(pencere_4,text="Birikim : ",font="Courier 10 bold",bg="#85bfcd")
        etiket_Zaman=tk.Label(pencere_4,text="Zaman : ",font="Courier 10 bold",bg="#85bfcd")
        etiket_Faiz=tk.Label(pencere_4,text="Faiz Oranı : ",font="Courier 10 bold",bg="#85bfcd")
        etiket_Birikim.place(x=40,y=50)
        etiket_Zaman.place(x=55,y=85)
        etiket_Faiz.place(x=15,y=115)

        #Veri girişi
        Birikim=tk.Entry(pencere_4,font="Courier 16 bold",width=10,justify="center")
        Zaman=tk.Entry(pencere_4,font="Courier 16 bold",width=10,justify="center")
        Faiz_Orani=tk.Entry(pencere_4,font="Courier 16 bold",width=10,justify="center")
        Birikim.place(x=120,y=50)
        Zaman.place(x=120,y=80)
        Faiz_Orani.place(x=120,y=110)

        #Butonlar (temizleme ve hesaplama olacak şekilde iki tane)
        Hesapla=Button(pencere_4,text="Hesapla",command=Basit_Fazilendirme,font="Courier 10 bold")
        Temizle=Button(pencere_4,text="Temizle",command=temizle,font="Courier 10 bold")
        Hesapla.place(x=280,y=50)
        Temizle.place(x=280,y=80)

def Bilesik_Faizlendirme_islemi():
        pencere_5=Toplevel()
        pencere_5.geometry("450x300")
        pencere_5.title("Bileşik Faiz İşlemi")
        pencere_5.configure(bg="#85bfcd")
        # Fonksin tanımlama
        def Bilesik_Faizlendirme():
                s1=float(Vr_birikim.get())
                s2=float(Vr_Faiz.get())
                s3=float(Vr_zaman.get())
                sonuc.configure(text=str(s1*((1+s2)**(s3))))
        
        def Temizlik():
                Vr_Faiz.delete(0,END)
                Vr_birikim.delete(0,END)
                Vr_zaman.delete(0,END)
        
        #Cıktı Tanımlama
        sonuc=tk.Label(pencere_5,text="Sonuç",font="Courier 16 bold",bg="#85bfcd")
        sonuc.place(x=180,y=200)
        #Etiketler
        Etiket_Birikim=tk.Label(pencere_5,text="Birikim : ",font="Courier 10 bold",bg="#85bfcd",fg="red")
        Etiket_Faiz=tk.Label(pencere_5,text="Faiz Oranı : ",font="Courier 10 bold",bg="#85bfcd")
        Etiket_Zaman=tk.Label(pencere_5,text="Zaman : ",font="Courier 10 bold",bg="#85bfcd")
        Etiket_Birikim.place(x=55,y=50)
        Etiket_Faiz.place(x=30,y=80)
        Etiket_Zaman.place(x=70,y=115)
        #Veri Girişi
        Vr_birikim=tk.Entry(pencere_5,font="Courier 16 bold",width=10,justify="center")
        Vr_Faiz=tk.Entry(pencere_5,font="Courier 16 bold",width=10,justify="center")
        Vr_zaman=tk.Entry(pencere_5,font="Courier 16 bold",width=10,justify="center")
        Vr_birikim.place(x=140,y=50)
        Vr_Faiz.place(x=140,y=80)
        Vr_zaman.place(x=140,y=110)
        #Butonlar
        Hesapla=Button(pencere_5,text="Hesapla",font="Courier 10 bold",command=Bilesik_Faizlendirme)
        Temizle=Button(pencere_5,text="Temizle",font="Courier 10 bold",command=Temizlik)
        Hesapla.place(x=280,y=50)
        Temizle.place(x=280,y=80)    

def Iskonto_Orani_Basit_islemi():
        pencere_6=Toplevel()
        pencere_6.geometry("450x300")
        pencere_6.title("İskonto Oranı İşlemi (Basit)")
        pencere_6.configure(bg="#85bfcd")
        # Fonksiyon Atama
        def iskonto_Orani_Basit():
                s1=float(Vr_1_Pesinat.get())
                s2=float(Vr_1_Zaman.get())
                s3=float(Vr_1_Pesinat.get())
                sonuc.configure(text=str(s1*(1-s2*s3)))
        
        def Temizlik():
                Vr_1_Pesinat.delete(0,END)
                Vr_1_Zaman.delete(0,END)
                Vr_1_Iskonto.delete(0,END)
        
        #Çıktı Atama
        sonuc=tk.Label(pencere_6,text="Sonuç",font="Courier 16 bold",bg="#85bfcd")
        sonuc.place(x=180,y=200)
        #Etiket Atama
        Etiket_Pesinat=tk.Label(pencere_6,text="Peşinat :",font="Courier 10 bold",bg="#85bfcd")
        Etiket_Zaman=tk.Label(pencere_6,text="Zaman :",font="Courier 10 bold",bg="#85bfcd")
        Etiket_Iskonto=tk.Label(pencere_6,text="İskonto :",font="Courier 10 bold",bg="#85bfcd")
        Etiket_Pesinat.place(x=55,y=50)
        Etiket_Zaman.place(x=70,y=80)
        Etiket_Iskonto.place(x=55,y=115)
        #Veri Girişi Atama
        Vr_1_Pesinat=tk.Entry(pencere_6,font="Courier 16 bold",width=10,justify="center")
        Vr_1_Zaman=tk.Entry(pencere_6,font="Courier 16 bold",justify="center",width=10)
        Vr_1_Iskonto=tk.Entry(pencere_6,font="Courier 16 bold",justify="center",width=10)
        Vr_1_Pesinat.place(x=140,y=50)
        Vr_1_Zaman.place(x=140,y=80)
        Vr_1_Iskonto.place(x=140,y=110)
        #Buton(Hesapla ve Temizle)
        Temiz=Button(pencere_6,text="Temizle",font="Courier 10 bold",command=Temizlik)
        Hesap=Button(pencere_6,text="Hesapla",font="Courier 10 bold",command=iskonto_Orani_Basit)
        Hesap.place(x=280,y=50)
        Temiz.place(x=280,y=80)

def Iskonto_orani_bileşik_islemi():
        pencere_7=Toplevel()
        pencere_7.geometry("450x300")
        pencere_7.title("İskonto Oranı İşlemi (Bileşik)")
        pencere_7.configure(bg="#85bfcd")
        #Fonksiyonon atama
        def iskonto_Orani_Bilesik():
                s1=float(Vr_pesinat.get())
                s2=float(Vr_iskonto.get())
                s3=float(Vr_zaman.get())
                sonuc.configure(text=str(s1*((1-s2)**(s3))))

        def Temizlik():
                Vr_pesinat.delete(0,END)
                Vr_iskonto.delete(0,END)
                Vr_zaman.delete(0,END)      
        # Çıktı atama
        sonuc=tk.Label(pencere_7,text="Sonuç",font="Courier 16 bold",bg="#85bfcd")
        sonuc.place(x=180,y=200)
        #Etiket atama
        Etiket_pesinat=tk.Label(pencere_7,text="Peşinat :",font="Courier 10 bold",bg="#85bfcd")
        Etiket_Iskonto=tk.Label(pencere_7,text="İskonto :",font="Courier 10 bold",bg="#85bfcd")
        Etiket_zaman=tk.Label(pencere_7,text="Zaman :",font="Courier 10 bold",bg="#85BFCD")
        Etiket_pesinat.place(x=55,y=50)
        Etiket_Iskonto.place(x=55,y=80)
        Etiket_zaman.place(x=70,y=110)
        # veri girişi
        Vr_pesinat=tk.Entry(pencere_7,font="Courier 16 bold",justify="center",width=10)
        Vr_iskonto=tk.Entry(pencere_7,font="Courier 16 bold",justify="center",width=10)
        Vr_zaman=tk.Entry(pencere_7,font="Courier 16 bold",justify="center",width=10)
        Vr_pesinat.place(x=140,y=50)
        Vr_iskonto.place(x=140,y=80)
        Vr_zaman.place(x=140,y=110)
        #Butonlar (Hesapla ve Temizle)
        hesap=Button(pencere_7,text="Hesapla",font="Courier 10 bold",command=iskonto_Orani_Bilesik)
        temiz=Button(pencere_7,text="Temizle",font="Courier 10 bold",command=Temizlik)
        hesap.place(x=280,y=50)
        temiz.place(x=280,y=80)

def Sabit_anlik_faiz_islemi():
        pencere_8=Toplevel()
        pencere_8.geometry("450x300")
        pencere_8.title("Sabit Anlık Faiz İşlemi")
        pencere_8.configure(bg="#85bfcd")
        #Fonkisyon Atama
        def Sabit_Anlik_faiz_orani():
                s1=float(Vr_pesinat.get())
                s2=float(Vr_zaman.get())
                s3=float(Vr_faiz.get())
                s4=float(Vr_exp.get())
                sonuc.configure(text=str(s1*(s4**(s2*s3))))
        
        def Temizlik ():
                Vr_exp.delete(0,END)
                Vr_faiz.delete(0,END)
                Vr_pesinat.delete(0,END)
                Vr_zaman.delete(0,END)

        #Çıktı atama
        sonuc=tk.Label(pencere_8,text="Sonuç",font="Courier 16 bold",bg="#85bfcd")
        sonuc.place(x=180,y=200)
        #Etiket atama
        Etiket_pesinat=tk.Label(pencere_8,text="Birikim :",font="Courier 10 bold",bg="#85bfcd")
        Etiket_Zaman=tk.Label(pencere_8,text="Zaman :",font="Courier 10 bold",bg="#85bfcd")
        Etiket_Faiz_kuvveti=tk.Label(pencere_8,text="Faiz Kuvveti :",font="Courier 10 bold",bg="#85bfcd")
        Etiket_Exp=tk.Label(pencere_8,text="Exp. :",font="Courier 10 bold",bg="#85bfcd")
        Etiket_pesinat.place(x=75,y=50)
        Etiket_Zaman.place(x=90,y=80)
        Etiket_Faiz_kuvveti.place(x=35,y=110)
        Etiket_Exp.place(x=100,y=140)
        # Veri Girişleri
        Vr_pesinat=tk.Entry(pencere_8,font="Courier 16 bold",justify="center",width=10)
        Vr_zaman=tk.Entry(pencere_8,font="Courier 16 bold",justify="center",width=10)
        Vr_faiz=tk.Entry(pencere_8,font="Courier 16 bold",justify="center",width=10)
        Vr_exp=tk.Entry(pencere_8,font="Courier 16 bold",justify="center",width=10)
        Vr_pesinat.place(x=160,y=50)
        Vr_zaman.place(x=160,y=80)
        Vr_faiz.place(x=160,y=110)
        Vr_exp.place(x=160,y=140)

        # Butonlar
        hesap=Button(pencere_8,text="Hesapla",font="Courier 10 bold",command=Sabit_Anlik_faiz_orani)
        temiz=Button(pencere_8,text="Temizle",font="Courier 10 bold",command=Temizlik)
        hesap.place(x=300,y=50)
        temiz.place(x=300,y=80)


def Donem_sonu_duzenli_odeme_islemi():
        pencere_9=Toplevel()
        pencere_9.geometry("450x300")
        pencere_9.title("Dönem Sonu Düzenli Ödeme İşlemi")
        pencere_9.configure(bg="#85bfcd")
        #fonkisyon atama
        def donem_sonu_duzenli_odemeler_serisi():
                s1=float(Vr_tutar.get())
                s2=float(Vr_adet.get())
                s3=float(Vr_faiz.get())
                sonuc.configure(text=str(s1*((1-((1+s3)**(-s2)))/s3)))
        
        def Temizlik():
                Vr_adet.delete(0,END)
                Vr_faiz.delete(0,END)
                Vr_tutar.delete(0,END)
        #Çıktı 
        sonuc=tk.Label(pencere_9,text="Sonuç",font="Courier 16 bold",bg="#85bfcd")
        sonuc.place(x=180,y=200)
        #Etiketler
        Etiket_tutar=tk.Label(pencere_9,text="Ödeme Tutar :",font="Courier 10 bold",bg="#85bfcd")
        Etiket_adet=tk.Label(pencere_9,text="Ödeme adet :",font="Courier 10 bold",bg="#85bfcd")
        Etiket_faiz=tk.Label(pencere_9,text="Faiz oranı :",font="Courier 10 bold",bg="#85bfcd")
        Etiket_tutar.place(x=30,y=50)
        Etiket_adet.place(x=35,y=80)
        Etiket_faiz.place(x=35,y=110)
        #veri giriş
        Vr_tutar=tk.Entry(pencere_9,font="Courier 16 bold",justify="center",width=10)
        Vr_adet=tk.Entry(pencere_9,font="Courier 16 bold",justify="center",width=10)
        Vr_faiz=tk.Entry(pencere_9,font="Courier 16 bold",justify="center",width=10)
        Vr_tutar.place(x=140,y=50)
        Vr_adet.place(x=140,y=80)
        Vr_faiz.place(x=140,y=110)
        #Butonlar
        hesap=Button(pencere_9,font="Courier 10 bold",text="Hesapla",command=donem_sonu_duzenli_odemeler_serisi)
        temiz=Button(pencere_9,font="Courier 10 bold",text="Temizle",command=Temizlik)
        hesap.place(x=280,y=50)
        temiz.place(x=280,y=80)


def Donem_basi_duzenli_odemeler_islemi():
        pencere_10=Toplevel()
        pencere_10.geometry("450x300")
        pencere_10.title("Dönem Başı Düzenli Ödeme İşlemi")
        pencere_10.configure(bg="#85bfcd")
        #Fonkisiyon
        def donem_basi_duzenli_odemler_serisi():
                s1=float("ödeme tutari")
                s2=float("iskonto")
                s3=float("faiz")
                s4=float("ödeme adedi")
                sonuc.configure(text=str(s1*((1-((1+s3)**(-s4)))/s2)))
        
        def Temizlik():
                Vr_adet.delete(0,END)
                Vr_faiz.delete(0,END)
                Vr_iskonto.delete(0,END)
                Vr_tutar.delete(0,END)

        # Sonuç
        sonuc=tk.Label(pencere_10,text="Sonuç",font="Courier 16 bold",bg="#85bfcd")
        sonuc.place(x=180,y=200)

        #Etiket
        Etiket_tutar=tk.Label(pencere_10,text="Ödeme tutar :",font="Courier 10 bold",bg="#85bfcd")
        Etiket_iskonto=tk.Label(pencere_10,text="İskonto :",font="Courier 10 bold",bg="#85bfcd")
        Etiket_faiz=tk.Label(pencere_10,text="Faiz oran :",font="Courier 10 bold",bg="#85bfcd")
        Etiket_adet=tk.Label(pencere_10,text="Ödemi adet :",font="Courier 10 bold",bg="#85bfcd")
        Etiket_tutar.place(x=30,y=50)
        Etiket_iskonto.place(x=60,y=80)
        Etiket_faiz.place(x=45,y=110)
        Etiket_adet.place(x=35,y=140)
        # Veri Giriş
        Vr_tutar=tk.Entry(pencere_10,font="Courier 16 bold",width=10,justify="center")
        Vr_iskonto=tk.Entry(pencere_10,font="Courier 16 bold",width=10,justify="center")
        Vr_faiz=tk.Entry(pencere_10,font="Courier 16 bold",width=10,justify="center")
        Vr_adet=tk.Entry(pencere_10,font="Courier 16 bold",width=10,justify="center")
        Vr_tutar.place(x=140,y=50)
        Vr_iskonto.place(x=140,y=80)
        Vr_faiz.place(x=140,y=110)
        Vr_adet.place(x=140,y=140)

        #Buton
        hesap=Button(pencere_10,font="Courier 10 bold",text="Hesapla",command=donem_basi_duzenli_odemler_serisi)
        Temiz=Button(pencere_10,text="Temizle",font="Courier 10 bold",command=Temizlik)
        hesap.place(x=280,y=50)
        Temiz.place(x=280,y=80)

def Ertelemeli_donem_sonu_odeme_islemi():
        pencere_11=Toplevel()
        pencere_11.geometry("450x300")
        pencere_11.title("Ertelemeli Dönem Sonu Ödeme İşlemi")
        pencere_11.configure(bg="#85bfcd")
        #Fonksiyonlar
        def ertelemeli_donem_sonu_ödeme_serisi():
                s1_1=float(Vr_faiz.get())
                s2_1=float(Vr_gecikme.get())
                s3_1=float(Vr_adet.get())
                sonuc.configure(text=str(((1+s1_1)**(-s2_1))* (1-(1+s1_1)**(-s3_1))/s1_1)) # burası bir problem yaratabilir.
        
        def Temizlik():
                Vr_faiz.delete(0,END)
                Vr_gecikme.delete(0,END)
                Vr_adet.delete(0,END)
        # Sonuç 
        sonuc=Label(pencere_11,text="Sonuç",font="Courier 16 bold",bg="#85bfcd")
        sonuc.place(x=180,y=200)
        #Etiket
        Etiket_faiz=Label(pencere_11,text="Faiz oran :",font="Courier 10 bold",bg="#85bfcd")
        Etiket_gecikme=Label(pencere_11,text="Gecikme süre :",font="Courier 10 bold",bg="#85bfcd")
        Etiket_adet=Label(pencere_11,text="Ödeme adet :",font="Courier 10 bold",bg="#85bfcd")
        Etiket_faiz.place(x=75,y=50)
        Etiket_gecikme.place(x=50,y=80)
        Etiket_adet.place(x=65,y=110)
        #veri giriş
        Vr_faiz=Entry(pencere_11,font="Courier 16 bold",justify="center",width=10)
        Vr_gecikme=Entry(pencere_11,font="Courier 16 bold",justify="center",width=10)
        Vr_adet=Entry(pencere_11,font="Courier 16 bold",justify="center",width=10)
        Vr_faiz.place(x=180,y=50)
        Vr_gecikme.place(x=180,y=80)
        Vr_adet.place(x=180,y=110)
        #Butonlar
        hesap=Button(pencere_11,text="Hesapla",font="Courier 10 bold",command=ertelemeli_donem_sonu_ödeme_serisi)
        temiz=Button(pencere_11,text="Temizle",font="Courier 10 bold",command=Temizlik)
        hesap.place(x=330,y=50)
        temiz.place(x=330,y=80)
def Ertelenmis_donem_basi_odemeler_islemi():
        pencere_12=Toplevel()
        pencere_12.geometry("450x300")
        pencere_12.title("Ertelemeli Dönem Başı Ödeme İşlemi")
        pencere_12.configure(bg="#85bfcd")
        #fonksiyonlar
        def ertelenmis_donem_basi_odeme_serisi():
                s1_1=float(Vr_faiz.get())
                s2_1=float(Vr_gecikme.get())
                s3_1=float(Vr_adet.get())
                sonuc.configure(text=str(((1+s1_1)**(-s2_1))*(1-(1+s1_1)**(-s3_1))/s1_1))

        def Temizlik():
                Vr_adet.delete(0,END)
                Vr_faiz.delete(0,END)
                Vr_gecikme.delete(0,END)        
        #Çıktı
        sonuc=Label(pencere_12,text="Sonuç",font="Courier 16 bold",bg="#85bfcd")
        sonuc.place(x=180,y=200)
        #etiketler
        Etiket_faiz=Label(pencere_12,text="Faiz oran :",font="Courier 10 bold",bg="#85bfcd")
        Etiket_gecikme=Label(pencere_12,text="Gecikme süresi :",font="Courier 10 bold",bg="#85bfcd")
        Etiket_adet=Label(pencere_12,text="Ödeme adet :",font="Courier 10 bold",bg="#85bfcd")
        Etiket_faiz.place(x=60,y=50)
        Etiket_gecikme.place(x=20,y=80)
        Etiket_adet.place(x=50,y=110)
        #veri giriş
        Vr_faiz=Entry(pencere_12,font="Courier 16 bold",justify="center",width=10)
        Vr_gecikme=Entry(pencere_12,font="Courier 16 bold",justify="center",width=10)
        Vr_adet=Entry(pencere_12,font="Courier 16 bold",justify="center",width=10)
        Vr_faiz.place(x=160,y=50)
        Vr_gecikme.place(x=160,y=80)
        Vr_adet.place(x=160,y=110)
        #Butonlar
        hesap=Button(pencere_12,text="Hesapla",font="Courier 10 bold",command=ertelenmis_donem_basi_odeme_serisi)
        temiz=Button(pencere_12,text="Temizle",font="Courier 10 bold",command=Temizlik)
        hesap.place(x=300,y=50)
        temiz.place(x=300,y=80)


def Donem_sonu_sonsuz_odemeler_islemi():
        #Özelleştirilmiş kütüphane ile tasarlandı.
        customtkinter.set_appearance_mode("system")
        customtkinter.set_default_color_theme("dark-blue")
        pencere_13=customtkinter.CTkToplevel()
        pencere_13.geometry("450x300")
        pencere_13.title("Dönem Sonu Sonsuz Ödeme İşlemi")
        #Fonksiyonlar        
        def donem_sonu_sonsuz_odemeler_serisi():
                s1=float(Vr_faiz.get())
                sonuc.configure(text=str(1/s1))

        def Temizlik():
                Vr_faiz.delete(0,END)
        #Çıktı
        sonuc=CTkLabel(pencere_13,text="Sonuç",font=CTkFont(family="Courier bold",size=20))
        sonuc.place(x=180,y=200)
        #Etiketler
        Etiket_faiz=CTkLabel(master=pencere_13,text="Faiz oran :",
                             font=CTkFont(family="Courier bold",size=14))
        Etiket_faiz.place(x=50,y=50)
        # veri giriş
        Vr_faiz=CTkEntry(pencere_13,font=CTkFont(family="Courier bold",size=20),width=100,justify="center")
        Vr_faiz.place(x=120,y=50)
        #Butonlar
        hesap=CTkButton(pencere_13,text="Hesapla",
                        font=CTkFont(family="Courier bold",size=12),command=donem_sonu_sonsuz_odemeler_serisi)
        temiz=CTkButton(pencere_13,text="Temizle",
                        font=CTkFont(family="Courier bold",size=12),command=Temizlik)
        hesap.place(x=240,y=50)
        temiz.place(x=240,y=80)



def Donem_bası_sonsuz_odeme_islemi():
        pencere_14=Toplevel()
        pencere_14.geometry("450x300")
        pencere_14.title("Dönem Başı Sonsuz Ödeme İşlemi")
        pencere_14.configure(bg="#85bfcd")
        #Fonksiyonlar
        def donem_basi_sonsuz_odeme_serisi():
                s1=float(Vr_iskonto.get())
                sonuc.configure(text=str(1/s1))
        
        def Temizlik():
                Vr_iskonto.delete(0,END)
        #Sonuc
        sonuc=Label(pencere_14,text="Sonuç",font="Courier 16 bold",bg="#85bfcd")
        sonuc.place(x=180,y=200)
        #Etik
        Etiket_iskonto=Label(pencere_14,text="İskonto :",font="Courier 10 bold",bg="#85bfcd")
        Etiket_iskonto.place(x=40,y=55)
        #veri giriş
        Vr_iskonto=Entry(pencere_14,font="Courier 16 bold",justify="center",width=10)
        Vr_iskonto.place(x=120,y=50)
        #butonlar
        hesap=Button(pencere_14,text="Hesapla",font="Courier 10 bold",command=donem_basi_sonsuz_odeme_serisi)
        temiz=Button(pencere_14,text="Temizle",font="Courier 10 bold",command=Temizlik)
        hesap.place(x=280,y=50)
        temiz.place(x=280,y=80)

def Surekli_duzenli_odeme_islemleri():
        pencere_15=Toplevel()
        pencere_15.geometry("450x300")
        pencere_15.title("Sürekli Düzenli Ödeme İşlemi")
        pencere_15.configure(bg="#85bfcd")
        #fonksiyon
        def surekli_duzenli_odemeler_serisi():
                s1=float(Vr_faiz.get())
                s2=float(Vr_adet.get())
                s3=float(Vr_kuvet.get())
                sonuc.configure(text=str((1-((1+s1)**-s2))/s3))

        def Temizlik():
                Vr_adet.delete(0,END)
                Vr_faiz.place(0,END)
                Vr_kuvet.place(0,END)
        #sonuç
        sonuc=Label(pencere_15,text="Sonuç",font="Courier 16 bold",bg="#85bfcd")
        sonuc.place(x=180,y=200)
        #Etiketler
        Etiket_faiz=Label(pencere_15,text="Faiz oran :",font="Courier 10 bold",bg="#85bfcd")
        Etiket_adet=Label(pencere_15,text="Ödeme adet :",font="Courier 10 bold",bg="#85bfcd")
        Etiket_kuvvet=Label(pencere_15,text="Faiz kuvvet :",font="Courier 10 bold",bg="#85bfcd")
        Etiket_faiz.place(x=40,y=50)
        Etiket_adet.place(x=30,y=80)
        Etiket_kuvvet.place(x=20,y=110)
        # veri girişi
        Vr_faiz=Entry(pencere_15,font="Courier 16 bold",justify="center",width=10)
        Vr_adet=Entry(pencere_15,font="Courier 16 bold",justify="center",width=10)
        Vr_kuvet=Entry(pencere_15,font="Courier 16 bold",justify="center",width=10)
        Vr_faiz.place(x=140,y=50)
        Vr_adet.place(x=140,y=80)
        Vr_kuvet.place(x=140,y=110)
        #Butonlar
        hesap=Button(pencere_15,text="Hesapla",font="Courier 10 bold",command=surekli_duzenli_odemeler_serisi)
        temiz=Button(pencere_15,text="Temizle",font="Courier 10 bold",command=Temizlik)
        hesap.place(x=280,y=50)
        temiz.place(x=280,y=80)

def Donem_sonu_artan_odeme_islemleri():
        pencere_16=Toplevel()
        pencere_16.geometry("450x300")
        pencere_16.title("Dönem Sonu Artan Ödeme İşlemi")
        pencere_16.configure(bg="#85bfcd")
        #Fonksiyonlar
        def donem_sonu_artan_odeme_serisi():
                s1=float(Vr_adet.get())
                s2=float(Vr_faiz.get())
                s3=float(Vr_iskonto.get())
                sonuc.configure(text=str((((1-(1+s2)**(-s1))/s3)-(s1*((1+s2)**(-s1))))/s2))
        
        def Temizlik():
                Vr_adet.delete(0,END)
                Vr_faiz.delete(0,END)
        #Çıktı
        sonuc=Label(pencere_16,text="Sonuç",font="Courier 16 bold",bg="#85bfcd")
        sonuc.place(x=180,y=200)
        #Etiket
        Etiket_adet=Label(pencere_16,text="Ödeme adet :",font="Courier 10 bold",bg="#85bfcd")
        Etiket_faiz=Label(pencere_16,text="Faiz oran :",font="Courier 10 bold",bg="#85bfcd")
        Etiket_iskonto=Label(pencere_16,text="İskonto :",font="Courier 10 bold",bg="#85bfcd")
        Etiket_adet.place(x=25,y=50)
        Etiket_faiz.place(x=35,y=80)
        Etiket_iskonto.place(x=50,y=110)
        #veri girişi
        Vr_adet=Entry(pencere_16,font="Courier 16 bold",justify="center",width=10)
        Vr_faiz=Entry(pencere_16,font="Courier 16 bold",justify="center",width=10)
        Vr_iskonto=Entry(pencere_16,font="Courier 16 bold",justify="center",width=10)
        Vr_adet.place(x=140,y=50)
        Vr_faiz.place(x=140,y=80)
        Vr_iskonto.place(x=140,y=110)
        #Butonlar
        hesap=Button(pencere_16,text="Hesapla",font="Courier 10 bold",command=donem_sonu_artan_odeme_serisi)
        temiz=Button(pencere_16,text="Temizle",font="Courier 10 bold",command=Temizlik)
        hesap.place(x=280,y=50)
        temiz.place(x=280,y=80)
def Donem_basi_artan_odeme_islemleri():
        pencere_17=Toplevel()
        pencere_17.geometry("450x300")
        pencere_17.title("Dönem Başı Artan Ödeme İşlemi")
        pencere_17.configure(bg="#85bfcd")
        #Fonksiyon
        def donem_basi_artan_odemeler_serisi():
                s1=float(Vr_iskonto.get())
                s2=float(Vr_adet.get())
                s3=float(Vr_faiz.get())
                sonuc.configure(text=str(((1-(1+s3)**(-s2))/s1)-((s2*((1+s3)**(-s2))))/s1))
        
        def temizlik():
                Vr_adet.delete(0,END)
                Vr_faiz.delete(0,END)
                Vr_iskonto.delete(0,END)
        #sonuç
        sonuc=Label(pencere_17,text="Sonuç",font="Courier 16 bold",bg="#85bfcd")
        sonuc.place(x=180,y=200)
        #Etiket 
        Etiket_iskonto=Label(pencere_17,text="İskonto oran :",font="Courier 10 bold",bg="#85bfcd")
        Etiket_adet=Label(pencere_17,text="Ödeme adet :",font="Courier 10 bold",bg="#85bfcd")
        Etiket_faiz=Label(pencere_17,text="Faiz oran :",font="Courier 10 bold",bg="#85bfcd")
        Etiket_iskonto.place(x=25,y=50)
        Etiket_adet.place(x=40,y=80)
        Etiket_faiz.place(x=50,y=110)
        #Veri giriş
        Vr_iskonto=Entry(pencere_17,font="Courier 16 bold",justify="center",width=10)
        Vr_adet=Entry(pencere_17,font="Courier 16 bold",justify="center",width=10)
        Vr_faiz=Entry(pencere_17,font="Courier 16 bold",justify="center",width=10)
        Vr_iskonto.place(x=140,y=50)
        Vr_adet.place(x=140,y=80)
        Vr_faiz.place(x=140,y=110)
        #butonlar
        hesap=Button(pencere_17,text="Hesapla",font="Courier 10 bold",command=donem_basi_artan_odemeler_serisi)
        temiz=Button(pencere_17,text="Temizle",font="Courier 10 bold",command=temizlik)
        hesap.place(x=280,y=50)
        temiz.place(x=280,y=80)

def Donem_sonu_azalan_odemeler_islemleri():
        pencere_18=Toplevel()
        pencere_18.geometry("450x300")
        pencere_18.title("Dönem Sonu Azalan Ödeme İşlemi")
        pencere_18.configure(bg="#85bfcd")
        #fonksiyon
        def donem_sonu_azalan_ödemeler_serisi():
                s1=float(Vr_adet.get())
                s2=float(Vr_faiz.get())
                sonuc.configure(text=str((s1-((1-(1+s2)**(-s1))/s2))/s2))
        
        def Temizlik():
                Vr_adet.delete(0,END)
                Vr_faiz.delete(0,END)

        #Çıktı
        sonuc=Label(pencere_18,text="Sonuç",font="Courier 16 bold",bg="#85bfcd")
        sonuc.place(x=180,y=200)
        #etiket
        Etiket_adet=Label(pencere_18,text="Ödeme adet :",font="Courier 10 bold",bg="#85bfcd")
        Etiket_faiz=Label(pencere_18,text="Faiz oran :",font="Courier 10 bold",bg="#85bfcd")
        Etiket_adet.place(x=40,y=50)
        Etiket_faiz.place(x=50,y=80)
        #Veri Giriş
        Vr_adet=Entry(pencere_18,font="Courier 16 bold",justify="center",width=10)
        Vr_faiz=Entry(pencere_18,font="Courier 16 bold",justify="center",width=10)
        Vr_adet.place(x=140,y=50)
        Vr_faiz.place(x=140,y=80)
        #butonlar
        hesap = Button(pencere_18,text="Hesapla",font="Courier 10 bold",command=donem_sonu_azalan_ödemeler_serisi)
        temiz=Button(pencere_18,text="Temizle",font="Courier 10 bold",command=Temizlik)
        hesap.place(x=280,y=50)
        temiz.place(x=280,y=80)

def Donem_basi_azalan_odemeler_islemi():
        pencere_19=Toplevel()
        pencere_19.geometry("450x300")
        pencere_19.title("Dönem Başı Azalan Ödeme İşlemi")
        pencere_19.configure(bg="#85bfcd")
        #Fonksiyon
        def donem_basi_azalan_odemeler_serisi():
                s1=float(Vr_adet.get())
                s3=float(Vr_iskonto.get())
                s4=float(Vr_faiz.get())
                sonuc.configure(text=str((s1-((1-(1+s4)**(-s1))/s4)/s3)))
        
        def temizlik():
                Vr_adet.delete(0,END)
                Vr_iskonto.delete(0,END)
                Vr_faiz.delete(0,END)
        
        #sonuc
        sonuc=Label(pencere_19,text="Sonuç",font="Courier 16 bold",bg="#85bfcd")
        sonuc.place(x=180,y=200)
        #Etiket
        Etiket_adet=Label(pencere_19,text="Ödeme adet :",font="Courier 10 bold",bg="#85bfcd")
        Etiket_iskonto=Label(pencere_19,text="İskonto oran :",font="Courier 10 bold",bg="#85bfcd")
        Etiket_faiz=Label(pencere_19,text="Faiz oran :",font="Courier 10 bold",bg="#85bfcd")
        Etiket_adet.place(x=40,y=50)
        Etiket_iskonto.place(x=25,y=80)
        Etiket_faiz.place(x=50,y=110)
        #veri girişi
        Vr_adet=Entry(pencere_19,font="Courier 16 bold",justify="center",width=10)
        Vr_iskonto=Entry(pencere_19,font="Courier 16 bold",justify="center",width=10)
        Vr_faiz=Entry(pencere_19,font="Courier 16 bold",justify="center",width=10)
        Vr_adet.place(x=140,y=50)
        Vr_iskonto.place(x=140,y=80)
        Vr_faiz.place(x=140,y=110)
        #butonlar
        hesap=Button(pencere_19,text="Hesapla",font="Courier 10 bold",command=donem_basi_azalan_odemeler_serisi)
        temiz=Button(pencere_19,text="Temizle",font="Courier 10 bold",command=temizlik)
        hesap.place(x=280,y=50)
        temiz.place(x=280,y=80)

#Ana pencere etkileşimi
#etiketler
baslik=tk.Label(pencere_1,text="Yapmak istediğiniz işlemi seçiniz.",background="#85bfcd",font="Courier 14 bold")
baslik.place(x=40,y=50)
#Menü buton 1 (peşinat işlemleri)
mbtn=Menubutton(pencere_1,text="Peşinat İşlemleri",relief=RAISED,height=2)
mbtn.grid
mbtn.menu= Menu(mbtn,tearoff=0)

mbtn["menu"]=mbtn.menu
mbtn.menu.add_command(label="Basit Faizlendirme İşlemi",command=Basit_faizlendirme_peşinat)
mbtn.menu.add_command(label="Bileşik Faizlendirme İşlemi",command=Bilesik_Faizlendirme_islemi)
mbtn.menu.add_command(label="İskonto Oranı (Basit)",command=Iskonto_Orani_Basit_islemi)
mbtn.menu.add_command(label="İskonto Oranı (Bileşik)",command=Iskonto_orani_bileşik_islemi)
mbtn.menu.add_command(label="Sabit Anlık Faiz Oranı",command=Sabit_anlik_faiz_islemi)
mbtn.menu.add_command(label="Dönem Sonu Düzenli Ödemeler Serisi",command=Donem_sonu_duzenli_odeme_islemi)
mbtn.menu.add_command(label="Dönem Başı Düzenli Ödemeler Serisi",command=Donem_basi_duzenli_odemeler_islemi)
mbtn.menu.add_command(label="Ertelemeli Dönem Sonu Ödeme Serisi",command=Ertelemeli_donem_sonu_odeme_islemi)
mbtn.menu.add_command(label="Ertelemeli Dönem Başı Ödeme Serisi",command=Ertelenmis_donem_basi_odemeler_islemi)
mbtn.menu.add_command(label="Dönem Sonu Sonsuz Ödeme",command=Donem_sonu_sonsuz_odemeler_islemi)
mbtn.menu.add_command(label="Dönem Başı Sonsuz Ödeme",command=Donem_bası_sonsuz_odeme_islemi)
mbtn.menu.add_command(label="Sürekli Düzenli Ödemeler Serisi",command=Surekli_duzenli_odeme_islemleri)
mbtn.menu.add_command(label="Dönem Sonu Artan Ödemeler Serisi",command=Donem_sonu_artan_odeme_islemleri)
mbtn.menu.add_command(label="Dönem Başı Artan Ödemeler Serisi",command=Donem_basi_artan_odeme_islemleri)
mbtn.menu.add_command(label="Dönem Sonu Azalan Ödemeler Serisi",command=Donem_sonu_azalan_odemeler_islemleri)
mbtn.menu.add_command(label="Dönem Başı Azalan Ödemeler Serisi",command=Donem_basi_azalan_odemeler_islemi)
#Ayırıcı çizgi
mbtn.menu.add_separator()
mbtn.menu.add_command(label="Çıkış",command=pencere_1.quit)


mbtn.place(x=100,y=80)

#Menü buton 2 (Birikim işlemleri)
mbtn_2=Menubutton(pencere_1,text="Birikim İşlemleri",relief=RAISED,height=2)
mbtn_2.grid
mbtn_2.menu=Menu(mbtn_2,tearoff=0)
mbtn_2["menu"]=mbtn_2.menu
mbtn_2.menu.add_command(label="Çıkış",command=pencere_1.quit)
mbtn_2.place(x=250,y=80)      



# mainloop hep en sonda dönmesi gerekiyor.
pencere_1.mainloop()