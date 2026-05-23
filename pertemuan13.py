# MATERI Pertemuan 13 dan 14: Tuple, Dictionaries, Exceptions in Python


# 1 (Membuat tuple dan tampilkan)
tuple_1 = (1, 2, 4, 8)
tuple_2 = 1., .5, .25, .125
print("tuple_1 =", tuple_1)
print("tuple_2 =", tuple_2)

# 2 (Menggunakan tuple)
my_tuple = (1, 10, 100, 1000)
print(my_tuple[0])
print(my_tuple[-1])
print(my_tuple[1:])
print(my_tuple[:-2])
for elemen in my_tuple:
    print(elemen)

# 3 (Memodifikasi tuple)
my_tuple = (1, 10, 100, 1000)

# Tuple bersifat immutable, tidak bisa dimodifikasi secara in situ.
# Cara satu-satunya adalah membuat tuple baru.
tuple_baru = my_tuple + (10000,)
print("Tuple baru (ditambah 10000):", tuple_baru)
# Contoh percobaan modifikasi yang akan error jika diaktifkan:
# my_tuple.append(10000)  # AttributeError
# del my_tuple[0]         # TypeError
# my_tuple[1] = -10       # TypeError

# 4 (Menggunakan tuple dengan len(), +, *, in dan not in)
my_tuple = (1, 10, 100, 1000)
t1 = my_tuple + (10000, 100000)
t2 = my_tuple * 3
print(len(t2))
print(t1)
print(t2)
print(10 in my_tuple)
print(-10 not in my_tuple)

# 5 (Penugasan simultan pada tuple)
x, y = 1, 2
print("Sebelum swap: x =", x, ", y =", y)
x, y = y, x
print("Setelah swap : x =", x, ", y =", y)
var = 123
t1 = (1, )
t2 = (2, )
t3 = (3, var)
t1, t2, t3 = t2, t3, t1
print(t1, t2, t3)

# 6 (Membuat dictionary dan tampilkan)
dictionary = {"cat": "kucing", "dog": "anjing", "horse": "kuda"}
nilai_alpro2 = {'morin': 90, 'arya': 95, 'faqih': 98}
dictionary_kosong = {}
print(dictionary)
print(nilai_alpro2)
print(dictionary_kosong)

# 7 (Mengakses isi dictionary)
dictionary = {"cat": "kucing", "dog": "anjing", "horse": "kuda"}
nilai_alpro2 = {'morin': 90, 'arya': 95, 'faqih': 98}
print(dictionary['cat'])
print(nilai_alpro2['morin'])

# Mengakses kunci yang tidak ada akan menyebabkan KeyError:
# print(dictionary['lion'])  # KeyError

# 8 (Method keys())
dictionary = {"cat": "kucing", "dog": "anjing", "horse": "kuda"}
for kunci in dictionary.keys():
    print(kunci, "->", dictionary[kunci])

# 9 (Method values())
dictionary = {"cat": "kucing", "dog": "anjing", "horse": "kuda"}
for indo in dictionary.values():
    print(indo)

# 10 (Method items())
dictionary = {"cat": "kucing", "dog": "anjing", "horse": "kuda"}
for eng, indo in dictionary.items():
    print(eng, "->", indo)


# 11 (Method update())
dictionary = {"cat": "kucing", "dog": "anjing", "horse": "kuda"}
print("Sebelum update:", dictionary)
dictionary.update({'duck': 'bebek'})
print("Setelah update :", dictionary)


# 12 (Method popitem())
dictionary = {"cat": "kucing", "dog": "anjing", "horse": "kuda"}
print("Sebelum popitem:", dictionary)
item_dihapus = dictionary.popitem()
print("Item yang dihapus:", item_dihapus)
print("Setelah popitem :", dictionary)


# 13 (Modifikasi dictionary)
dictionary = {"cat": "kucing", "dog": "anjing", "horse": "kuda"}
dictionary['cat'] = 'mpus'
print("Setelah ubah 'cat':", dictionary)
dictionary['lion'] = 'singa'
print("Setelah tambah 'lion':", dictionary)
del dictionary['dog']
print("Setelah hapus 'dog':", dictionary)
for key in sorted(dictionary.keys()):
    print(key, "->", dictionary[key])

dictionary_copy = dictionary.copy()
print("Salinan dictionary:", dictionary_copy)

warna = (("hijau", "#008000"), ("biru", "#0000FF"))
kamus_warna = dict(warna)
print("Kamus warna:", kamus_warna)

dictionary_copy.clear()
print("Setelah clear():", dictionary_copy)

# 14 (Menangani exception)
while True:
    try:
        bilangan = int(input("Masukkan bilangan natural: "))
        print("Kebalikan dari", bilangan, "adalah", 1 / bilangan)
        break
    except:
        print("Peringatan: bilangan yang dimasukkan bukan bilangan bulat!")

# 15 (Menangani multiple exception)
while True:
    try:
        bilangan = int(input("Masukkan bilangan natural (bukan 0): "))
        print("Kebalikan dari", bilangan, "adalah", 1 / bilangan)
        break
    except ValueError:
        print("Peringatan: bilangan yang dimasukkan bukan bilangan bulat!")
    except ZeroDivisionError:
        print("Peringatan! tidak bisa membagi dengan 0")
    except:
        print("Maaf sepertinya ada yang salah nih... :(")