#input nilai
bindo = int(input("Masukkan nilai Bahasa Indonesia : "))
ipa = int(input("Masukkan nilai IPA : "))
mat = int(input("Masukkan nilai Matematika : "))

#status kelulusan
if(bindo >= 60) and (mat >= 60) and (mat > 70):
    print("Status kelulusan: LULUS")
else: print("Status kelulusan: TIDAK LULUS")
