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
        
starFormation2(4)


    
