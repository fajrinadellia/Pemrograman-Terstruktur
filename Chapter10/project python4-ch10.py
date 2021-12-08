dataFile = open("teks2.txt", "r")
dataList = []
data = dataFile.readlines()

for i in range(len(data)):
    pisahData = data[i].split("|")
    dataDict = {"nim": pisahData[0], "nama": pisahData[1], "alamat": pisahData[2].replace("\n", "")}
    dataList.append(dataDict)

search = input("Masukkan NIM yang mau dicari: ")

for dataX in dataList:
    if dataX["nim"] == search:
        print("Data Mahasiawa")
        print("NIM   :",dataX["nim"])
        print("NAMA  :",dataX["nama"])
        print("ALAMAT:",dataX["alamat"])
        break
else:
    print("Data mahasiswa tidak ditemukan")
    
dataFile.close()
