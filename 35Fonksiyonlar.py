#
#
# Fonksiyonlar
#
#


#
# Fonksiyon Tanımlamak ve Çağırmak
#

>>> def kayit_olustur(isim, soyisim, issis, sehir):
...     print("-"*30)
...     print("isim           : ", isim)
...     print("soyisim        : ", soyisim)
...     print("işletim sistemi: ", issis)
...     print("şehir          : ", sehir)
...     print("-"*30)
...



>>> kayit_olustur("Şahin","Beşinci","Ubuntu","Istanbul")
------------------------------
isim           :  Şahin
soyisim        :  Beşinci
işletim sistemi:  Ubuntu
şehir          :  Istanbul
------------------------------


#
# Fonksiyonların Yapısı
#

>>> def bir_fonksiyon():
        (...)

>>> def selamla():
...     print("Elveda Zalim Dünya!")
...
>>> selamla()
Elveda Zalim Dünya!


>>> def sistem_bilgisi_göster():
...     import sys
...     print("\nSistemde kurulu Python'ın;")
...     print("\tana sürüm numarası:", sys.version_info.major)
...     print("\talt sürüm numarası:", sys.version_info.minor)
...     print("\tminik sürüm numarası:", sys.version_info.micro)
...     print("\nKullanılan işletim sisteminin;")
...     print("\tadı:", sys.platform)
...
>>> sistem_bilgisi_göster()

Sistemde kurulu Python'ın;
        ana sürüm numarası: 3
        alt sürüm numarası: 6
        minik sürüm numarası: 8

Kullanılan işletim sisteminin;
        adı: linux


>>> def kare_bul():
...     sayı = 12
...     çıktı = "{} sayısının karesi {} sayısıdır"
...     print(çıktı.format(sayı, sayı**2))
...
>>> kare_bul()
12 sayısının karesi 144 sayısıdır

>>> def kare_bul(sayı):
...     çıktı = "{} sayısının karesi {} sayısıdır"
...     print(çıktı.format(sayı, sayı**2))
...
>>> kare_bul(100)
100 sayısının karesi 10000 sayısıdır


>>> def uzunluk(öğe):
...     c = 0
...     for s in öğe:
...         c += 1
...     print(c)
...
>>> uzunluk("şahin")
5
>>> uzunluk("istihza")
7
>>> uzunluk("Afyonkarahisar")
14
>>> uzunluk("Tarım ve Köyişleri Bakanlığı")
28

>>> liste = ["ahmet", "mehmet", "veli"]
>>> uzunluk(liste)
3


#
# Parametreler ve Argümanlar
#

>>> def kopyala(kaynak_dosya, hedef_dizin):
...     çıktı = "{} adlı dosya {} adlı dizin içine kopyalandı!"
...     print(çıktı.format(kaynak_dosya, hedef_dizin))
...
>>> kopyala("deneme.txt", "/home/istihza/Desktop")
deneme.txt adlı dosya /home/istihza/Desktop adlı dizin içine kopyalandı!


#
# Sıralı (veya İsimsiz) Parametreler
#

>>> def kayıt_oluştur(isim, soyisim, işsis, şehir):
...     print("-"*30)
...     print("isim           : ", isim)
...     print("soyisim        : ", soyisim)
...     print("işletim sistemi: ", işsis)
...     print("şehir          : ", şehir)
...     print("-"*30)
...
>>> kayıt_oluştur("Ahmet", "Öz", "Debian", "Ankara")
------------------------------
isim           :  Ahmet
soyisim        :  Öz
işletim sistemi:  Debian
şehir          :  Ankara
------------------------------


#
# İsimli Parametreler
#

>>> def kayıt_oluştur(isim, soyisim, işsis, şehir):
...     print("-"*30)
...     print("isim           : ", isim)
...     print("soyisim        : ", soyisim)
...     print("işletim sistemi: ", işsis)
...     print("şehir          : ", şehir)
...     print("-"*30)
...
>>> kayıt_oluştur(soyisim="Öz", isim="Ahmet", işsis="Debian", şehir= "Ankara")
------------------------------
isim           :  Ahmet
soyisim        :  Öz
işletim sistemi:  Debian
şehir          :  Ankara
------------------------------


>>> kayıt_oluştur(soyisim="Öz", isim="Ahmet", "Debian", "Ankara")
  File "<stdin>", line 1
SyntaxError: positional argument follows keyword argument


#
# Varsayılan Değerli Parametreler
#

>>> def kur(kurulum_dizini="/usr/bin/"):
...     print("Program {} dizinine kuruldu!".format(kurulum_dizini))
...
>>> kur()
Program /usr/bin/ dizinine kuruldu!

>>> kur("C:\\Users\\firat")
Program C:\Users\firat dizinine kuruldu!


>>> kur(kurulum_dizini="C:\\Users\\firat")
Program C:\Users\firat dizinine kuruldu!


#
# Rastgele Sayıda İsimsiz Parametre Belirleme
#

>>> def fonksiyon(*parametreler):
...     print(parametreler)
...
>>> fonksiyon(1, 2, 3, 4, 5)
(1, 2, 3, 4, 5)


>>> def carp(*sayılar):
...     sonuç = 1
...     for i in sayılar:
...         sonuç *= i
...     print(sonuç)
...
>>> carp(1, 2, 3, 4)
24

>>> print(*'TBMM', sep='.')
T.B.M.M

>>> liste = ["Ahmet", "Mehmet", "Veli"]
>>> print(*liste)
Ahmet Mehmet Veli

>>> sözlük = {"a": 1, "b": 2}
>>> print(*sözlük)
a b

>>> print(*sözlük.items())
('a', 1) ('b', 2)

>>> print(*sözlük.keys())
a b

>>> print(*sözlük.values())
1 2



#
# Rastgele Sayıda İsimli Parametre Belirleme
#

>>> def fonksiyon(**parametreler):
...     print(parametreler)
...
>>> fonksiyon(isim="Ahmet", soyisim="Öz", meslek="Mühendis", şehir="Ankara")
{'isim': 'Ahmet', 'soyisim': 'Öz', 'meslek': 'Mühendis', 'şehir': 'Ankara'}


>>> def karşılık_bul(*args, **kwargs):
...     for sözcük in args:
...         if sözcük in kwargs:
...             print("{} = {}".format(sözcük, kwargs[sözcük]))
...         else:
...             print("{} kelimesi sözlükte yok!".format(sözcük))
...
>>> sözlük = {"kitap"      : "book",
...           "bilgisayar" : "computer",
...           "programlama": "programming"}
>>> karşılık_bul("kitap", "bilgisayar", "programlama", "fonksiyon", **sözlük)
kitap = book
bilgisayar = computer
programlama = programming
fonksiyon kelimesi sözlükte yok!


>>> def bas(*args, start='', **kwargs):
...     for öğe in args:
...         print(start+öğe, **kwargs)
...
>>> bas('öğe1', 'öğe2', 'öğe3', start="#.")
#.öğe1
#.öğe2
#.öğe3



#
# return Deyimi
#

>>> def ismin_ne():
...     isim = input("ismin ne? ")
...     return isim
...
>>> isim = ismin_ne()
ismin ne? Vedat

>>> isim
'Vedat'


#
# Örnek bir Uygulama
#

import random

def sayı_üret(başlangıç=0, bitiş=500, adet=6):
    sayılar = set()
    while len(sayılar) < adet:
        sayılar.add(random.randrange(başlangıç, bitiş))
    return sayılar

>>> import random
>>> sayı_üret()
{356, 136, 113, 498, 276, 58}

>>> [i for i in dir(random) if not i.startswith("_")]
['BPF', 'LOG4', 'NV_MAGICCONST', 'RECIP_BPF', 'Random', 'SG_MAGICCONST', 'SystemRandom', 'TWOPI', 'betavariate', 'choice', 'choices', 'expovariate', 'gammavariate', 'gauss', 'getrandbits', 'getstate', 'lognormvariate', 'normalvariate', 'paretovariate', 'randint', 'random', 'randrange', 'sample', 'seed', 'setstate', 'shuffle', 'triangular', 'uniform', 'vonmisesvariate', 'weibullvariate']

>>> liste = ["ahmet", "mehmet", "sevgi", "sevim", "selin", "zeynep", "selim"]
>>> random.sample(liste, 2)
['sevim', 'ahmet']

>>> random.sample(liste, 2)
['sevgi', 'zeynep']

>>> random.sample(liste, 5)
['selin', 'zeynep', 'ahmet', 'selim', 'mehmet']


>>> liste = ["ahmet", "mehmet", "sevgi", "sevim",
... "selin", "zeynep", "selim"]
>>> random.shuffle(liste)
>>> liste
['zeynep', 'selin', 'mehmet', 'sevgi', 'sevim', 'ahmet', 'selim']


r>>> random.randrange(0, 500)
156

>>> import random
>>>
>>> def sayı_üret(başlangıç=0, bitiş=500, adet=6):
...     sayılar = set()
...     while len(sayılar) < adet:
...         sayılar.add(random.randrange(başlangıç, bitiş))
...     return sayılar
...
>>> sayı_üret(5,15,6)
{5, 6, 8, 9, 11, 13}

>>> sayı_üret()
{2, 34, 486, 232, 41, 52}



#
# Fonksiyonların Kapsamı ve global Deyimi
#

>>> x = 0

>>> def fonk():
...     x = 1
...     return x
...
>>> print('fonksiyon içindeki x: ', fonk())
fonksiyon içindeki x:  1

>>> print('fonksiyon dışındaki x: ', x)
fonksiyon dışındaki x:  0


>>> x = []
>>> print('x\'in ilk hali:', x)
x'in ilk hali: []

>>> def değiştir():
...     print('x\'i değiştiriyoruz...')
...     x.append(1)
...     return x
...
>>> değiştir()
x'i değiştiriyoruz...
[1]
>>> print('x\'in son hali: ', x)
x'in son hali:  [1]


>>> x = set()

>>> def fonk():
...     x.add(10)
...     return x
...
>>> print(fonk())
{10}


>>> isim = 'Fırat'
>>> def fonk():
...     global isim
...     isim += ' Özgül'
...     return isim
...
>>> print(fonk())
Fırat Özgül


>>> isim_listesi = []
>>> def fonk():
...     isim_listesi += ['Fırat Özgül', 'Orçun Kunek']
...     return isim_listesi
...
>>> print(fonk())
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<stdin>", line 2, in fonk
UnboundLocalError: local variable 'isim_listesi' referenced before assignment


>>> def fonk():
...     isim_listesi.extend(['Fırat Özgül', 'Orçun Kunek'])
...     return isim_listesi
...
>>> print(fonk())
['Fırat Özgül', 'Orçun Kunek']
