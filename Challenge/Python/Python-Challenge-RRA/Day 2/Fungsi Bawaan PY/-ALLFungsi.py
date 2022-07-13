# TODO ─── Penggunaan Fungsi Abs ──────────────────────────────────────────────────────
# abs() digunakan untuk mengembalikan nilai mutlak suatu bilangan
# misalnya |3| = 3 dan |-3|=3

from datetime import date
print("abs(-15) : ", abs(-15))  # 15
print("abs(10.32) : ", abs(10.32))  # 10.32
print("abs(-100) : ", abs(-100))  # 100

# ────────────────────────────────────────────────────────────────────────────────

# TODO ─── Penggunaan Fungsi All ──────────────────────────────────────────────────────
# Fungsi all() mengembalikan True apabila SEMUA anggota dari iterable(sequence) -
# bernilai True (tidak ada yang kosong/nol/0, False atau None)

# ─── List ───────────────────────────────────────────────────────────────────────
l = [1, 1, 0]
print(all(l))  # False
l = [1, False, 3]
print(all(l))  # False
l = [None]
print(all(l))  # False
l = []
print(all(l))  # True
# ─── String ─────────────────────────────────────────────────────────────────────
s = 'pythonindo is good'
print(all(s))  # True
s = 'None'
print(all(s))  # True


# TODO ─── Penggunaan Fungsi Any ──────────────────────────────────────────────────────
# mengembalikan True jika ada salah satu anggota iterable yang bernilai True.
# Bila tidak ada satupun, maka any() mengembalikan False.

l = [1, 2, 3, 0]
print(any(l))  # T

l = [0, False]
print(any(l))  # F

l = [0, False, 5]
print(any(l))  # T

l = []
print(any(l))  # F

# ────────────────────────────────────────────────────────────────────────────────


# TODO ─── Penggunaan Fungsi Ascii ────────────────────────────────────────────────────
# Fungsi ascii() mengembalikan string yang berisi representasi objek yang dapat dicetak.
# Fungsi ascii() mengembalikan karakter escape dari karakter non-ASCII menggunakan karakter escape \x, \u, atau \U.
# ASCII singkatan dari American Standard Code for Information Interchange atau Kode Standar Amerika untuk Pertukaran Informasi

text_normal = 'Python is very interesting'
print(ascii(text_normal))  # 'Python is very interesting'

other_text = 'Pythön is very interesting'
print(ascii(other_text))  # 'Pyth\xf6n is very interesting'

print('Pyth\xf6n is very interesting')  # Pyth�n is very interesting

# ────────────────────────────────────────────────────────────────────────────────


# TODO ─── Penggunaan Fungsi Bin ──────────────────────────────────────────────────────
# Fungsi bin() mengubah integer dan mengembalikan nilai dalam bentuk string biner.
# bin()num
# #

angka = 7
print("Nilai biner dari 7 adalah", bin(angka))
# Nilai biner dari 7 adalah 0b111
angka = 78
print("Nilai biner dari 78 adalah", bin(angka))
# Nilai biner dari 78 adalah 0b1001110


# ────────────────────────────────────────────────────────────────────────────────


# TODO ─── Penggunaan Fungsi Bool ─────────────────────────────────────────────────────
# Fungsi bool() mengubah sebuah nilai menjadi nilai Boolean (True atau False) dan mengembalikannya.
# bool(x)
# x – Nilai yang akan diubah menjadi True atau False
# False – apabila x dikosongkan atau bernilai False
# True – apabila x bernilai True
# Nilai – Nilai berikut dianggap False oleh Python:
# None, False, 0, tuple kosong (), list kosong[], string kosong ”, dan dictionary kosong {}

test = []
print(test, 'adalah', bool(test))  # False

test = [0]
print(test, 'adalah', bool(test))  # True

test = 0.0
print(test, 'adalah', bool(test))  # False

test = 'python'
print(test, 'adalah', bool(test))  # True

test = ""
print(test, 'adalah', bool(test))  # False

# ────────────────────────────────────────────────────────────────────────────────


# TODO ─── Penggunaan Fungsi Bytearray ────────────────────────────────────────────────
# Fungsi bytearray() mengembalikan objek bytearray dari suatu objek
# Syntax : bytearray([source[, encoding[, errors]]]
# source – objek yang akan diubah jadi byte array
# encoding – encoding string bila sourcenya adalah string
# errors – aksi yang dilakukan bila proses encoding gagal
# Fungsi bytearray() mengembalikan byte array berdasarkan inisialisasi panjang
# dan ukuran awal objek.
#
# String : Mengubah string menjadi byte menggunakan str.encode(),
# bisa juga menggunakan opsi encoding dan opsi errors
#
# Integer : Menciptakan array dengan ukuran tertentu, semuanya diinisialisasi dengan null
#
# Object : Buffer read-only dari objek yang digunakan untuk menginisialisai byte array
#
# Iterable : Menciptakan array dengan ukuran yang sama dengan panjang iterable dan mengisialisasinya menjadi anggota – anggota iterable.
# Harus berisi iterable dari integer antara 0 <= x < 256
#
# Kosong : Menciptakan array berukuran 0
# #


# string
s = "Python is fun"
arr = bytearray(s, 'utf-8')
print(arr)  # bytearray(b'Python is fun')

# integer
# Menciptakan array dengan ukuran tertentu, semuanya diinisialisasi dengan null
size = 9
arr = bytearray(size)
print(arr)  # bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00')

# list
# Menciptakan array dengan ukuran yang sama dengan panjang iterable dan mengisialisasinya menjadi anggota – anggota iterable.
# Harus berisi iterable dari integer antara 0 <= x < 256
l = {1, 2, 3, 4, 5, 6}
arr = bytearray(l)
print(arr)  # bytearray(b'\x01\x02\x03\x04\x05\x06')

# ────────────────────────────────────────────────────────────────────────────────


# TODO ─── Penggunaan Fungsi Callable ─────────────────────────────────────────────────
# Fungsi callable() mengembalikan True jika objek yang menjadi argumennya bisa dipanggil (callable).
# Jika tidak maka kembaliannya adalah False.
# Syntax : callable(object)
# Fungsi callable() akan mengembalikan:
# True – jika objek bisa dipanggil
# False – jika objek tidak bisa dipanggil
# Note : meskipun kembalian dari callable() adalah True, bisa saja pemanggilan terhadap objek masih gagal.
# #

x = 10
print(callable(x))  # False


def tes_fungsi():
    print("tes")
    print("tes")
    print("tes")


y = tes_fungsi
print(callable(y))  # True

# ────────────────────────────────────────────────────────────────────────────────


# TODO ─── Penggunaan Fungsi Bytes ────────────────────────────────────────────────────
# Fungsi bytes() mengembalikan objek byte yang bersifat immutable dari suatu objek
# Syntax : bytes([source[, encoding[, errors]]]
# source – objek yang akan diubah jadi byte array
# encoding – encoding string bila sourcenya adalah string
# errors – aksi yang dilakukan bila proses encoding gagal
# Fungsi bytes() mengembalikan byte berdasarkan inisialisasi panjang dan ukuran awal objek.
# #


# string
s = "Python is fun"
arr = bytes(s, 'utf-8')
print(arr)  # b'Python is fun

# integer
size = 5
arr = bytes(size)
print(arr)  # b'\x00\x00\x00\x00\x00'

# list
l = [1, 2, 3, 4, 5]
arr = bytes(l)
print(arr)  # b'\x01\x02\x03\x04\x05'

# ────────────────────────────────────────────────────────────────────────────────


# TODO ─── Penggunaan Fungsi Chr ──────────────────────────────────────────────────────
# Fungsi chr() mengembalikan karakter unicode dari bilangan integer (mengubah integer menjadi string)
# Syntax : chr(i)
# i – integer, bilangan yang akan diubah jadi karakter unicode
# Fungsi chr() mengembalikan karakter unicode yang bersesuaian dengan integer i
# #

print(chr(65))  # A
print(chr(97))  # a
print(chr(100))  # d

# ────────────────────────────────────────────────────────────────────────────────


# TODO ─── Penggunaan Fungsi Compile ──────────────────────────────────────────────────
# Fungsi compile() mengembalikan kode objek python dari source code.
# Fungsi ini digunakan jika kita ingin mengubah kode dalam bentuk deretan string menjadi kode python (yang bisa dieksekusi python).
# Objek kode yang dikembalikan tersebut nantinya bisa dieksekusi oleh fungsi-fungsi exec() dan eval().

# Syntax :  - compile(source, filename, mode)
#           - compile(source, filename, mode, flags=0, dont_inherit=False, optimize=-1)

# Fungsi compile() memiliki beberapa parameter yaitu:
# source – string, byte string, atau objek AST
# filename – file yang akan dibaca kodenya. Kita bisa memberi nama sesuai keinginan kita
# mode – Bisa exec, eval, atau single.
# - eval – hanya menerima ekspresi tunggal
# - exec – bisa menerima beberapa baris kode pernyataan, kelas, fungsi dan lain sebagainya
# - single – berisi satu pernyataan

# flags dan dont_inherit – mengontrol pernyataan yang nantinya mempengaruhi kompilasi dari source.
# optimize – level optimasi dari kompiler

string_kode = 'a = 7\nb = 8\njumlah=a+b\nprint("jumlah =",jumlah)'
kode_objek = compile(string_kode, 'kodestring', 'exec')

exec(kode_objek)  # jumlah = 15

# ────────────────────────────────────────────────────────────────────────────────
# TODO ─── Penggunaan Fungsi Classmethod ──────────────────────────────────────────────
# Fungsi classmethod() mengembalikan fungsi kelas dari suatu fungsi.
# Syntax : classmethod(function)
# Function – Fungsi yang akan diubah menjadi fungsi kelas
# Fungsi classmethod() mengembalikan fungsi kelas untuk fungsi yang dijadikan argumennya
# def classMethod(cls, args...)
# #

# from datetime import date //Hilangkan


class Orang:
    usia = 25

    def print_usia(cls):
        print('Usianya:', cls.usia)


# menciptakan fungsi kelas print_usia
Orang.print_usia = classmethod(Orang.print_usia)

Orang.print_usia()  # Usianya: 25
print("--------------------------------------------------------------------")

# random Person


class Orang:  # ini class
    def __init__(self, nama, umur, tinggi):  # digunakan untuk menampung String pada input bawah
        self.nama = nama  # menampung data name
        self.umur = umur  # menampung data age
        self.tinggi = tinggi  # menampung data tinggi

    @classmethod
    def tahunlahir(cls, nama, tahunlahirmu, tinggimu):  # rumus classmethod
        tinggiminimum = 150
        return cls(nama, date.today().year - tahunlahirmu, tinggimu-tinggiminimum)

    def display(self):
        print(self.nama + "'s age is: " +
              str(self.umur)+" tinggi is: "+str(self.tinggi))


person = Orang('Adam', 19, 20)  # bisa menggunakan class
person.display()

person1 = Orang.tahunlahir('John',  1985, 170)  # bisa menggunakan class method
person1.display()


# ────────────────────────────────────────────────────────────────────────────────
# ────────────────────────────────────────────────────────────────────────────────


# random Person

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @staticmethod
    def fromFathersAge(name, fatherAge, fatherPersonAgeDiff):
        return Person(name, date.today().year - fatherAge + fatherPersonAgeDiff)

    @classmethod
    def fromBirthYear(cls, name, birthYear):
        return cls(name, date.today().year - birthYear)

    def display(self):
        print(self.name + "'s age is: " + str(self.age))


class Man(Person):
    sex = 'Male'


man = Man.fromBirthYear('John', 1985)
man.display()
print(isinstance(man, Man))


man1 = Man.fromFathersAge('John', 1965, 20)
man.display()
print(isinstance(man1, Man))

# ────────────────────────────────────────────────────────────────────────────────
# ────────────────────────────────────────────────────────────────────────────────

# TODO ─── Penggunaan Fungsi Complex ──────────────────────────────────────────────────
# Fungsi complex() mengembalikan bilangan kompleks dari argumen riil dan imajiner yang diberikan.
# Syntax : complex([real[, imag])
# Fungsi complex() memiliki dua parameter yaitu:
#   real – bagian real dari bilangan. Bila tidak dimasukkan, defaultnya 0
#   imag – bagian imajiner dari bilangan. Bila tidak dimasukkan, defaultnya 0
# ungsi complex() mengembalikan bilangan dalam bentuk bilangan kompleks yaitu dalam format real+imagj
# #

z = complex(3, 3)
print(z)  # (3+3j)

z = complex(2)
print(z)  # (2+0j)

z = complex()
print(z)  # (0j)

z = complex('5-9j')
print(z)  # (5-9j)
# ────────────────────────────────────────────────────────────────────────────────
# ────────────────────────────────────────────────────────────────────────────────

a = 2+3j
print('a =', a)  # 2+3j
print('Type of a is', type(a))  # Type of a is <class 'complex'>

b = -2j
print('b =', b)  # -0-2j
print('Type of b is', type(a))  # Type of b is <class 'complex'>

c = -1+2j
print('c =', c)  # -1+2j
print('Type of c is', type(c))  # Type of c is <class 'complex'>

d = 2j
print('d =', d)  # 2j
print('Type of c is', type(d))  # Type of d is <class 'complex'>

# ────────────────────────────────────────────────────────────────────────────────
# ────────────────────────────────────────────────────────────────────────────────
