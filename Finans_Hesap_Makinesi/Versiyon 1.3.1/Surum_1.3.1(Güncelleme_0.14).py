# pencere oluşturma ve düzenleme.
from tkinter import *
import tkinter as tk 
import customtkinter
from customtkinter import *
from tkinter import messagebox # değerlendirilecek

customtkinter.set_appearance_mode("system")
customtkinter.set_default_color_theme("dark-blue")  

pencere_1=tk.Tk()
pencere_1.geometry('450x300')#Bu kod Pencere boyuru ayarlıyor.
pencere_1.title("Finans Hesap aracı")# pencere başlığını değiştiriyor.
pencere_1.configure(background="#85bfcd")
pencere_1.iconbitmap("finans.ico")
bg=PhotoImage(file="stat.png")
png=Label(pencere_1,image=bg,background="#85bfcd")
png.place(x=40,y=150)
kurcu=Label(pencere_1,text="©IWT",bg="#85bfcd",font="Courier 10 bold")
kurcu.place(x=380,y=260)
#uyarı kutusu deneme
def Mesaj_kutusu():
        msg_box=messagebox.askquestion("Gerçekten mi?","Çıkış yapmak istediğinizden emin misiniz?")
        if msg_box == "yes":
                pencere_1.destroy()
        else:
                pencere_1         
                
#Menü buton kodları;
#Fonksiyon kodları altında çalışmakta olduğundan en aşağıda yer almak zorunda.
#--------------------
#Peşinat işlemleri kısmı
def Basit_faizlendirme_peşinat(): # Aklımdaki Tasarım Tam Anlamı ile gerçekleşti Yavaş yavaş kodlayıp github'a atıcağım.
        pencere_4=Toplevel()
        pencere_4.geometry("450x300")
        pencere_4.title("Basit Faizlendirme İşlemi")
        pencere_4.configure(background="#85bfcd")
        pencere_4.iconbitmap("calc.ico")
        kurcu=Label(pencere_4,text="©IWT",bg="#85bfcd",font="Courier 7 bold")
        kurcu.place(x=400,y=280)
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
        pencere_5.iconbitmap("calc.ico")
        kurcu=Label(pencere_5,text="©IWT",bg="#85bfcd",font="Courier 7 bold")
        kurcu.place(x=400,y=280)
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
        pencere_6.iconbitmap("calc.ico")
        kurcu=Label(pencere_6,text="©IWT",bg="#85bfcd",font="Courier 7 bold")
        kurcu.place(x=400,y=280)
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
        pencere_7.iconbitmap("calc.ico")
        kurcu=Label(pencere_7,text="©IWT",bg="#85bfcd",font="Courier 7 bold")
        kurcu.place(x=400,y=280)
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
        pencere_8.iconbitmap("calc.ico")
        kurcu=Label(pencere_8,text="©IWT",bg="#85bfcd",font="Courier 7 bold")
        kurcu.place(x=400,y=280)
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
        pencere_9.iconbitmap("calc.ico")
        kurcu=Label(pencere_9,text="©IWT",bg="#85bfcd",font="Courier 7 bold")
        kurcu.place(x=400,y=280)
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
        pencere_10.iconbitmap("calc.ico")
        kurcu=Label(pencere_10,text="©IWT",bg="#85bfcd",font="Courier 7 bold")
        kurcu.place(x=400,y=280)
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
        pencere_11.iconbitmap("calc.ico")
        kurcu=Label(pencere_11,text="©IWT",bg="#85bfcd",font="Courier 7 bold")
        kurcu.place(x=400,y=280)
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
        pencere_12.iconbitmap("calc.ico")
        kurcu=Label(pencere_12,text="©IWT",bg="#85bfcd",font="Courier 7 bold")
        kurcu.place(x=400,y=280)
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
        pencere_13.iconbitmap("calc.ico")
        kurcu=CTkLabel(pencere_13,text="©IWT"
                       ,font=CTkFont(family="Courier bold",size=7))
        kurcu.place(x=400,y=280)
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
        pencere_14.iconbitmap("calc.ico")
        kurcu=Label(pencere_14,text="©IWT",bg="#85bfcd",font="Courier 7 bold")
        kurcu.place(x=400,y=280)
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
        pencere_15.iconbitmap("calc.ico")
        kurcu=Label(pencere_15,text="©IWT",bg="#85bfcd",font="Courier 7 bold")
        kurcu.place(x=400,y=280)
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
        pencere_16.iconbitmap("calc.ico")
        kurcu=Label(pencere_16,text="©IWT",bg="#85bfcd",font="Courier 7 bold")
        kurcu.place(x=400,y=280)
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
        pencere_17.iconbitmap("calc.ico")
        kurcu=Label(pencere_17,text="©IWT",bg="#85bfcd",font="Courier 7 bold")
        kurcu.place(x=400,y=280)
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
        pencere_18.iconbitmap("calc.ico")
        kurcu=Label(pencere_18,text="©IWT",bg="#85bfcd",font="Courier 7 bold")
        kurcu.place(x=400,y=280)
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
        pencere_19.iconbitmap("calc.ico")
        kurcu=Label(pencere_19,text="©IWT",bg="#85bfcd",font="Courier 7 bold")
        kurcu.place(x=400,y=280)
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

# menü devamı 
def Donem_sonu_sonsuz_Artan_odemeler_Serisi():
        pencere_20=Toplevel()
        pencere_20.title("Dönem Sonu Sonsuz Artan Ödemler İşlemi")
        pencere_20.geometry("450x300")
        pencere_20.configure(bg="#85bfcd")
        pencere_20.iconbitmap("calc.ico")
        kurcu=Label(pencere_20,text="©IWT",bg="#85bfcd",font="Courier 7 bold")
        kurcu.place(x=400,y=280)
        #Fonksiyonlar

def Donem_basi_sonsuz_artan_ödemler_serisi():
        pencere_21=Toplevel()
        pencere_21.title("Dönem Sonu Sonsuz Artan Ödemeler İşlemi")
        pencere_21.configure(bg="#85bfcd")
        pencere_21.geometry("450x300")
        pencere_21.iconbitmap("calc.ico")
        kurcu=Label(pencere_21,text="©IWT",bg="#85bfcd",font="Courier 7 bold")
        kurcu.place(x=400,y=280)

def Surekli_ödemeli_artan_ödemeler_Serisi():
        pencere_22=Toplevel()
        pencere_22.title("Sürekli Ödemeli Artan Ödemeler İşlemi")
        pencere_22.geometry("450x300")
        pencere_22.configure(bg="#85bfcd")
        pencere_22.iconbitmap("calc.ico")
        kurcu=Label(pencere_22,text="©IWT",bg="#85bfcd",font="Courier 7 bold")
        kurcu.place(x=400,y=280)

def Surekli_ödemeli_azalan_ödemeler_serisi():
        pencere_23=Toplevel()
        pencere_23.geometry("450x300")
        pencere_23.title("Sürekli Ödemeli Artan Ödemeler")
        pencere_23.configure(bg="#85bfcd")
        pencere_23.iconbitmap("calc.ico")
        kurcu=Label(pencere_23,text="©IWT",bg="#85bfcd",font="Courier 7 bold")
        kurcu.place(x=400,y=280)

def Surekli_ödemeli_artan_sonsuz_ödemeler_serisi():
        pencere_24=Toplevel()
        pencere_24.geometry("450x300")
        pencere_24.title("Sürekli Ödemeli Artan Sonsuz Ödemeler İşlemi")
        pencere_24.configure(bg="#85bfcd")
        pencere_24.iconbitmap("calc.ico")
        kurcu=Label(pencere_24,text="©IWT",bg="#85bfcd",font="Courier 7 bold")
        kurcu.place(x=400,y=280)

def Ussel_artan_dönem_sonu_ödemeler_serisi():
        pencere_25=Toplevel()
        pencere_25.geometry("450x300")
        pencere_25.title("Üssel Artan Dönem Sonu Ödemeler İşlemi")
        pencere_25.configure(bg="#85bfcd")
        pencere_25.iconbitmap("calc.ico")
        kurcu=Label(pencere_25,text="©IWT",bg="#85bfcd",font="Courier 7 bold")
        kurcu.place(x=400,y=280)

def Ussel_artan_dönem_basi_ödemeler_serisi():
        pencere_26=Toplevel()
        pencere_26.geometry("450x300")
        pencere_26.title("Üssel Artan Dönem Başı Ödemeler İşlemi")
        pencere_26.configure(bg="#85bfcd")
        pencere_26.iconbitmap("calc.ico")
        kurcu=Label(pencere_26,text="©IWT",bg="#85bfcd",font="Courier 7 bold")
        kurcu.place(x=400,y=280)

def Surekli_degisken_nakit_akisi():
        pencere_27=Toplevel()
        pencere_27.geometry("450x300")
        pencere_27.title("Sürekli Değişken Nakit Akış İşleme")
        pencere_27.configure(bg="#85bfcd")
        pencere_27.iconbitmap("calc.ico")
        kurcu=Label(pencere_27,text="©IWT",bg="#85bfcd",font="Courier 7 bold")
        kurcu.place(x=400,y=280)

def T_anında_t_ödeme_oranlı_surekli_artan_seri():
        pencere_28=Toplevel()
        pencere_28.geometry("450x300")
        pencere_28.title("T Anında t Ödeme Oranlı Sürekli Artan İşlem")
        pencere_28.configure(bg="#85bfcd")
        pencere_28.iconbitmap("calc.ico")
        kurcu=Label(pencere_28,text="©IWT",bg="#85bfcd",font="Courier 7 bold")
        kurcu.place(x=400,y=280)

def T_anında_n_t_ödeme_oranlı_sürekli_azalan_seri():
        pencere_29=Toplevel()
        pencere_29.title("T Anında n-t Ödeme Oranlı Sürekli Azalan İşlem")
        pencere_29.geometry("450x300")
        pencere_29.configure(bg="#85bfcd")
        pencere_29.iconbitmap("calc.ico")
        kurcu=Label(pencere_29,text="©IWT",bg="#85bfcd",font="Courier 7 bold")
        kurcu.place(x=400,y=280)

def T_anında_t_ödeme_oranlı_surekli_sonsuz_artan_seri():
        pencere_30=Toplevel()
        pencere_30.title("T Anında t Ödeme Oranlı Sürekli Sonsuz artan İşlem")
        pencere_30.geometry("450x300")
        pencere_30.configure(bg="#85bfcd")
        pencere_30.iconbitmap("calc.ico")
        kurcu=Label(pencere_30,text="©IWT",bg="#85bfcd",font="Courier 8 bold")
        kurcu.place(x=400,y=280)

def Net_pesin_deger():
        pencere_31=Toplevel()
        pencere_31.geometry("450x300")
        pencere_31.title("Net Peşin Değer İşlemi")
        pencere_31.configure(bg="#85bfcd")
        pencere_31.iconbitmap("calc.ico")
        kurcu=Label(pencere_31,text="©IWT",bg="#85bfcd",font="Courier 8 bold")
        kurcu.place(x=400,y=280)

def iç_verim_getiri_oranı_karsılastırma():
        pencere_32=Toplevel()
        pencere_32.geometry("450x300")
        pencere_32.title("İç Verim / Getiri Oranı Karşılaştırma İşlemi")
        pencere_32.iconbitmap("calc.ico")
        pencere_32.configure(bg="#85bfcd")
        kurcu=Label(pencere_32,text="©IWT",bg="#85bfcd",font="Courier 8 bold")
        kurcu.place(x=400,y=280)

def nominal_ve_gercek_nakit_akıslarının_pesin_degeri():
        pencere_33=Toplevel()
        pencere_33.geometry("450x300")
        pencere_33.title("Nominal ve Gerçek Nakit Akışlarının Peşin Değer İşlemi")
        pencere_33.configure(bg="#85bfcd")
        pencere_33.iconbitmap("calc.ico")
        kurcu=Label(pencere_33,text="©IWT",bg="#85bfcd",font="Courier 8 bold")
        kurcu.place(x=400,y=280)

def para_agirlikli_faiz_getiri_orani():
        pencere_34=Toplevel()
        pencere_34.geometry("450x300")
        pencere_34.title("Para Ağırlıklı Faiz/Getiri Oranı")
        pencere_34.configure(bg="#85bfcd")
        pencere_34.iconbitmap("calc.ico")
        kurcu=Label(pencere_34,text="©IWT",bg="#85bfcd",font="Courier 8 bold")
        kurcu.place(x=400,y=280)
#Ana pencere etkileşimi
#etiketler
baslik=tk.Label(pencere_1,text="Yapmak istediğiniz işlemi seçiniz.",background="#85bfcd",font="Courier 14 bold")
baslik.place(x=40,y=50)
#Menü buton 1 (peşinat işlemleri)
mbtn=Menubutton(pencere_1,text="Peşinat İşlemleri",relief=RAISED,height=2)
mbtn.grid
mbtn.menu= Menu(mbtn,tearoff=0,border=20)
mbtn.place(x=100,y=80)
#Menü Listesi
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

#Sub Menü_1
sub_menu=Menu(mbtn.menu,tearoff=0)
sub_menu.add_command(label="Dönem Sonu Sonsuz Artan Ödemeler Serisi",command=Donem_sonu_sonsuz_Artan_odemeler_Serisi)
sub_menu.add_command(label="Dönem Başı Sonsuz Artan Ödemeler Serisi",command=Donem_basi_sonsuz_artan_ödemler_serisi)
sub_menu.add_command(label="Sürekli Ödemeli Artan Ödemeler Serisi",command=Surekli_ödemeli_artan_ödemeler_Serisi)
sub_menu.add_command(label="Sürekli Ödemeli Azalan Ödemler Serisi",command=Surekli_ödemeli_azalan_ödemeler_serisi)
sub_menu.add_command(label="Sürekli Ödemeli Artan Sonsuz Ödemeler Serisi",command=Surekli_ödemeli_artan_sonsuz_ödemeler_serisi)
sub_menu.add_command(label="Üssel Artan Dönem Sonu Ödemeler Serisi",command=Ussel_artan_dönem_sonu_ödemeler_serisi)
sub_menu.add_command(label="Üssel Artan Dönem Başı Ödemeler Serisi",command=Ussel_artan_dönem_basi_ödemeler_serisi)
sub_menu.add_command(label="Sürekli Değişen Nakit Akışı",command=Surekli_degisken_nakit_akisi)
sub_menu.add_command(label="T Anında t Ödeme Oranlı Sürekli Artan Seri",command=T_anında_t_ödeme_oranlı_surekli_artan_seri)
sub_menu.add_command(label="T Anında n-t Ödeme Oranlı Sürekli Azalan Seri",command=T_anında_n_t_ödeme_oranlı_sürekli_azalan_seri)
sub_menu.add_command(label="T Anında t Ödeme Oranlı Sürekli Sonsuz Artan Seri",command=T_anında_t_ödeme_oranlı_surekli_sonsuz_artan_seri)
sub_menu.add_command(label="Net Peşin Değer",command=Net_pesin_deger)
sub_menu.add_command(label="İç Verim/Getiri Oranı Karşılaştırma",command=iç_verim_getiri_oranı_karsılastırma)
sub_menu.add_command(label="Nominal ve Gerçek Nakit Akışlarının Peşin Değeri",command=nominal_ve_gercek_nakit_akıslarının_pesin_degeri)
sub_menu.add_command(label="Para Ağırlıklı Faiz/Getiri Oranı",command=para_agirlikli_faiz_getiri_orani)
sub_menu.add_command(label="Zaman Ağırlıklı Faiz/Getiri Oranı")
#menü 3. sayfa eklenebilir.
sub_menu_2=Menu(mbtn.menu,tearoff=0)#menü içerisine bir menü daha oluşturdu ve komut atadık.
sub_menu_2.add_command(label="Çıkış",command=quit)
#Ayırıcı çizgi
mbtn.menu.add_separator()
mbtn.menu.add_cascade(label="Sayfa 2",menu=sub_menu)
mbtn.menu.add_cascade(label="Sayfa 3",menu=sub_menu_2)
mbtn.menu.add_command(label="Çıkış",command=Mesaj_kutusu)
#Diğer menü
#Brikimli menü fonksiyonları bu satırdan sonra yazılacak.


#Menü buton 2 (Birikim işlemleri)
mbtn_2=Menubutton(pencere_1,text="Birikim İşlemleri",relief=RAISED,height=2)
mbtn_2.grid
mbtn_2.menu=Menu(mbtn_2,tearoff=0)
mbtn_2.place(x=250,y=80)  
#Menü Listesi
mbtn_2["menu"]=mbtn_2.menu
mbtn_2.menu.add_command(label="Basit Faizlendirme İşlemi")
mbtn_2.menu.add_command(label="Bileşik Faizlendirme İşlemi")
mbtn_2.menu.add_command(label="İskonto Oranı (Basit)")
mbtn_2.menu.add_command(label="İskonto Oranı (Bileşik)")
mbtn_2.menu.add_command(label="Sabit Anlık Faiz Oranı")
mbtn_2.menu.add_command(label="Dönem Sonu Düzenli Ödemeler Serisi")
mbtn_2.menu.add_command(label="Dönem Başı Düzenli Ödemeler Serisi")
mbtn_2.menu.add_command(label="Ertelemeli Dönem Sonu Ödeme Serisi")
mbtn_2.menu.add_command(label="Ertelemeli Dönem Başı Ödeme Serisi")
mbtn_2.menu.add_command(label="Sürekli Düzenli Ödemeler Serisi")
mbtn_2.menu.add_command(label="Dönem Sonu Artan Ödemeler Serisi")
mbtn_2.menu.add_command(label="Dönem Başı Artan Ödemeler Serisi")
mbtn_2.menu.add_command(label="Dönem Sonu Azalan Ödemeler Serisi")
mbtn_2.menu.add_command(label="Dönem Başı Azalan Ödemeler Serisi")
#Ayırıcı Çizgi Birikim butonu için
mbtn_2.menu.add_separator()
mbtn_2.menu.add_command(label="Çıkış",command=Mesaj_kutusu)

# mainloop hep en sonda dönmesi gerekiyor.
pencere_1.mainloop()