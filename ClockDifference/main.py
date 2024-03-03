def clockDif(x, y):
    if x > 12:
        x = x - 12
        
    akrepAciDegeri = 30
    yelkovanAciDegeri = 6
    akrepDerece = int (x * akrepAciDegeri)
    yelkovanDerece = int (y * yelkovanAciDegeri)

    print("Akrep derecesi: ", akrepDerece)
    print("Yelkovan derecesi: ", yelkovanDerece)

    if (akrepDerece > yelkovanDerece):  #akrep degeri, yelkovandan buyuk ise
        result = akrepDerece - yelkovanDerece
    else :                              #yelkovan degeri akrepten buyuk ise
        result = yelkovanDerece - akrepDerece

    print(result)

while True:
    x=int (input("Saati gir: "))
    y=int (input("Dakikayi gir: "))
    clockDif(x, y) 

    