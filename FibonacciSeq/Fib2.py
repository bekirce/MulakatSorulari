def fib2(sayi,memo):                    #fib2 hafizaya atarak yapar. yani her degeri önce hafızaya atar zamanı geldiginde o hafızadan alır ve son degeri  verir.
    if memo[sayi] is not None: #null
        return memo[sayi]

    if sayi == 1 or sayi == 2:
        toplam = 1
        return toplam

    else:
        toplam = fib2(sayi-1,memo)+fib2(sayi-2,memo)
        memo[sayi]=toplam
        return toplam

def fib_memo(sayi):
    memo = [None]*(sayi+1)
    return fib2(sayi,memo)

print(fib_memo(950))