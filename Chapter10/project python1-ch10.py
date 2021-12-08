myFile = open ("teks1.txt", "r")
bilGenap = 0
bilGanjil = 0
i = 0
dataFile = myFile.readlines()
myFile.close()

for data in dataFile:
    if int(dataFile[i]) % 2 == 0:
        bilGenap += 1
    else:
        bilGanjil += 1
        
    i += 1

print("Banyaknya bilangan genap: ", bilGenap)
print("Banyaknya bilangan ganjil: ", bilGanjil)


