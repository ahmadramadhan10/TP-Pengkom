# NIM/Nama  : 16522075/ Ahmad Ramadhan
# Tanggal   : 18 Oktober 2022
# Deskripsi : kita punya string s1 dan s2, carilah berapa kali muncul s1 muncul di s2
# cek dari 0 sampai s2.size - s1.size trus cek substring dari string 2 dengan
# ukuran n
# jika sama varibel count di tambah 1

# Kamus
# a,b string
# x,y list of char
# n, m, cnt int

n = int(input('Masukkan panjang string 1: '))
a = str(input('Masukkan string 1: '))
m = int(input('Masukkan panjang string 2: '))
b = str(input('Masukkan string 2: '))

cnt = 0

x = ['']*n # inisasi array of char
y = ['']*m # inisiasi array of char

for i in range(0,n): # inisiasi string ke array of char
  x[i] = a[i]
for i in range(0,m): # inisiasi string ke array of char
  y[i] = b[i]

for i in range(0,m-n+1):
  same = True
  for j in range(0,n): # cek substring
    if x[j] != y[j + i]: # jika satu huruf satu aja beda maka pasti dia bukan substring dari string1 
      same = False
  if same == True:
    cnt += 1
print('String 1 muncul sebanyak ' + str(cnt) + ' kali.')
