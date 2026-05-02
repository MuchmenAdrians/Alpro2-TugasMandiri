# MATERI PERTEMUAN 12: Scope and Multi-Parameter Function in Python

# 1. Variabel local: variable yang berada di dalam fungsi dan hanya dapat diakses di dalam fungsi tersebut.
def fungsi_local(x):
    angka = 10
    return x + angka
print(fungsi_local(10)) # Output:
print(angka) # Error: NameError (variabel angka tidak dapat diakses di luar fungsi)

# 2. Contoh 1: Variable di luar fungsi
Nilai = 100
def tampilkan_nilai():
    return f"Nilai yang di dalam fungsi: {Nilai}"
print(tampilkan_nilai()) # Output: Nilai yang di dalam fungsi: 100
print(f"Nilai yang di luar fungsi: {Nilai}") # Output: Nilai yang di luar fungsi: 100

# 3. Contoh 2: Variable di luar fungsi
Nilai = 100
def tampilkan_nilai():
    Nilai = 50
    return f"Nilai yang di dalam fungsi: {Nilai}"
print(tampilkan_nilai()) # Output: Nilai yang di dalam fungsi: 50
print(f"Nilai yang di luar fungsi: {Nilai}") # Output: Nilai yang di luar fungsi: 100

# 4. Variable globsl dengan keyword globsl
x = 500 # Variabel global
def ubah_global():
    global x
    x = 1000 # Mengubah nilai variabel global x
    return f"Nilai x di dalam fungsi: {x}"
print(ubah_global()) # Output: Nilai x di dalam fungsi: 1000
print(f"Nilai x di luar fungsi: {x}") # Output: Nilai x di luar fungsi: 1000

# 5. Kuis IMT
def hitung_imt(berat, tinggi):
    imt = berat / (tinggi ** 2)
    return imt

berat = float(input("Masukkan berat badan (kg): "))
tinggi = float(input("Masukkan tinggi badan (m): "))

index_massa_tubuh = hitung_imt(berat, tinggi)
kategori = ["Normal", "Gemuk", "Obesitas"]

if index_massa_tubuh < 18.5:
    print("Index massa tubuh anda adalah", index_massa_tubuh, "termasuk kategori Kurus")
elif index_massa_tubuh < 25:
    print("Index massa tubuh anda adalah", index_massa_tubuh, "termasuk kategori", kategori[0])
elif index_massa_tubuh < 30:
    print("Index massa tubuh anda adalah", index_massa_tubuh, "termasuk kategori", kategori[1])
else:
    print("Index massa tubuh anda adalah", index_massa_tubuh, "termasuk kategori", kategori[2], ". Anda harus diet!")

# 6. Fungsi Segitiga dengan cara pertama
def cek_segitiga(a, b, c):
    if a + b <= c:
        return False
    if b + c <= b:
        return False
    if c + a <= a:
        return False
    return True
print(cek_segitiga(3, 4, 5)) # Output: True (karena 3 + 4 > 5, 4 + 5 > 3, dan 5 + 3 > 4)
print(cek_segitiga(1, 1, 3)) # Output: False (karena 1 + 1 <= 3)

# 7. Fungsi Segitiga dengan cara kedua
def cek_segitiga(a, b, c):
    if a + b <= c or b + c <= a or c + a <= b:
        return False
    return True
print(cek_segitiga(3, 4, 5)) # Output: True (karena 3 + 4 > 5, 4 + 5 > 3, dan 5 + 3 > 4)
print(cek_segitiga(1, 1, 3)) # Output: False (karena 1 + 1 <= 3)

# 8. Fungsi Segitiga dengan cara ketiga
def cek_segitiga(a, b, c):
    return a + b > c and b + c > a and c + a > b    
print(cek_segitiga(3, 4, 5)) # Output: True (karena 3 + 4 > 5, 4 + 5 > 3, dan 5 + 3 > 4)
print(cek_segitiga(1, 1, 3)) # Output: False (karena 1 + 1 <= 3)

# 9. kuis Faktorial
def faktorial(n):
    if n < 0:
        return None
    if n < 2:
        return 1
    
    hasil = 1
    for i in range(2, n + 1):
        hasil *= i
    return hasil

n = int(input("Masukkan nilai yang ingin di faktorial: "))
print(n, "! = ", faktorial(n))

# 10. Kuis Fibonacci
def fibonacci(n):
    if n < 1:
        return None
    if n < 3:
        return 1
    
    elem_1 = elem_2 = 1
    hasil_jumlah = 0
    for i in range(3, n + 1):
        hasil_jumlah = elem_1 + elem_2
        elem_1, elem_2 = elem_2, hasil_jumlah
    return hasil_jumlah

# test
for i in range(1, 10):
    print(i, "->", fibonacci(i)) 

# 11. Rekursif Faktorial
def faktorial_rekursif(n):
    if n < 0:
        return None
    if n < 2:
        return 1
    return n * faktorial_rekursif(n - 1)

n = int(input("Masukkan nilai yang ingin di faktorial: "))
print(n, "! = ", faktorial_rekursif(n))

# 12. Rekursif Fibonacci
def fibonacci_rekursif(n):
    if n < 1:
        return None
    if n < 3:
        return 1
    return fibonacci_rekursif(n - 1) + fibonacci_rekursif(n - 2)
# test
for i in range(1, 10):
    print(i, "->", fibonacci_rekursif(i))
