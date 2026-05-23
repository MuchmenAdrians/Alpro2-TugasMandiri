# MATERI Pertemuan 13 dan 14: Tuple, Dictionaries, Exceptions in Python

# 1 (Membuat tuple dan tampilkan)
warna_primer = ("merah", "kuning", "biru")
koordinat = 3.5, 7.2, 1.8
print(warna_primer)
print(koordinat)

# 2 (Menggunakan tuple)
hari = ("Senin", "Selasa", "Rabu", "Kamis")
print(hari[0])
print(hari[-1])
print(hari[1:])
print(hari[:-2])
for h in hari:
    print(h)

# 3 (Memodifikasi tuple)
hari = ("Senin", "Selasa", "Rabu", "Kamis")

# Tuple bersifat immutable, tidak bisa dimodifikasi secara in situ.
# Cara satu-satunya adalah membuat tuple baru.
hari_lengkap = hari + ("Jumat",)
print("Tuple baru:", hari_lengkap)

# Contoh percobaan modifikasi yang akan error jika diaktifkan:
# hari.append("Jumat")   # AttributeError
# del hari[0]            # TypeError
# hari[1] = "Minggu"     # TypeError

# 4 (Menggunakan tuple dengan len(), +, *, in dan not in)
hari = ("Senin", "Selasa", "Rabu", "Kamis")
gabungan = hari + ("Jumat", "Sabtu")
diulang = hari * 2
print(len(diulang))
print(gabungan)
print(diulang)
print("Rabu" in hari)
print("Minggu" not in hari)

# 5 (Penugasan simultan pada tuple)
panjang, lebar = 15, 8
print("Sebelum swap: panjang =", panjang, ", lebar =", lebar)

panjang, lebar = lebar, panjang
print("Setelah swap: panjang =", panjang, ", lebar =", lebar)

kode_pos = 45321
p = (1,)
q = (2,)
r = (3, kode_pos)
p, q, r = q, r, p
print(p, q, r)

# 6 (Membuat dictionary dan tampilkan)
menu_harga = {"nasi goreng": 15000, "mie ayam": 12000, "soto": 10000}
profil = {'nama': 'Mentari', 'jurusan': 'Informatika', 'semester': 2}
kosong = {}
print(menu_harga)
print(profil)
print(kosong)

# 7 (Mengakses isi dictionary)
menu_harga = {"nasi goreng": 15000, "mie ayam": 12000, "soto": 10000}
profil = {'nama': 'Mentari', 'jurusan': 'Informatika', 'semester': 2}
print(menu_harga['nasi goreng'])
print(profil['nama'])

# Mengakses kunci yang tidak ada akan menyebabkan KeyError:
# print(menu_harga['bakso'])  # KeyError

# 8 (Method keys())
menu_harga = {"nasi goreng": 15000, "mie ayam": 12000, "soto": 10000}
for makanan in menu_harga.keys():
    print(makanan, "->", menu_harga[makanan])

# 9 (Method values())
menu_harga = {"nasi goreng": 15000, "mie ayam": 12000, "soto": 10000}
for harga in menu_harga.values():
    print(harga)

# 10 (Method items())
menu_harga = {"nasi goreng": 15000, "mie ayam": 12000, "soto": 10000}

for nama_menu, harga in menu_harga.items():
    print(nama_menu, "->", harga)

# 11 (Method update())
menu_harga = {"nasi goreng": 15000, "mie ayam": 12000, "soto": 10000}
print("Sebelum update:", menu_harga)

menu_harga.update({'bakso': 13000})
print("Setelah update:", menu_harga)

# 12 (Method popitem())
menu_harga = {"nasi goreng": 15000, "mie ayam": 12000, "soto": 10000}
print("Sebelum popitem:", menu_harga)

item_keluar = menu_harga.popitem()
print("Item yang dihapus:", item_keluar)
print("Setelah popitem:", menu_harga)

# 13 (Modifikasi dictionary)
menu_harga = {"nasi goreng": 15000, "mie ayam": 12000, "soto": 10000}
menu_harga['soto'] = 11000
print("Setelah ubah harga 'soto':", menu_harga)
menu_harga['bakso'] = 13000
print("Setelah tambah 'bakso':", menu_harga)
del menu_harga['mie ayam']
print("Setelah hapus 'mie ayam':", menu_harga)
for m in sorted(menu_harga.keys()):
    print(m, "->", menu_harga[m])
cadangan = menu_harga.copy()
print("Salinan:", cadangan)
kode_warna = (("merah", "#FF0000"), ("hijau", "#00FF00"), ("biru", "#0000FF"))
palet = dict(kode_warna)
print("Palet warna:", palet)
cadangan.clear()
print("Setelah clear():", cadangan)

# 14 (Menangani exception)
while True:
    try:
        suhu = int(input("Masukkan suhu dalam Celsius (bilangan bulat): "))
        print("Suhu dalam Fahrenheit:", (suhu * 9/5) + 32)
        break
    except:
        print("Peringatan: input yang dimasukkan bukan bilangan bulat!")

# 15 (Menangani multiple exception)
while True:
    try:
        stok = int(input("Masukkan jumlah stok barang (bukan 0): "))
        print("Rata-rata per hari:", 100 / stok, "barang")
        break
    except ValueError:
        print("Peringatan: input yang dimasukkan bukan bilangan bulat!")
    except ZeroDivisionError:
        print("Peringatan! stok tidak boleh bernilai 0")
    except:
        print("Maaf sepertinya ada yang salah nih... :(")