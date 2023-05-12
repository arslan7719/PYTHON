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
        pencere_2.title("Basit Fazilendirme İslemi")

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

        #deneme buton menü
        
        
        

        basitislem=IntVar()
        tahmin=IntVar()

        mbtn.menu.add_checkbutton(label="Basit işlem",variable=basitislem)
        mbtn.menu.add_checkbutton(label="tahmin",variable=tahmin)

        

        mbtn.pack() 
          
       
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

        # Fonksiyon tanımlama 
        def Basit_Fazilendirme():
                s1=float(Birikim.get())
                s2=float(Zaman.get())
                s3=float(Faiz_Orani.get())
                sonuc.configure(text=str(s1*((1+s2*s3)**(-1))))

        #Çıktı etiketi hazırlancak
        sonuc = tk.Label(pencere_4,text="Sonuç",font="Courier 16 bold",width=30,justify="center")
        sonuc.pack()

        #Etiketler hazırlancak

        #Veri girişi
        Birikim=tk.Entry(pencere_4,font="Courier 16 bold",width=10,justify="center")
        Zaman=tk.Entry(pencere_4,font="Courier 16 bold",width=10,justify="center")
        Faiz_Orani=tk.Entry(pencere_4,font="Courier 16 bold",width=10,justify="center")
        Birikim.place(x=200,y=50)
        Zaman.place(x=200,y=100)
        Faiz_Orani.place(x=200,y=150)

        #Butonlar (temizleme ve hesaplama olacak şekilde iki tane)
        Hesapla=Button(pencere_4,text="Hesapla",command=Basit_Fazilendirme,font="Courier 16 bold")
        Hesapla.place(x=320,y=120)

def Bilesik_Faizlendirme_islemi():
        pencere_5=Toplevel()
        pencere_5.geometry("450x300")
        pencere_5.title("Bileşik Faiz İşlemleri")
        def Bilesik_Faizlendirme():
                s1=("Birikim")
                s2=("faiz orani")
                s3=("zaman")
                sonuc=s1*((1+s2)**(s3))

def Iskonto_Orani_Basit_islemi():
        pencere_6=Toplevel()
        pencere_6.geometry("450x300")
        pencere_6.title("İskonto Oranı İşlemi (Basit)")
        def iskonto_Orani_Basit():
                s1=("Peşinat")
                s2=("zaman")
                s3=("iskonto")
                sonuc=s1*(1-s2*s3)

def Iskonto_orani_bileşik_islemi():
        pencere_7=Toplevel()
        pencere_7.geometry("450x300")
        pencere_7.title("İskonto Oranı İşlemi (Bileşik)")
        def iskonto_Orani_Bilesik():
                s1=("peşinat")
                s2=("iskonto")
                s3=("zaman")
                sonuc=s1*((1-s2)**(s3))

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
        def donem_sonu_duzenli_odemeler_serisi():
                s1=("Ödeme tutari")
                s2=("ödeme adedi")
                s3=("faiz orani")
                sonuc=s1*((1-((1+s3)**(-s2)))/s3)

def Donem_basi_duzenli_odemeler_islemi():
        pencere_10=Toplevel()
        pencere_10.geometry("450x300")
        def donem_basi_duzenli_odemler_serisi():
                s1=("ödeme tutari")
                s2=("iskonto")
                s3=("faiz")
                s4=("ödeme adedi")
                sonuc=s1*((1-((1+s3)**(-s4)))/s2)

def Ertelemeli_donem_sonu_odeme_islemi():
        pencere_11=Toplevel()
        pencere_11.geometry("450x300")
        def ertelemeli_donem_sonu_ödeme_serisi():
                s1_1=("faiz")
                s2_1=("gecikme süresi")
                sonuc=((1+s1_1)**(-s2_1))*""" donem_sonu_duzenli_odemeler_serisi """ # burası bir problem yaratabilir.

def Ertelenmis_donem_basi_odemeler_islemi():
        pencere_12=Toplevel()
        pencere_12.geometry("450x300")
        def ertelenmis_donem_basi_odeme_serisi():
                s1_1=("faiz")
                s2_1=("gecikme süresi")
                sonuc=((1+s1_1)**(-s2_1))*""" donem_basi_duzenli_odemler_serisi """

def Donem_sonu_sonsuz_odemeler_islemi():
        pencere_13=Toplevel()
        pencere_13.geometry("450x300")
        def donem_sonu_sonsuz_odemeler_serisi():
                s1=("faiz")
                sonuc=1/s1

def Donem_bası_sonsuz_odeme_islemi():
        pencere_14=Toplevel()
        pencere_14.geometry("450x300")
        def donem_basi_sonsuz_odeme_serisi():
                s1=("iskonto")
                sonuc=1/s1

def Surekli_duzenli_odeme_islemleri():
        pencere_15=Toplevel()
        pencere_15.geometry("450x300")
        def surekli_duzenli_odemeler_serisi():
                s1=("faiz oranı")
                s2=("ödeme adedi")
                s3=("Faiz kuvvet orani")
                sonuc=(1-((1+s1)**-s2))/s3

def Donem_sonu_artan_odeme_islemleri():
        pencere_16=Toplevel()
        pencere_16.geometry("450x300")
        def donem_sonu_artan_odeme_serisi():
                s1=("ödeme adedi")
                s2=("faiz orani")
                sonuc=(""" donem_basi_duzenli_odemler_serisi """-(s1*((1+s2)**(-s1))))/s2

def Donem_basi_artan_odeme_islemleri():
        pencere_17=Toplevel()
        pencere_17.geometry("450x300")
        def donem_basi_artan_odemeler_serisi():
                s1=("iskonto orani")
                s2=("ödeme adedi")
                s3=("faiz orani")
                sonuc=(""" donem_basi_duzenli_odemler_serisi """-(s2*((1+s3)**(-s2))))/s1

def Donem_sonu_azalan_odemeler_islemleri():
        pencere_18=Toplevel()
        pencere_18.geometry("450x300")
        def donem_sonu_azalan_ödemeler_serisi():
                s1=("ödeme adedi")
                s2=("faiz orani")
                sonuc=(s1-""" donem_sonu_duzenli_odemeler_serisi """)/s2

def Donem_basi_azalan_odemeler_islemi():
        pencere_19=Toplevel()
        pencere_19.geometry("450x300")
        def donem_basi_azalan_odemeler_serisi():
                s1=("odeme adedi")
                s3=("iskonto oranı")
                sonuc=(s1-""" donem_sonu_duzenli_odemeler_serisi """)/s3

#Ana pencere etkileşimi
#etiketler
baslik=tk.Label(pencere_1,text="Yapmak istediğiniz işlemi seçiniz.",background="#85bfcd",font="Courier 14 bold")
baslik.place(x=40,y=50)
#butınlar
mbtn=Menubutton(pencere_1,text="Peşinat İşlem Türü",relief=RAISED)
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