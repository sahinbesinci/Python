#
#
# Karakter Dizilerinin Metotları
#
#


#
# str.maketrans(), translate()
#

>>> kaynak = "şçöğüıŞÇÖĞÜİ"
>>> hedef  = "scoguiSCOGUI"
>>> çeviri_tablosu = str.maketrans(kaynak, hedef)
>>> metin = "Bildiğiniz gibi, internet üzerinde bazen Türkçe karakterleri kullanamıyoruz."
>>> print(metin.translate(çeviri_tablosu))
Bildiginiz gibi, internet uzerinde bazen Turkce karakterleri kullanamiyoruz.

>>> print(çeviri_tablosu)
{351: 115, 231: 99, 246: 111, 287: 103, 252: 117, 305: 105, 350: 83, 199: 67, 214: 79, 286: 71, 220: 85, 304: 73}

>>> for i in 351, 231, 246, 287, 252, 305, 350, 199, 214, 286, 220, 304:
...    print(i, chr(i), end=", ")
351 ş, 231 ç, 246 ö, 287 ğ, 252 ü, 305 ı, 350 Ş, 199 Ç, 214 Ö, 286 Ğ, 220 Ü, 304 İ,

>>> for i in 115, 99, 111, 103, 117, 105, 83, 67, 79, 71, 85, 73:
...    print(i, chr(i), end=", ")
115 s, 99 c, 111 o, 103 g, 117 u, 105 i, 83 S, 67 C, 79 O, 71 G, 85 U, 73 I,

>>> çeviri_tablosu = str.maketrans(kaynak, hedef)

# satırını şu şekilde de yazabilirsiniz:

>>> çeviri_tablosu = ''.maketrans(kaynak, hedef)
>>> çeviri_tablosu = 'mahmut'.maketrans(kaynak, hedef)
>>> çeviri_tablosu = 'zalim dünya!'.maketrans(kaynak, hedef)


>>> metin = "Bfjflrk öa kdhsı yteua idjslyd bdcusldvdj ks?"
>>> q_klavye_düzeni = "qwertyuıopğüasdfghjklşi,zxcvbnmöç."
>>> f_klavye_düzeni = "fgğıodrnhpqwuieaütkmlyşxjövcçzsb.,"
>>> çeviri_tablosu = str.maketrans(q_klavye_düzeni, f_klavye_düzeni)
>>> print(metin.translate(çeviri_tablosu))
Bakalım bu metin doğru şekilde çevrilecek mi?


>>> metin = "Cem Yılmaz"
>>> kaynak = "CY"
>>> hedef  = "cy"
>>> silinecek = "eıa "
>>> çeviri_tablosu = str.maketrans(kaynak, hedef, silinecek)
>>> print(metin.translate(çeviri_tablosu))
cmylmz


#
# isalpha() 
#
# Bu metot yardımıyla bir karakter dizisinin ‘alfabetik’ olup olmadığını denetleyeceğiz
# Eğer bir karakter dizisi içinde yalnızca alfabe harfleri (‘a’, ‘b’, ‘c’ gibi...) varsa o karakter dizisi için ‘alfabetik’ diyoruz.
#

>>> a = "kezban"
>>> a.isalpha()
True

>>> b = "k3zb6n"
>>> b.isalpha()
False

#
# isdigit() 
#
# Bu metot da isalpha() metoduna benzer. 
#

>>> a = "12345"
>>> a.isdigit()
True

>>> b = "123445b"
>>> b.isdigit()
False

#
# isalnum() 
#
# Bu metot, bir karakter dizisinin ‘alfanümerik’ olup olmadığını denetlememizi sağlar
# Yani sayı ve harflerden oluşan karakter dizilerine alfanümerik karakter dizileri adı verilir.
#


>>> a = "123abc"
>>> a.isalnum()
True

>>> b = "123abc>"
>>> b.isalnum()
False


#
# isdecimal() 
#

>>> a = "123"
>>> a.isdecimal()
True

>>> a = "123.3"
>>> a.isdecimal()
False


#
# isidentifier() 
#

>>> 1a = 12
  File "<stdin>", line 1
    1a = 12
     ^
SyntaxError: invalid syntax

>>> "1a".isidentifier()
False

>>> "liste1".isidentifier()
True


#
# isnumeric() 
#

>>> "12".isnumeric()
True

>>> "dasd".isnumeric()
False


#
# isspace() 
#

>>> a = " "
>>> a.isspace()
True

>>> a = "    "
>>> a.isspace()
True

>>> a = "" #karakter dizimiz tamamen boş. İçinde boşluk karakteri bile yok...
>>> a.isspace()
False

>>> a = "fd"
>>> a.isspace()
False


#
# isprintable() 
#

>>> print("birinci satır\nikinci satır")
birinci satır
ikinci satır


>>> karakter = "a"
>>> karakter.isprintable()
True

>>> karakter = "\n"
>>> karakter.isprintable()
False
