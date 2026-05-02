# MATERI PERTEMUAN 11: Returning a Result from a Function

# 1. Return tanpa ekspresi: memanggil fungsi tanpa argumen
def fungsi_tanpa_argumen():
    print("Fungsi ini tidak memiliki argumen.")
    return

fungsi_tanpa_argumen() # Output: Fungsi ini tidak memiliki argumen.

# 2. Return tanpa ekspresi: memanggil fungsi dengan argumen False
def fungsi_dengan_argumen(argumen):
    if argumen == True:
        print("Argumen bernilai True.")
    else:
        print("Argumen bernilai False.")
    return
fungsi_dengan_argumen(False) # Output: Argumen bernilai False.

# 3. Return dengan ekspresi: menyimpan nilai yang di return ke dalam variabel
def mesin_cetak():
    return "Hasil cetak dari mesin."
hasil = mesin_cetak()
print(hasil) # Output: Hasil cetak dari mesin.

# 4. Return dengan ekspresi: mengabaikan nilai yang di return dari fungsi
def mesin_cetak():
    print("Mesin sedang mencetak...")
    return "Hasil cetak dari mesin."
mesin_cetak() # Output: Mesin sedang mencetak... (nilai return diabaikan)

# 5. Keyword None
def cek_kosong(data):
    if data is None:
        return None
    else:
        return f"Data tidak kosong, datanya adalah {data}"
    
print(cek_kosong(None)) # JIKA DATA ADALAH NONE, MAKA OUTPUTNYA ADALAH None
print(cek_kosong("ADA")) # JIKA DATA BUKAN NONE, MAKA OUTPUTNYA ADALAH Data tidak kosong, datanya adalah ADA

# 6. List sebagai argument dari fungsi
def jumlah_list(n):
    return sum(n)
print(jumlah_list([1, 2, 3, 4, 5])) # Output: 15

# 7. List sebagai argument dari fungsi mengganti nilai list yang di luar fungsi
def jumlah_list(n):
    return sum(n)
print(jumlah_list([5, 10, 15])) # Output: 30

# 8. List sebagai hasil dari fungsi 
def buat_list(n):
    return [i for i in range(n)]
print(buat_list(5)) # Output: [0, 1, 2, 3, 4]

#9. Kuis 23 
def tahun_kabisat(tahun):
    return tahun % 4 == 0 and (tahun % 100 != 0 or tahun % 400 == 0)

data_uji = [1900, 2000, 2016, 1987]
data_hasil = [False, True, True, False]

for i in range(len(data_uji)):
    th = data_uji[i] 
    print(th, "->", end=" ")
    hasil = tahun_kabisat(th)
    if hasil == data_hasil[i]:
        print("OK")
    else:
        print("Gagal")

#10. Kuis 24
def tahun_kabisat(tahun):
    return (tahun % 4 == 0 and (tahun % 100 != 0 or tahun % 400 == 0))
def hari_didalam_tahun(tahun, bulan):
    if bulan == 2:
        return 29 if tahun_kabisat(tahun) else 28
    elif bulan in [4, 6, 9, 11]:
        return 30
    else:
        return 31
    
data_uji = [1900, 2000, 2016, 1987]
data_bulan = [2, 2, 1, 11]
data_hasil = [28, 29, 31, 30]

for i in range(len(data_uji)):
    thn = data_uji[i]
    bln = data_bulan[i]
    print(thn, bln, "->", end=" ")
    hasil = hari_didalam_tahun(thn, bln)
    if hasil == data_hasil[i]:
        print("OK")
    else:
        print("Gagal")

# 11. Kuis 25
def tahun_kabisat(tahun):
    return (tahun % 4 == 0 and (tahun % 100 != 0 or tahun % 400 == 0))

def hari_didalam_tahun(tahun, bulan):
    if bulan in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    elif bulan == 2:
        return 29 if tahun_kabisat(tahun) else 28
    elif bulan in [4, 6, 9, 11]:
        return 30
    else:
        return 31
    
def hari_pada_tahun(tahun, bulan, hari):
    if bulan < 1 or bulan > 12 or hari < 1:
        return None
    if hari > hari_didalam_tahun(tahun, bulan):
        return None
    total_hari = 0
    for b in range(1, bulan):
        total_hari += hari_didalam_tahun(tahun, b)
    return total_hari + hari
print(hari_pada_tahun(2000, 12, 31)) # Output: 366

# 12. Kuis 26
def cek_prima(bilangan):
    if bilangan <= 1:
        return False
    for i in range(2, int(bilangan**0.5) + 1):
        if bilangan % i == 0:
            return False
    return True
for i in range(1, 20):
    if cek_prima(i+1):
        print(i + 1, end=" ") # Output: 2 3 5 7 11 13 17 19
print()

# 13. Kuis 27
def cek_prima(bilangan):
    if bilangan <= 1:
        return False
    for i in range(2, int(bilangan**0.5) + 1):
        if bilangan % i == 0:
            return False
    return True
for i in range(1, 20):       
    if cek_prima(i+1):
        print(i + 1, end=" ") # Output: 2 3 5 7 11 13 17 19 
print()

# 14. Kuis 28
def Liter100km_ke_mpg(liter):
    mil_per_100km = 100000 / 1609.344
    galon = liter / 3.785411784
    return mil_per_100km / galon

def mpg_ke_Liter100km(mil):
    km_per_mil = 1609.344 / 1000
    liter_per_mil = 3.785411784
    km100 = 100
    liter = (km100 / (mil * km_per_mil)) * liter_per_mil
    return liter
print(Liter100km_ke_mpg(3.9)) # Output: 60.31143162393162
print(Liter100km_ke_mpg(7.5)) # Output: 31.361944444444443
print(Liter100km_ke_mpg(10.)) # Output: 23.521458333333332
print(mpg_ke_Liter100km(60.3)) # Output: 3.9000000000000004
print(mpg_ke_Liter100km(31.4)) # Output: 7.500000000000001
print(mpg_ke_Liter100km(23.5)) # Output: 10.000000000000002