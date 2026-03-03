#1 membuat fungsi input
print("Masukan angka : ")
Angka = input()
print("Angka yang kamu masukkan adalah: " + Angka)

#2 membuat fungsi input dengan argumen
print("Halo")
nama = input("Masukkan nama kamu: ")
print("Selamat datang, " + nama + "!")

#3 memahami hasil dari fungsi input
Data = int(input("Masukkan angka pertama : "))
Data += int(input("Masukan angka kedua : "))
print("Hasilnya", Data)

#4 membuat konversi tipe data float pada input()
Angka = float(input("Masukkan angka desimal: "))
print("Angka yang kamu masukkan adalah: " + Angka)

#5 Menghitung sisi miring segitiga sebagai rumus segitiga dengan variabel Hypotenusa
a = float(input("Masukkan sisi alas: "))
t = float(input("Masukkan sisi tinggi: "))
hypo = (a**2 + t**2)**0.5
print("Sisi miring segitiga adalah:", hypo) 

#6 Menghitung sisi miring segitiga sebagai rumus segitiga tanpa variabel
a = float(input("Masukkan sisi alas: "))
t = float(input("Masukkan sisi tinggi: "))
print("Sisi miring segitiga adalah:", (a**2 + t**2)**0.5)

#7 Operator Konkatenasi
Nama = str(input("Masukkan nama : "))
Kota = str(input("Masukan Kota asal : "))
print("Hai, saya " + Nama + " dari Kota " + Kota + ".")

#8 Operator Replikasi 
simbol = input("Masukkan simbol yang ingin direplikasi: ")
print((simbol + " ")*5)

#9 Konversi Tipe Data
umur = int(input("Masukkan umur Anda: "))
print("Wow umurmu sudah " + str(umur) + " tahun!")

#10 Melihat Tipe Data dari Variabel
nama = "Adriansyah"
NIM = 123456789
nilai = 100.
Mahasiswa = True
print(type(nama))
print(type(NIM))    
print(type(nilai))
print(type(Mahasiswa))

#11 KUIS 7
a = int(input("Masukkan angka pertama: "))
b = int(input("Masukkan angka kedua: "))
print("Hasil penjumlahan:", a + b)
print("Hasil pengurangan:", a - b)
print("Hasil pembagian:", a / b)
print("Hasil perkalian:", a * b)
print("Selamat kamu sudah pintar Matematika.")

#12 KUIS 8
x = float(input("Masukan nilai x : "))
y = 1.0 / (x+1.0 / (x+1.0 / (x+1.0 /x)))
print("Hasil dari y adalah : ", y) 

#13 KUIS 9
jam = int(input("waktu mulai (jam) : "))
menit = int(input("waktu mulai (menit) : "))
durasi = int(input("Durasi Acara (menit) : "))
#Tambah durasi ke menit
menit += durasi
#Hitung tambahan jam 
jam += menit // 60
menit %= 60
#Supaya jam tak lebih dari 24
jam %= 24
print("Acara berakhir pukul", jam, ":", menit)