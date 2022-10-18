# Nama  : Ahmad Ramadhan
# NIM   : 16522075
# Deskripsi : Problem 3

# input waktu ketika mulai berlari
print('Masukkan waktu mulai!')
jam_mulai = int(input('Jam    : '))
menit_mulai = int(input('Menit  : '))
detik_mulai = int(input('Detik  : '))

#input waktu ketika selesai berlari
print('Masukkan waktu selesai!')
jam_akhir = int(input('Jam    : '))
menit_akhir = int(input('Menit  : '))
detik_akhir = int(input('Detik  : '))

# awalnya semua dikonversi ke detik untuk menentukan total tempuh nya

mulai = jam_mulai * 3600 + menit_mulai * 60 + detik_mulai
akhir = jam_akhir * 3600 + menit_akhir * 60 + detik_akhir

waktu_tempu = akhir - mulai
print('Tuan Riz berlari selama',end=' ')

if waktu_tempu // 3600 > 0:
  print(waktu_tempu//3600,'jam',end=' ')
  waktu_tempu %= 3600

if waktu_tempu // 60 > 0:
  print(waktu_tempu//60,'menit',end=' ')
  waktu_tempu %= 60

print(waktu_tempu,'detik.')
