#Kombinasi
print('a. c(5,3)')
n = 5
r = 3
def faktorial(x):
               if x == 1:
                   return 1
               elif x == 0:
                   return 1
               else:
                   return (x*faktorial(x-1))
hasil = (faktorial(n)/faktorial(n-r)*faktorial(r))
print(hasil)

#Permutasi
print('b. p(10,7)')
n = 10
r = 7
def faktorial(x):
               if x == 1:
                   return 1
               elif x == 0:
                   return 1
               else:
                   return (x*faktorial(x-1))
hasil = (faktorial(n)/faktorial(n-r))
print(hasil)
