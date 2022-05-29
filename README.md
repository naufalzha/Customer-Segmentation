# Customer-Segmentation
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Made withJupyter](https://img.shields.io/badge/Made%20with-Jupyter-orange?style=for-the-badge&logo=Jupyter)

Membagi Customer ke beberapa cluster, agar dapat membuat strategi pemasaran yang lebih tepat dan juga efisien bagi tiap tiap pelanggan, you can acces the data in [Custommer Segmentation Data](https://dqlab-dataset.s3-ap-southeast-1.amazonaws.com/customer_segments.txt)

## Pre-Processing Data
`Data Numerik : Variabel Umur dan Variabel Nilai Belanja Setahun`

**1. Eksplorasi Data**

<img src="/Gambar/Ekplorasi%20Data%20Numerik.svg"  width="750" height="750">

**2. Standarisasi Data**

Menampilkan __3 Data teratas hasil standarisasi__

|    Umur  Sebelum     |    Belanja Sebelum    |    Umur Sesudah      |     Belanja Sesudah   |                  
| ---------------------| ----------------------| ---------------------| ----------------------|
|58 |             9497927|1.411245     |        0.946763|
|14 |             2722700|-1.617768    |       -1.695081|
|48 |             5286429|0.722833     |       -0.695414|



`Variabel Katagorik : Variabel Jenis Kelami, Variabel Profesi dan Variabel Tipe Residen`
**1. Ekplorasi Data** 
<img src="/Gambar/Ekplorasi%20Data%20Katagorik.svg"  width="550" >

**2. Label Encoding**

Menampilkan __3 Data teratas hasil Label Encoding__
| Jenis Kelamin  Sebelum | Profesi Sebelum    |  Tipe Residen sebelum | Jenis Kelamin Sesudah | Profesi Sesudah   |  Tipe Residen sesudah                
| ---------------------| ----------------------| ---------------------| ----------------------| ---------------------| ----------------------|
|Pria |             Wiraswasta |        Sector|0          |4      |1|
|Wanita|             Pelajar |       Cluster|1            |2      |0|
|Pria |             Professional    |       Cluster|0        |3      |0|

## Modelling
Jenis machine learning yang diterapkan adalah Unsupervised Learning atau clustering, dengan model yang akan digunakan kali ini adalah [**KPrototypes**](https://kprototypes.readthedocs.io/en/latest/). Model ini digunakan karena cocok untuk data campuran yang bertipe numerik dan katagorik.

**1. Menentukan Jumlah Cluster Optimal** 

<img src="/Gambar/Nilai%20K%20Optimal.png"  width="500" height="500">

dapat dilihat dari gambar diatas bahwa nilai cluster optimal yang terbentuk adalah **5 Cluster**


**2. Model** 

model yang digunakan dapat di akses [DI SINI](/Model)

**3. Hasil Pengelompokan** 

Hasil pengelompokan customer bedasarkan data yang ada dengan menggunakan algoritma KPrototypes dapat dilihat [DI SINI](Hasil%20Pengelompokan/hasil%20pengelompokan%20customer.csv)

## Kesimpulan 

**1. Visualisasi Bedasarkan Variabel** 

karakteristik kelompok bedasarkan setiap variabel dapat dilihat [DI SINI](Hasil%20Pengelompokan/Visualisasi%20Hasil)

**2. Keterangan Kelompok** 
| Cluster | Keterangan  |
| --------| ------------|
|0|Young Entreprenuer, Customer dengan rata-rata belanja 10 juta dengan umur 18-41 tahun dan rata-rata umur 29 tahun
|1|Senior Entreprenuer, Customer dengan rata-rata belanja 10 juta dengan umur 45-64 tahun dan rata-rata umur 51 tahun
|2|Student, Customer pelajar dan mahasiswa dengan rata-rata umur 16 tahun dan nilai belanja mendekati 3 juta
|3|Young Member, Customer professional atau ibu rumah tangga dengan umur 20-40 atau rata rata usia 30 tahun dan  rata-rata belanja mendekati 6 juta
|4|Senior Member, Customer professional atau ibu rumah tangga dengan umur 46-6 atau rata rata usia 53 tahun dan  rata-rata belanja mendekati 6 juta

-------------------------------------------------------------------------------------------------------------------------------------------------------
Thank You For Attention! :grin: , See u Next Project :v:

©Naufal Zhafran Albaqi-

