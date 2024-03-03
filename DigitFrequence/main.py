def freq_Digit(x):                              #s = girilen str
    str_digit_memo = []                         #girilen diziden sayilar bu dizinin içine alınır. harfler atılır.
    int_digit_memo = []                         # bu dizi char karakterlerden olustugu için bu int degerlere donusturulur ve bu degerler yeni diziye atılır.
    repu = 0                                    #aynı sayı tekrar ettiginde sonun kacıncı kez tekrar ettigini bulmak için sayı degişkeni kullanılır.
    s=0

    for i in range(len(x)):                     #ilk anda girilen dizinin boyutu kadar for döngüsü yapılır.
        if x[i] > chr(47) and x[i]<chr(58) :    #girilen diziden sayıları almak için girilen stringin asci degerlerine bakılır.
            str_digit_memo += x[i]              #48 ve 57 arasındakiler sayı oldugu için onlar yeni diziye atılır
        elif x[i] == ' ':                       #egerki input olarak sadece null girildiyse s değişkenin degeri degiştirilir.
            s=1
            break

    if s==0:                                    #null dirilmediyse dizideki char karakterler inte donusturulur ve yeni diziye aktırılma işlemi burda yapılır
        for i in range(10):
            for j in range(len(str_digit_memo)):
                t = int(str_digit_memo[j])
                if t == i:
                    repu += 1

            int_digit_memo += [repu]
            repu = 0

        print("Output :",*int_digit_memo)       #* olmasaydı yazdırılan output = [1,2,0,1,3,4,0,0,0,1,0]... şeklinde olucaktı(örnek olarak)

    elif s==1:
        print("Output : NULL")

while True:
    x=(input("Input  : "))
    freq_Digit(x)