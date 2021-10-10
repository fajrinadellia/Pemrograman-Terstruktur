#import library
import time

#tarif sewa mobil
tarifawalsewamobil = 200000 #12jam
tarifberikutnyasewamobil = 10000 #per-jam
awalwaktusewamobil = 6.00
akhirwaktusewamobil = 23.50

#menghitung berapa lama sewa mobil
lamasewamobil = int (akhirwaktusewamobil-awalwaktusewamobil)
print(lamasewamobil)

#jeda 2 detik
time.sleep(2)

#menghitung lama berikutnya sewa mobil
lamaberikutnyasewamobil = lamasewamobil - 12
print(lamaberikutnyasewamobil)

#jeda 2 detik
time.sleep(2)

#menghitung tarif berikutnya sewa mobil
tarifberikutnyasewamobil = lamaberikutnyasewamobil * tarifberikutnyasewamobil
totaltarifsewamobil = tarifawalsewamobil + tarifberikutnyasewamobil
print('jadi total tarif yang harus dia bayarkan kepada rental mobil adalah',totaltarifsewamobil)

