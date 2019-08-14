#
#
# f-string
#
#


>>> isim = 'Buğra'
>>> print('Selam {kime}!'.format(kime=isim))
Selam Buğra!

>>> "Selam Dünya!" # Normal bir karakter dizisi
'Selam Dünya!'
>>> f"Selam Dünya!" # Bu artık bir f-string
'Selam Dünya!'


isim = 'Buğra'
print(f'Selam {isim}!')


>>> isim = 'Buğra'
>>> yas = 18
>>> f'Onun adı {isim} ve o {yas} yaşında.'
'Onun adı Buğra ve o 18 yaşında.'

>>> isim = 'Buğra'
>>> yas = 18
>>> "Onun adı {} ve o {} yaşında.".format(isim, yas)
'Onun adı Buğra ve o 18 yaşında.'

>>> birinci_rakam = 5
>>> ikinci_rakam = 3
>>> f'Rakamların toplamı {birinci_rakam + ikinci_rakam} eder.'
'Rakamların toplamı 8 eder.'

>>> birinci_sayi = int(input('Birinci sayıyı girin: '))
Birinci sayıyı girin: 24
>>> ikinci_sayi = int(input('İkinci sayıyı girin: '))
İkinci sayıyı girin: 26
>>> f'Sayıların toplamı {birinci_sayi+ikinci_sayi} eder.'
'Sayıların toplamı 50 eder.'

>>> f'Sayıların toplamı { int(input("Birinci sayıyı girin: ")) + int(input("İkinci sayıyı girin: ")) } eder.'
Birinci sayıyı girin: 10
İkinci sayıyı girin: 7
'Sayıların toplamı 17 eder.'








