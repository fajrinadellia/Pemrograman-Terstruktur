n = 0
sum = 0

print("-" *28)
print("PROGRAM HITUNG RATA-RATA")
print("-" *28)

while True:
    try:
        bil = int(input("Masukkan bilangan bulat:" ))
        n = n + 1
        sum = sum = bil
        ulang = input("Lagi(y/n)?: ")
        while(ulang != "y" and ulang != "n"):
            ulang = input("\nMaaf inputan salah. Coba lagi.\nLagi(y/n)?: ")
        if ulang == "n":
            ratarata= sum/n
            print("Rata-ratanya adalah:", ratarata)
            break
        elif ulang !="y":
            break
        
    except ValueError:
        print("Bukan bilangan bulat")


