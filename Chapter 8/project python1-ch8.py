n = int(input("\nBanyaknya Data: "))
print()
data = []
jum = 0
while jum < n:
    try:
        temp = int(input('Masukkan data ke-%d: \n' % (jum+1)))
        data.append(temp)
        jum+=1
        data.sort()
        print('\nUrutan bilangan bulat dari kecil ke besar:\n',data)
    except ValueError:
        print('\nData yang dimasukkan salah\n')
