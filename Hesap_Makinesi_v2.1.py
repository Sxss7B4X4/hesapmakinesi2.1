import time
print ("Yapılacak Matematik İşlemini Seçiniz")

print ("Çarpma İçin 1 Toplama İçin 2")

secim=input("Seçiminiz Nedir 1-2 : ")

sayi1 = int(input("1.ci Sayı : "))
sayi2 = int(input("2.ci Sayı : "))
if secim =="1":
    print(sayi1, "*" ,sayi2,)
print (sayi1 * sayi2)
if secim=="2":
    print(sayi1, "+" ,sayi2, "=" ,sayi1+sayi2)
time.sleep(3)
# Made By Memati Baş#4472
