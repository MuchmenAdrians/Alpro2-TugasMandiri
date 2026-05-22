# Materi pertemuan 7: Lists In Python

# 1. Indexing List
List = [0, 2, 3, 4, 5]
print(f"List sebelum diubah: {List}")
List[0] = 1 # Mengubah nilai pada index ke-0 menjadi 1
print(f"List setelah diubah: {List}")

# 2. Mengakses isi list
arr = ["a", "b", "c", "d"]
print(arr[0]) # Output: a
print(arr[1]) # Output: b   
print(arr[2]) # Output: c
print(arr[3]) # Output: d

# 3. Fungsi len() untuk menghitung jumlah elemen dalam list
Bahasa = ["Python", "JavaScript", "C++", "Java"]
print(f"Jumlah elemen dalam list Bahasa: {len(Bahasa)}") # Output: 4

# 4. Menghapus elemen dalam list menggunakan dengan del
Nilai = [60, 70, 80, 90]
print(f"Nilai sebelum dihapus: {Nilai}")
del Nilai[1] # Menghapus elemen pada index ke-1 (70)
print(f"Nilai setelah dihapus: {Nilai}") # Output: [60, 80, 90]

# 5. Negative Index untuk mengakses elemen dari belakang
Kendaraan = ["Mobil", "Motor", "Sepeda", "Truk"]
print(Kendaraan[-1]) # Output: Truk
print(Kendaraan[-2]) # Output: Sepeda
print(Kendaraan[-3]) # Output: Motor
print(Kendaraan[-4]) # Output: Mobil

# 6. Kuis 19
topi_list = [1, 2, 3, 4, 5]
topi_list[2] = int(input("Masukkan angka : ")) # Mengubah angka tengah (index ke-2) dengan input dari user
del topi_list[-1] # Menghapus elemen terakhir (5) dari list
print(len(topi_list)) # Output: 4
print(topi_list) # Output: [1, 2, input_value, 4] (tergantung pada input yang diberikan)

# 7. Contoh 1: Metode append() dan insert() untuk menambahkan elemen ke dalam list
Game = ["Free Fire", "Mobile Legends", "PUBG"]
Game.append("Call of Duty") # Menambahkan elemen "Call of Duty" ke akhir list
print(Game) 
Game.insert(1, "Valorant") # Menambahkan elemen "Valorant" pada index ke-1
print(Game) 

# 8. Contoh 2: Metode append() untuk menambahkan elemen ke dalam list
kuadrat1 = []
for i in range(1, 6):
    kuadrat1.append(i**2) # Menambahkan kuadrat dari i ke dalam list 
print(kuadrat1) # Output: [1, 4, 9, 16, 25]

# 9. Contoh 2 : Metode insert() untuk menambahkan elemen ke dalam list
kuadrat = []
for i in range(1, 6):
    kuadrat.insert(0, i**2) # Menambahkan kuadrat dari i ke awal list
print(kuadrat) # Output: [25, 16, 9, 4, 1]

# 10. Menggunakan list for i in range(len(list))
daftar_skor = [10,20,25]
total_skor = 0
for i in range(len(daftar_skor)):
    total_skor += daftar_skor[i]
print(f"Total skor: {total_skor}") # Output: Total skor: 55

# 11 Menggunakan list for i in list 
daftar_skor = [10,20,25]
total_skor = 0
for skor in daftar_skor:
    total_skor += skor
print(f"Total skor: {total_skor}") # Output: Total skor: 55

# 12 List in python 2
my_list = [0,2,4,6,8]
my_list[0], my_list[4] = my_list[4], my_list[0] # Menukar nilai pada index ke-0 dan ke-4
my_list[1], my_list[3] = my_list[3], my_list[1] # Menukar nilai pada index ke-1 dan ke-3
print(my_list) # Output: [8, 6, 4, 2, 0]
# Menggunakan for i in range(len(my_list)) untuk tukar dari ujung ke ujung
my_list = [0,2,4,6,8]
panjang = len(my_list)
for i in range(panjang // 2):
    my_list[i], my_list[panjang - i - 1] = my_list[panjang - i - 1], my_list[i]  
print(my_list) # Output: [8, 6, 4, 2, 0]

# 13. Kuis 20
# Langkah 1: buat list kosong
exo = []
print("Langkah 1:", exo)

# Langkah 2: tambah anggota dengan append()
exo.append("Suho")
exo.append("Kai")
exo.append("Chanyeol")
exo.append("Sehun")
print("Langkah 2:", exo)

# Langkah 3: gunakan for untuk menambah anggota
anggota_tambahan = ["DO", "Baekhyun", "Kris", "Lay", "Luhan", "Tao", "Chen"]
for nama in anggota_tambahan:
    exo.append(nama)
print("Langkah 3:", exo)

# Langkah 4: hapus anggota Kris, Luhan, Tao
del exo[6] # Menghapus anggota Kris pada index ke-6
del exo[7] # Menghapus anggota Luhan pada index ke-7 (setelah Kris dihapus)
del exo[7] # Menghapus anggota Tao pada index ke-7 (setelah Kris dan Luhan dihapus)
print("Langkah 4:", exo)

# Langkah 5: insert Xiumin di elemen ke-3 dari terakhir
exo.insert(-2, "Xiumin") # Menambahkan Xiumin di elemen ke-3 dari terakhir (index -2)
print("Langkah 5:", exo)
# jumlah anggota
print("Jumlah anggota exo:", len(exo))