#
#
# Sayma Sistemleri
#
#


#
# Onlu Sayma Sistemi
#

>>> (0 * (10 ** 0)) + (8 * (10 ** 1)) + (9 * (10 ** 2)) + (1 * (10 ** 3))
1980


#
# Sekizli Sayma Sistemi
#

>>> sayı_sistemleri = ["onlu", "sekizli"]
>>> print(("{:^5} "*len(sayı_sistemleri)).format(*sayı_sistemleri))
onlu  sekizli
>>> for i in range(17):
...     print("{0:^5} {0:^5o}".format(i))
...
#onlu  sekizli
  0     0
  1     1
  2     2
  3     3
  4     4
  5     5
  6     6
  7     7
  8    10
  9    11
 10    12
 11    13
 12    14
 13    15
 14    16
 15    17
 16    20


#
# On Altılı Sayma Sistemi
#

>>> sayı_sistemleri = ["onlu", "sekizli", "on altılı"]
>>> print(("{:^8} "*len(sayı_sistemleri)).format(*sayı_sistemleri))
  onlu   sekizli  on altılı
>>> for i in range(17):
...     print("{0:^8} {0:^8o} {0:^8x}".format(i))
...
#onlu   sekizli  on altılı
   0        0        0
   1        1        1
   2        2        2
   3        3        3
   4        4        4
   5        5        5
   6        6        6
   7        7        7
   8        10       8
   9        11       9
   10       12       a
   11       13       b
   12       14       c
   13       15       d
   14       16       e
   15       17       f
   16       20       10


#
# İkili Sayma Sistemi
#


>>> sayı_sistemleri = ["onlu", "sekizli", "on altılı", "ikili"]
>>> print(("{:^9} "*len(sayı_sistemleri)).format(*sayı_sistemleri))
  onlu     sekizli  on altılı   ikili
>>> for i in range(17):
...     print("{0:^9} {0:^9o} {0:^9x} {0:^9b}".format(i))
...
#onlu     sekizli  on altılı   ikili
    0         0         0         0
    1         1         1         1
    2         2         2        10
    3         3         3        11
    4         4         4        100
    5         5         5        101
    6         6         6        110
    7         7         7        111
    8        10         8       1000
    9        11         9       1001
   10        12         a       1010
   11        13         b       1011
   12        14         c       1100
   13        15         d       1101
   14        16         e       1110
   15        17         f       1111
   16        20        10       10000


#
# Sayma Sistemlerini Birbirine Dönüştürme
# Fonksiyon Kullanarak



#
# bin() ->  binary iki karakteri (‘0b’), o sayının ikili sisteme ait bir sayı olduğunu gösteren bir işarettir
#  

>>> bin(2)
'0b10'

>>> bin(2)[2:]
'10'


#
# hex() -> on altılı
#  

>>> hex(10)
'Oxa'


#
# oct() -> sekizli 
#  

>>> oct(10)
'0o12'


#
# int()
#  

>>> int('7bc', 16)
1980

>>> int('1100', 2)
12

>>> int('1100', 16)
4352


#
# Biçimlendirme Yoluyla
#  


#
# b
#  

>>> '{:b}'.format(12)
'1100'



#
# x
#  

>>> '{:x}'.format(1980)
'7bc'


#
# o
#  

>>> '{:o}'.format(1980)
'3674'

>>> sayı_sistemleri = ["onlu", "sekizli", "on altılı", "ikili"]
>>> print(("{:^9} "*len(sayı_sistemleri)).format(*sayı_sistemleri))
  onlu     sekizli  on altılı   ikili
>>> for i in range(17):
...     print("{0:^9} {0:^9o} {0:^9x} {0:^9b}".format(i))
...
#  onlu     sekizli  on altılı   ikili
    0         0         0         0
    1         1         1         1
    2         2         2        10
    3         3         3        11
    4         4         4        100
    5         5         5        101
    6         6         6        110
    7         7         7        111
    8        10         8       1000
    9        11         9       1001
   10        12         a       1010
   11        13         b       1011
   12        14         c       1100
   13        15         d       1101
   14        16         e       1110
   15        17         f       1111
   16        20        10       10000























































































































