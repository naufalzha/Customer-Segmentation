#Library
import pandas as pd                                 #Proses Analisis Data
import matplotlib.pyplot as plt                     #Visualisasi Data
import seaborn as sns                               #Visualisasi Data
from sklearn.preprocessing  import LabelEncoder     #Mengubah kategorik menjadi dummy
from sklearn.preprocessing import StandardScaler   

from kmodes.kmodes import KModes                    #Pemodelan KMods
from kmodes.kprototypes import KPrototypes          #Pemodelan KPrototypess

# Deskripsi Statistik
# import dataset  
df = pd.read_csv("https://dqlab-dataset.s3-ap-southeast-1.amazonaws.com/customer_segments.txt", sep="\t")
print('\033[92m' +' 5 Data Teratas:\033[0m')
print(df.head())         #Menampilkan Data teratas
print('\n')
print('\033[92m' +' Data Info:\033[0m')
print(df.info())         #Info Data

#sebaran data numerik
sns.set(style='white')
plt.clf()
  
# Fungsi untuk membuat plot  
def sebarandata(features):  
    fig, axs = plt.subplots(2, 2, figsize=(10, 9))
    for i, kol in enumerate(features):
	    sns.boxplot(df[kol], ax = axs[i][0])
	    sns.distplot(df[kol], ax = axs[i][1])   
	    axs[i][0].set_title('mean = %.2f\n median = %.2f\n std = %.2f'%(df[kol].mean(), df[kol].median(), df[kol].std()))
    plt.tight_layout()
    plt.show()
  
# Memanggil fungsi untuk membuat Plot untuk data numerik  
kolom_numerik = ['Umur','NilaiBelanjaSetahun']
sebarandata(kolom_numerik)

#sebaran data Katagorik
plt.clf() 
# Menyiapkan kolom kategorikal  
kolom_kategorikal = ['Jenis Kelamin','Profesi', 'Tipe Residen'] 
# Membuat canvas
fig, axs = plt.subplots(3,1,figsize=(7,10)) 
# Membuat plot untuk setiap kolom kategorikal  
for i, kol in enumerate(kolom_kategorikal):  
    # Membuat Plot
    sns.countplot(df[kol], order = df[kol].value_counts().index, ax = axs[i])  
    axs[i].set_title('\nCount Plot %s\n'%(kol), fontsize=15)  
    # Memberikan anotasi  
    for p in axs[i].patches:  
        axs[i].annotate(format(p.get_height(), '.0f'),  
                        (p.get_x() + p.get_width() / 2., p.get_height()),  
                        ha = 'center',  
                        va = 'center',  
                        xytext = (0, 10),  
                        textcoords = 'offset points')      
    # Setting Plot  
    sns.despine(right=True,top = True, left = True)  
    axs[i].axes.yaxis.set_visible(False) 
    plt.tight_layout()

# Tampilkan plot
plt.show()

## Pre-Processing Data
print('\033[92m' +'Sebelum standardisasi:\033[0m')
print(df[kolom_numerik].head())

kolom_numerik = ['Umur','NilaiBelanjaSetahun']
# Standardisasi
df_std = StandardScaler().fit_transform(df[kolom_numerik])
# Membuat DataFrame
df_std = pd.DataFrame(data=df_std, index=df.index, columns=df[kolom_numerik].columns)

# Menampilkan contoh isi data dan summary statistic
print('\033[92m' +'Contoh hasil standardisasi:\033[0m')
print(df_std.head())

# Inisiasi nama kolom kategorikal
kolom_kategorikal = ['Jenis Kelamin','Profesi','Tipe Residen']
print('\033[92m' +'Sebelum di Konvensi Katagorik Jadi Angka:\033[0m')
print(df[kolom_kategorikal].head())

# Membuat salinan data frame
df_encode = df[kolom_kategorikal].copy()


# Melakukan labelEncoder untuk semua kolom kategorikal
for col in kolom_kategorikal:
		df_encode[col] = LabelEncoder().fit_transform(df_encode[col])

# Menampilkan data
print('\033[92m' +'Sesudah Konvensi Katagorik Jadi Angka:\033[0m')
print(df_encode.head())

#Analisis
# Menggabungkan data frame
df_model = df_encode.merge(df_std, left_index = True, right_index=True, how = 'left')
print('\033[92m' +' Tabal Pakai:\033[0m')
print (df_model.head())

# Jumlah Kluster
# Melakukan Iterasi untuk Mendapatkan nilai Cost  
cost = {}  
for k in range(2,10):  
    kproto = KPrototypes(n_clusters = k,random_state=75)  
    kproto.fit_predict(df_model, categorical=[0,1,2])  
    cost[k]= kproto.cost_  
  
# Memvisualisasikan Elbow Plot  
sns.pointplot(x=list(cost.keys()), y=list(cost.values())) 
plt.title('S')
plt.show()

# Menggunakan Model
kproto = KPrototypes(n_clusters=5, random_state = 75)
kproto = kproto.fit(df_model, categorical=[0,1,2])

# Menentukan segmen tiap pelanggan
clusters = kproto.predict(df_model, categorical=[0,1,2])
# Menggabungkan data awal dan segmen pelanggan
df_final = df.copy()
df_final['cluster'] = clusters
print('\033[92m' +' Halis Cluster:\033[0m')
print(df_final.head()) 

## Visualisasi Cluster Bedasarkan variabel
# Data Kategorikal  
kolom_categorical = ['Jenis Kelamin','Profesi','Tipe Residen']  
  
for i in kolom_categorical:  
    plt.figure(figsize=(6,4))  
    ax = sns.countplot(data = df_final, x = 'cluster', hue = i )  
    plt.title('\nCount Plot {}\n'.format(i), fontsize=12)  
    ax.legend(loc='right', bbox_to_anchor =(1.5,0.5), shadow = True, ncol=1)  
    for p in ax.patches:  
        ax.annotate(format(p.get_height(), '.0f'),  
                    (p.get_x() + p.get_width() / 2., p.get_height()),  
                     ha = 'center',  
                     va = 'center',  
                     xytext = (0, 10),  
                     textcoords = 'offset points')  
      
    sns.despine(right=True,top = True, left = True)  
    ax.axes.yaxis.set_visible(False)  
    plt.show()  
    
# Data Numerical
kolom_numerik = ['Umur','NilaiBelanjaSetahun']  
  
for i in kolom_numerik:  
    plt.figure(figsize=(6,4))  
    ax = sns.boxplot(x = 'cluster',y = i, data = df_final)  
    plt.title('\nBox Plot {}\n'.format(i), fontsize=12)  
    plt.show()  
    
###################################################################
