#
#
# Sayılar
#
#



#
# Sayıların Metotları
#


#
# Tam Sayıların Metotları
#

>>> [i for i in dir(int) if not i.startswith("_")]
['bit_length', 'conjugate', 'denominator', 'from_bytes', 'imag', 'numerator', 'real', 'to_bytes']


#
# bit_length()
#

>>> for i in range(11):
...     print(i, bin(i)[2:], len(bin(i)[2:]), sep="\t")
...
0       0       1
1       1       1
2       10      2
3       11      2
4       100     3
5       101     3
6       110     3
7       111     3
8       1000    4
9       1001    4
10      1010    4


>>> sayı = 10
>>> sayı.bit_length()
4

>>> len(bin(10)[2:]) == (10).bit_length()
True

>>> 10.bit_length()
  File "<stdin>", line 1
    10.bit_length()
                ^
SyntaxError: invalid syntax

>>> a = 10
>>> a.bit_length()
4

>>> (10).bit_length()
4

>>> type(10.)
<class 'float'>


#
# Kayan Noktalı Sayıların Metotları
#

>>> [i for i in dir(float) if not i.startswith("_")]
['as_integer_ratio', 'conjugate', 'fromhex', 'hex', 'imag', 'is_integer', 'real']


#
# as_integer_ratio()
#

#9 sayısını 2 sayısına böldüğümüzde 4.5 sayısını elde ederiz. İşte as_integer_ratio() metodu, bu 9 ve 2 sayılarını bize ayrı ayrı verir.
>>> sayı = 4.5
>>> sayı.as_integer_ratio()
(9, 2)


#
# is_integer()
#

>>> (12.0).is_integer()
True

>>> (12.5).is_integer()
False


#
# Karmaşık Sayıların Metotları
#

>>> [i for i in dir(complex) if not i.startswith("_")]
['conjugate', 'imag', 'real']


#
# imag
#

#İşte imag adlı nitelik, bize bir karmaşık sayının sanal kısmını verir:
>>> c = 12+4j
>>> c.imag
4.0


#
# real
#

>>> c = 12+4j
>>> c.real
12.0


#
# Aritmetik Fonksiyonlar
#

#
# abs() -> bir sayının mutlak değerini verir
#

>>> abs(-2)
2

>>> abs(2)
2


#
# divmod() -> bölümü ve kalanı verir:
#

>>> divmod(10, 2)
(5, 0)

>>> divmod(14, 3)
(4, 2)


#
# max()
#

>>> sayılar = [996780, 121633, 436419, 471, 776271, 91626, 209175, 894281, 417963, 624464, 736535, 418888, 506194, 591087, 64075, 50252, 952943, 25878, 217085, 223996, 416042, 484123, 810460, 423284, 956886, 237772, 960241]
>>> max(sayılar)
996780

>>> isimler = ["ahmet", "mehmet", "necla", "sedat", "abdullah", "gıyaseddin", "sibel", "can", "necmettin", "savaş", "özgür"]
>>> print(max(isimler, key=len))
gıyaseddin


#
# min()
#

>>> sayılar = [996780, 121633, 436419, 471, 776271, 91626, 209175, 894281, 417963, 624464, 736535, 418888, 506194, 591087, 64075, 50252, 952943, 25878, 217085, 223996, 416042, 484123, 810460, 423284, 956886, 237772, 960241]
>>> min(sayılar)
471

>>> isimler = ["ahmet", "mehmet", "necla", "sedat", "abdullah", "gıyaseddin", "sibel", "can", "necmettin", "savaş", "özgür"]
print(min(isimler, key=len))
can


#
# sum()
#

>>> a = [10, 20, 43, 45 , 77, 2, 0, 1]
>>> sum(a)
198

>>> sum(a, 10)
208
