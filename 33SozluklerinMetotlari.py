#
#
# Sözlüklerin Metotları
#
#



#
# keys()
#

>>> sözlük = {"a": 0,
...           "b": 1,
...           "c": 2,
...           "d": 3}
>>> print(sözlük.keys())
dict_keys(['b', 'c', 'a', 'd'])

>>> liste = list(sözlük.keys())
>>> liste
['b', 'c', 'a', 'd']

>>> demet = tuple(sözlük.keys())
>>> demet
('b', 'c', 'a', 'd')

>>> kardiz = "".join(sözlük.keys())
>>> kardiz
'bcad'

>>> kardiz = ', '.join(sözlük.keys())
>>> kardiz
'b, c, a, d'


#
# values()
#

>>> sözlük
{'b': 1, 'c': 2, 'a': 0, 'd': 3}

>>> print(sözlük.values())
dict_values([1, 2, 0, 3])

>>> liste = list(sözlük.values())
>>> liste
[1, 2, 0, 3]

>>> demet = tuple(sözlük.values())
>>> demet
(1, 2, 0, 3)

>>> kardiz = "".join([str(i) for i in sözlük.values()])
>>> kardiz
'1203'

>>> kardiz = ", ".join([str(i) for i in sözlük.values()])
>>> kardiz
'1, 2, 0, 3'


#
# items()
#

>>> sözlük.items()
dict_items([('a', 0), ('b', 1), ('c', 2), ('d', 3)])

>>> for anahtar, değer in sözlük.items():
...     print("{} = {}".format(anahtar, değer))
...
a = 0
b = 1
c = 2
d = 3


#
# get()
# Birinci argüman sorgulamak istediğimiz sözlük öğesidir. İkinci argüman ise bu öğenin sözlükte bulunmadığı durumda kullanıcıya hangi mesajın gösterileceğini belirtir. 

>>> ing_sözlük = {"dil": "language", "bilgisayar": "computer", "masa": "table"}
>>> sorgu = input("Lütfen anlamını öğrenmek istediğiniz kelimeyi yazınız:")
Lütfen anlamını öğrenmek istediğiniz kelimeyi yazınız:dil

>>> print(ing_sözlük.get(sorgu, "Bu kelime veritabanımızda yoktur!"))
language


>>> sorgu = input("Lütfen anlamını öğrenmek istediğiniz kelimeyi yazınız:")
Lütfen anlamını öğrenmek istediğiniz kelimeyi yazınız:sarı

>>> print(ing_sözlük.get(sorgu, "Bu kelime veritabanımızda yoktur!"))
Bu kelime veritabanımızda yoktur!


#
# clear()
#

>>> lig = {"şampiyon": "Adana Demirspor", "ikinci": "Mersin İdman Yurdu", "üçüncü": "Adana Gençlerbirliği"}
>>> lig
{'şampiyon': 'Adana Demirspor', 'ikinci': 'Mersin İdman Yurdu', 'üçüncü': 'Adana Gençlerbirliği'}

>>> lig["şampiyon"]
'Adana Demirspor'

>>> lig["üçüncü"]
'Adana Gençlerbirliği'

>>> lig.clear()
>>> lig
{}

>>> del lig
>>> lig
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'lig' is not defined


#
# copy()
#

>>> hava_durumu = {"İstanbul": "yağmurlu", "Adana": "güneşli", "İzmir": "bulutlu"}
>>> yedek_hava_durumu = hava_durumu.copy()

>>> hava_durumu["Mersin"] = "sisli"
>>> hava_durumu
{'İstanbul': 'yağmurlu', 'Adana': 'güneşli', 'Mersin': 'sisli', 'İzmir':
'bulutlu'}

>>> yedek_hava_durumu
{'İstanbul': 'yağmurlu', 'Adana': 'güneşli', 'İzmir': 'bulutlu'}


#
# fromkeys()
#

>>> elemanlar = "Ahmet", "Mehmet", "Can"
>>> adresler = dict.fromkeys(elemanlar, "Kadıköy")
>>> adresler
{'Ahmet': 'Kadıköy', 'Mehmet': 'Kadıköy', 'Can': 'Kadıköy'}


#
# pop()
#

>>> sepet = {"meyveler": ("elma", "armut"), "sebzeler": ("pırasa", "fasulye"),
... "içecekler": ("su", "kola", "ayran")}
>>> sepet.pop("meyveler")
('elma', 'armut')

>>> sepet.pop("tatlılar")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 'tatlılar'

>>> sepet.pop("tatlılar", "Silinecek öğe yok!")
'Silinecek öğe yok!'


#
# popitem()
# bu metot öğeleri rastgele silmeyi tercih eder...


>>> sepet = {"meyveler": ("elma", "armut"), "sebzeler": ("pırasa", "fasulye")}
>>> sepet.popitem()
('sebzeler', ('pırasa', 'fasulye'))


#
# setdefault()
#

>>> sepet = {"meyveler": ("elma", "armut"), "sebzeler": ("pırasa", "fasulye")}
>>> sepet.setdefault("içecekler", ("su", "kola"))
('su', 'kola')

>>> sepet
{'meyveler': ('elma', 'armut'), 'sebzeler': ('pırasa', 'fasulye'), 'içecekler': ('su', 'kola')}

>>> sepet.setdefault("meyveler", ("erik", "çilek"))
('elma', 'armut')
>>> sepet
{'meyveler': ('elma', 'armut'), 'sebzeler': ('pırasa', 'fasulye'), 'içecekler': ('su', 'kola')}


#
# update()
#

>>> stok = {"elma": 5, "armut": 10, "peynir": 6, "sosis": 15}
>>> yeni_stok = {"elma": 3, "armut": 20, "peynir": 8, "sosis": 4, "sucuk": 6}
>>> stok.update(yeni_stok)
>>> print(stok)
{'elma': 3, 'armut': 20, 'peynir': 8, 'sosis': 4, 'sucuk': 6}

>>> yeni_stok = {"zeytin": 5}
>>> stok.update(yeni_stok)
>>> print(stok)
{'elma': 3, 'armut': 20, 'peynir': 8, 'sosis': 4, 'sucuk': 6, 'zeytin': 5}
