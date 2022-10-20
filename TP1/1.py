# Nama  : Ahmad Ramadhan
# NIM   : 16522075
# Deskripsi : Problem 1

#input harga awal dan jual pada tiap barang

a_dasar = int(input('Masukkan harga dasar barang A: '))
a_jual  = int(input('Masukkan harga jual barang A: '))
b_dasar = int(input('Masukkan harga dasar barang B: '))
b_jual  = int(input('Masukkan harga jual barang B: '))
c_dasar = int(input('Masukkan harga dasar barang C: '))
c_jual  = int(input('Masukkan harga jual barang C: ')) 

#nentuin profit tiap barang
#profit = harga jual - harga dasar

a_prof = a_jual - a_dasar
b_prof = b_jual - b_dasar
c_prof = c_jual - c_dasar

print('Barang yang harus ditawarkan adalah barang',end= ' ')

if a_prof > b_prof and a_prof > b_prof:
  print('A')
elif b_prof > a_prof and b_prof > c_prof:
  print('B')
elif c_prof > a_prof and c_prof > b_prof:
  print('C')
