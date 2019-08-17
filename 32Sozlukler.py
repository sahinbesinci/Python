#
#
# Sözlükler
#
#

>>> çeviri_tablosu = {"Ö": "O",
...                   "ç": "c",
...                   "Ü": "U",
...                   "Ç": "C",
...                   "İ": "I",
...                   "ı": "i",
...                   "Ğ": "G",
...                   "ö": "o",
...                   "ş": "s",
...                   "ü": "u",
...                   "Ş": "S",
...                   "ğ": "g"}


#
# Sözlük Tanımlamak
#

>>> kelimeler = {"kitap": "book"}

>>> sözlük = {}

>>> type(sözlük)
<class 'dict'>

>>> len(kelimeler)
1

>>> kelimeler = {"kitap": "book", "bilgisayar": "computer"}
>>> len(kelimeler)
2

>>> sözlük = {"kitap"      : "book",
...           "bilgisayar" : "computer",
...           "programlama": "programming",
...           "dil"        : "language",
...           "defter"     : "notebook"}


#
# Sözlük Öğelerine Erişmek
#


>>> print(sözlük["kitap"])
book

>>> print(sözlük["bilgisayar"])
computer

>>> çeviri_tablosu = {"Ö": "O",
...                   "ç": "c",
...                   "Ü": "U",
...                   "Ç": "C",
...                   "İ": "I",
...                   "ı": "i",
...                   "Ğ": "G",
...                   "ö": "o",
...                   "ş": "s",
...                   "ü": "u",
...                   "Ş": "S",
...                   "ğ": "g"}
>>> print(çeviri_tablosu["Ö"])
O
>>> print(çeviri_tablosu["ç"])
c
>>> print(çeviri_tablosu["Ü"])
U
>>> print(çeviri_tablosu["Ç"])
C
>>> print(çeviri_tablosu["İ"])
I
>>> print(çeviri_tablosu["ı"])
i
>>> print(çeviri_tablosu["Ğ"])
G
>>> print(çeviri_tablosu["ö"])
o
>>> print(çeviri_tablosu["Ş"])
S
>>> print(çeviri_tablosu["ğ"])
g



>>> for i in çeviri_tablosu:
...     print(çeviri_tablosu[i])
...
O
c
U
C
I
i
G
o
s
u
S
g



#
# Sözlüklerin Yapısı
#

>>> sözlük = {"sıfır": 0,
...           "bir"  : 1,
...           "iki"  : 2,
...           "üç"   : 3,
...           "dört" : 4,
...           "beş"  : 5}

>>> sözlük = {"Ahmet Özkoparan": ["İstanbul", "Öğretmen", 34],
...           "Mehmet Yağız"   : ["Adana", "Mühendis", 40],
...           "Seda Bayrak"    : ["İskenderun", "Doktor", 30]}

>>> print(sözlük["Seda Bayrak"])
['İskenderun', 'Doktor', 30]



>>> kişiler = {"Ahmet Özkoparan": {"Memleket": "İstanbul",
...                                "Meslek"  : "Öğretmen",
...                                "Yaş"     : 34},
...
...            "Mehmet Yağız"   : {"Memleket": "Adana",
...                                "Meslek"  : "Mühendis",
...                                "Yaş"     : 40},
...
...            "Seda Bayrak"    : {"Memleket": "İskenderun",
...                                "Meslek"  : "Doktor",
...                                "Yaş"     : 30}}
>>> print(kişiler["Mehmet Yağız"]["Memleket"])
Adana
>>> print(kişiler["Seda Bayrak"]["Yaş"])
30
>>> print(kişiler["Ahmet Özkoparan"]["Meslek"])
Öğretmen


>>> liste = [["Ahmet", "Mehmet", "Ayşe"],
...          ["Sedat", "Serkan", "Selin"],
...          ["Zeynep", "Nur", "Eda"]]
>>> print(liste[0][0])
Ahmet



#
# Sözlüklere Öğe Eklemek
#

>>> sözlük = {}

>>> sözlük["Ahmet"] = "Adana"

>>> print(sözlük)
{'Ahmet': 'Adana'}

>>> print(sözlük["Ahmet"])
Adana

>>> sözlük["Mehmet"] = "İstanbul"
>>> sözlük
{'Ahmet': 'Adana', 'Mehmet': 'İstanbul'}

>>> sözlük["Seda"] = "Mersin"
>>> sözlük
{'Ahmet': 'Adana', 'Mehmet': 'İstanbul', 'Seda': 'Mersin'}

>>> sözlük["Eda"] = "Tarsus"
>>> sözlük
{'Ahmet': 'Adana', 'Eda': 'Tarsus', 'Mehmet': 'İstanbul', 'Seda': 'Mersin'}


>>> sözlük = {'a': 1}
>>> sözlük = {'a': (1,2,3)}
>>> sözlük = {'a': 'kardiz'}
>>> sözlük = {'a': [1,2,3]}
>>> sözlük
{'a': [1, 2, 3]}



>>> sözlük = {}

>>> l = (1,2,3)
>>> sözlük[l] = 'falanca'
>>> sözlük
{(1, 2, 3): 'falanca'}

>>> l = 45
>>> sözlük[l] = 'falanca'
>>> sözlük
{45: 'falanca', (1, 2, 3): 'falanca'}

>>> l = 'kardiz'
>>> sözlük[l] = 'falanca'
>>> sözlük
{'kardiz': 'falanca', 45: 'falanca', (1, 2, 3): 'falanca'}




>>> l = [1,2,3]
>>> sözlük[l] = 'falanca'

Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unhashable type: 'list'


>>> l = {"a": 1, "b": 2, "c": 3}
>>> sözlük[l] = 'falanca'

Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unhashable type: 'dict'



#
# Sözlük Öğeleri Üzerinde Değişiklik Yapmak
#

>>> notlar = {'Seda': 98, 'Ege': 95, 'Mehmet': 77,
... 'Zeynep': 100, 'Deniz': 95, 'Ahmet': 45}

>>> notlar["Ahmet"] = 65
>>> print(notlar)
{'Seda': 98, 'Ege': 95, 'Mehmet': 77, 'Zeynep': 100, 'Deniz': 95, 'Ahmet': 65}



#
# Sözlük Üreteçleri (Dictionary Comprehensions)
#

>>> harfler = 'abcçdefgğhıijklmnoöprsştuüvyz'

>>> sözlük = {}
>>> for i in harfler:
...     sözlük[i] = harfler.index(i)
...

#    ve ya

>>> sözlük = {}
>>> for i in range(len(harfler)):
...     sözlük[harfler[i]] = i

#    ve ya

>>> sözlük = {i: harfler.index(i) for i in harfler}

>>> sözlük
{'a': 0, 'b': 1, 'c': 2, 'ç': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'ğ': 8, 'h': 9, 'ı': 10, 'i': 11, 'j': 12, 'k': 13, 'l': 14, 'm': 15, 'n': 16, 'o': 17, 'ö': 18, 'p': 19, 'r': 20, 's': 21, 'ş': 22, 't': 23, 'u': 24, 'ü': 25, 'v': 26, 'y': 27, 'z': 28}


>>> isimler = ["ahmet", "mehmet", "fırat", "zeynep", "selma", "abdullah", "cem"]

>>> sözlük = {i: len(i) for i in isimler}
>>> sözlük
{'ahmet': 5, 'mehmet': 6, 'fırat': 5, 'zeynep': 6, 'selma': 5, 'abdullah': 8, 'cem': 3}
