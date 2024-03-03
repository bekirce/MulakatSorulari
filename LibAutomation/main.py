import os
kitapListe = list()

menu = """
[1] Kitap Ekle
[2] Kitap Al
[3] Kitap Listele
[Q] Cikis
"""

def Kitap_Ekle(kitap:tuple,liste:list):
    liste.append(kitap)
    print ("Ekleme islemi tamamlandi")
    print ("Ana menuye donmek icinde enter'a basin!")
    input ()

def kontrol(kitap:tuple,liste:list):
    if kitap in liste:
        return True
    else:
        return False

def Kitap_Cikar(kitap:tuple,liste:list):
    if kontrol(kitap,liste):
        liste.remove(kitap)
        print("Kitap Cikartildi")
        print("Ana menuye donmek icin enter'a basin!")
        input()
    else:
        print("Aradiginiz Kitap Mevcut Degildir")
        print("Ana menuye donmek icin enter'a basin!")
        input()

def Kitap_Listele(liste:list):
    for i in liste:
        print("Kitap Adi :{} ---->>> Kitabin Yazari : {}".format(i[0],i[1]))

    print("Ana menuye donmek icin enter'a basin!")
    input()

while True :
    os.system("cls")
    print(menu)
    secim = input("Isleminizi seciniz : ")

    if secim =="1":
        kitap_adi=input("Kitabin Adi : ")
        kitap_yazari= input("Kitabin Yazari : ")
        kitap = (kitap_adi,kitap_yazari)
        Kitap_Ekle(kitap,kitapListe)

    elif secim =="2":
        kitap_adi=input("Kitabin Adi : ")
        kitap_yazari= input("Kitabin Yazari : ")
        kitap = (kitap_adi,kitap_yazari)
        Kitap_Cikar(kitap,kitapListe)

    elif secim =="3":
        Kitap_Listele(kitapListe)

    elif secim =="Q" or secim == "q":
        print("Yine Bekleriz...")
        quit()

    else :
        print("Hatali Giris Yaptiniz...")
        input("Ana menuye donmek icin enter'a basin ")