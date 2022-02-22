# 1
# input panjang dan lebar
p = float(input())
l = float(input())

# proses menghitung luas persegi panjang
luas = p * l

# output luas persegi panjang dengan pembulatan 2 digit di belakang koma
print("{:.2f}".format(luas))


# 2
# input
x = float(input())

# proses perhitungan
y = (2 * x - 5) * (3 * x - 1)

# output
print("{:.3f}".format(y))

# 3
# input
n = float(input())

# proses perhitungan
fx = (n + 1 / n) ** 2

# output
print("{:.1f}".format(fx))


# 4
# input besaran kecepatan dalam km / jam
k = float(input())

# proses konversi kecepatan dari km / jam ke meter / detik
hasil = k * 1000 / 3600

# output dengan pembulatan 2 digit di belakang koma
print("{:.2f}".format(hasil))


# 5
# input jari-jari bola
r = float(input())

# hitung volume bola
volume = 4 / 3 * (3.14 * r ** 3)

# output dengan pembulatan 2 digit di belakang koma
print("{:.2f}".format(volume))


# 6
# input jari-jari bola
r = float(input())

# hitung luas permukaan bola
luas = 4 * 3.14 * r ** 2

# output dengan pembulatan 4 digit di belakang koma
print("{:.4f}".format(luas))


# 7
# input
a = int(input())
b = int(input())
c = int(input())
d = int(input())

# proses penjumlahan
hasil = a + b + c + d

# output
print(hasil)


# 8
# input jumlah buah apel per hari
a = int(input())

# hitung total harga penjualan buah apel per hari
total_penjualan = a * 5000

# output
print(total_penjualan)


# 9
# input umur dan nilai mahasiswa
x = int(input())
y = int(input())

# output nilai dan umur
print(y)
print(x)


# 10
# input nilai mil dan kilomter
mil = int(input())
kilometer = int(input())

# menghitung konversi mil menjadi kilometer dan kilometer menjadi mil
mil_ke_kilometer = mil * 1.61
kilometer_ke_mil = kilometer / 1.61
# output dengan pembulatan 2 digit di belakang koma
print("{:.2f}".format(mil_ke_kilometer))
print("{:.2f}".format(kilometer_ke_mil))


# 11
# input nilai x
x = int(input())

# menghitung nilai y
hasil = (3 * (x ** 3)) - (2 * (x ** 2)) + (3 * x) - 1

# output
print(hasil)


# 12
# input buah apel dari Joko, Icha, dan Ratna
a = int(input())
b = int(input())
c = int(input())

# menghitung jumlah apel dari Joko, Icha, dan Ratna
total_apel = a + b + c

# output total apel
print(total_apel)


# 13
# input string
x = input()

# output string
print(x)


# 14
# input nama, warna favorit, dan usia
nama = input()
warna = input()
usia = int(input())

# output nama, warna favorit, dan usia
print(f"Nama: {nama}. Warna favorit: {warna}. Usia: {usia}")


# 15
# input dan type casting nama, id, harga, dan diskon barang
id = input()
nama_barang = input()
harga = float(input())
diskon = float(input())

# formatting harga dan diskon
harga = "{:.2f}".format(harga)
diskon = "{:.1f}".format(diskon)

print(
    "Barang bernama",
    nama_barang,
    "dan id",
    id,
    "memiliki harga Rp",
    harga,
    "dan diskon",
    diskon + "%",
)


# 16
# input tahun lahir user
tahun_lahir = int(input())

# menghitung umur pada tahun 2021
umur_2021 = 2021 - tahun_lahir

# menghitung umur 25 tahun yang akan datang
umur_2025 = umur_2021 + 25

# output
print(umur_2021)
print(umur_2025)


# 17
# input nilai x
x = int(input())

# hitung nilai f(x)
f = (x ** 3) + (3 * (x ** 2)) - (2 * x) - 10

# output nilai f(x)
print(f)


# 18
# input data V0, V dan S berupa float
V0 = float(input())
V = float(input())
S = float(input())

# hitung percepatan a
a = ((V ** 2) - (V0 ** 2)) / (2 * S)

# hitung waktu t
t = (V - V0) / a

# output hasil
print(a)
print(t)


# 19
# input berat dan harga mangga yang dibeli
kg = int(input())
harga = int(input())

# hitung total belanja
belanja = kg * harga

# hitung total potongan yang didapat
potongan = belanja * 0.15

# hitung total yang harus dibayar setelah diskon
total = belanja - potongan

# output
print("belanja: Rp", belanja)
print("potongan: Rp", potongan)
print("total: Rp", total)


# 20
# input
m = float(input())
R = float(input())

# hitung besar momen inersia batu
momenInersia = m * R ** 2

# outputkan hasil
print(momenInersia)


# 21
# Set nilai konstanta
pi = 3.14

# input
r = float(input())
s = float(input())

# operasi aritmatika
luas = pi * r * (r + s)

# output
print(luas)


# 22
# set nilai pi
pi = 3.14

# input
r = int(input())
p = int(input())
l = int(input())

# hitung total keliling
keliling = (2 * pi * r) + (2 * (p + l))

# output
print("{:.2f}".format(keliling))


# 23
# input
s1 = int(input())
s2 = int(input())
t = int(input())

# tung luas
luas = 1 / 2 * (s1 + s2) * t

# output
print(luas)


# 24
# input
m = int(input())
v = int(input())

# operasi aritmatika
ek = 1 / 2 * m * v ** 2

# output
print(ek)


# 25
# input
Vf = int(input())
a = int(input())
t = int(input())

# menghitung kecepatan awaal
v_awal = Vf - (a * t)

# output
print(v_awal)


# 27
# input
x = int(input())

# periksa bilangan ganjil
isGanjil = x % 2 != 0

# output
print(isGanjil)


# 28
# input
C = float(input())

# menghitung konversi
R = 4 / 5 * C
F = 9 / 5 * C + 32
K = C + 273

# output
print("{:.1f}".format(R))
print("{:.1f}".format(F))
print("{:.1f}".format(K))


# 29
# input
m = float(input())
v = float(input())

# menghitung massa jenis
massa_jenis = m / v

# output
print(massa_jenis)


# 30
# input data
m = float(input())
a = float(input())

# menghitung gaya
F = m * a

# output
print(F)


# 31
# input
m = int(input())

# proses konversi
cm = m * 100

# output
print(cm)


# 32
# input data
x = int(input())

# proses hitung bilangan kubik
kubik = x ** 3

# output
print(kubik)


# 33
# input
s = int(input())
pp = int(input())

# menghitung hipertropi
P = (100 / s) - (100 / pp)

# Output
print("{:.2f}".format(P))


# 34

# Input
a = int(input())
x = int(input())
n = int(input())

# perhitungan turunan
f = n * a * x ** (n - 1)

print(f)


# 35
# Input
g = float(input())
v = float(input())

# Math Formula (silakan menambahkan formula yang diperlukan)
m = g / 40 * 1 / v

# Output
print("{:.2f}".format(m))


# 36
# Input
v = float(input())
i = float(input())

# Math Formula
w = v * i * 1.5
harga = w * 1000

# output
print(harga)


# 37
# Input
x = int(input())

# Math Formula
gx = 5 * x / 2
fx = (3 * gx ** 2) + (4 * gx) - 5

# Output
print(fx)


# 38
# Soal 1: tambahkan tanda kurung sehingga menghasilkan nilai 3
soal_1 = (29 + 1) // 10

# Soal 2: tambahkan tanda kurung sehingga menghasilkan nilai 2
soal_2 = (20 + 2) * (2 - 1) % 10

# Soal 3: tambahkan tanda kurung sehingga menghasilkan nilai 0
soal_3 = (10 - 9) * 2 - (1 + 1)

# Jangan ubah kode di bawah ini jika ingin mendapatkan nilai
print(soal_1)
print(soal_2)
print(soal_3)


# 39
# input
a = input()
b = input()

# casting
a1 = float(a)
t1 = float(b)

# menghitung luas segitiga
luas = (a1 * t1) / 2

# Untuk menghitung keliling segitiga diperlukan sisi ketiga, hitunglah sisi ketiga
m = ((a1 ** 2) + (t1 ** 2)) ** (1 / 2)

# menghitung keliling segitiga
keliling = a1 + t1 + m

# Tampilkan luas dan keliling dari segitiga
print(luas)
print(keliling)

# 40
# input
emas_oze = int(input())
emas_jabami = int(input())
emas_ethan = int(input())

# menghitung banyak emas yang didapat
total_emas = emas_oze + emas_jabami + emas_ethan

# menghitung banyak emas yang dikembalikan ke dalam dungeon
dikembalikan = total_emas % 3

# menghitung banyak emas yang didapat tiap petualang
didapat = (total_emas - dikembalikan) / 3

# tampilkan emas yang dikembalikan dan didapat
print(dikembalikan)
print(didapat)

# 41
# Tampilkan pesan "Thrice"
print("Thrice")

# Input
s1 = str(input())
s2 = str(input())
s3 = str(input())

# Tampilkan s1, s2 dan, s3 dengan melengkapi kode berikut
s4 = s1 + " " + s2 + " " + s3
print(s4)

# buatlah variabel bernama s5 dengan isi variable s4 sebanyak tiga kali
s5 = (s4 + "\n") * 3

# Tampilkan variabel s4 dengan melengkapi kode berikut
print("Je ireumeun " + s4 + " imnida")


# 42
pi = 3.14159  # perkiraan

# Input
diameter = int(input())


# Buatlah variabel bernama radius dengan rumus radius lingkaran
radius = diameter / 2

# Lengkapi variabel luas dengan rumus luas lingkaran
luas = pi * (radius ** 2)

# Tampilkan nilai variabel luas
print(luas)


# 43
# input
d1 = float(input())
d2 = float(input())

# proses menghitung luas layang-layang
luas = d1 * d2 / 2

# output
print(luas)


# 44
# input
sa = float(input())
sb = float(input())

# proses menghitung keliling layang-layang
keliling = 2 * (sa + sb)

# output
print(keliling)

# 45
# input
jarak = float(input())
waktu = float(input())

# proses menghitung kecepatan
kecepatan = jarak / waktu

# output
print(kecepatan)


# 46
# Proses input
angka = int(input())
pangkat = int(input())

# Tahap menghitung pangkat
hasil = angka ** pangkat

# Output
print(hasil)


# 47
# input
p = float(input())
l = float(input())
t = float(input())

# proses menghitung volume kolam
v = p * l * t

# output
print(v)


# 48
# input
r = int(input())
t = int(input())

volume = 22 / 7 * r ** 2 * t

# output
print("Volume tabung dengan jari-jari", r, " adalah ", volume)


# 49
# Input
a = int(input())
b = int(input())
c = int(input())
d = int(input())

s1 = b ** (1 / a)
s2 = d ** (1 / c)

# Output
print(s1 > s2)


# 50
# Input
a = int(input())
b = int(input())

# // atau %
c = a // 100000
d = (b // 10000) % 10

# Output
print(c)
print(d)


# 51
# input
p = float(input())
l = float(input())

ruangan = 50

# hitung luas meja
meja = p * l

# output
print(meja < ruangan)


# 52
# input
s = float(input())

# hitung luas rubik
volume = s ** 3

# output
print(volume)


# 53
# input
m = int(input())

# konversi ke kilometer
kilometer = m * 1.6

# output
print(kilometer, "kilometer")


# 54
# input
u = int(input())

# hitung dekade
dekade = u // 10

# output
print(dekade, "dekade")


# 55
# input
g = float(input())

# perhitungan
orangtua = g * 0.15
tabungan = g * 0.05
hidup = g * 0.5
sekolah = g * 0.3

# output
print("uang ke orangtua = ", orangtua)
print("uang tabungan = ", tabungan)
print("uang kebutuhan hidup = ", hidup)
print("uang sekolah anak = ", sekolah)


# 56
# input
t = float(input())
r = float(input())


# hitung luas tabung
tabung = 3.14 * r ** 2 * t

# output
print(tabung * 0.25)


# 57
# input
s = float(input())

# proses menghitung keliling
keliling = 5 * s

# output
print("Keliling Segi Lima =", keliling)


# 58
# Input
bil1 = int(input())
bil2 = int(input())

# proses menghitung
hasil = (bil1 * bil2) / (bil1 - bil2)

# output
print(hasil)


# 59
# input
a = int(input())
b = int(input())
c = int(input())

# perhitungan dan output
print(a, "kelipatan dari", c, "?", a % c == 0)
print(b, "kelipatan dari", c, "?", b % c == 0)


# 60
# Input
uang = int(input())

# Proses Perhitungan Pecahan
hasil = uang // 1000
sisa = uang % 1000

# Output
print(
    "Uang tersebut mengandung pecahan seribu sebanyak",
    hasil,
    "dan sisa uang sebanyak",
    sisa,
)


# 61
# input jarak dalam satuan km
j = input()

jarak = float(j)

# konversi jarak
m = jarak * 1000
cm = jarak * 100000
mm = jarak * 1000000

# Output jarak
print("Jarak", j, "km =", m, "m")
print("Jarak", j, "km =", cm, "cm")
print("Jarak", j, "km =", mm, "mm")


# 62
# input besarnya gaji
g = input()

# type casting ke float
gaji = float(g)

# proses perhitungan pajak
pajak = gaji * 0.1

# output
print("Gaji sebesar", g, "harus membayar pajak sebesar", pajak)


# 63
# input keliling dan panjang persegi panjang
k = float(input())
p = float(input())

# hitung lebar persegi panjang
lebar = k / 2 - p

# output
print(lebar)


# 64
# input luas lingkaran
luas = float(input())

# hitung jari-jari lingkaran
r = (luas / 3.14) ** 0.5

# hitung diameter
diameter = 2 * r

# output dengan pembulatan 2 digit di belakang koma
print("{:.2f}".format(diameter))


# 65
# input dan type casting x
x = float(input())

# hitung fungsi f(x)
fx = ((x ** 3) + (3 * x)) / ((x ** 4) - (3 * x ** 2) + 4)

# output dengan pembulatan 2 digit di belakang koma
print("{:.2f}".format(fx))


# 66
# input waktu
t = int(input())

# perhitungan posisi
posisi = t ** 3 - 12 * t ** 2 + 36 * t - 30

# output
print(posisi)
