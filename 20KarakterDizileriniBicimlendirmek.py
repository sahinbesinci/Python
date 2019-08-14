#
#
# Karakter Dizilerini Biçimlendirmek
#
#


#
# % İşareti ile Biçimlendirme (Eski Yöntem)
#

>>> parola = input("parola: ")
parola: test
>>> print("Girdiğiniz parola (%s) kurallara uygun bir paroladır!" %parola)
Girdiğiniz parola (test) kurallara uygun bir paroladır!

>>> print("%s ve %s iyi bir ikilidir!" %("Python", "Django"))
Python ve Django iyi bir ikilidir!

>>> for i in range(100):
...     print("%s" %i)
...

#Burada % işaretini arka arkaya iki kez kullanarak bir adet % işareti elde ettik. 
>>> for i in range(100):
...     print("%%%s" %i)
...

>>> print("Karakter dizilerinin toplam %s adet metodu vardır" %len(dir(str)))
Karakter dizilerinin toplam 77 adet metodu vardır

>>> for i in dir(str):
...     print("%15s" %i)
        __add__
      __class__
   __contains__
    __delattr__
        __dir__

>>> print("|%15s|" %"istihza")
|        istihza|

>>> print("istihza".rjust(15))
        istihza

>>> print("|%s|" %"istihza".rjust(15))
|        istihza|

>>> print("|%-15s|" %"istihza")
|istihza        |

>>> print("|%s|" %"istihza".ljust(15))
|istihza        |

print("depoda %(miktar)s kilo %(ürün)s kaldı" %{"miktar": 25,"ürün": "elma"})
depoda 25 kilo elma kaldı

# "%(değişken_adı)s" % {"değişken_adı": "değişken_değeri"}


#
# Biçimlendirme Karakterleri
#

# %s

>>> print("Benim adım %s" %"istihza")
Benim adım istihza

# %d, %i
# i harfi de integer, yani ‘tam sayı’ kelimesinin kısaltmasıdır. Kullanım ve işlev olarak, d harfinden hiç bir farkı yoktur.

>>> print("Şubat ayı bu yıl %d gün çekiyor" %28)
Şubat ayı bu yıl 28 gün çekiyor.


>>> print("Şubat ayı bu yıl %s gün çekiyor" %28)
Şubat ayı bu yıl 28 gün çekiyor

>>> print("Şubat ayı bu yıl %d gün çekiyor" %"yirmi sekiz")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: %d format: a number is required, not str


>>> print("%d" %13.5)
13

>>> sayı = 13.5
>>> print("%d" %float(sayı))
13

>>> print("%10.5d" %23)
     00023

>>> print("%010.d" %23)
0000000023

>>> "23".zfill(10)
'0000000023'

>>> "%-5d" %10
'10   '


# %o

>>> print("%i sayısının sekizli düzendeki karşılığı %o sayısıdır." %(10, 10))
10 sayısının sekizli düzendeki karşılığı 12 sayısıdır.


# %x, %X
# %X tıpkı x harfinde olduğu gibi, onaltılı düzendeki sayıları temsil eder. Ancak bunun farkı, harfle gösterilen onaltılı sayıları büyük harfle temsil etmesidir

print("%i sayısının onaltılı düzendeki karşılığı %x sayısıdır." %(20, 20))
20 sayısının onaltılı düzendeki karşılığı 14 sayısıdır.


# %f

>>> print("Dolar %f TL olmuş..." %1.4710)
Dolar 1.471000 TL olmuş...

>>> print("%f" %10)
10.000000

>>> print("%f"%23.6)
23.600000

>>> print("%.2f" % 10)
10.00

>>> print("%.1f" % 10)
10.0


# %c

>>> print("%c" %"a")
a

>>> print("%c" %65)
A

>>> for i in range(128):
...     print("%s ==> %c" %(i, i))
..
41 ==> )
42 ==> *
43 ==> +
44 ==> ,
45 ==> -
46 ==> .
47 ==> /
48 ==> 0
49 ==> 1
50 ==> 2
..



#
# format() Metodu ile Biçimlendirme (Yeni Yöntem)
#

>>> print("{} ve {} iyi bir ikilidir!".format("Django", "Python"))
Django ve Python iyi bir ikilidir!


kalkış       = "İstanbul"
varış        = "Trabzon"
isim_soyisim = "Şahin Beşinci"
bilet_sayısı = "1"
print("{} noktasından {} noktasına, 14:30 hareket saatli sefer için {} adına {} adet bilet ayrılmıştır!".format(kalkış,varış,isim_soyisim,bilet_sayısı))
İstanbul noktasından Trabzon noktasına, 14:30 hareket saatli sefer için Şahin Beşinci adına 1 adet bilet ayrılmıştır!

>>> "{0} {1}".format("Fırat", "Özgül")
'Fırat Özgül'

>>> "{1} {0}".format("Fırat", "Özgül")
'Özgül Fırat'

>>> "{0} {1} ({1} {0})".format("Fırat", "Özgül")
'Fırat Özgül (Özgül Fırat)'

>>> print("{dil} dersleri".format(dil="python"))
python dersleri

#   >	sağa yaslama
#   <	sola yaslama
#   ^	ortalama

>>> print("|{:>15}|".format("istihza"))
|       istihza|

>>> print("|{:<15}|".format("istihza"))
|istihza        |

>>> print("|{:^15}|".format("istihza"))
|    istihza    |


# 
#  s,c ,d, o, x, X, b, f, ','
# 

>>> print("{:s}".format("karakter dizisi"))
karakter dizisi

>>> print("{:s} ve {:s} iyi bir ikilidir!".format("Python", "Django"))
Python ve Django iyi bir ikilidir!

>>> print("{:c}".format(65))
A

>>> print("{:d}".format(65))
65

>>> print("{:o}".format(65))
101

>>> print("{:x}".format(65))
41

>>> "{:X}".format(65)
'41'

>>> "{:b}".format(2)
'10'

>>> print("{:.2f}".format(50))
50.00

>>> "{:,}".format(1234567890)
'1,234,567,890'

