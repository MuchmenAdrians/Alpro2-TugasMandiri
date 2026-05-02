#1 Comparison Operators
jumlah_jeruk = 10
jumlah_apel = 15
print(jumlah_jeruk == jumlah_apel) #False
print(jumlah_jeruk != jumlah_apel) #True
print(jumlah_jeruk > jumlah_apel) #False        
print(jumlah_jeruk < jumlah_apel) #True
print(jumlah_jeruk >= jumlah_apel) #False
print(jumlah_jeruk <= jumlah_apel) #True

#2 Kuis 11
Input_n = int(input("Masukkan nilai: "))
print(Input_n > 100) #True jika nilai lebih besar dari 100, False jika tidak    

#3 Conditiomal Statements: If tunggal
stok_buku = 5
if stok_buku > 0: #Kondisi untuk memeriksa 
    print("Buku tersedia")

#4 Conditional Statements: Rangkaian If
umur_Adrian = 20
if umur_Adrian >= 18: #Kondisi untuk memeriksa apakah Adrian dewasa
    print("Adrian dewasa")
if umur_Adrian < 18: #Kondisi untuk memeriksa apakah Adrian belum dewasa
    print("Adrian belum dewasa")

#5 Conditional Statements: If-Else
Nilai_Adrian = 90
if Nilai_Adrian >= 60: #Kondisi memeriksa lulus atau tidak
    print("Adrian lulus")
else:
    print("Adrian tidak lulus")

#6 Conditional Statements: If-Elif-Else
Nilai_Adrian = 85
if Nilai_Adrian >= 90: #Kondisi untuk nilai A
    print("Nilai Adrian: A")
elif Nilai_Adrian >= 80: #Kondisi untuk nilai B
    print("Nilai Adrian: B")
else:
    print("Nilai Adrian: C") #Jika nilai kurang dari 80, maka nilai C

#7 Membandingkan 2 angka input
angka1 = int(input("Masukkan angka pertama: "))
angka2 = int(input("Masukkan angka kedua: "))
if angka1 > angka2: #Kondisi untuk membandingkan angka1 dan angka2
    print("Angka pertama lebih besar")
elif angka1 < angka2: #Kondisi untuk membandingkan angka1 dan angka2    
    print("Angka kedua lebih besar")
else:
    print("Kedua angka sama") #Jika angka1 dan angka2 sama

#8 Kuis 12
input_angka1 = int(input("Masukkan angka pertama: "))
input_angka2 = int(input("Masukkan angka kedua: "))
input_angka3 = int(input("Masukkan angka ketiga: "))
AngkaTerbesar = input_angka1
if input_angka2 > AngkaTerbesar: 
    AngkaTerbesar = input_angka2
if input_angka3 > AngkaTerbesar:
    AngkaTerbesar = input_angka3
print("Angka terbesar adalah:", AngkaTerbesar)

#9 Menggunakan fungsi max() untuk mencari angka terbesar
TinggiMenara = float(input("Masukkan tinggi menara: "))
TinggiGedung = float(input("Masukkan tinggi gedung: "))
TinggiPohon = float(input("Masukkan tinggi pohon: "))
Tertinggi = max(TinggiMenara, TinggiGedung, TinggiPohon) #Menggunakan fungsi max() untuk mencari nilai tertinggi
print("Yang tertinggi adalah:", Tertinggi)

#10 Kuis 13
pendapatan = float(input("Masukkan pendapatan bulanan Anda: "))
pajak = 0
pendapatan_tahunan = pendapatan * 12

if pendapatan_tahunan <= 60000000:
    pajak = pendapatan_tahunan * 0.05
elif pendapatan_tahunan <= 250000000:
    pajak = pendapatan_tahunan * 0.15
elif pendapatan_tahunan <= 500000000:
    pajak = pendapatan_tahunan * 0.25
else:
    pajak = pendapatan_tahunan * 0.30

print("Pajak penghasilan yang harus anda bayar adalah ", pajak, "rupiah")