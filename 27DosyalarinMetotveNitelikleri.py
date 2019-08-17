#
#
# Dosyaların Metot ve Nitelikleri
#
#

>>> dosya = open("tahsilat_dosyası.txt", "w")
>>> print(*[metot for metot in dir(dosya) if not metot.startswith("_")], sep="\n")
buffer
close
closed
detach
encoding
errors
fileno
flush
isatty
line_buffering
mode
name
newlines
read
readable
readline
readlines
seek
seekable
tell
truncate
writable
write
writelines


#
# closed Niteliği
#

>>> dosya.closed
False

>>> dosya.close()
>>> dosya.closed
True


#
# readable() Metodu
# Bu metot bir dosyanın okuma yetkisine sahip olup olmadığını sorgulamamızı sağlar. 

>>> dosya = open("tahsilat_dosyası.txt", "w")
>>> dosya.readable()
False

>>> dosya = open("tahsilat_dosyası.txt", "r")
>>> dosya.readable()
True


#
# writable() Metodu
# Bu metot bir dosyanın yazma yetkisine sahip olup olmadığını sorgulamamızı sağlar.

>>> dosya = open("tahsilat_dosyası.txt", "w")
>>> dosya.writable()
True

>>> dosya = open("tahsilat_dosyası.txt", "r")
>>> dosya.writable()
False


#
# truncate() Metodu
# Bu metot, henüz işlemediğimiz metotlar arasında en önemlilerinden biridir. Bu metot yardımıyla dosyalarımızı istediğimiz boyuta getirebiliyoruz.

>>> with open("tahsilat_dosyası.txt", "r+") as tahsilat_dosyası:
...     tahsilat_dosyası.truncate(10)


#
# mode Niteliği
# 

>>> tahsilat_dosyası = open("tahsilat_dosyası.txt")
>>> tahsilat_dosyası.mode
'r'

#
# name  Niteliği
# 

>>> tahsilat_dosyası = open("tahsilat_dosyası.txt")
>>> tahsilat_dosyası.name
'tahsilat_dosyası.txt'

#
# encoding   Niteliği
# 

>>> tahsilat_dosyası = open("tahsilat_dosyası.txt")
>>> tahsilat_dosyası.encoding
'UTF-8'
