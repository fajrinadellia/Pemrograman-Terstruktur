def ubahHuruf(teks, a, b):
    myList = list(teks)
    gabung = ''
    for huruf in myList:
        if(huruf == a):
            huruf = b
        gabung = ''.join([gabung, huruf])
    return gabung
print(ubahHuruf('MATEMATIKA', 'T', 'S'))
