myFile = open("teks6.txt", "w")
teks = input("Masukkan teks asli             :")
n = input("Jumlah huruf yang ingin digeser:")
teksAsli = teks +"\nNilai n = "+ str(n)
myFile.write(teksAsli)

teks = list(teks)
h = 0
newTeks = []
for char in teks:
    alphabet = teks[h]
    if alphabet != " ":
        asci = ord(str(alphabet))
        asci = int(asci) + int(n)
        if asci > 90:
            asciAngka = asci-90+64
        else:
            asciAngka = asci
        newAsci = chr(asciAngka)
        newTeks.append(newAsci)
    else:
        newAsci = " "
        newTeks.append(newAsci)
    h += 1

newFile = open("teks6_2.txt", "w")
newFile.write("".join(newTeks))

newFile.close()
myFile.close()


