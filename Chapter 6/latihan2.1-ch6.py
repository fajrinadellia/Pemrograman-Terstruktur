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
        
starFormation1(4)


    
