# pencere oluşturma ve düzenleme.
from tkinter import *
import tkinter as tk 
from dash import dcc #?
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
        Etiket_Birikim=tk.Label(pencere_5,text="Birikim : ",font="Courier 10 bold",bg="#85bfcd")
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
        #Fonktison atama
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
        def Sabit_Anlik_faiz_orani():
                s1=("peşinat")
                s2=("zaman")
                s3=("Faiz kuvvet orani")
                s4=("exp değeri")
                sonuc=s1*(s4**(s2*s3))

def Donem_sonu_duzenli_odeme_islemi():
        pencere_9=Toplevel()
        pencere_9.geometry("450x300")
        pencere_9.title("Dönem Sonu Düzenli Ödeme İşlemi")
        def donem_sonu_duzenli_odemeler_serisi():
                s1=("Ödeme tutari")
                s2=("ödeme adedi")
                s3=("faiz orani")
                sonuc=s1*((1-((1+s3)**(-s2)))/s3)

def Donem_basi_duzenli_odemeler_islemi():
        pencere_10=Toplevel()
        pencere_10.geometry("450x300")
        pencere_10.title("Dönem Başı Düzenli Ödeme İşlemi")
        def donem_basi_duzenli_odemler_serisi():
                s1=("ödeme tutari")
                s2=("iskonto")
                s3=("faiz")
                s4=("ödeme adedi")
                sonuc=s1*((1-((1+s3)**(-s4)))/s2)

def Ertelemeli_donem_sonu_odeme_islemi():
        pencere_11=Toplevel()
        pencere_11.geometry("450x300")
        pencere_11.title("Ertelemeli Dönem Sonu Ödeme İşlemi")
        def ertelemeli_donem_sonu_ödeme_serisi():
                s1_1=("faiz")
                s2_1=("gecikme süresi")
                sonuc=((1+s1_1)**(-s2_1))*""" donem_sonu_duzenli_odemeler_serisi """ # burası bir problem yaratabilir.

def Ertelenmis_donem_basi_odemeler_islemi():
        pencere_12=Toplevel()
        pencere_12.geometry("450x300")
        pencere_12.title("Ertelemeli Dönem Başı Ödeme İşlemi")
        def ertelenmis_donem_basi_odeme_serisi():
                s1_1=("faiz")
                s2_1=("gecikme süresi")
                sonuc=((1+s1_1)**(-s2_1))*""" donem_basi_duzenli_odemler_serisi """

def Donem_sonu_sonsuz_odemeler_islemi():
        pencere_13=Toplevel()
        pencere_13.geometry("450x300")
        pencere_13.title("Dönem Sonu Sonsuz Ödeme İşlemi")
        def donem_sonu_sonsuz_odemeler_serisi():
                s1=("faiz")
                sonuc=1/s1

def Donem_bası_sonsuz_odeme_islemi():
        pencere_14=Toplevel()
        pencere_14.geometry("450x300")
        pencere_14.title("Dönem Başı Sonsuz Ödeme İşlemi")
        def donem_basi_sonsuz_odeme_serisi():
                s1=("iskonto")
                sonuc=1/s1

def Surekli_duzenli_odeme_islemleri():
        pencere_15=Toplevel()
        pencere_15.geometry("450x300")
        pencere_15.title("Sürekli Düzenli Ödeme İşlemi")
        def surekli_duzenli_odemeler_serisi():
                s1=("faiz oranı")
                s2=("ödeme adedi")
                s3=("Faiz kuvvet orani")
                sonuc=(1-((1+s1)**-s2))/s3

def Donem_sonu_artan_odeme_islemleri():
        pencere_16=Toplevel()
        pencere_16.geometry("450x300")
        pencere_16.title("Dönem Sonu Artan Ödeme İşlemi")
        def donem_sonu_artan_odeme_serisi():
                s1=("ödeme adedi")
                s2=("faiz orani")
                sonuc=(""" donem_basi_duzenli_odemler_serisi """-(s1*((1+s2)**(-s1))))/s2

def Donem_basi_artan_odeme_islemleri():
        pencere_17=Toplevel()
        pencere_17.geometry("450x300")
        pencere_17.title("Dönem Başı Artan Ödeme İşlemi")
        def donem_basi_artan_odemeler_serisi():
                s1=("iskonto orani")
                s2=("ödeme adedi")
                s3=("faiz orani")
                sonuc=(""" donem_basi_duzenli_odemler_serisi """-(s2*((1+s3)**(-s2))))/s1

def Donem_sonu_azalan_odemeler_islemleri():
        pencere_18=Toplevel()
        pencere_18.geometry("450x300")
        pencere_18.title("Dönem Sonu Azalan Ödeme İşlemi")
        def donem_sonu_azalan_ödemeler_serisi():
                s1=("ödeme adedi")
                s2=("faiz orani")
                sonuc=(s1-""" donem_sonu_duzenli_odemeler_serisi """)/s2

def Donem_basi_azalan_odemeler_islemi():
        pencere_19=Toplevel()
        pencere_19.geometry("450x300")
        pencere_19.title("Dönem Başı Azalan Ödeme İşlemi")
        def donem_basi_azalan_odemeler_serisi():
                s1=("odeme adedi")
                s3=("iskonto oranı")
                sonuc=(s1-""" donem_sonu_duzenli_odemeler_serisi """)/s3

#Ana pencere etkileşimi
#etiketler
baslik=tk.Label(pencere_1,text="Yapmak istediğiniz işlemi seçiniz.",background="#85bfcd",font="Courier 14 bold")
baslik.place(x=40,y=50)
#butınlar
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
mbtn.menu.add_command(label="Çıkış",command=pencere_1.quit)
mbtn.place(x=100,y=80)

# mainloop hep en sonda dönmesi gerekiyor.
pencere_1.mainloop()