# Nama  : Ahmad Ramadhan
# NIM   : 16522075
# Deskripsi : Problem 2

nim = int(input('Masukkan akhiran NIM: '))

print('Mahasiswa masuk kelas K',end='')

# cek apakah dia masuk di range nim 001-100
if nim <= 100: 
  print('1' if nim % 2 else '2')

# cek apakah dia masuk di range nim 101 - 200  
elif 100 < nim and nim <= 200: 
  print('3' if nim % 2 else '4')

# cek apakah dia masuk di range nim 201 - 300 
elif 200 < nim and nim <= 300: 
  print('5' if nim % 2 else '6')

# ketika 3 kasus pertama salah maka dia akan masuk di antara K7 atau K8  
else: 
  print('7' if nim % 2 else '8')
