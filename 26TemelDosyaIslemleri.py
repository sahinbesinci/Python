#
#
# Temel Dosya İşlemleri
#
#


#
# Dosya Oluşturmak
# f = open(dosya_adı, kip)

>>> tahsilat_dosyası = open("tahsilat_dosyası.txt", "w")

#  r adlı kaçış dizisinden de yararlanabilirsiniz:
>>> open("C:\\aylar\\nisan\\toplam masraf\\masraf.txt", "w")
>>> open(r"C:\aylar\nisan\toplam masraf\masraf.txt", "w")
>>> open("/dosyayı/oluşturmak/istediğimiz/dizin/dosya_adı", "w")



#
# Dosyaya Yazmak
# dosya.write(yazılacak_şeyler)

>>> tahsilat_dosyası = open("tahsilat_dosyası.txt", "w")
>>> tahsilat_dosyası.write("Halil Pazarlama: 120.000 TL")
>>> tahsilat_dosyası.close()



#
# Dosya Okumak
#

>>> tahsilat_dosyası = open("tahsilat_dosyası.txt", "r")
>>> print(tahsilat_dosyası.read())
Ahmet Özbudak : 0533 123 23 34
Mehmet Sülün  : 0532 212 22 22
Sami Sam      : 0542 333 34 34


>>> tahsilat_dosyası = open("tahsilat_dosyası.txt", "r")
>>> print(tahsilat_dosyası.readline())
Ahmet Özbudak : 0533 123 23 34

>>> print(tahsilat_dosyası.readline())
Mehmet Sülün  : 0532 212 22 22

>>> print(tahsilat_dosyası.readline())
Sami Sam      : 0542 333 34 34

>>> print(tahsilat_dosyası.readline())


>>> tahsilat_dosyası = open("tahsilat_dosyası.txt", "r")
>>> for satir in tahsilat_dosyası.readlines():
...     print(satir)
...
Ahmet Özbudak : 0533 123 23 34

Mehmet Sülün  : 0532 212 22 22

Sami Sam      : 0542 333 34 34

>>> tahsilat_dosyası = open("tahsilat_dosyası.txt", "r")
>>> print(tahsilat_dosyası.readlines())
['Ahmet Özbudak : 0533 123 23 34\n', 'Mehmet Sülün  : 0532 212 22 22\n', 'Sami Sam      : 0542 333 34 34']


#
# Dosyaları Otomatik Kapatma
#

>>> with open("tahsilat_dosyası.txt", "a") as tahsilat_dosyası:
...    tahsilat_dosyası.write("Şahin Beşinci : 0537 055 66 77\n")
...


#
# Dosyayı İleri-Geri Sarmak
#

>>> tahsilat_dosyası = open("tahsilat_dosyası.txt", "r")
>>> print(tahsilat_dosyası.read())
Ahmet Özbudak : 0533 123 23 34
Mehmet Sülün  : 0532 212 22 22
Sami Sam      : 0542 333 34 34
Şahin Beşinci : 0537 055 66 77

>>> print(tahsilat_dosyası.read())

>>> tahsilat_dosyası.tell()
131

>>> tahsilat_dosyası.seek(0)
0

>>> print(tahsilat_dosyası.read())
Ahmet Özbudak : 0533 123 23 34
Mehmet Sülün  : 0532 212 22 22
Sami Sam      : 0542 333 34 34
Şahin Beşinci : 0537 055 66 77

>>> tahsilat_dosyası.seek(20)
20

>>> print(tahsilat_dosyası.read())
3 123 23 34
Mehmet Sülün  : 0532 212 22 22
Sami Sam      : 0542 333 34 34
Şahin Beşinci : 0537 055 66 77


#
# Dosyalarda Değişiklik Yapmak
#

>>> with open("tahsilat_dosyası.txt", "a") as tahsilat_dosyası:
...    tahsilat_dosyası.write("Cavit Fidan   : 0555 555 55 55\n")

>>> print(open("tahsilat_dosyası.txt", "r").read())
Ahmet Özbudak : 0533 123 23 34
Mehmet Sülün  : 0532 212 22 22
Sami Sam      : 0542 333 34 34
Şahin Beşinci : 0537 055 66 77
Cavit Fidan   : 0555 555 55 55


#
# Dosyaların Başında Değişiklik Yapmak
#

>>> with open("tahsilat_dosyası.txt", "r+") as tahsilat_dosyası:
...     veri = tahsilat_dosyası.read()
...     tahsilat_dosyası.seek(0)
...     tahsilat_dosyası.write("Sedat Köz\t: 0322 234 45 45\n"+veri)
...
0
180
>>> print(open("tahsilat_dosyası.txt", "r").read())
Sedat Köz     : 0322 234 45 45
Ahmet Özbudak : 0533 123 23 34
Mehmet Sülün  : 0532 212 22 22
Sami Sam      : 0542 333 34 34
Şahin Beşinci : 0537 055 66 77
Cavit Fidan   : 0555 555 55 55


#
# Dosyaların Ortasında Değişiklik Yapmak
#

>>> with open("tahsilat_dosyası.txt", "r+") as tahsilat_dosyası:
...     veri = tahsilat_dosyası.readlines()
...     veri.insert(2, "Sedat Köz\t: 0322 234 45 45\n")
...     tahsilat_dosyası.seek(0)
...     tahsilat_dosyası.writelines(veri)
...
0
>>> print(open("tahsilat_dosyası.txt", "r").read())
Sedat Köz     : 0322 234 45 45
Ahmet Özbudak : 0533 123 23 34
Sedat Köz     : 0322 234 45 45
Mehmet Sülün  : 0532 212 22 22
Sami Sam      : 0542 333 34 34
Şahin Beşinci : 0537 055 29 61
Cavit Fidan   : 0555 555 55 55



#
# Dosyaya Erişme Kipleri
#


"r"	Bu öntanımlı kiptir. Bu kip dosyayı okuma yetkisiyle açar. Ancak bu kipi kullanabilmemiz için, ilgili dosyanın disk üzerinde halihazırda var olması gerekir. Eğer bu kipte açılmak istenen dosya mevcut değilse Python bize bir hata mesajı gösterecektir. Dediğimiz gibi, bu öntanımlı kiptir. Dolayısıyla dosyayı açarken herhangi bir kip belirtmezsek Python dosyayı bu kipte açmak istediğimizi varsayacaktır.
"w"	Bu kip dosyayı yazma yetkisiyle açar. Eğer belirttiğiniz adda bir dosya zaten disk üzerinde varsa, Python hiçbir şey sormadan dosya içeriğini silecektir. Eğer belirttiğiniz adda bir dosya diskte yoksa, Python o adda bir dosyayı otomatik olarak oluşturur.
"a"	Bu kip dosyayı yazma yetkisiyle açar. Eğer dosya zaten disk üzerinde mevcutsa içeriğinde herhangi bir değişiklik yapılmaz. Bu kipte açtığınız bir dosyaya eklediğiniz veriler varolan verilere ilave edilir. Eğer belirttiğiniz adda bir dosya yoksa Python otomatik olarak o adda bir dosyayı sizin için oluşturacaktır.
"x"	Bu kip dosyayı yazma yetkisiyle açar. Eğer belirttiğiniz adda bir dosya zaten disk üzerinde varsa, Python varolan dosyayı silmek yerine size bir hata mesajı gösterir. Zaten bu kipin “w” kipinden farkı, varolan dosyaları silmemesidir. Eğer belirttiğiniz adda bir dosya diskte yoksa, bu kip yardımıyla o ada sahip bir dosya oluşturabilirsiniz.
"r+"	Bu kip, bir dosyayı hem yazma hem de okuma yetkisiyle açar. Bu kipi kullanabilmeniz için, belirttiğiniz dosyanın disk üzerinde mevcut olması gerekir.
"w+"	Bu kip bir dosyayı hem yazma hem de okuma yetkisiyle açar. Eğer dosya mevcutsa içerik silinir, eğer dosya mevcut değilse oluşturulur.