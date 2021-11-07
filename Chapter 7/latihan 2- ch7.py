try:
    namafile = input("Masukkan nama file: ")
    while True:
        file = open(namafile, "a")
        tambahdata = input("Data yang mau ditambahkan: ")
        file.write(tambahdata + "\n")
        file.close()
        ulang = input("Mau lagi(y/n): ")
        while(ulang != "y" and ulang != "n"):
            ulang = input("\nMaaf inputan salah. Coba lagi.\nMau lagi(y/n): ")
        if ulang == "n":
            break
        elif ulang !="y":
            break
    
except FileNotFoundError:
        print("File tidak ditemukan")


    

