kontrol = True
while kontrol == True:
    ilk_sayı    = input("ilk sayı: ")
    ikinci_sayı = input("ikinci sayı: ")
    try:
        sayı1 = int(ilk_sayı)
        sayı2 = int(ikinci_sayı)
        print(sayı1, "/", sayı2, "=", sayı1 / sayı2)
        kontrol = False
    except ValueError:
        print("Lütfen sadece sayı girin!")
        kontrol = True
    except ZeroDivisionError:
        print("Lütfen sıfıra bölünemeyen sayı girmeyiniz.")
        kontrol = True