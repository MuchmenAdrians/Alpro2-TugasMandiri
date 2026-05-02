# MATERI PERTEMUAN KE-9: Sorting and Operations Lists in Python

# 1. Bubble sort
data = [32, 16, 8, 4, 2, 1]
n = len(data)
for i in range(n):
    for j in range(0, n-i-1):
        if data[j] > data[j+1]:
            data[j], data[j+1] = data[j+1], data[j]
    print(f"Iterasi ke-{i+1}: {data}")
print(f"Hasil akhir: {data}")

# 2. Interactive Bubble sort 
print("Interactive Bubble Sort")
DaftarAngka = input("Masukkan angka-angka yang ingin diurutkan (pisahkan dengan koma): ")
data = []
for angka in DaftarAngka.split(","):
    data.append(int(angka))
print(f"Data sebelum diurutkan: {data}")

n = len(data) # Menghitung jumlah elemen dalam list data
for i in range(n):
    for j in range(n-i-1): # Loop untuk membandingkan elemen yang berdekatan
        if data[j] > data[j+1]: # # Tukar elemen jika elemen yg ditemukan lebih besar dari elemen berikutnya
            data[j], data[j+1] = data[j+1], data[j]     
            print(data)
print(f"Data setelah diurutkan: {data}")

# 3. Metode sort() 
list_angka = [5, 2, 9, 1, 7, 6]
print("Sebelum diurutkan:", list_angka)
list_angka.sort()
print("Setelah diurutkan:", list_angka)

# 4. Metode Reverse()
list_angka = [5, 2, 9, 1, 7, 6]
print("Sebelum dibalik:", list_angka)
list_angka.reverse()
print("Setelah dibalik:", list_angka)

# 5. The Inner life of list 1
list_a = [1, 2, 3]
list_b = list_a
list_a.append(4)
print("List A:", list_a)
print("List B:", list_b)

# 6. Slice 1 [awal:akhir:langkah]
list_angka = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print("List asli:", list_angka[:]) # Menampilkan seluruh elemen dari list_angka
print("Slice [2:5]:", list_angka[2:5]) # Menampilkan elemen dari indeks 2 hingga 4

# 7. Slice 2 [positif:negatif]
list_angka = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print("List asli:", list_angka[:]) # Menampilkan seluruh elemen dari list_angka
print("Slice [2:-2]:", list_angka[2:-2]) # Menampilkan elemen dari indeks 2 hingga indeks -3

# 8. Slice 3 [negatif:positif]
list_angka = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print("List asli:", list_angka[:]) # Menampilkan seluruh elemen dari list_angka
print("Slice [-5:1]:", list_angka[-5:1]) # Menampilkan elemen dari indeks -5 hingga indeks 0

# 9 Slice 4 [:akhir]
list_angka = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print("List asli:", list_angka[:]) # Menampilkan seluruh elemen dari list_angka
print("Slice [:5]:", list_angka[:5]) # Menampilkan elemen dari indeks 0 hingga indeks 4

# 10. Slice 5 [awal:]
list_angka = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print("List asli:", list_angka[:]) # Menampilkan seluruh elemen dari list_angka
print("Slice [6:]:", list_angka[6:]) # Menampilkan elemen dari indeks 6 hingga akhir list

# 11. Slice 6 [:]
list_angka = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print("Slice [:]:", list_angka[:]) # Menampilkan seluruh elemen dari list_angka

# 12. Menghapus elemen dengan slice
list_angka = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print("List asli:", list_angka[:]) # Menampilkan seluruh elemen dari list_angka
del list_angka[3:5] # Menghapus elemen dari indeks 3 hingga indeks 4
print("List setelah dihapus:", list_angka)

# 13. Menghapus semua elemen dengan slice
list_angka = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print("List asli:", list_angka[:]) # Menampilkan seluruh elemen dari list_angka
del list_angka[:] # Menghapus seluruh elemen dari list_angka
print("List setelah dihapus:", list_angka)

# 14. Menghapus list itu sendiri
list_angka = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print("List asli:", list_angka[:]) # Menampilkan seluruh elemen dari list_angka
del list_angka # Menghapus list_angka
print("List setelah dihapus:", list_angka) 

# 15. Operator in
DaftarPlanet = ["Venus", "Bumi", "Mars", "Jupiter", "Saturnus"]
print("Bumi" in DaftarPlanet) # Output: True
print("Merkurius" in DaftarPlanet) # Output: False

# 16. Operator not in
DaftarPlanet = ["Venus", "Bumi", "Mars", "Jupiter", "Saturnus"]
print("Matahari" not in DaftarPlanet) # Output: True
print("Jupiter" not in DaftarPlanet) # Output: False

# 17. Simple program dari list 1
baterai_laptop = [100, 40, 60, 80, 20, 0]
tertinggi = baterai_laptop[0]

for i in range(1,len(baterai_laptop)):
    if baterai_laptop[i] > tertinggi:
        tertinggi = baterai_laptop[i]
        
print(tertinggi)

# 18. Simple program dari list 2
baterai_laptop = [100, 40, 60, 80, 20, 0]
tertinggi = baterai_laptop[0]

for i in baterai_laptop:
    if i > tertinggi:
        tertinggi = i

print(tertinggi)

# 19. Simple program dari list 3
angka_unik = [12,25,7,30,18,45,9,60]
target_cari = 18
found = False 

for i in range(len(angka_unik)):
    found = angka_unik[i] == target_cari
    if found:
        break
if found:
    print(f"Data ditemukan pada index ke-{i}")
else:
    print("Data tidak ditemukan dalam list")

# 20. Kuis 21
tebakan = [3,7,11,42,34,49]
hasil = [5,9,11,42,3,49]
benar = 0

for angka in tebakan:
    if angka in hasil:
        benar += 1
print(f"Jumlah tebakan yang benar:", benar)

# 21. Kuis 22
data = [1,2,4,4,1,4,2,6,2,9]
unik = []

for angka in data:
    if angka not in unik:
        unik.append(angka)
print(f"List tanpa duplikat: {unik}")