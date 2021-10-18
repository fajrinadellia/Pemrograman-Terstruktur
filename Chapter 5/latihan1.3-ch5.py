#input nilai
bindo = int(input("Masukkan nilai Bahasa Indonesia : "))
ipa = int(input("Masukkan nilai IPA : "))
mtk = int(input("Masukkan nilai Matematika : "))

#status kelulusan
if(bindo >= 0) and (bindo <= 100) and (ipa >= 0) and (ipa <= 100) and (mtk >= 0) and (mtk <= 100):
    if(bindo >= 60) and (ipa >= 60) and (mtk > 70):
        print("Status kelulusan: LULUS")
    else:
        sebab = ""
        if(bindo < 60):
            sebab += "- Nilai Bahasa Indonesia kurang dari 60"
        if(ipa < 60):
            sebab += "- Nilai IPA kurang dari 60"
        if(mtk < 70):
            sebab += "- Nilai Matematika kurang dari 70"
        print("Status Kelulusan: TIDAK LULUS")
        print("Sebab : ")
        print(sebab)
else: print("Maaf input ada yang tidak valid")
