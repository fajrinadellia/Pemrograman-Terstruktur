dataFile = open("teks2.txt", "r")
dataList = []
data = dataFile.readlines()

for i in range(len(data)):
    pisahData = data[i].split("|")
    dataDict = {"nim": pisahData[0], "nama": pisahData[1], "alamat": pisahData[2].replace("\n", "")}
    dataList.append(dataDict)
print(dataList)
dataFile.close()
