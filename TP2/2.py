# NIM/Nama  : Ahmad Ramadhan
# Tanggal   : 6 Oktober 2022
# Deskripsi : TP Minggu 2A, no 2
i = 2 
cnt = 0 # buat menghitung tidak membesar secara beruturut
tot = 0 # jumlah nilai yg membesar
a = int(input('Angka ke-1: '))
bef = a

while cnt != 3: # jika 3 angka tidak membesar secara beturut-turut maka hentikan looping
  a = int(input('Angka ke-'+str(i)+': '))
  if a > bef: # jika dia membesar maka variabel tot ditambah oleh input
    tot += a
    cnt = 0 # dan variable cnt kita reset lagi
  else: # jika dia tidak membesar maka kita tambah variabel count
    cnt += 1
  bef = a
  i += 1
print('Jumlah nilai yang membesar adalah ' + str(tot) + '.')
