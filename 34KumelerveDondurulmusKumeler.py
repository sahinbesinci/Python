#
#
# Kümeler ve Dondurulmuş Kümeler
#
#



#
# Kümeler > Küme Oluşturmak
#

>>> boş_küme = set()

>>> type(boş_küme)
<class 'set'>

>>> liste = ["elma", "armut", "kebap"]
>>> küme = set(liste)
>>> küme
{'elma', 'armut', 'kebap'}

>>> demet = ("elma", "armut", "kebap")
>>> küme = set(demet)
>>> küme
{'elma', 'armut', 'kebap'}

>>> kardiz = "Python Programlama Dili için Türkçe Kaynak"
>>> küme = set(kardiz)
>>> küme
{'D', 'ü', 'y', 'r', 'a', 'm', 'T', ' ', 't', 'g', 'l', 'ç', 'i', 'n', 'o', 'k', 'e', 'h', 'K', 'P'}

>>> kardiz = "a"
>>> küme = set(kardiz)

>>> n = 10
>>> küme = set(n)
TypeError: 'int' object is not iterable


>>> bilgi = {"işletim sistemi": "GNU", "sistem çekirdeği": "Linux",
... "dağıtım": "Ubuntu GNU/Linux"}
>>> küme = set(bilgi)
>>> küme
{'işletim sistemi', 'dağıtım', 'sistem çekirdeği'}

>>> liste = [(anahtar, değer) for anahtar, değer in bilgi.items()]
>>> küme = set(liste)
>>> küme
{('dağıtım', 'Ubuntu GNU/Linux'), ('sistem çekirdeği', 'Linux'), ('işletim sistemi', 'GNU')}


#
# Kümelerin Yapısı
#

>>> kardiz = "Python Programlama Dili"
>>> küme = set(kardiz)
>>> print(küme)
{'g', 'D', 'a', ' ', 'o', 'n', 'm', 'l', 'i', 'h', 't', 'r', 'P', 'y'}

>>> liste = ["elma", "armut", "elma", "kebap", "şeker", "armut",
... "çilek", "ağaç", "şeker", "kebap", "şeker"]

>>> for i in set(liste):
...     print(i)
...
ağaç
elma
şeker
kebap
çilek
armut

>>> liste = ["elma", "armut", "elma", "kiraz",
... "çilek", "kiraz", "elma", "kebap"]

>>> for i in set(liste):
...     print("{} listede {} kez geçiyor!".format(i, liste.count(i)))

kebap listede 1 kez geçiyor!
elma listede 3 kez geçiyor!
kiraz listede 2 kez geçiyor!
armut listede 1 kez geçiyor!
çilek listede 1 kez geçiyor!

>>> arayüz_takımları = {'Tkinter', 'PyQT', 'PyGobject'}
>>> arayüz_takımları
{'PyGobject', 'PyQT', 'Tkinter'}

>>> arayüz_takımları[0]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'set' object does not support indexing



#
# Küme Üreteçleri (Set Comprehensions)
#

>>> import random
>>> liste = [random.randint(0, 10000) for i in range(1000)]

>>> yüzden_küçük_sayılar = [i for i in liste if i < 100]
>>> print(yüzden_küçük_sayılar)
[20, 40, 24, 17, 61, 24, 70, 78, 14, 53, 43, 2, 18]



#
# Kümelerin Metotları
#

>>> dir(set)
['__and__', '__class__', '__contains__', '__delattr__', '__doc__',
'__eq__', '__format__', '__ge__', '__getattribute__', '__gt__',
'__hash__', '__iand__', '__init__', '__ior__', '__isub__', '__iter__',
'__ixor__', '__le__', '__len__', '__lt__', '__ne__', '__new__',
'__or__', '__rand__', '__reduce__', '__reduce_ex__', '__repr__',
'__ror__', '__rsub__', '__rxor__', '__setattr__', '__sizeof__',
'__str__', '__sub__', '__subclasshook__', '__xor__', 'add',
'clear','copy', 'difference', 'difference_update', 'discard',
'intersection', 'intersection_update', 'isdisjoint', 'issubset',
'issuperset', 'pop', 'remove', 'symmetric_difference',
'symmetric_difference_update', 'union', 'update']

>>> for i in dir(set):
...     if "__" not in i:
...         print(i)
...
add
clear
copy
difference
difference_update
discard
intersection
intersection_update
isdisjoint
issubset
issuperset
pop
remove
symmetric_difference
symmetric_difference_update
union
update


#
# clear()
#

>>> km = set("adana")
>>> for i in km:
...     print(i)
...
a
d
n

>>> km.clear()
>>> km
set()


#
# copy()
#

>>> km = set("kahramanmaraş")
>>> yedek = km.copy()
>>> yedek
{'a', 'r', 'h', 'k', 'm', 'ş', 'n'}

>>> km
{'a', 'h', 'k', 'm', 'n', 'r', 'ş'}


#
# add()
#

>>> küme = set(["elma", "armut", "kebap"])
>>> küme.add("çilek")
>>> print(küme)
{'elma', 'armut', 'kebap', 'çilek'}

>>> yeni = [1,2,3]
>>> for i in yeni:
...     küme.add(i)
...

>>> küme
{1, 2, 3, 'elma', 'kebap', 'çilek', 'armut'}

>>> küme = set()

>>> l = (1,2,3)
>>> küme.add(l)
>>> küme
{(1, 2, 3)}

>>> l = 45
>>> küme.add(l)
>>> küme
{45, (1, 2, 3)}

>>> l = 'Jacques Derrida'
>>> küme.add(l)
>>> küme
{'Jacques Derrida', 45, (1, 2, 3)}

>>> l = [1,2,3]
>>> küme.add(l)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unhashable type: 'list'

>>> l = {"a": 1, "b": 2, "c": 3}
>>> küme.add(l)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unhashable type: 'dict'

>>> l = {1, 2, 3}
>>> küme.add(l)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unhashable type: 'set'



#
# difference()
#

>>> k1 = set([1, 2, 3, 5])
>>> k2 = set([3, 4, 2, 10])

>>> k1.difference(k2)
{1, 5}

>>> k2.difference(k1)
{10, 4}

>>> k1 - k2
{1, 5}

>>> k2 - k1
{10, 4}



#
# difference_update()
#

>>> k1 = set([1, 2, 3])
>>> k2 = set([1, 3, 5])
>>> k1.difference_update(k2)
>>> print(k1)
{2}

>>> print(k2)
{1, 3, 5}


#
# discard()
#

>>> hayvanlar = set(["kedi", "köpek", "at", "kuş", "inek", "deve"])
>>> hayvanlar.discard("kedi")
>>> print(hayvanlar)
{'kuş', 'inek', 'deve', 'köpek', 'at'}

>>> hayvanlar.discard("yılan")
>>> print(hayvanlar)
{'deve', 'köpek', 'kuş', 'inek', 'at'}


#
# remove()
#

>>> hayvanlar.remove("köpek")
>>> hayvanlar
{'deve', 'kuş', 'inek', 'at'}

>>> hayvanlar.remove("fare")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 'fare'


#
# intersection() -> Türkçe’de “kesişim” anlamına gelir
#

>>> k1 = set([1, 2, 3, 4])
>>> k2 = set([1, 3, 5, 7])
>>> k1.intersection(k2)
{1, 3}

>> k1 & k2
{1, 3}


>>> tr = "şçöğüıŞÇÖĞÜİ"
>>> parola = "çilek"
>>> set(tr) & set(parola)
{'ç'}



#
# intersection_update() -> Türkçe’de “kesişim” anlamına gelir
#

>>> k1 = set([1, 2, 3])
>>> k2 = set([1, 3, 5])
>>> k1.intersection_update(k2)
>>> print(k1)
{1, 3}

>>> print(k2)
{1, 3, 5}


#
# isdisjoint()  -> iki kümenin kesişim kümesinin boş olup olmadığını
#

>>> a = set([1, 2, 3])
>>> b = set([2, 4, 6])
>>> a.isdisjoint(b)
False

>>> a = set([1, 3, 5])
>>> b = set([2, 4, 6])
>>> a.isdisjoint(b)
True


#
# issubset()  -> başka bir küme içinde yer alıp yer almadığını sorgulayabiliriz
#

>>> a = set([1, 2, 3])
>>> b = set([0, 1, 2, 3, 4, 5])
>>> a.issubset(b)
True


#
# issuperset()  -> "a kümesi b kümesinin alt kümesidir"
#

>>> a = set([1, 2, 3])
>>> b = set([0, 1, 2, 3, 4, 5])
>>> b.issuperset(a)
True


#
# union()  -> iki kümenin birleşimini almamızı sağlar
#

>>> a = set([2, 4, 6, 8])
>>> b = set([1, 3, 5, 7])
>>> a.union(b)
{1, 2, 3, 4, 5, 6, 7, 8}

>>> a | b


#
# update() 
#

>>> küme = set(["elma", "armut", "kebap"])
>>> yeni = [1, 2, 3]

>>> for i in yeni:
...     küme.add(i)
...
>>> küme
{1, 2, 3, 'elma', 'armut', 'kebap'}



>>> küme = set(["elma", "armut", "kebap"])
>>> yeni = [1, 2, 3]
>>> küme.update(yeni)
>>> print(küme)
{1, 2, 3, 'elma', 'armut', 'kebap'}


#
# symmetric_difference()
#

>>> a = set([1, 2, 5])
>>> b = set([1, 4, 5])


>>> a.difference(b)
{2}

>>> b.difference(a)
{4}

>>> a.symmetric_difference(b)
{2, 4}


#
# symmetric_difference_update()
#

>>> a = set([1,2, 5])
>>> b = set([1,4, 5])
>>> a.symmetric_difference_update(b)
>>> print(a)
{2, 4}


#
# pop() -> rastgele siliyor 
#

>>> a = set(["elma", "armut", "kebap"])
>>> a.pop()
'elma'



#
# Dondurulmuş Kümeler (Frozenset)
#

>>> dondurulmuş = frozenset(["elma", "armut", "ayva"])

>>> dir(dondurulmuş)

['__and__', '__class__', '__contains__', '__delattr__', '__doc__', '__eq__',
 '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__',
 '__init__', '__iter__', '__le__', '__len__', '__lt__', '__ne__', '__new__',
 '__or__', '__rand__', '__reduce__', '__reduce_ex__', '__repr__', '__ror__',
 '__rsub__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__',
 '__subclasshook__', '__xor__', 'copy', 'difference', 'intersection',
 'isdisjoint', 'issubset', 'issuperset', 'symmetric_difference', 'union']

# Gördüğünüz gibi, add(), remove(), update() gibi, değişiklik yapmaya yönelik metotlar listede yok.
