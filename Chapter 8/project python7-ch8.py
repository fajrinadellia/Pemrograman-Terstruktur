def urutpalingmahal(data):
    isi = list(data.values())
    isi.sort(reverse=True)
    for x,y in data.items():
        if(isi[0] == y):
            return x
    return False
    

buah = {"apel" : 5000, "jeruk" : 8500, "mangga" : 7800, "duku" : 6500}
hasil = urutpalingmahal(buah)
print("Nama buah yang harga satuannya paling mahal yaitu : ", hasil)
