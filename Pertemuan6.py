#MATERI ALPRO II: LOOPS IN PYTHON
#1 Contoh 1: Perulangan while
while True:
    print("Perulangan ini tak berujung 😜") # Infinite loop

#2 Contoh 2: Perulangan while
Hitung = 5
while Hitung > 0:
    print("Peluncuran dalam", Hitung)
    Hitung -= 1
print("Rocket Diluncurkan!")

#3 Menghitung angka ganjil dan angka genap dengan perulangan while
n = int(input("Masukan angka batas : "))
i = 1 #variabel penghitung
ganjil = 0
genap = 0

while i <= n: #Berjalan selama i kurang atau sama dengan n
    if i % 2 == 0: #jika genap
        genap += 1
    else: #jika bukan genap
        ganjil += 1
    i += 1
print("Jumlah genap", genap)
print("Jumlah ganjil", ganjil)

#4 Kuis 15
secret_number = 777

print("""
+====================================+
| Selamat datang di game saya, muggle! |
| masukkan suatu angka dan tebak      |
| angka berapa yang saya pilih        |
| untuk kamu.                         |
| Jadi, berapa angka rahasianya?      |
+====================================+
""")
# Meminta user memasukkan angka
tebak = int(input("Masukkan tebakanmu: "))
# Perulangan selama tebakan tidak sama dengan angka rahasia
while tebak != secret_number:
    print("hahaha! Kamu nyangkut deh di Loop saya")
    tebak = int(input("Masukkan angka lagi: "))
print("Selamat, Muggle! kamu bebas sekarang!")

#5 Contoh 1: Perulangan for
for a in range(10):
    print("nilai a saat ini adalah", a) 
print() # spasi
for b in range(2,8):
    print("nilai b saat ini adalah", b)
print() # spasi
for c in range(2,8,3):
    print("nilai c saat ini adalah", c)
print() #  spasi
for d in range(1,1):
    print("nilai d saat ini adalah", d)
print() # spasi
for e in range(2,1):
    print("nilai e saat ini adalah", e)

#6 Contoh 2: Perulangan for
power = 1
for expo in range(0,11):
    print("2 pangkat", expo, "adalah", power)
    power *= 2

#7 Contoh break dan continue
for i in range(10):
    if i == 8:
        break
    if i == 5:
        continue
    print("Nilai :", i)  

#8 Kuis 16
secret_number = 777

print("""
+====================================+
| Selamat datang di game saya, muggle! |
| masukkan suatu angka dan tebak      |
| angka berapa yang saya pilih        |
| untuk kamu.                         |
| Jadi, berapa angka rahasianya?      |
+====================================+
""")

while True: 
    tebak = int(input("Masukkan tebakanmu: "))
    # Jika tebakan benar
    if tebak == secret_number:
        print("Selamat, Muggle! kamu bebas sekarang!")
        break
    # Jika tebakan salah
    else:
        print("hahaha! Kamu nyangkut deh di Loop saya")

#9 Kuis 17
kata = input("Masukkan sebuah kata: ")
kata = kata.upper() # mengubah kata menjadi huruf kapital
for huruf in kata: 
    # jika huruf vokal, maka dilewati
    if huruf == "A":
        continue
    elif huruf == "I":
        continue
    elif huruf == "U":
        continue
    elif huruf == "E":
        continue
    elif huruf == "O":
        continue
    else:
        print(huruf) # menampilkan huruf konsonan
        
#10 Perulangan while dengan else
push_up = 1
while push_up <= 5:
    print("Push up ke-", push_up)
    push_up += 1
else:
    print("Latihan selesai di hitungan", push_up)

#11 Perulangan for dengan else
for i in range(5):
    print("Hitung mundur:", i, "...")
else:
    print("Waktunya meledak! BOOM...terakhir i =", i)

#12 Contoh Ekspresi logika pada python
belajar = True
main_hp = False
ujian = True
hasil = (belajar and not main_hp) or ujian
print(hasil)

#13 Operasi Logical vs Bit pada python
a = 2 #10 dalam biner
b = 3 #11 dalam biner 
#Logical Operator
log = a and b #output : 3
logneg = not a #output : False
#Bitwise Operator
bit = a & b #output : 2
bitneg = ~a #output : -3
print("===Logical===")
print("a and b :", log) 
print("not a   :", logneg)
print("===Bitwise===")
print("a & b :", bit)
print("~a    :", bitneg)

#14 Binary Shifting
num = 4
print("Original:", num)
print("Left Shift << 1:", num << 1) #output: 8
print("Right Shift >> 1:", num >> 1) #output: 2

#15 Kuis 18
x = 4 #100 (dalam binary)
y = 1 #001 (dalam binary)

a = x & y # 100 & 001
b = x | y # 100 | 001
c = ~x # -(x+1)
d = x ^ 5 # 100 ^ 101 
e = x >> 2 # Right shift: x // 2**2
f = x << 2 # Left shift: x * 2**2

print(a,b,c,d,e,f)