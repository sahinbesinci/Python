#
#
# Listelerin ve Demetlerin Metotları
#
#


#
# Listelerin Metotları
#

>>> dir(list)
>>> dir([])
['__add__', '__class__', '__contains__', '__delattr__', '__delitem__',
 '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__',
 '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__',
 '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__',
 '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__',
 '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__',
 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop',
 'remove', 'reverse', 'sort']


>>> [i for i in dir(list) if not "_" in i]
['append', 'clear', 'copy', 'count', 'extend', 'index',
 'insert', 'pop', 'remove', 'reverse', 'sort']


#
# append()
#

>>> liste = ["elma", "armut", "çilek"]
>>> liste.append("erik")

>>> liste = ["elma", "armut", "çilek"]
>>> liste = liste + ["erik"]
>>> print(liste)
['elma', 'armut', 'çilek', 'erik']

>>> liste = [1, 2, 3]
>>> liste.append([4, 5, 6])
>>> print(liste)
[1, 2, 3, [4, 5, 6]]


#
# extend()
#


>>> li1 = [1, 3, 4]
>>> li2 = [10, 11, 12]
>>> li1. append(li2)
>>> print(li1)
[1, 3, 4, [10, 11, 12]]

li1 = [1, 3, 4]
li2 = [10, 11, 12]
li1. extend(li2)
print(li1)


#
# insert()
#

>>> liste = ["elma", "armut", "çilek"]
>>> liste.insert(0, "erik")
>>> print(liste)


#
# remove()
#

>>> liste = ["elma", "armut", "çilek"]
>>> liste.remove("elma")
>>> liste
['armut', 'çilek']


#
# reverse()
#
>>> liste = ["elma", "armut", "çilek"]
>>> liste.reverse()
>>> liste
['çilek', 'armut', 'elma']

>>> meyveler = ["elma", "armut", "çilek", "kiraz"]
>>> meyveler[::-1]
['kiraz', 'çilek', 'armut', 'elma']

>>> print(*reversed(meyveler))
kiraz çilek armut elma

>>> print(list(reversed(meyveler)))
['kiraz', 'çilek', 'armut', 'elma']

>>> for i in reversed(meyveler):
...     print(i)
...
kiraz
çilek
armut
elma


#
# pop()
#

>>> liste = ["elma", "armut", "çilek"]
>>> liste.pop()
'çilek'
>>> liste
['elma', 'armut']

>>> liste.pop(0)
'elma'
>>> liste
['armut']


#
# sort()
#

>>> üyeler = ['Ahmet', 'Mehmet', 'Ceylan', 'Seyhan', 'Mahmut', 'Zeynep',
...           'Abdullah', 'Kadir', 'Kemal', 'Kamil', 'Selin', 'Senem',
...           'Sinem', 'Tayfun', 'Tuna', 'Tolga']
>>> üyeler.sort()
>>> print(üyeler)
['Abdullah', 'Ahmet', 'Ceylan', 'Kadir', 'Kamil', 'Kemal', 'Mahmut', 'Mehmet', 'Selin', 'Senem', 'Seyhan', 'Sinem', 'Tayfun', 'Tolga', 'Tuna', 'Zeynep']

>>> sayılar = [1, 0, -1, 4, 10, 3, 6]
>>> sayılar.sort()
>>> print(sayılar)
[-1, 0, 1, 3, 4, 6, 10]

>>> üyeler = ['Ahmet', 'Mehmet', 'Ceylan', 'Seyhan', 'Mahmut', 'Zeynep',
...           'Abdullah', 'Kadir', 'Kemal', 'Kamil', 'Selin', 'Senem',
...           'Sinem', 'Tayfun', 'Tuna', 'Tolga']
>>> üyeler.sort(reverse=True)
>>> print(üyeler)
['Zeynep', 'Tuna', 'Tolga', 'Tayfun', 'Sinem', 'Seyhan', 'Senem', 'Selin', 'Mehmet', 'Mahmut', 'Kemal', 'Kamil', 'Kadir', 'Ceylan', 'Ahmet', 'Abdullah']

>>> isimler = ["Ahmet", "Işık", "İsmail", "Çiğdem", "Can", "Şule"]
>>> isimler.sort()
>>> isimler
['Ahmet', 'Can', 'Işık', 'Çiğdem', 'İsmail', 'Şule']


#
# index()
#

>>> liste = ["elma", "armut", "çilek"]
>>> liste.index("elma")
0


#
# count()
#

>>> liste = ["elma", "armut", "elma", "çilek"]
>>> liste.count("elma")
2


#
# copy()
#

>>> liste1 = ["ahmet", "mehmet", "özlem"]
>>> liste2 = liste1[:]

>>> liste2 = list(liste1)

>>> liste2 = liste1.copy()


#
# clear()
#

>>> liste = [1, 2, 3, 5, 10, 20, 30, 45]
>>> liste.clear()
>>> liste
[]


#
# Demetlerin Metotları
#

>>> dir(tuple)


#
# index()
#

>>> demet = ("elma", "armut", "çilek")
>>> demet.index("elma")
0


#
# count()
#

>>> demet = ("elma", "armut", "elma", "çilek")
>>> demet.count("elma")
2
