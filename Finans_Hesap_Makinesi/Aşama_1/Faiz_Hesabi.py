# Basit faiz işlemleri
x=int(input("Anapara'yı belirtiniz:"))
y=int(input("Faiz işleme süresini belirtiniz:"))
z=float(input("Faiz oranını belirtiniz (0.05 halinde):"))

basit_faiz=x*(1+(z*y))

print("Basit faiz tutarı:",basit_faiz)

# bileşik Faiz işlemleri

""" atamalar girişde yapıldığı için direk formule geçildi  """

bilesik_faiz=x*((1+z)**y)
print("Bileşik Faiz Tutarı:",bilesik_faiz)