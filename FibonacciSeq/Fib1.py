def fib1(sayi):                         
    if sayi == 1 or sayi == 2:
        toplam = 1
        return toplam

    else:
        toplam = fib1(sayi-1)+fib1(sayi-2)
        return toplam

print(fib1(40))