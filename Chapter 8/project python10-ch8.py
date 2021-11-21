buah = {'apel' : 5000, 'jeruk' : 8500, 'mangga' : 7800, 'duku' : 6500}
print("\nDaftar Bauh :")
number = 1
for x,y in buah.items():
    print("{0}. {1} - {2}".format(number,x,y))
    number += 1

total = 0
lagi = 'y'
while lagi == 'y':
    try:
        pilih = input("\nNama buah yang dibeli: ")
        if(pilih in buah):
            kg = float(input('Berapa Kg            : '))
            total += (buah[pilih] * kg)
            lagi = input("Beli buah yang lain (y/n) ? ")
        else:
            print('\n{0} tidak ada dalam daftar buah '.format(pilih))
        
    except ValueError:
        print('data yang anda masukan salah')

print('-'*35)
print("Total harga           :",total)
