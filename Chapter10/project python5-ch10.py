dataFile = open("teks5.txt", "r")
dataList = []
data = dataFile.readlines()
i = 0

for dataKu in data:
    pisahData = str(data[i])
    pisahData = pisahData.split("|")
    dataList.append(pisahData)
    i += 1
      
fileBaru = open("teks5_2.txt", "w+")
a = 0
for bilangan in dataList:
    bil1 = int(dataList[a][0])
    bil2 = int(dataList[a][1])
    fileBaru.write(str(bil1+bil2)+"\n")
    a += 1
fileBaru.close()
    
result = open ("teks5_2.txt")
print(result.read())

dataFile.close()
result.close()
    
    


