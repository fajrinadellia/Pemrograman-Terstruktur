try:
    
    namafile = input("Masukkan nama file: ")
    print("Isi file ", namafile, "adalah:")
    file = open(namafile, "r")
    print(file.read())
    
except FileNotFoundError:
    print("File tidak ditemukan")
