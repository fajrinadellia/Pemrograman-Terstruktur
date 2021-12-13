from datetime import*
from datetime import date

def diffDate(x):
    skrg = datetime.now()
    skrgX = datetime.date(datetime.now())
    x = x.split("-")
    year = int(x[0])
    month = int(x[1])
    day = int(x[2])
    date = datetime(year, month, day)
    selisih = skrg-date
    return selisih.days

def search(kodeMember):
    dataFile = open("data perpus.txt", "r")
    dataList = []
    data = dataFile.readlines()
    i = 0
    for i in range(len(data)):
        pisahData = data[i].split("|")
        dataList.append(pisahData)
        i += 1
        if kodeMember == pisahData[0]:
            print("\nData Peminjam Buku\n")
            print("Kode Member		    :", pisahData[0])
            print("Nama Member		    :", pisahData[1])
            print("Judul Buku		    :", pisahData[2])
            print("Tanggal Mulai Peminjaman    :", pisahData[3])
            print("Tanggal Maks Peminjaman     :", pisahData[4])
            print("Tanggal Pengembalian	    :", datetime.date(datetime.now()))
            
            terlambat = diffDate(pisahData[4])
            if terlambat < 0:
                kembali = terlambat*(-1)
                print("Terlambat                   : {} hari".format(kembali))
                denda = 2000*abs(kembali)
                print("Denda                       : Rp{}".format(denda))
            elif terlambat > 0:
                print("Terlambat                    : Tidak Terlambat")

kodeMember = input("Masukkan Kode Member        :")
search(kodeMember)
    

