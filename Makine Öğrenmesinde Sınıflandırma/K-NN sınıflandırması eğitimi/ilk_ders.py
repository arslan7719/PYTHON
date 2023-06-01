import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt

veri=pd.read_excel("Siniflandirma.xlsx") # veri setini bu kısında dosyamızdan okuyoruz.

x=veri.iloc[:,[2,3]].values # yaş ve tahmini maaş değişkenlerini almış oldu.
y=veri.iloc[:,4].values # satın aldımı değişkenini aldı

from sklearn.model_selection import train_test_split # yeni sürümde model_selection kullanılmaktadır.
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.25,random_state=0) 
# veri setinde bir kısmını eğitmek kalan bir kısmınıda test etmek için ayırmış olduk.

from sklearn.preprocessing import StandardScaler
sc_x=StandardScaler() # standartlaştırma başlatıldı.
x_train=sc_x.fit_transform(x_train)
x_test=sc_x.fit_transform(x_test)
#değişkenler aynı birimde olmadığı için ölçeklendirme yapıyoruz.

from sklearn.neighbors import KNeighborsClassifier
classifier = KNeighborsClassifier(n_neighbors=5,metric="minkowski",p=2)
classifier.fit(x_train,y_train)
# en yakın komuşu modelini oluşturduk.
#n_neighbors: komşu sayısnı anlamında kullanılır.
#metric:  komşuların yakınlığını belirlemede kullanılır.
#p: mesefa yöntemi belirtilir.

y_pred = classifier.predict(x_test) # ayırmış olduğumuz veri ile tahmin verisini karşılaştırma yapacağız.
"""print(y_pred,y_test)""" # tahmin edilenle test verileri karşılaştırdı.

from sklearn.metrics import confusion_matrix
cm=confusion_matrix(y_test,y_pred)
print(cm) # test verimiz ile tahmin verimiz arasında ki hatalar belirlendi ve yedi hata oldğunu gösterir.

from matplotlib.colors import ListedColormap
x_set,y_set=x_test,y_test
x1,x2=np.meshgrid(np.arange(start=x_set[:,0].min()-1,stop=x_set[:,0].max()+1,step=0.01),
                  np.arange(start=x_set[:,1].min()-1,stop=x_set[:,1].max()+1,step=0.01))
plt.contourf(x1,x2,classifier.predict(np.array([x1.ravel(),x2.ravel()]).T).reshape(x1.shape),alpha=0.75,cmap=ListedColormap(("lightblue","lightgreen")))
plt.xlim(x1.min(),x1.max())
plt.ylim(x2.min(),x2.max())
for i, j in enumerate(np.unique(y_set)):
     plt.scatter(x_set[y_set == j, 0], x_set[y_set == j, 1],
                 c = ListedColormap(('red', 'black'))(i), label = j)
plt.title('K En Yakın Komşu (Eğitim Seti)')
plt.xlabel('Yaş')
plt.ylabel('Maaş')
plt.legend()
plt.show() 
# test verilerinde 7 adet yanılma olduğu gözlemlenmiştir.