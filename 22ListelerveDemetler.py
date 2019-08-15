#
#
# Listeler ve Demetler
#
#



#
# Listeler 
#

>>> kardiz = "karakter dizisi"
>>> liste = ["öğe1", "öğe2", "öğe3"]
<class 'list'>

>>> liste = ["Ahmet", "Mehmet", 23, 65, 3.2]
>>> liste
['Ahmet', 'Mehmet', 23, 65, 3.2]

>>> liste = ["Ali", "Veli", ["Ayşe", "Nazan", "Zeynep"], 34, 65, 33, 5.6]
>>> liste
['Ali', 'Veli', ['Ayşe', 'Nazan', 'Zeynep'], 34, 65, 33, 5.6]

>>> for öğe in liste:
...     print("{} adlı öğenin veri tipi: {}".format(öğe, type(öğe)))
...
Ali adlı öğenin veri tipi: <class 'str'>
Veli adlı öğenin veri tipi: <class 'str'>
['Ayşe', 'Nazan', 'Zeynep'] adlı öğenin veri tipi: <class 'list'>
34 adlı öğenin veri tipi: <class 'int'>
65 adlı öğenin veri tipi: <class 'int'>
33 adlı öğenin veri tipi: <class 'int'>
5.6 adlı öğenin veri tipi: <class 'float'>

>>> komut = dir(str)
>>> type(komut)
<class 'list'>

>>> kardiz = "İstanbul Büyükşehir Belediyesi"
>>> kardiz.split()
['İstanbul', 'Büyükşehir', 'Belediyesi']

>>> liste = kardiz.split()
>>> liste[0]
'İstanbul'

>>> diller = ["İngilizce", "Fransızca", "Türkçe", "İtalyanca", "İspanyolca"]
>>> len(diller)
5

>>> sayılar = [[0, 10], [6, 60], [12, 54], [67, 99]]
>>> for i in sayılar:
...     print(range(*i))
...
range(0, 10)
range(6, 60)
range(12, 54)
range(67, 99)

>>> sayılar = [[0, 10], [6, 60], [12, 54], [67, 99]]
>>> for i in sayılar:
...     print(*range(*i))
...
0 1 2 3 4 5 6 7 8 9
6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59
12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53
67 68 69 70 71 72 73 74 75 76 77 78 79 80 81 82 83 84 85 86 87 88 89 90 91 92 93 94 95 96 97 98


#
# list() Fonksiyonu 
#

>>> isimler = "ahmet mehmet cem"
>>> isimler.split()
['ahmet', 'mehmet', 'cem']

>>> isimler = "elma, armut, çilek"
>>> isimler.split(", ")
['elma', 'armut', 'çilek']

>>> alfabe = "abcçdefgğhıijklmnoöprsştuüvyz"
>>> alfabe.split()
['abcçdefgğhıijklmnoöprsştuüvyz']

>>> alfabe.split("i")
['abcçdefgğhı', 'jklmnoöprsştuüvyz']

>>> harf_listesi = list(alfabe)
>>> print(harf_listesi)
['a', 'b', 'c', 'ç', 'd', 'e', 'f', 'g', 'ğ', 'h', 'ı', 'i', 'j',
 'k', 'l', 'm', 'n', 'o', 'ö', 'p', 'r', 's', 'ş', 't', 'u', 'ü',
 'v', 'y', 'z']

>>> k = "123"
>>> int(k)
123

>>> li = list()
>>> print(li)
[]

>>> list(range(10))
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


#
# Listelerin Öğelerine Erişmek 
#

>>> kardiz = "python"
>>> kardiz[0]
'p'

>>> meyveler = ["elma", "armut", "çilek", "kiraz"]
>>> meyveler[0]
'elma'

>>> meyveler = ["elma", "armut", "çilek", "kiraz"]
>>> for meyve in meyveler:
...     print(meyve)
...
elma
armut
çilek
kiraz

>>> meyveler = ["elma", "armut", "çilek", "kiraz"]
>>> for öğe_sırası in range(len(meyveler)):
...     print("{}. {}".format(öğe_sırası, meyveler[öğe_sırası]))
...
0. elma
1. armut
2. çilek
3. kiraz

>>> for sıra, öğe in enumerate(meyveler, 1):
...     print("{}. {}".format(sıra, öğe))
...
1. elma
2. armut
3. çilek
4. kiraz

>>> meyveler = ["elma", "armut", "çilek", "kiraz"]
>>> meyveler[-1]
'kiraz'

>>> meyveler[::-1]
['kiraz', 'çilek', 'armut', 'elma']


>>> liste = ["Ali", "Veli", ["Ayşe", "Nazan", "Zeynep"], 34, 65, 33, 
>>> len(liste)
7

>>> liste[2][0]
'Ayşe'

>>> liste[2][1]
'Nazan'

>>> liste[2][2]
'Zeynep'

>>> yeni_liste = liste[2]
>>> yeni_liste
['Ayşe', 'Nazan', 'Zeynep']

>>> yeni_liste[0]
'Ayşe'

>>> yeni_liste[1]
'Nazan'

>>> yeni_liste[2]
'Zeynep'

>>> liste = range(10)
>>> print(len(liste))
10

>>> liste[len(liste)-1]
9


#
# Listelerin Öğelerini Değiştirmek 
#

>>> kardiz = "istihza"
>>> kardiz = "İ" + kardiz[1:]
>>> kardiz
'İstihza'

>>> renkler = ["kırmızı", "sarı", "mavi", "yeşil", "beyaz"]
>>> print(renkler)
['kırmızı', 'sarı', 'mavi', 'yeşil', 'beyaz']

>>> renkler[0] = "siyah"
>>> print(renkler)
['siyah', 'sarı', 'mavi', 'yeşil', 'beyaz']

# renkler[öğe_sırası] = yeni_öğe

>>> renkler[2] = "mor"
>>> print(renkler)
['siyah', 'sarı', 'mor', 'yeşil', 'beyaz']

>>> liste = [1, 2, 3]
>>> liste[0:len(liste)]
[1, 2, 3]
>>> liste[0:3]
[1, 2, 3]
>>> liste[:]
[1, 2, 3]

>>> liste[0:len(liste)] = 5, 6, 7
>>> print(liste)
[5, 6, 7]



#
# Listeye Öğe Eklemek 
#

>>> liste = [2, 4, 5, 7]

>>> liste = liste + ["8"]
>>> liste
[1, 2, 3, '8']
>>> liste = liste + [8]
>>> liste
[1, 2, 3, '8', 8]


#
# Listeleri Birleştirmek 
#

>>> derlenen_diller = ["C", "C++", "C#", "Java"]
>>> yorumlanan_diller = ["Python", "Perl", "Ruby"]
>>> programlama_dilleri = derlenen_diller + yorumlanan_diller
>>> programlama_dilleri
['C', 'C++', 'C#', 'Java', 'Python', 'Perl', 'Ruby']

>>> liste = []
>>> alfabe = "sadfasdfasdfwer"
>>> for i in alfabe:
...     liste += i
...
>>> print(liste)
['s', 'a', 'd', 'f', 'a', 's', 'd', 'f', 'a', 's', 'd', 'f', 'w', 'e', 'r']

#
# Listeden Öğe Çıkarmak 
#

>>> liste = [1, 5, 3, 2, 9]
>>> del liste[-1]
>>> liste

[1, 5, 3, 2]

#
# Listeleri Silmek 
#

>>> liste = [1, 5, 3, 2, 9]
>>> del liste
>>> liste

Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'liste' is not defined


#
# Listeleri Kopyalamak 
#

#!!
>>> li1 = ["elma", "armut", "erik"]
>>> li2 = li1
>>> print(li1)
["elma", "armut", "erik"]
>>> print(li2)
["elma", "armut", "erik"]
>>> li1[0] = "karpuz"
>>> print(li1)
["karpuz", "armut", "erik"]
>>> print(li2)
["karpuz", "armut", "erik"]


>>> li1 = ["elma", "armut", "erik"]
>>> li2 = li1[:]
>>> li1[0] = "veli"
>>> li1
['veli', 'armut', 'erik']
>>> li2
['elma', 'armut', 'erik']


>>> liste1 = ["ahmet", "mehmet", "özlem"]
>>> liste2 = list(liste1)
>>> liste2
['ahmet', 'mehmet', 'özlem']
>>> liste1
['ahmet', 'mehmet', 'özlem']
>>> liste2[0] = 'veli'
>>> liste2
['veli', 'mehmet', 'özlem']
>>> liste1
['ahmet', 'mehmet', 'özlem']


#
# Liste Üreteçleri (List Comprehensions) 
#


>>> liste = [i for i in range(1000)]

>>> liste = []
>>> for i in range(1000):
...     liste += [i]


>>> liste = [i for i in range(1000) if i % 2 == 0]

>>> liste = []
>>> for i in range(1000):
...     if i % 2 == 0:
...         liste += [i]

>>> liste = [[1, 2, 3],
...          [4, 5, 6],
...          [7, 8, 9],
...          [10, 11, 12]]
>>> tümü = [z for i in liste for z in i]
>>> print(tümü)
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]



#
# Demetler
#

#
# Demet Tanımlamak
#


>>> demet = ("ahmet", "mehmet", 23, 45)
>>> type(demet)
<class 'tuple'>

>>> demet = "ahmet", "mehmet", 23, 45

>>> tuple('abcdefg')
('a', 'b', 'c', 'd', 'e', 'f', 'g')

>>> tuple(["ahmet", "mehmet", 34, 45])
('ahmet', 'mehmet', 34, 45)

#
# Tek Öğeli bir Demet Tanımlamak
#

>>> demet = ('ahmet')
>>> type(demet)
<class 'str'>

>>> demet = ('ahmet',)
>>> demet = 'ahmet',
>>> type(demet)
<class 'tuple'>


#
# Demetlerin Öğelerine Erişmek
#

>>> demet = ('elma', 'armut', 'kiraz')
>>> demet[0]
'elma'

>>> demet[-1]
'kiraz'

>>> demet[:2]
('elma', 'armut')


#
# Demetlerle Listelerin Birbirinden Farkı
# 
# listelerin değiştirilebilir (mutable) bir veri tipi iken, demetlerin değiştirilemez (immutable) bir veri tipi olmasıdır. Fakat her iki veri tipi de eklenebilirdir.
# 

>>> demet = ('elma', 'armut', 'kiraz')
>>> demet[0] = 'karpuz'

Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'tuple' object does not support item assignment

>>> demet = ('ahmet', 'mehmet')
>>> demet = demet + ('selin',)


#
# Demetlerin Kullanım Alanı
# Ama aslında oldukça yaygın kullanılan bir veri tipidir bu. Özellikle programların ayar (conf) dosyalarında bu veri tipi sıklıkla kullanılır. Örneğin Python tabanlı bir web çatısı (framework) olan Django’nun settings.py adlı ayar dosyasında pek çok değer bir demet olarak saklanır.

TEMPLATE_DIRS = ('/home/projects/djprojects/blog/templates',)

