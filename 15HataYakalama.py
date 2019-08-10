#
# Hata Yakalama
#


# try... except... as... finally...

while True:
    ilk_sayı    = input("ilk sayı: ")
    ikinci_sayı = input("ikinci sayı: ")
    try:
        sayı1 = int(ilk_sayı)
        sayı2 = int(ikinci_sayı)
        print(sayı1, "/", sayı2, "=", sayı1 / sayı2)
        break
    except (ValueError, ZeroDivisionError) as e:
        print("Bir hata oluştu!")
        print("Error Message:", e)
'''
    except ValueError as e:
        print("Lütfen sadece sayı girin!")
        print("Error Message:", e)
    except ZeroDivisionError as e:
        print("Lütfen böleni sıfır girmeyin!")
        print("Error Message:", e)
'''


# raise -> ‘Python tarzı’ bir hata mesajı göstermek için
bölünen = int(input("bölünecek sayı: "))

if bölünen == 23:
    raise Exception("Bu programda 23 sayısını görmek istemiyorum!")

bölen = int(input("bölen sayı: "))
print(bölünen/bölen)