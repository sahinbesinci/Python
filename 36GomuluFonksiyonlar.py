#
#
# Gömülü Fonksiyonlar
#
#


#
# abs() -> "mutlak değer"
#

>>> abs(-20)
20

>>> abs(20)
20

>>> abs(20.0)
20.0

>>> abs(20+3j)
20.223748416156685


#
# round()
#

>>> round(12.4)
12

>>> round(12.7)
13

>>> 22/7
3.142857142857143

>>> round(22/7)
3

>>> round(22/7)
3

>>> round(22/7, 0)
3.0

>>> round(22/7, 1)
3.1

>>> round(22/7, 2)
3.14

>>> round(22/7, 3)
3.143

>>> round(22/7, 4)
3.1429


#
# all()
# True ise True değeri, eğer bu değerlerden herhangi biri False ise de False değeri döndürmektir.

>>> liste = [1, 2, 3, 4]

>>> all(liste)
True

>>> liste = [0, 1, 2, 3, 4]
>>> all(liste)
False

>>> liste = ['ahmet', 'mehmet', '']
>>> all(liste)
False


#
# any()
# bütün değerlerden en az biri True ise True çıktısı vermektir.

>>> liste = ['ahmet', 'mehmet', '']
>>> any(liste)
True

>>> l = ['', 0, [], (), set(), dict()]
>>> any(l)
False



#
# ascii()
#

>>> a = 'istihza'
>>> print(ascii(a))
'istihza'

>>> print(ascii('\n!'))
'\n'

>>> a = 'ışık'
>>> print(ascii(a))
'\u0131\u015f\u0131k'

>>> for i in a:
...     print(ascii(i))
...
'\u0131'
'\u015f'
'\u0131'
'k'

>>> liste = ['elma', 'armut', 'erik']
>>> temsil = ascii(liste)
>>> print(temsil)
['elma', 'armut', 'erik']

>>> print(type(temsil))
<class 'str'>

>>> temsil[0]
'['


#
# repr()
#

>>> ascii('şeker')
"'\\u015feker'"

>>> repr('şeker')
"'şeker'"


#
# bool()
#

>>> bool(0)
False

>>> bool(1)
True

>>> bool([])
False


#
# bin()
#

>>> bin(12)
'0b1100'


#
# bytes()
#

>>> bytes(10)
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'

>>> a = bytes(10)

>>> a
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'

>>> a[0]
0

>>> a[1]
0

>>> a[2]
0

>>> 'ışık'.encode('utf-8')
b'\xc4\xb1\xc5\x9f\xc4\xb1k'

>>> 'ışık'.encode('cp857')
b'\x8d\x9f\x8dk'

>>> 'ışık'.encode('cp1254')
b'\xfd\xfe\xfdk'

>>> bytes('ışık', 'utf-8')
b'\xc4\xb1\xc5\x9f\xc4\xb1k'

>>> bytes('ışık', 'cp1254')
b'\xfd\xfe\xfdk'

>>> bytes('ışık', 'cp857')
b'\x8d\x9f\x8dk'


#
# list()
#

>>> l = list()

>>> list('istihza')
['i', 's', 't', 'i', 'h', 'z', 'a']

>>> s = {'elma': 44, 'armut': 10, 'erik': 100}
>>> list(s)
['armut', 'erik', 'elma']

>>> list(s.values())
[10, 100, 44]


#
# set()
#

>>> k = set()

>>> i = 'istihza'
>>> set(i)
{'t', 's', 'z', 'a', 'i', 'h'}


#
# tuple()
#

>>> tuple('a')
('a',)


#
# frozenset()
#

>>> s = set('istihza')
>>> df = frozenset(s)
>>> df
frozenset({'t', 's', 'a', 'z', 'i', 'h'})


#
# complex()
#

>>> 12+0j

>>> complex(15)
(15+0j)

>>> complex(15, 2)
(15+2j)


#
# float()
#

>>> float('134')
134.0

>>> float(12)
12.0


#
# int()
#

>>> int('10')
10

>>> int(12.4)
12

>>> int('12', 8)
10

>>> int('4cf', 16)
1231


#
# str()
#

>>> str(12)
'12'

>>> bayt = b'istihza'
>>> bayt
b'istihza'

>>> kardiz = str(bayt, encoding='utf-8')
>>> print(kardiz)
istihza


#
# dict()
#

>>> s = dict()

>>> s = dict(a=1, b=2, c=3)
{'a': 1, 'b': 2, 'c': 3}

>>> öğeler = (['a', 1], ['b', 2], ['c', 3])
>>> dict(öğeler)
{'a': 1, 'b': 2, 'c': 3}


#
# callable()
# bir nesnenin ‘çağrılabilir’ olup olmadığını denetler.

>>> callable(open)
True

>>> import sys
>>> callable(sys.version)
False


#
# ord()
# bir karakterin karşılık geldiği ondalık sayıyı verir

>>> ord('a')
97

>>> ord('ı')
305


#
# oct()
#

>>> oct(10)
'0o12'


#
# hex()
#

>>> hex(305)
'Ox131'


#
# eval(), exec(), globals(), locals(), compile()
#

>>> eval('5 + 25')
30

>>> exec('a = 5')
>>> a
5

>>> globals()
{'__name__': '__main__', '__doc__': None, '__package__': None, '__loader__': <class '_frozen_importlib.BuiltinImporter'>, '__spec__': None, '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>, 'bayt': b'istihza', 'a': 5}

>>> globals()['z'] = 23
>>> z
23

>>> def fonksiyon(param1, param2):
...     x = 10
...     print(locals())
...
>>> fonksiyon(10, 20)
{'x': 10, 'param2': 20, 'param1': 10}


#
# copyright()
#

>>> copyright()

Copyright (c) 2001-2012 Python Software Foundation.
All Rights Reserved.

Copyright (c) 2000 BeOpen.com.
All Rights Reserved.

Copyright (c) 1995-2001 Corporation for National Research Initiatives.
All Rights Reserved.

Copyright (c) 1991-1995 Stichting Mathematisch Centrum, Amsterdam.
All Rights Reserved.


#
# credits()
#

>>> credits()

Thanks to CWI, CNRI, BeOpen.com, Zope Corporation and a cast of thousands
for supporting Python development.  See www.python.org for more information.


#
# license()
#

A. HISTORY OF THE SOFTWARE
==========================

Python was created in the early 1990s by Guido van Rossum at Stichting
Mathematisch Centrum (CWI, see http://www.cwi.nl) in the Netherlands
as a successor of a language called ABC.  Guido remains Python's
principal author, although it includes many contributions from others.

In 1995, Guido continued his work on Python at the Corporation for
National Research Initiatives (CNRI, see http://www.cnri.reston.va.us)
in Reston, Virginia where he released several versions of the
software.

In May 2000, Guido and the Python core development team moved to
BeOpen.com to form the BeOpen PythonLabs team.  In October of the same
year, the PythonLabs team moved to Digital Creations, which became
Zope Corporation.  In 2001, the Python Software Foundation (PSF, see
https://www.python.org/psf/) was formed, a non-profit organization
created specifically to own Python-related Intellectual Property.
Zope Corporation was a sponsoring member of the PSF.

All Python releases are Open Source (see http://www.opensource.org for
the Open Source Definition).  Historically, most, but not all, Python
Hit Return for more, or q (and Return) to quit: q


#
# dir()
#

>>> dir()
['__annotations__', '__builtins__', '__doc__', '__loader__', '__name__', '__package__', '__spec__', 'a', 'bayt', 'fonksiyon', 'z']

>>> dir('')
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']

>>> dir([])
['__add__', '__class__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']

>>> dir({})
['__class__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 'pop', 'popitem', 'setdefault', 'update', 'values']


#
# divmod()
#

>>> divmod(10, 2)
(5, 0)

>>> divmod(10, 3)
(3, 1)


#
# enumerate()
#

>>> enumerate('istihza')
<class 'enumerate'>

>>> list(enumerate('istihza'))
[(0, 'i'), (1, 's'), (2, 't'), (3, 'i'), (4, 'h'), (5, 'z'), (6, 'a')]

>>> [i for i in enumerate('istihza')]
[(0, 'i'), (1, 's'), (2, 't'), (3, 'i'), (4, 'h'), (5, 'z'), (6, 'a')]

>>> print(*enumerate('istihza'))
(0, 'i') (1, 's') (2, 't') (3, 'i') (4, 'h') (5, 'z') (6, 'a')

>>> for sıra, öğe in enumerate('istihza', 1):
...     print("{}. {:>2}".format(sıra, öğe))
...
1.  i
2.  s
3.  t
4.  i
5.  h
6.  z
7.  a


#
# exit()
# o anda çalışan programdan çıkmanızı sağlar.



#
# help()
# 

>>> help(dir)


#
# id()
# 

>>> a = 50
>>> id(a)
505494576

>>> kardiz = "Elveda Zalim Dünya!"
>>> id(kardiz)
14461728


#
# input()
# kullanıcı ile veri alışverişi yapar.



#
# format()
# 

>>> format(12, '.2f')
'12.00'

>>> '{:.2f}'.format(12)
'12.00'


#
# filter()
# 

>>> l = [400, 176, 64, 175, 355, 13, 207, 298, 397, 386, 31, 120, 120, 236, 241, 123, 249, 364, 292, 153]
>>> def tek(sayı):
...     return sayı % 2 == 1
...
>>> print(*filter(tek, l))
175 355 13 207 397 31 241 123 249 153



#
# hash()
# 

>>> hash('istihza')
-840510580

>>> hash('python')
212829695


#
# isinstance()
# 

>>> type('istihza')
<class 'str'>

>>> isinstance('istihza', str)
True

>>> isinstance('istihza', list)
False


#
# len()
# 

>>> len('istihza')
7

>>> l = [1, 4, 5, 3, 2, 9, 10]
>>> len(l)
7


#
# map()
# 

>>> l = [1, 4, 5, 4, 2, 9, 10]

>>> for i in l:
...     i ** 2
...
1
16
25
16
4
81
100


>>> def karesi(n):
...     return n ** 2
...

>>> list(map(karesi, l))
[1, 16, 25, 16, 4, 81, 100]



#
# max()
# 

>>> max(1, 2, 3)
3

>>> liste = [1, 2, 3]
>>> max(liste)
3

>>> isimler = ['ahmet', 'can', 'mehmet', 'selin', 'abdullah', 'kezban']
>>> max(isimler, key=len)
'abdullah'


#
# min()
# min() fonksiyonu max() fonksiyonunun tam tersini yapar



#
# open()
# 

>>> open(dosya_adi, mode='r', buffering=-1, encoding=None,
...      errors=None, newline=None, closefd=True, opener=None)

>>> open('falanca_dosya.txt')

>>> open('/home/istihza/Desktop/dosya.txt')

>>> f = open('test\nisan.txt')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
OSError: [Errno 22] Invalid argument: 'test\nisan.txt'

>>> f = open('ni.txt', 'w', buffering=1)
>>> f.write('birinci satır\n')
14

>>> f.write('ikinci satır\n')
13

>>> f.write('aaa')
3

>>> f.write('\n')
1


#
# pow()
# 

>>> pow(2, 3)
8

>>> pow(2, 3, 2)
0
>>> (2 ** 3) % 2
0

>>> pow(12, 2)
144



#
# print()
# 

print(deg1, deg2, deg3, ..., sep=' ', end='\n', file=sys.stdout, flush=False)



#
# quit()
# Bu fonksiyonu programdan çıkmak için kullanıyoruz.



#
# range()
# range(başlangıç_değer, bitiş_değeri, atlama_değeri)

>>> l = range(0, 10)

>>> print(l)
range(0, 10)

>>> type(l)
<class 'range'>

>>> list(l)
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

>>> tuple(l)
(0, 1, 2, 3, 4, 5, 6, 7, 8, 9)

>>> set(l) #küme
{0, 1, 2, 3, 4, 5, 6, 7, 8, 9}

>>> frozenset(l) #dondurulmuş küme
frozenset({0, 1, 2, 3, 4, 5, 6, 7, 8, 9})

>>> print(*range(10), sep=', ')
0, 1, 2, 3, 4, 5, 6, 7, 8, 9

>>> list(range(0, 10, 2))
[0, 2, 4, 6, 8]


#
# reversed()
# 

>>> isimler = ['ahmet', 'mehmet', 'veli', 'ayşe', 'çiğdem', 'ışık']

>>> isimler[::-1]
['ışık', 'çiğdem', 'ayşe', 'veli', 'mehmet', 'ahmet']

>>> reversed(isimler)
<list_reverseiterator object at 0x00EB9710>

>>> list(reversed(isimler))
['ışık', 'çiğdem', 'ayşe', 'veli', 'mehmet', 'ahmet']



#
# sorted()
# 

>>> sorted('ahmet')
['a', 'e', 'h', 'm', 't']

>>> sorted(('elma', 'armut', 'kiraz', 'badem'))
['armut', 'badem', 'elma', 'kiraz']

>>> sorted(['elma', 'armut', 'kiraz', 'badem'])
['armut', 'badem', 'elma', 'kiraz']

>>> sorted([10, 9, 4, 14, 20])
[4, 9, 10, 14, 20]

>>> elemanlar = [('ahmet',       33,    'karataş'),
...              ('mehmet',      45,    'arpaçbahşiş'),
...              ('sevda',       24,    'arsuz'),
...              ('arzu',        40,    'siverek'),
...              ('abdullah',    30,    'payas'),
...              ('ilknur',      40,    'kilis'),
...              ('abdurrezzak', 40,    'bolvadin')]
>>> print(*sorted(elemanlar), sep='\n')
('abdullah', 30, 'payas')
('abdurrezzak', 40, 'bolvadin')
('ahmet', 33, 'karataş')
('arzu', 40, 'siverek')
('ilknur', 40, 'kilis')
('mehmet', 45, 'arpaçbahşiş')
('sevda', 24, 'arsuz')


>>> def sırala(liste):
...     return liste[1]
...
>>> elemanlar = [('ahmet',       33,    'karataş'),
...              ('mehmet',      45,    'arpaçbahşiş'),
...              ('sevda',       24,    'arsuz'),
...              ('arzu',        40,    'siverek'),
...              ('abdullah',    30,    'payas'),
...              ('ilknur',      40,    'kilis'),
...              ('abdurrezzak', 40,    'bolvadin')]
>>> print(*sorted(elemanlar, key=sırala), sep='\n')
('sevda', 24, 'arsuz')
('abdullah', 30, 'payas')
('ahmet', 33, 'karataş')
('arzu', 40, 'siverek')
('ilknur', 40, 'kilis')
('abdurrezzak', 40, 'bolvadin')
('mehmet', 45, 'arpaçbahşiş')



#
# slice()
# slice(başlangıç, bitiş, atlama)

>>> l = ['ahmet', 'mehmet', 'ayşe', 'senem', 'salih']

>>> l[0:2]
['ahmet', 'mehmet']

>>> dl = slice(0, 3)

>>> l[dl]
['ahmet', 'mehmet', 'ayşe']


#
# sum()
# 

>>> l = [1, 2, 3]
>>> sum(l)
6

>>> l = [1, 2, 3]
>>> sum(l, 10)
16


#
# type()
# 

>>> type('elma')
<class 'str'>


#
# zip()
# 

>>> a1 = ['a', 'b', 'c']
>>> a2 = ['d', 'e', 'f']

>>> zip(a1, a2)
<zip object at 0x00FD0BE8>

>>> print(*zip(a1, a2))
('a', 'd') ('b', 'e') ('c', 'f')

>>> list(zip(a1, a2))
[('a', 'd'), ('b', 'e'), ('c', 'f')]

>>> dict(zip(a1,a2))
{'a': 'd', 'b': 'e', 'c': 'f'}

>>> for a, b in zip(a1, a2):
...     print(a, b)
...
a d
b e
c f


#
# vars()
# locals() fonksiyonuyla aynı çıktıyı elde ederiz

>>> vars()
{'__builtins__': <module 'builtins' (built-in)>, '__name__': '__main__',
 '__package__': None, '__loader__': <class '_frozen_importlib.BuiltinImporter'>,
 '__doc__': None}

>>> vars(str)
>>> vars(list)
>>> vars(dict)
