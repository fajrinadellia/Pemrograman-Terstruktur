dataFile = open("teks2.txt", "w")
while True:
    nim = input("Masukkan NIM		:")
    nama = input("Masukkan Nama Mhs	:")
    alamat = input("Masukkan Alamat	:")

    string = nim+"|"+nama+"|"+alamat+"\n"

    dataFile.write(string)
    ans = input("Input data lagi(y/n)?")
    if ans in("N", "n"):
        break

dataFile.close()
    
