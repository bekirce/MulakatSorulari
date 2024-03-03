def fib3(sayi):
    if sayi == 1 or sayi == 2:
        toplam = 1
        return toplam
    bottom_up = [None]*(sayi+1) #dizi oluşturur   
    bottom_up[1] = 1 
    bottom_up[2] = 1 
    for i in range(3,sayi+1):    # range(0,sayi+1): 0dan baslayarak 6 sayi git yani 5. dizi son olur
        bottom_up[i]=bottom_up[i-1]+bottom_up[i-2]
    return bottom_up[sayi]

print(fib3(1500))