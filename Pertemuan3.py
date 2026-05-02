# Pertemuan 3 - Variabel dan Tipe Data
# 1. Membuat dan menggunakan variabel var, nilai, nama_mahasiswa
var = 2026
nilai = 100
nama_mahasiswa = "Adrian"
print(var) # output: 2026
print(nilai) # output: 100
print(nama_mahasiswa) # output: Adrian
print(var, nilai, nama_mahasiswa) # output: 2026 100 Adrian

# 2. Membuat dan mencetak variabel dengan nilai berupa "Budi"
Nama = "Budi"
print(nama) # output: NameError: Karena nama tak terdefinisi

# 3.
umur = 60
print(umur) # output: 60
umur = umur + 10
print(umur) # output: 70

# 4. 
Tabungan = 100000
Tabungan =  20000 + 50000 
print(Tabungan) # output: 70000

# 5.
level = 100
level += 50
xp = 500
xp *= 2
print(level, xp) # output: 150 1000

# 6.
a = 5
b = 12
hasil = (a ** 2 + b ** 2) ** 0.5
print(hasil) # output: 13.0

#7. KUIS 3 
Ayu = 10000
Bagus = 20000
Citra = 30000
print(Ayu, Bagus, Citra) # output: 10000 20000 30000
JumlahTabungan = Ayu + Bagus + Citra
print("jumlah tabungan adalah ", JumlahTabungan) # output: jumlah tabungan adalah 60000

#8. KUIS 4
Kilometer = 12.25
Miles = 7.38
miles_to_kilometer = Miles * 1.61
kilometer_to_miles = Kilometer / 1.61
print(Miles, "miles is", round(miles_to_kilometer, 2), "kilometers") # output: 7.38 miles is 11.88 kilometers
print(Kilometer, "kilometers is", round(kilometer_to_miles, 2), "miles") # output: 12.25 kilometers is 7.61 miles

#9. KUIS 5 
# JIKA x = 0
x = 0
x = float(x)
y = 3*x**3-2*x**2+3*x-1
print("nilai y adalah", y) # output: nilai y adalah -1.0
# JIKA x = 1
x = 1
x = float(x)
y = 3*x**3-2*x**2+3*x-1
print("nilai y adalah", y) # output: nilai y adalah 3.0
# JIKA x = -1
x = -1
x = float(x)
y = 3*x**3-2*x**2+3*x-1
print("nilai y adalah", y) # output: nilai y adalah -9.0