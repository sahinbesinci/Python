# 
#
# Karakter Dizileri
#
# 

karakter_dizisi[öğe_sırası]

>>> kardiz = "istihza"
>>> len(kardiz)
7

>>> kardiz[0]
'i'

>>> kardiz[len(kardiz)-1]
'a'

>>> kardiz[len(kardiz)]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: string index out of range

>>> kardiz[-1]
'a'

>>> kardiz[-2]
'z'

>>> for i in range(7):
>>>     print(kardiz[i])
i
s
t
i
h
z
a

>>> for karakter in range(len(kardiz)):
>>>     print(kardiz[karakter])

>>> isim = input("isminiz: ")
>>> for i in range(len(isim)):
>>>     print("isminizin {}. harfi: {}".format(i, isim[i]))
isminizin 0. harfi: Ş
isminizin 1. harfi: a
isminizin 2. harfi: h
isminizin 3. harfi: i
isminizin 4. harfi: n


# Karakter Dizilerini Dilimlemek
# karakter_dizisi[ilk_karakter:son_karakter]
# karakter_dizisi[ilk_karakter:son_karakter:atlama_sayısı]


>>> site = "www.istihza.com"
>>> site[4:11]
'istihza'

>>> site[12:16]
'com'

>>> site1 = "www.google.com"
>>> site2 = "www.istihza.com"
>>> site3 = "www.yahoo.com"
>>> site4 = "www.gnu.org"
>>> for isim in site1, site2, site3, site4:
>>>     print("site: ", isim[4:-4])
site:  google
site:  istihza
site:  yahoo
site:  gnu

>>> kardiz = "Sana Gül Bahçesi Vadetmedim"

>>> kardiz[:4]
'Sana'

>>> kardiz[17:]
'Vadetmedim'

# 
# 
# Karakter Dizilerini Ters Çevirmek
# kardiz[ilk_karakter:son_karakter:atlama_sayısı]
# 

>>> kardiz[::-1]
'midemtedaV iseçhaB lüG anaS'

>>> kardiz[7:4:-1]
'lüG'

>>> for i in reversed("Sana Gül Bahçesi Vadetmedim"):
>>>     print(i, end="")
midemtedaV iseçhaB lüG anaS

>>> print(*reversed("Sana Gül Bahçesi Vadetmedim"), sep="")
midemtedaV iseçhaB lüG anaS

# 
# 
# Karakter Dizilerini Alfabe Sırasına Dizmek
# 
# 

>>> sorted("kitap")
['a', 'i', 'k', 'p', 't']

>>> print(*sorted("kitap"), sep="")
aikpt

>>> import locale
>>> locale.setlocale(locale.LC_ALL, "Turkish_Turkey.1254") #Windows için
>>> locale.setlocale(locale.LC_ALL, "tr_TR") #GNU/Linux için
>>> sorted("çiçek", key=locale.strxfrm)
['ç', 'ç', 'e', 'i', 'k']
#yada
>>> harfler = "abcçdefgğhıijklmnoöprsştuüvyz"
>>> çevrim = {i: harfler.index(i) for i in harfler}
>>> sorted("afgdhkıi", key=çevrim.get)
['a', 'd', 'f', 'g', 'h', 'ı', 'i', 'k']

>>> print(çevrim)
{'ğ': 8, 'ı': 10, 'v': 26, 'g': 7, 'ş': 22, 'a': 0, 'c': 2, 'b': 1, 'e': 5,
'd': 4, 'ç': 3, 'f': 6, 'i': 11, 'h': 9, 'k': 13, 'j': 12, 'm': 15, 'l': 14,
'o': 17, 'n': 16, 'p': 19, 's': 21, 'r': 20, 'u': 24, 't': 23, 'ö': 18,
'y': 27, 'z': 28, 'ü': 25}

# 
# 
# Karakter Dizileri Üzerinde Değişiklik Yapmak
# 
# 

>>> kardiz = "istihza"
>>> kardiz = kardiz[:3] + "İH" + kardiz[5:]
>>> kardiz
'istİHza'


# 
# 
# Üç Önemli Fonksiyon
# 
#


# dir() -> karakter dizilerinin bize hangi metotları sunduğunu görmek için bu fonksiyonu şöyle kullanabiliriz: dir(str)



>>> dir(str)

['__add__', '__class__', '__contains__', '__delattr__', '__doc__', '__eq__',
'__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__',
'__gt__', '__hash__', '__init__', '__iter__', '__le__', '__len__', '__lt__',
'__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__',
'__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__',
'__subclasshook__', 'capitalize', 'center', 'count', 'encode', 'endswith',
'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha',
'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable',
'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip',
'maketrans', 'partition', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition',
'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase',
'title', 'translate', 'upper', 'zfill']

>>> dir(int)
['__abs__', '__add__', '__and__', '__bool__', '__ceil__', '__class__', '__delattr__', '__dir__', '__divmod__', '__doc__', '__eq__', '__float__', '__floor__', '__floordiv__', '__format__', '__ge__', '__getattribute__', '__getnewargs__', '__gt__', '__hash__', '__index__', '__init__', '__init_subclass__', '__int__', '__invert__', '__le__', '__lshift__', '__lt__', '__mod__', '__mul__', '__ne__', '__neg__', '__new__', '__or__', '__pos__', '__pow__', '__radd__', '__rand__', '__rdivmod__', '__reduce__', '__reduce_ex__', '__repr__', '__rfloordiv__', '__rlshift__', '__rmod__', '__rmul__', '__ror__', '__round__', '__rpow__', '__rrshift__', '__rshift__', '__rsub__', '__rtruediv__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__truediv__', '__trunc__', '__xor__', 'bit_length', 'conjugate', 'denominator', 'from_bytes', 'imag', 'numerator', 'real', 'to_bytes']

>>> dir(float)

>>> dir(complex)


# enumerate() -> Enumerate kelimesi İngilizcede ‘numaralamak, numaralandırmak’ gibi anlamlara gelir

>>> print(*enumerate("istihza"))
(0, 'i') (1, 's') (2, 't') (3, 'i') (4, 'h') (5, 'z') (6, 'a')

>>> for i in enumerate("istihza"):
...     print(i)
...
(0, 'i')
(1, 's')
(2, 't')
(3, 'i')
(4, 'h')
(5, 'z')
(6, 'a')

>>> for sıra, metot in enumerate(dir("")):
...     print(sıra, metot)
0 __add__
1 __class__
2 __contains__
3 __delattr__
4 __dir__
35 center
36 count
41 format
42 format_map
43 index
44 isalnum
..

# numaralandırmaya 0‘dan başlıyor, eğer isterseniz bu fonksiyonun numaralandırmaya kaçtan başlayacağını kendiniz de belirleyebilirsiniz
>>> for sıra, harf in enumerate("istihza", 1):
...     print(sıra, harf)
...
1 i
2 s
3 t
4 i
5 h
6 z
7 a

# help()

>>> help()

help> dir

Help on built-in function dir in module builtins:

dir(...)
    dir([object]) -> list of strings

    If called without an argument, return the names in the current scope.
    Else, return an alphabetized list of names comprising (some of) the attributes
    of the given object, and of attributes reachable from it.
    If the object supplies a method named __dir__, it will be used; otherwise
    the default dir() logic is used and returns:
      for a module object: the module's attributes.
      for a class object:  its attributes, and recursively the attributes of its bases.
      for any other object: its attributes, its class's attributes, and
      recursively the attributes of its class's base classes.


>>> help(dir)

Help on built-in function dir in module builtins:

dir(...)
    dir([object]) -> list of strings

    If called without an argument, return the names in the current scope.
    Else, return an alphabetized list of names comprising (some of) the attributes
    of the given object, and of attributes reachable from it.
    If the object supplies a method named __dir__, it will be used; otherwise
    the default dir() logic is used and returns:
      for a module object: the module's attributes.
      for a class object:  its attributes, and recursively the attributes of its bases.
      for any other object: its attributes, its class's attributes, and
      recursively the attributes of its class's base classes.




help> len

Help on built-in function len in module builtins:

len(...)
    len(object) -> integer

    Return the number of items of a sequence or mapping.

