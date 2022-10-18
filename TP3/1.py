# NIM/Nama  : 16522075 / Ahmad Ramadhan
# Tanggal   : 18 Oktober 2022
# Deskripsi : awalnya diskon dinisiasi dengan -1, trus jika diskon di
# di indeks i sama dengan dengan diskon cek, jika i < idx_ans, maka
# idx_ans = i, dan diskon = diskon di index ke i

# KAMUS
# h[] -> list harga barang ke-i (integer)
# d[] -> list diskon barang ke-i (integer)
# 
#
n = int(input('Masukkan banyak barang: '))
tot_dis = -1 # inisiasi diskon dengan harga terkecil
idx = 0 # inisiasi idx jawaban

h = [0]*n# inisiasi list
d = [0]*n# inisiasi list

for i in range(0,n):
  prc = int(input('Masukkan harga awal barang ke-' + str(i + 1) + ': '))
  h[i] = prc
for i in range(0,n):
  dis = int(input('Masukkan besar diskon (dalam persen) barang ke-' + str(i + 1) + ': '))
  d[i] = dis
for i in range(0,n):
  dis = h[i] * d[i] // 100 # itung diskon barang ke - i
  if dis > tot_dis: # cek jika diskon sekarang lebih besar dari diskon diskon sebelumnya
    idx = i + 1
    tot_dis = dis
  elif dis == tot_dis and i + 1 < idx: # jika diskon ke-i sama dengan diskon sekrang maka cek apakah i lebih kecil dari idx jawaban sementara
    idx = i + 1
    tot_dis = dis
print('Barang ' + str(idx) + ' memiliki diskon paling besar yaitu ' + str(tot_dis) + '.')
