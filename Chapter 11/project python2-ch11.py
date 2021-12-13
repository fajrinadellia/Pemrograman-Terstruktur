from datetime import*

dataFile = open("data perpus.txt", "a")
dataList = []
while True:
    kode = input("Masukkan Kode Member	:")
    nama = input("Masukkan Nama Member	:")
    buku = input("Masukkan Judul Buku	:")
    tanggalPinjam = datetime.date(datetime.now())
    tanggalKembali = tanggalPinjam + timedelta(days=7)
    string = kode+"|"+nama+"|"+buku+"|"+str(tanggalPinjam)+"|"+str(tanggalKembali)+"\n"
    dataList.append(string)
    ans = input("Input data lagi(y/n)?")
    if ans in("N", "n"):
        break
i = 0
for data in dataList:
    dataX = str(dataList[i])
    dataFile.write(dataX+"\n")
    i += 1

dataFile.close()
