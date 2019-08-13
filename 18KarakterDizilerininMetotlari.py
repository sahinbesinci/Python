#
#
# Karakter Dizilerinin Metotları
#
#


#
# capitalize()
# metodunun görevi karakter dizilerinin yalnızca ilk harfini büyütmektir. 

>>> a = "python"
>>> a.capitalize()
'Python'

>>> a = "python programlama dili"
>>> a.capitalize()
'Python programlama dili'

#
# title()
# 

>>> a.title()
'Python Programlama Dili'

#
# swapcase()
#

>>> kardiz = "python"
>>> kardiz.swapcase()
'PYTHON'

>>> kardiz = "PYTHON"
>>> kardiz.swapcase()
'python'

>>> kardiz = "Python"
>>> kardiz.swapcase()
'pYTHON'


#
# casefold()
#

>>> "ß".lower()
'ß'

>>> "ß".casefold()
'ss'


#
# strip(), lstrip(), rstrip()
#

>>> kardiz = " istihza "
>>> kardiz.strip()
'istihza'

>>> kardiz = "python"
>>> kardiz.strip("p")
'ython'

>>> kardiz = "kazak"
>>> kardiz.strip("k")
'aza'

>>> metin = """
> Python programlama dili Guido Van Rossum adlı Hollandalı bir programcı tarafından
> 90'lı yılların başında geliştirilmeye başlanmıştır. Çoğu insan, isminin Python
> olmasına bakarak, bu programlama dilinin, adını piton yılanından aldığını düşünür.
> Ancak zannedildiğinin aksine bu programlama dilinin adı piton yılanından gelmez.
> Guido Van Rossum bu programlama dilini, The Monty Python adlı bir İngiliz komedi
> grubunun, Monty Python's Flying Circus adlı gösterisinden esinlenerek adlandırmıştır.
> Ancak her ne kadar gerçek böyle olsa da, Python programlama dilinin pek çok yerde
> bir yılan figürü ile temsil edilmesi neredeyse bir gelenek halini almıştır diyebiliriz.
"""

>>> for i in metin.split():
...    print(i.strip("> "), end=" ")
 Python programlama dili Guido Van Rossum adlı Hollandalı bir programcı tarafından  90'lı yılların başında geliştirilmeye başlanmıştır. Çoğu insan, isminin Python  olmasına bakarak, bu programlama dilinin, adını piton yılanından aldığını düşünür.  Ancak zannedildiğinin aksine bu programlama dilinin adı piton yılanından gelmez.  Guido Van Rossum bu programlama dilini, The Monty Python adlı bir İngiliz komedi  grubunun, Monty Python's Flying Circus adlı gösterisinden esinlenerek adlandırmıştır.  Ancak her ne kadar gerçek böyle olsa da, Python programlama dilinin pek çok yerde  bir yılan figürü ile temsil edilmesi neredeyse bir gelenek halini almıştır diyebiliriz.

>>> "kazak".lstrip("k")
'azak'

>>> "kazak".rstrip("k")
'kaza'


#
# join()
#

>>> kardiz = "Beşiktaş Jimnastik Kulübü"
>>> bölünmüş = kardiz.split()
>>> print(bölünmüş)
['Beşiktaş', 'Jimnastik', 'Kulübü']
>>> " ".join(bölünmüş)
'Beşiktaş Jimnastik Kulübü'

>>> birleştirme_karakteri = " "
>>> birleştirme_karakteri.join(bölünmüş)

>>> "-".join(bölünmüş)
'Beşiktaş-Jimnastik-Kulübü'
>>> "".join(bölünmüş)
'BeşiktaşJimnastikKulübü'


#
# count()
#

>>> şehir = "Kahramanmaraş"
>>> şehir.count("a")

>>> şehir = "adana"
>>> şehir.count("a")
3

>>> şehir.count("a", 1)
2

>>> şehir.count("a", 2)
2

>>> şehir.count("a", 3)
1

>>> şehir.count("a", 4)
1


#
# index(), rindex()
#

>> kardiz = "pythonn"
>>> kardiz.index("p")
0

>>> kardiz.index("n")
5

>>> kardiz = "adana"
>>> kardiz.index("a")
0

>>> kardiz.rindex("a")
4


#
# find(), rfind()
#

>>> kardiz = "adana"
>>> kardiz.find("a")

0

>>> kardiz.rfind("a")

4

# Peki index()/rindex() ve find()/rfind() metotları arasında ne fark var?

>>> kardiz = "adana"
>>> kardiz.index("z")

Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: substring not found
Ama find() ve rfind() metotları böyle bir durumda -1 çıktısı verir:

>>> kardiz = "adana"
>>> kardiz.find("z")

-1


#
# center(), rjust(), ljust()
#

>>> kardiz = "python"
>>> kardiz.center(1)
'python'

>>> kardiz.center(10)
'  python  '

>>> for metot in dir(""):
...    print(metot.center(15))
...	
    __add__
   __class__
  __contains__
  __delattr__
    __dir__
	..
	..
	
>>> for i in range(1, 20):
...     kardiz.center(i)
...
'python'
'python'
'python'
'python'
'python'
'python'
' python'
' python '
'  python '
'  python  '


>>> for i in dir(""):
...      print(i.ljust(20))
...
__add__
__class__
__contains__
__delattr__
__dir__


>>> for i in dir(""):
...      print(i.rjust(20))
...
             __add__
           __class__
        __contains__
         __delattr__
             __dir__

>>> kardiz = "tel no"
>>> kardiz.ljust(10, ".")
'tel no....'

>>> for i in "elma", "armut", "patlıcan":
...     i.rjust(10, ".")
...
'......elma'
'.....armut'
'..patlıcan'


#
# zfill()
#

>>> a = "12"
>>> a.zfill(3)
'012'


#
# partition(), rpartition()
#

>>> a = "istanbul"
>>> a.partition("an")
('ist', 'an', 'bul')

>>> a = "istanbul"
>>> a.partition("h")
('istanbul', '', '')

>>> b = "istihza"
>>> b.partition("i")
('', 'i', 'stihza')

>>> b.rpartition("i")
('ist', 'i', 'hza')

>>> b.partition("g")
('istihza', '', '')

>>> b.rpartition("g")
('', '', 'istihza')


#
# encode()
#

>>> "çilek".encode("cp1254")
b'\xe7ilek'


#
# expandtabs()
#

>>> a = "elma\tbir\tmeyvedir"
>>> a.expandtabs(10)
'elma      bir       meyvedir'

>>> print(a)
elma    bir     meyvedir

>>> a.expandtabs(20)
'elma                bir                 meyvedir'





