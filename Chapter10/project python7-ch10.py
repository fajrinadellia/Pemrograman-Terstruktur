myFile = open("teks7_2.txt", "w")
teks = input("Masukkan teks sandi             :")
n = input("Jumlah huruf yang sudah digeser:")
teksSandi = teks +"\nNilai n = "+ str(n)
myFile.write(teksSandi)

teks = list(teks)
h = 0
teksAsli = []
for char in teks:
    alphabet = teks[h]
    if alphabet != " ":
        asci = ord(str(alphabet))
        asci = int(asci) - int(n)
        if asci < 65:
            asciAngka = 90-(64-asci)
        else:
            asciAngka = asci
        asciAsli = chr(asciAngka)
        teksAsli.append(asciAsli)
    else:
        asciAsli = " "
        teksAsli.append(asciAsli)
    h += 1

newFile = open("teks7.txt", "w")
newFile.write("".join(teksAsli))

newFile.close()
myFile.close()
