import random
print("Aklımda 1-100 arası sayı var ve seninde bunu bulmak için 9 hakkın var.İyi eğlenceler")
sayi = random.randint(1,100)
can = 9
hak = can
sayac = 0

while hak > 0:
    hak -= 1
    sayac += 1
    tahmin = int(input('tahmin: '))

    if sayi == tahmin:
        print(f'Tebrikler {sayac}. defada bildiniz.')
        break
    elif sayi > tahmin:
        print('Daha yüksek sayı tahmin et')
    else:
        print('Daha küçük sayı tahmin et')

    if hak == 0:
        print(f'hakkınız bitti. Tutulan sayı : {sayi}')