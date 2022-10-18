# NIM/Nama  : Ahmad Ramadhan
# Tanggal   : 6 Oktober 2022
# Deskripsi : TP Minggu 2A, no 3

# untuk mencari jawabannya berarti harus loop dari i = {1 - N}
# tiap i kita cek apakah prima atau tidak, cukup menghitung faktor primanya dari 1 sampai i

N = int(input('Masukkan N: '))
tot = 0 # total faktor

print('Faktor primanya adalah',end=' ')

for i in range(2, N + 1):
  if N % i == 0:
    cnt = 0 # untuk menghitung 
    for j in range(1,i + 1):
      if i % j == 0: # cek apakah divisor dari N ini adalah prima atau tidak
        cnt += 1
    if cnt == 2:
      if tot == 0: # jika dia faktor pertama maka tak perlu cetak koma di awal
        print(i,end='')
        tot += 1
      else:
        print(', ' + str(i),end='')
print('.')
