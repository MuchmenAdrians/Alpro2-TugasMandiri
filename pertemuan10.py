# MATERI PERTEMUAN 10: List in advance applications in Python

# 1. List comprehension
squares = [x**2 for x in range(1, 11)]
print(squares)

# 2. Array 2 dimensi
matriks_identitas = [[1 if i  ==j else 0 for j in range(3)] for i in range(3)]
for baris in matriks_identitas:
    print(baris)
print(f"Elemen [0][0]: {matriks_identitas[0][0]}") # Akses elemen baris 0, kolom 0
print(f"Elemen [1][2]: {matriks_identitas[1][2]}") # Akses elemen baris 1, kolom 2
print(f"Elemen [2][1]: {matriks_identitas[2][1]}") # Akses elemen baris 2, kolom 1

# 3. List multidimensi
kubus = [[[i for k in range(2)] for j in range(2)] for i in range(2)]
print(kubus)

# 4. Fungsi berparameter variabel
def bintang(n):
    print('*' * n)

bintang(10)

# 5. Kuis 1
genap = [x*3 for x in range(1,11) if x % 2 == 0]
print(genap)

# 6. Kuis 2
array_2d = [[i*3 + j + 1 for j in range(3)] for i in range(3)] # Array 2D 3x3 dengan angka 1-9
for baris in array_2d: 
    print(baris) # Tampilkan isi array

# 7. Kuis 3
data = [[2,4], [6,8], [10,12]]
flatten = [angka for baris in data for angka in baris] # Flatten list 2D menjadi 1D
print(flatten)

# 8. Kuis 4
def luas_persegipanjang(panjang, lebar):
    print(panjang * lebar)
    
luas_persegipanjang(8, 5)
