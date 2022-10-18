# NIM/Nama  : 16522075 / Ahmad Ramadhan
# Tanggal   : 18 Oktober 2022
# Deskripi  : Ada n lampu, dan q operasi
# tiap qi akan menekan tombol ke-i(tombol bersifat toggle) jadi
# jika keadaan sekarang mati di detekan maka akan nyala dan vice versa
# idenya adalah jika total tombol ditekan sama dengan bilangan genap maka 
# tombol keaddan akhir akan mati dan ganji akan hidup
# KAMUS
# cnt[] -> list integer dari total tombol yang di tekan
# n,q, now -> integer

n = int(input('Masukkan banyak lampu: '))
q = int(input('Masukkan berapa kali Tuan Kil menekan tombol: '))
cnt = [0]*(n+2) # inisiasi array dengan tambahan 2 agar kiri dan kanannya lebih
# saya melebihkan array nya agar memudahkan biar dipengolahan algonya tak perlu else if
# dan menghindari runtime error pada list/array

for i in range(0,q):
  now = int(input('Tombol yang ditekan ke ' + str(i + 1) + ': '))
  cnt[now - 1] += 1 # tombol sebelah kiri i dipencet
  cnt[now] += 1 # tombol ke i dipencet
  cnt[now + 1] += 1 # tombol sebelah kanan i dipencet

print('Keadaan akhir rangkaian lampu adalah',end=' ')
for i in range(1,n+1):
  if cnt[i] % 2 == 1:
    print(end='1')
  else:
    print(end='0')
print('.')
