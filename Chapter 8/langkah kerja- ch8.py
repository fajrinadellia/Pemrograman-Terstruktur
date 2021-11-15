#membuat list a dan b
a = [1, 5, 6, 3, 6, 9, 11, 20, 12] 
b = [7, 4, 5, 6, 7, 1, 12, 5, 9]

print('list a:\n', a)
print('list b:\n', b)
print('-'*80)

#menyisipkan nilai 10 ke dalam indeks ke 3 dari a, dan 15 ke dalam indeks ke 2 dari b
a.insert(3, 10)
b.insert(2, 15)
print('\nsetelah disisipkan nilai 10 ke dalam indeks ke 3 dari a:\n', a)
print('setelah disisipkan nilai 15 ke dalam indeks ke 2 dari b:\n', b)
print('-'*80)

#menyisipkan nilai 4 ke indeks terakhir dari a, dan 8 ke indeks terakhir dari b
a.append(4)
b.append(8)
print('\nsetelah disisipkan nilai 4 ke indeks terakhir dari a:\n', a)
print('setelah disisipkan nilai 8 ke indeks terakhir dari b:\n', b)
print('-'*80)

#melakukan sorting secara ascending pada list a dan b
a.sort()
b.sort()
print('\nsorting ascending list a:\n', a)
print('sorting ascending list b:\n', b)
print('-'*80)

#membuat list c yang elemennya merupakan sublist dari a (mulai dari indeks ke 0 s/d 7), dan list d yang elemennya merupakan sublist dari b (mulai indeks ke 2 s/d 9)
c=(a[0:8])
d=(b[2:10])
print('\nlist c dengan elemen sublist a dari indeks 0 s/d 7:\n', c)
print('list d dengan elemen sublist b dari indeks 2 s/d 9:\n', d)
print('-'*80)

#membuat serangkaian langkah untuk mendapatkan list e yang elemennya merupakan hasil penjumlahan dari setiap elemen c dan d yang bersesuaian indeksnya
e=[]
for i in range(len(c)):
    e += [c[i]+d[i]]
print('\nhasil penjumlahan dari setiap elemen c dan d bersesuaian indeksnya\n', e)
print('-'*80)

#mengubah list e ke dalam tuple
e=tuple(e)
print('\nmengubah list e ke dalam tuple:\n', e)
print('-'*80)

#mencari nilai min, maks, dan jumlahan seluruh elemen dari e
min=min(e)
max=max(e)
sum=sum(e)
print('\nnilai min dari seluruh elemen e:\n', min)
print('nilai maks dari seluruh elemen e:\n', max)
print('jumlahan seluruh elemen e:\n', sum)
print('-'*80)

#membuat sebuah string myString = “python adalah bahasa pemrograman yang menyenangkan”
myString= "python adalah bahasa pemrograman yang menyenangkan"
setmyString= set(myString)
print('\nsebuah string:\n', myString)
print('-'*80)

#menentukan karakter huruf apa saja yang menyusun string tersebut
print('menentukan karakter huruf apa saja yang menyusun string:\n', setmyString)
print('-'*80)

#mengurutkan secara alfabet himpunan karakter huruf yang diperoleh dari langkah 10, dengan terlebih dahulu mengubahnya ke list
setStringList=list(setmyString)
print('\nbentuk list dari myString\n', setStringList)
setStringList.sort()
print('sorting ascending alfabet himpunan karakter huruf dari myString\n', setStringList)
