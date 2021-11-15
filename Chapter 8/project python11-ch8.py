buah = {'apel' : 5000, 'jeruk' : 8500, 'mangga' : 7800, 'duku' : 6500}
def showData(data):
    print("\nDaftar Buah :")
    number = 1
    for x,y in data.items():
        print("{0}. {1} - {2}".format(number,x,y))
        number += 1
        
showData(buah)
olahlagi = 'y'
while olahlagi == 'y':
    print('-'*35)
    print('A. Tambah data buah')
    print('B. Beli buah')
    piliholahdata = input("\npilihan menu : ")
    if(piliholahdata == 'A'):
        namabuahbaru = input('Masukkan nama buah : ')
        if(namabuahbaru in buah):
            print('buah sudah ada di dalam daftar')
        else:
            while True:
                try:
                    hargabaru = int(input('Masukkan harga satuan	: '))
                    buah[namabuahbaru] = hargabaru
                    showData(buah)
                    break
                except ValueError:
                    print('data yang anda masukan bukan angka / salah')
    elif(piliholahdata == 'B'):
        showData(buah)
        total = 0
        belilagi = 'y'
        while belilagi == 'y':
            choose = input("\nNama buah yang dibeli : ")
            if(choose in buah):
                while True:
                    try:
                        kg = float(input('Berapa Kg : '))
                        total += (buah[choose] * kg)
                        belilagi = input("Beli buah yang lain (y/n) ? ")
                        break
                    except ValueError:
                        print('data yang anda masukan bukan angka / salah')
                            
            else:
                print('\n{0} tidak ada dalam daftar buah'.format(choose))
        print('='*35)
        print("Total harga :",total)
        break
    
   
