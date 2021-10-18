import random

angka_pilihan = random.randint(1, 100)

print("=" * 40)
print("“Hai.. nama saya Mr. Lappie, saya telah memilih sebuah bilangan bulat secara acak antara 0 s/d 100. Silakan tebak ya!!!”")
print("=" * 40)

score=100
while True:
  jawaban = int(input("Tebakan Anda:"))

  if jawaban == angka_pilihan:
    print("Yeeee… Bilangan tebakan anda BENAR :-)")
    break
  elif jawaban < angka_pilihan:
    print("Hehehe… Bilangan tebakan anda terlalu kecil") 
    score -= 2
  elif jawaban > angka_pilihan:
    print("Hehehe… Bilangan tebakan anda terlalu besar")
    score -= 2

if (score>=0) and (score<=100) :
    print("Score Anda:", str(score))
elif (score < 0) :
    print("Score Anda:0")
