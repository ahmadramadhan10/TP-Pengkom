# NIM/Nama  : Ahmad Ramadhan
# Tanggal   : 6 Oktober 2022
# Deskripsi : TP Minggu 2A, no 1
# algo nya adalah cukup cek sampe n
# jika i = {1....n-1} membagi n masukkan ke sum
# di akhir cek apakah sama atau tidak
# input bilangan yang ingin di cek
n = int(input('Masukkan bilangan: '))
tot = 0

for i in range(1, n):
  if n % i == 0: # jika i habis membagi n maka tambah variabel tot
    tot += i

if tot == n: # cek apakah total nya sama dengan n
  print('Bilangan tersebut adalah bilangan sempurna.')
else:
  print('Bilangan tersebut bukan bilangan sempurna.')
