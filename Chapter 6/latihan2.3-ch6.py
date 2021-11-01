from math import floor
def starFormation1(n):
    kolom = 1
    
    i = 0
    while (i < n):
        j = 0
        while (j < kolom):
            print('* '*(i + 1), end =' ')
            j += 1
        print(' ')
        i += 1

def starFormation2(n):
    kolom = 4
    
    i = 0
    while (i < n):
        j = 0
        while (j < kolom):
            print('*', end =' ')
            j += 1
        kolom -= 1 
        print(' ')
        i += 1
n = 7
n = floor(n/2) + 1
starFormation1(n)
starFormation2(n)
