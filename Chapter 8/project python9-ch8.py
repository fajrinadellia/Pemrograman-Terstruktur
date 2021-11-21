try:
    buah = {'apel' : 5000, 'jeruk' : 8500, 'mangga' : 7800, 'duku' : 6500}
    print("\nDaftar Buah :")
    number = 1
    for x,y in buah.items():
        print("{0}. {1} - {2}".format(number,x,y))
        number += 1

    pilih = input("\nNama buah yang dibeli: ")
    if(pilih in buah):
        berat = float(input('Berapa Kg            : '))
        print('-'*35)
        print("Total harga:", buah[pilih] * berat)
    else:
        print('\n{0} tidak dalam daftar'.format(pilih))
except ValueError:
    print('data yang anda masukan salah')
