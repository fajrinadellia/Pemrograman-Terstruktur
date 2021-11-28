mhs = ['K001:ROSIHAN ARI:1979-09-01:SOLO', 
       'K002:DWI AMALIA FITRIANI:1979-09-17:KUDUS',
       'K003:FAZA FAUZAN:2005-01-28:KARANGANYAR']

print("="*63)
print("NIM".ljust(8), "NAMA MAHASISWA".ljust(20),"TGL LAHIR".ljust(15),"TEMPAT LAHIR".ljust(15))
print("-"*63)

i = 0    
for x in mhs:
    data = mhs[i].split(":")
    nim = data[0]
    namaMhs = data[1]
    tglLahir = data[2].split("-")
    tglLahir = tglLahir[2] + "/" + tglLahir[1] + "/" + tglLahir[0]
    tmptLahir = data[3]
    i += 1
    print (nim.ljust(8), namaMhs.ljust(20), tglLahir.ljust(15), tmptLahir.ljust(15))
    
print("-"*63)
