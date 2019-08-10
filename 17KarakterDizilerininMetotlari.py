#
#
# Karakter Dizilerinin Metotları
#
#

#
# replace() -> Yani bu metodu kullanarak bir karakter dizisi içindeki karakterleri başka karakterlerle değiştirebileceğiz.
#

# karakter_dizisi.replace(eski_karakter_dizisi, yeni_karakter_dizisi)

>>> kardiz = "elma"
>>> kardiz.replace("e", "E")
'Elma'

>>> kardiz = "memleket"
>>> kardiz.replace("ket", "KET")
'memleKET'

>>> kardiz.replace("e", "")
'mmlkt'

#Burada replace() metodunu üçüncü bir parametre ile birlikte kullandık. Üçüncü parametre olarak 1 sayısını verdiğimiz için replace() metodu sadece tek bir "e" harfini sildi.

>>> kardiz.replace("e", "", 1)
'mmleket'

>>> kardiz.replace("e", "", 2)
'mmlket'


#
# split(), rsplit(), splitlines()
#

>>> kardiz = "İstanbul Büyükşehir Belediyesi"

>>> kardiz.split()
['İstanbul', 'Büyükşehir', 'Belediyesi']

>>> for i in kardiz.split():
...     print(i)
...
İstanbul
Büyükşehir
Belediyesi

>>> kardiz = "Bolvadin, Kilis, Siverek, İskenderun, İstanbul"
>>> kardiz = kardiz.split(",")
>>> print(kardiz)
['Bolvadin', ' Kilis', ' Siverek', ' İskenderun', ' İstanbul']

>>> for i in kardiz:
...     print(i)
...
Bolvadin
Kilis
Siverek
İskenderun
İstanbul

>>> kardiz = "Ankara Büyükşehir Belediyesi"

>>> kardiz.split(" ", 1)
['Ankara', 'Büyükşehir Belediyesi']

# Bu ikinci parametre, karakter dizisinin kaç kez bölüneceğini belirler:
>>> kardiz.split(" ", 2)
['Ankara', 'Büyükşehir', 'Belediyesi']

>>> import sys
>>> sürüm = sys.version

>>> sürüm[:5].split(".")
['3', '6', '8']

>>> sürüm[:5].split(".")[0]
'3'

>>> int(sürüm[:5].split(".")[0])
3

>>> kardiz.split(" ", 1)
['Ankara', 'Büyükşehir Belediyesi']

>>> kardiz.rsplit(" ", 1)
['Ankara Büyükşehir', 'Belediyesi']

>>> metin = """Python programlama dili Guido Van Rossum adlı Hollandalı bir programcı
... tarafından 90'lı yılların başında geliştirilmeye başlanmıştır. Çoğu insan, isminin
... Python olmasına bakarak, bu programlama dilinin, adını piton yılanından aldığını
... düşünür. Ancak zannedildiğinin aksine bu programlama dilinin adı piton yılanından
... gelmez. Guido Van Rossum bu programlama dilini, The Monty Python adlı bir İngiliz
... komedi grubunun, Monty Python's Flying Circus adlı gösterisinden esinlenerek
... adlandırmıştır. Ancak her ne kadar gerçek böyle olsa da, Python programlama
... dilinin pek çok yerde bir yılan figürü ile temsil edilmesi neredeyse bir gelenek
... halini almıştır diyebiliriz."""
>>> print(metin.splitlines())
['Python programlama dili Guido Van Rossum adlı Hollandalı bir programcı', "tarafından 90'lı yılların başında geliştirilmeye başlanmıştır. Çoğu insan, isminin", 'Python olmasına bakarak, bu programlama dilinin, adını piton yılanından aldığını', 'düşünür. Ancak zannedildiğinin aksine bu programlama dilinin adı piton yılanından', 'gelmez. Guido Van Rossum bu programlama dilini, The Monty Python adlı bir İngiliz', "komedi grubunun, Monty Python's Flying Circus adlı gösterisinden esinlenerek", 'adlandırmıştır. Ancak her ne kadar gerçek böyle olsa da, Python programlama', 'dilinin pek çok yerde bir yılan figürü ile temsil edilmesi neredeyse bir gelenek', 'halini almıştır diyebiliriz.']

>>> print(metin.splitlines(True))
['Python programlama dili Guido Van Rossum adlı Hollandalı bir programcı\n', "tarafından 90'lı yılların başında geliştirilmeye başlanmıştır. Çoğu insan, isminin\n", 'Python olmasına bakarak, bu programlama dilinin, adını piton yılanından aldığını\n', 'düşünür. Ancak zannedildiğinin aksine bu programlama dilinin adı piton yılanından\n', 'gelmez. Guido Van Rossum bu programlama dilini, The Monty Python adlı bir İngiliz\n', "komedi grubunun, Monty Python's Flying Circus adlı gösterisinden esinlenerek\n", 'adlandırmıştır. Ancak her ne kadar gerçek böyle olsa da, Python programlama\n', 'dilinin pek çok yerde bir yılan figürü ile temsil edilmesi neredeyse bir gelenek\n', 'halini almıştır diyebiliriz.']

#
# lower()
#

>>> kardiz = "Ankara Büyükşehir Belediyesi"
>>> kardiz.lower()
'ankara büyükşehir belediyesi'

>>> kardiz = "arMuT"
>>> kardiz.lower()
'armut'


#
# upper()
#

>>> kardiz = "kalem"
>>> kardiz.upper()
'KALEM'

#
# islower(), isupper()
#

>>> kardiz = "istihza"
>>> kardiz.islower()
True

>>> kardiz = "Ankara"
>>> kardiz.islower()
False

>>> kardiz = "İSTİHZA"
>>> kardiz.isupper()
True

>>> kardiz = "python"
>>> kardiz.isupper()
False


#
# endswith(), startswith()
#


>>> kardiz = "istihza"
>>> kardiz.endswith("a")
True

>>> kardiz.endswith("z")
False


>>> d1 = "python.ogg"
>>> d2 = "tkinter.mp3"
>>> d3 = "pygtk.ogg"
>>> d4 = "movie.avi"
>>> d5 = "sarki.mp3"
>>> d6 = "filanca.ogg"
>>> d7 = "falanca.mp3"
>>> d8 = "dosya.avi"
>>> d9 = "perl.ogg"
>>> d10 = "c.avi"
>>> d11 = "c++.mp3"
>>>
>>> for i in d1, d2, d3, d4, d5, d6, d7, d8, d9, d10, d11:
...     if i.endswith(".mp3"):
...         print(i)
...
tkinter.mp3
sarki.mp3
falanca.mp3
c++.mp3


>>> for i in d1, d2, d3, d4, d5, d6, d7, d8, d9, d10, d11:
...     if i[-4:len(i)] == ".mp3":
...         print(i)
...
tkinter.mp3
sarki.mp3
falanca.mp3
c++.mp3


>>> kardiz = "python"
>>> kardiz.startswith("p")
True

>>> kardiz.startswith("a")
False


>>> for i in d1, d2, d3, d4, d5, d6, d7, d8, d9, d10, d11:
...     if i.startswith("py"):
...         print(i)
...
python.ogg
pygtk.ogg
