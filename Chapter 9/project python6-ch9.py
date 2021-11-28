nilai = [{'nim' : 'A01', 'nama' : 'Agustina', 'mid' : 50, 'uas' : 80},
         {'nim' : 'A02', 'nama' : 'Budi', 'mid' : 40, 'uas' : 90}, 
         {'nim' : 'A03', 'nama' : 'Chicha', 'mid' : 100, 'uas' : 50}, 
         {'nim' : 'A04', 'nama' : 'Donna', 'mid' : 20, 'uas' : 100},
         {'nim' : 'A05', 'nama' : 'Fatimah', 'mid' : 70, 'uas' : 100}]

print("="*63)
print("NIM     NAMA         N.MID     N.UAS      N.AKHIR        STATUS")
print("-"*63)

for x in nilai:
    nilaiAkhir = (x['mid']+(2*x['uas']))/3
    nAkhir = round(nilaiAkhir)
    if nAkhir >= 60:
        statusKelulusan = "LULUS"
    else:
        statusKelulusan = "TIDAK LULUS"
    print(x['nim'].ljust(6).rjust(6), x['nama'].ljust(10).rjust(11), str (x['mid']).rjust(7),
          str(x['uas']).rjust(9), str(nAkhir).ljust(10).rjust(20),
          str(statusKelulusan).rjust(4))

print("-"*63)

