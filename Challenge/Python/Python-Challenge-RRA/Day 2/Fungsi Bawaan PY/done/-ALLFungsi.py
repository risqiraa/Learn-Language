# TODO ─── Penggunaan Fungsi Abs ──────────────────────────────────────────────────────
# abs() digunakan untuk mengembalikan nilai mutlak suatu bilangan
# misalnya |3| = 3 dan |-3|=3

from math import *
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

# TODO ─── Penggunaan Fungsi Delattr ──────────────────────────────────────────────────
# Delattr() menghapus atribut dari objek (jika objek mengizinkannya).
# Syntax : delattr(objek, nama)
# delattr()membutuhkan dua parameter:
#   -objek - objek dari mana nama atribut harus dihapus
#   -name - string yang harus berupa nama atribut yang akan dihapus dariobyek
# delattr()tidak mengembalikan nilai apa pun(mengembalikan None).
# Itu hanya menghapus atribut(jika objek mengizinkannya).
# #


class Coordinate:
    x = 10
    y = -5
    z = 0


point1 = Coordinate()

print('x = ', point1.x)
print('y = ', point1.y)
print('z = ', point1.z)

delattr(Coordinate, 'z')

print('--After deleting z attribute--')
print('x = ', point1.x)  # x = 10
print('y = ', point1.y)  # y =  -5

# Raises Error
# AttributeError: 'Coordinate' object has no attribute 'z'
print('z = ', point1.z)

# ────────────────────────────────────────────────────────────────────────────────
# ────────────────────────────────────────────────────────────────────────────────


class Coordinate:
    x = 10
    y = -5
    z = 0


point1 = Coordinate()

print('x = ', point1.x)
print('y = ', point1.y)
print('z = ', point1.z)

# Deleting attribute z
del Coordinate.z

print('--After deleting z attribute--')
print('x = ', point1.x)
print('y = ', point1.y)

# Raises Attribute Error
print('z = ', point1.z)

# ────────────────────────────────────────────────────────────────────────────────
# ────────────────────────────────────────────────────────────────────────────────

# ─── Penggunaan Fungsi Dict ─────────────────────────────────────────────────────
# Konstruktor dict() membuat kamus dengan Python.
# Syntax : class dict(**kwarg)
# class dict(mapping, **kwarg)
# class dict(iterable, **kwarg)
# Catatan: **kwarg biarkan Anda mengambil sejumlah argumen kata kunci yang berubah-ubah.
#
"""Argumen kata kunci adalah argumen yang didahului oleh pengenal (mis. name=). 
Oleh karena itu, argumen kata kunci dari formulir kwarg=value diteruskan ke dict()konstruktor 
untuk membuat kamus."""
#
# dict()tidak mengembalikan nilai apa pun (mengembalikan None).
# #

# ─── Contoh 1: Buat Kamus Menggunakan Argumen Kata Kunci Saja ───────────────────

numbers = dict(x=5, y=0)
print('numbers =', numbers)  # numbers = {'x': 5, 'y': 0}
print(type(numbers))  # < class 'dict' >

empty = dict()
print('empty =', empty)  # empty = {}
print(type(empty))  # < class 'dict' >
# ────────────────────────────────────────────────────────────────────────────────


# ─── Contoh 2: Buat Kamus Menggunakan Iterable ──────────────────────────────────

# keyword argument is not passed
numbers1 = dict([('x', 5), ('y', -5)])
print('numbers1 =', numbers1)  # numbers1 = {'x' : 5, 'y' : -5}

# keyword argument is also passed
numbers2 = dict([('x', 5), ('y', -5)], z=8)
print('numbers2 =', numbers2)  # numbers2 = {'x' : 5, 'y' : -5, 'z' : 8}

# zip() creates an iterable in Python 3
numbers3 = dict(zip(['x', 'y', 'z'], [1, 2, 3]))
print('numbers3 =', numbers3)  # numbers3 = {'x': 1, 'y': 2, 'z': 3}
# ────────────────────────────────────────────────────────────────────────────────
# ────────────────────────────────────────────────────────────────────────────────


# ─── Penggunaan Fungsi Dir ──────────────────────────────────────────────────────
# Metode dir()mengembalikan daftar atribut yang valid dari objek yang diteruskan.
# Syntax : dir(object)
# Metode dir()ini mengambil satu parameter:
# objek - bisa berupa tupel kosong/terisi, daftar, set, kamus dll atau objek yang ditentukan pengguna
# Metode dir()mengembalikan daftar atribut objek yang diteruskan ke metode
# #

# ─── Contoh 0 ───────────────────────────────────────────────────────────────────
number = [12]
# returns valid attributes of the number list
print(dir(number))
# Output: ['__add__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']


# ─── Contoh 1 : Python dir() dengan List───────────────────────────────────────────────────────────────────

number1 = [1, 2, 3]

# dir with a filled list
print(dir(number1))
# Output: ['__add__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']

number2 = []

# dir() with an empty list
print(dir(number2))
# Output: ['__add__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']

# ────────────────────────────────────────────────────────────────────────────────


# ─── Contoh 2 : Python dir() Dengan Set ───────────────────────────────────────────
number = {12, 15, 18, 21}

# dir() with a filled set
print(dir(number))
# Output : ['__and__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__iand__', '__init__', '__init_subclass__', '__ior__', '__isub__', '__iter__', '__ixor__', '__le__', '__len__', '__lt__', '__ne__', '__new__', '__or__', '__rand__', '__reduce__', '__reduce_ex__', '__repr__', '__ror__', '__rsub__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__xor__', 'add', 'clear', 'copy', 'difference', 'difference_update', 'discard', 'intersection', 'intersection_update', 'isdisjoint', 'issubset', 'issuperset', 'pop', 'remove', 'symmetric_difference', 'symmetric_difference_update', 'union', 'update']
number1 = []

# dir() with an empty set
print(dir(number1))
# Output : ['__add__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']

# ────────────────────────────────────────────────────────────────────────────────

# TODO ─── Penggunaan Fungsi Divmod ───────────────────────────────────────────────────
# Metode divmod()ini mengambil dua angka sebagai argumen dan mengembalikan hasil bagi dan sisanya dalam sebuah tupel.
# Syntax : divmod(number1, number2)
# Metode divmod()ini mengambil dua parameter:
#   -number1 - pembilang, bisa berupa bilangan bulat atau bilangan floating point
#   -number2 - penyebut, bisa berupa bilangan bulat atau bilangan floating point
# Metode divmod()mengembalikan:
#   -(quotient, remainder)- Tuple yang berisi hasil bagi dan sisa pembagian
#   -TypeError - untuk argumen non-numerik
# #

# ─── Contoh 0 ───────────────────────────────────────────────────────────────────
# returns the quotient and remainder of 8/3
result = divmod(8, 3)

print('Quotient and Remainder = ', result)

# Output: Quotient and Remainder =  (2, 2)

# ────────────────────────────────────────────────────────────────────────────────

# ─── Contoh 1 : Python divmod() dengan Argumen Integer ──────────────────────────
# divmod() with integer arguments
print('divmod(8, 3) = ', divmod(8, 3))
# Output : divmod(8, 3) =  (2, 2)

# divmod() with integer arguments
print('divmod(3, 8) = ', divmod(3, 8))
# Output : divmod(3, 8) =  (0, 3)

# divmod() with integer arguments
print('divmod(5, 5) = ', divmod(5, 5))
# Output : divmod(5, 5) =  (1, 0)

# ────────────────────────────────────────────────────────────────────────────────

# ─── Contoh 2: Python divmod() dengan Float Arguments ───────────────────────────
# divmod() with float arguments
print('divmod(8.0, 3) = ', divmod(8.0, 3))
# Output : divmod(8.0, 3) =  (2.0, 2.0)

# divmod() with float arguments
print('divmod(3, 8.0) = ', divmod(3, 8.0))
# Output : divmod(3, 8.0) =  (0.0, 3.0)

# divmod() with float arguments
print('divmod(7.5, 2.5) = ', divmod(7.5, 2.5))
# Output : divmod(7.5, 2.5) =  (3.0, 0.0)

# divmod() with float arguments
print('divmod(2.6, 0.5) = ', divmod(2.6, 0.5))
# Output : divmod(2.6, 0.5) =  (5.0, 0.10000000000000009)

# ────────────────────────────────────────────────────────────────────────────────

# TODO ─── Penggunaan Fungsi Enumerate ────────────────────────────────────────────────
# Metode enumerate()ini menambahkan penghitung ke iterable dan mengembalikannya(objek enumerate).
# Syntax : enumerate(iterable, start=0)
# enumerate()metode membutuhkan dua parameter:
# iterable - urutan, iterator, atau objek yang mendukung iterasi
# start(optional) - enumerate() mulai menghitung dari nomor ini. Jika start dihilangkan, is diambil sebagai awal..
# enumerate()metode menambahkan penghitung ke iterable dan mengembalikannya.
# Objek yang dikembalikan adalah objek enumerate.
# #

# ─── Contoh 0 ───────────────────────────────────────────────────────────────────

languages = ['Python', 'Java', 'JavaScript']

enumerate_prime = enumerate(languages)

# convert enumerate object to list
print(list(enumerate_prime))

# Output: [(0, 'Python'), (1, 'Java'), (2, 'JavaScript')]

# ────────────────────────────────────────────────────────────────────────────────

# ─── Contoh 1 : Bagaimana Enumerate Bekerja ─────────────────────────────────────

grocery = ['bread', 'milk', 'butter']
enumerateGrocery = enumerate(grocery)

print(type(enumerateGrocery))
# Output : <class 'enumerate'>

# converting to list
print(list(enumerateGrocery))
#Output : [(0, 'bread'), (1, 'milk'), (2, 'butter')]

# ketika menghitung mulai dari angka yang ditentukan
enumerateGrocery = enumerate(grocery, 10)
print(list(enumerateGrocery))
# Output : [(10, 'bread'), (11, 'milk'), (12, 'butter')]

# ────────────────────────────────────────────────────────────────────────────────

# ─── Contoh 2: Perulangan Obyek Enumerate ────────────────────────────────
grocery = ['bread', 'milk', 'butter']

for item in enumerate(grocery):
    print(item)
    # Output :
    # (0, 'bread')
    # (1, 'milk')
    # (2, 'butter')
print('\n')


for count, item in enumerate(grocery):
    print(count, item)
    # 0 bread
    # 1 milk
    # 2 butter
print('\n')


# changing default start value
for count, item in enumerate(grocery, 100):
    print(count, item)
# 0 bread
# 1 milk
# 2 butter


# ────────────────────────────────────────────────────────────────────────────────
# ────────────────────────────────────────────────────────────────────────────────


# TODO ─── Penggunaan Fungsi Static Method ────────────────────────────────────────────
# Fungsi staticmethod()bawaan mengembalikan metode statis untuk fungsi tertentu.
# Syntax : staticmethod(function)
#
"""staticmethod()dianggap sebagai cara yang tidak Pythonik untuk membuat fungsi statis. 
Oleh karena itu, dalam versi Python yang lebih baru, 
Anda dapat menggunakan @staticmethoddekorator."""
# Syntax baru :
# @staticmethod
# def func(args, ...)
# Metode staticmethod()ini mengambil satu parameter:
#   fungsi - fungsi yang perlu dikonversi ke metode statis
# staticmethod()Mengembalikan metode statis untuk fungsi yang diteruskan sebagai parameter .
# #

"""
 Apa itu metode statis?
 
 Metode statis, seperti metode kelas , adalah metode yang terikat ke kelas daripada objeknya.

 Mereka tidak memerlukan pembuatan instance kelas. Jadi, mereka tidak tergantung pada keadaan objek.

 Perbedaan antara metode statis dan metode kelas adalah:

 Metode statis tidak tahu apa-apa tentang kelas dan hanya berurusan dengan parameter.
 Metode kelas bekerja dengan kelas karena parameternya selalu kelas itu sendiri.
 Mereka dapat dipanggil baik oleh kelas dan objeknya.
 
    Class.staticmethodFunc() 
    atau bahkan 
    Class().staticmethodFunc()

 """

# ─── Contoh 0 ───────────────────────────────────────────────────────────────────


class Calculator:

    def add_numbers(num1, num2):
        return num1 + num2


# convert add_numbers() to static method
Calculator.add_numbers = staticmethod(Calculator.add_numbers)

sum = Calculator.add_numbers(5, 7)
print('Sum:', sum)

# Output: Sum: 12

# ────────────────────────────────────────────────────────────────────────────────

# ─── Contoh 1 : Buat Metode Statis Menggunakan Staticmethod ─────────────────────


class Mathematics:

    def addNumbers(x, y):
        return x + y


# create addNumbers static method
Mathematics.addNumbers = staticmethod(Mathematics.addNumbers)

print('The sum is:', Mathematics.addNumbers(5, 10))
# The sum is : 15

# ────────────────────────────────────────────────────────────────────────────────


# Kapan Anda menggunakan metode statis?
# ─── 1. Mengelompokkan Fungsi Utilitas Ke Kelas ─────────────────────────────────
"""
Metode statis memiliki kasus penggunaan terbatas karena, seperti metode kelas atau metode lain 
apa pun di dalam kelas, mereka tidak dapat mengakses properti kelas itu sendiri.

Namun, ketika Anda membutuhkan fungsi utilitas yang tidak mengakses properti apa pun dari 
suatu kelas tetapi masuk akal bahwa itu milik kelas, kami menggunakan fungsi statis.
"""
# ─── Contoh 2: Buat Fungsi Utilitas Sebagai Metode Statis ───────────────────────


class Dates:
    def __init__(self, date):
        self.date = date

    def getDate(self):
        return self.date

    @staticmethod
    def toDashDate(date):
        return date.replace("/", "-")


date = Dates("15-12-2016")
dateFromDB = "15/12/2016"
dateWithDash = Dates.toDashDate(dateFromDB)

if(date.getDate() == dateWithDash):
    print("Equal")
else:
    print("Unequal")

# Output is : Equal/setara

# ────────────────────────────────────────────────────────────────────────────────

"""
Di sini, kami memiliki Dateskelas yang hanya berfungsi dengan tanggal dengan tanda hubung. Namun, di database kami sebelumnya, semua tanggal ada dalam garis miring.
Untuk mengonversi slash-dates menjadi dash-dates, kami telah membuat fungsi utilitas toDashDatedi dalam Dates.
Ini adalah metode statis karena tidak perlu mengakses properti Datesitu sendiri dan hanya membutuhkan parameter.
Kami juga dapat membuat toDashDatedi luar kelas, tetapi karena ini hanya berfungsi untuk tanggal, logis untuk menyimpannya di dalam Dateskelas.
"""

# ─── 2. Memiliki Implementasi Tunggal ───────────────────────────────────────────
# Metode statis digunakan ketika kita tidak ingin subkelas dari suatu kelas
# mengubah/menimpa implementasi metode tertentu.


# ─── Contoh 3: Bagaimana Pewarisan Bekerja Dengan Metode Statis ─────────────────
class Dates:
    def __init__(self, date):
        self.date = date

    def getDate(self):
        return self.date

    @staticmethod
    def toDashDate(date):
        return date.replace("/", "-")


class DatesWithSlashes(Dates):
    def getDate(self):
        return Dates.toDashDate(self.date)


date = Dates("15-12-2016")
dateFromDB = DatesWithSlashes("15/12/2016")

if(date.getDate() == dateFromDB.getDate()):
    print("Equal")
else:
    print("Unequal")

# Output is : Equal/Setara

# ────────────────────────────────────────────────────────────────────────────────

"""
Di sini, kami tidak ingin subkelas DatesWithSlashesmenimpa metode utilitas statis toDashDatekarena hanya memiliki satu penggunaan, 
yaitu mengubah tanggal menjadi tanggal putus-putus.
Kita dapat dengan mudah menggunakan metode statis untuk keuntungan kita dengan 
getDate()mengganti metode di subkelas sehingga bekerja dengan baik dengan DatesWithSlasheskelas.
"""

# ────────────────────────────────────────────────────────────────────────────────
# ────────────────────────────────────────────────────────────────────────────────


# TODO ─── Penggunaan Fungsi Filter ───────────────────────────────────────────────────
# Fungsi filter()mengekstrak elemen dari iterable (daftar, tuple, dll.) yang mengembalikan fungsi True.
# Syntax : filter(function, iterable)
# Fungsi filter()ini mengambil dua argumen:
#   fungsi - fungsi
#   iterable - iterable seperti set, list, tuple dll.
# Fungsi filter()mengembalikan iterator.
# Catatan: Anda dapat dengan mudah mengonversi iterator ke urutan seperti daftar, tupel, string, dll.
# #

# ─── Contoh 1: Kerja Filter ─────────────────────────────────────────────────────

letters = ['a', 'b', 'd', 'e', 'i', 'j', 'o']

# a function that returns True if letter is vowel


def filter_vowels(letter):
    vowels = ['a', 'e', 'i', 'o', 'u']
    return True if letter in vowels else False


filtered_vowels = filter(filter_vowels, letters)

# converting to tuple
vowels = tuple(filtered_vowels)
print(vowels)

# Output : ('a e i o')
"""
Di sini, filter()fungsinya hanya mengekstrak huruf vokal dari lettersdaftar. Berikut cara kerja kode ini:
Setiap elemen lettersdaftar diteruskan ke filter_vowels()fungsi.
Jika filter_vowels()return True, elemen itu diekstraksi jika tidak maka akan disaring.
"""
# Catatan: Anda juga dapat memfilter daftar menggunakan loop, namun menggunakan filter()fungsi ini jauh lebih bersih.
# ────────────────────────────────────────────────────────────────────────────────


# ─── Contoh 2: Menggunakan Fungsi Lambda Di Dalam Filter ────────────────────────
numbers = [1, 2, 3, 4, 5, 6, 7]

# the lambda function returns True for even numbers
even_numbers_iterator = filter(lambda x: (x % 2 == 0), numbers)

# converting to list
even_numbers = list(even_numbers_iterator)

print(even_numbers)

#Output : [2, 4, 6]

# ────────────────────────────────────────────────────────────────────────────────

"""
Di sini, kami telah langsung melewati fungsi lambda di dalam filter().
Fungsi lambda kami kembali Trueuntuk angka genap. Oleh karena itu, filter()fungsi mengembalikan iterator yang hanya berisi angka genap.
"""

# ─── Contoh 3: Menggunakan None Sebagai Filter Di Dalam Fungsi ──────────────────
# random list
random_list = [1, 'a', 0, False, True, '0']

filtered_iterator = filter(None, random_list)

# converting to list
filtered_list = list(filtered_iterator)

print(filtered_list)
# Output : [1, 'a', Benar, '0']

# ────────────────────────────────────────────────────────────────────────────────
"""
Ketika Nonedigunakan sebagai argumen pertama ke filter()fungsi, semua elemen yang merupakan nilai kebenaran (diberikan Truejika dikonversi ke boolean) diekstraksi.
"""

# ────────────────────────────────────────────────────────────────────────────────
# ────────────────────────────────────────────────────────────────────────────────

# TODO ─── Penggunaan Fungsi Eval ─────────────────────────────────────────────────────
# Metode eval()ini mem-parsing ekspresi yang diteruskan ke metode ini dan menjalankan ekspresi python (kode) di dalam program.
# Syntax : eval(expression, globals=None, locals=None)
# The eval() function takes three parameters:
# ekspresi - string diuraikan dan dievaluasi sebagai ekspresi Python
# global (opsional) - kamus
# penduduk setempat(opsional) - objek pemetaan. Kamus adalah tipe pemetaan standar dan umum digunakan dalam Python.
# penggunaan dari global dan locals akan dibahas nanti di artikel ini.
#
# Metode eval()mengembalikan hasil yang dievaluasi dariekspresi.
# #

# ─── Contoh 0 ───────────────────────────────────────────────────────────────────

number = 9

# eval performs the multiplication passed as argument
square_number = eval('number * number')
print(square_number)

# Output: 81

# ─── Contoh 1 Bagaimana Eval Bekerja ────────────────────────────────────────────
x = 1
print(eval('x + 1'))
# Output = 2
# ────────────────────────────────────────────────────────────────────────────────
# ? Di sini, eval()fungsi mengevaluasi ekspresi x + 1dan printdigunakan untuk menampilkan nilai ini.

# ─── Contoh 2: Contoh Praktis Untuk Mendemonstrasikan Penggunaan Eval ───────────

# Perimeter of Square


def calculatePerimeter(l):
    return 4*l

# Area of Square


def calculateArea(l):
    return l*l


expression = input("Type a function: ")

for l in range(1, 5):
    if (expression == 'calculatePerimeter(l)'):
        print("If length is ", l, ", Perimeter = ", eval(expression))
    elif (expression == 'calculateArea(l)'):
        print("If length is ", l, ", Area = ", eval(expression))
    else:
        print('Wrong Function')
        break
# Output :
# Ketikkan fungsi: countArea(l)
# Jika panjangnya 1, Luas = 1
# Jika panjangnya 2, Luas = 4
# Jika panjangnya 3, Luas = 9
# Jika panjangnya 4, Luas = 16

# ────────────────────────────────────────────────────────────────────────────────
# ────────────────────────────────────────────────────────────────────────────────

# TODO ─── Penggunaan Fungsi Exec ─────────────────────────────────────────────────────
# Metode exec()mengeksekusi program yang dibuat secara dinamis, yang berupa string atau objek kode.
# Syntax : exec(object, globals, locals)
# The exec() method takes three parameters:
# objek - Baik string atau objek kode
# global (opsional) - kamus
# locals (opsional) - objek pemetaan (biasanya kamus)
# Metode exec()tidak mengembalikan nilai apa pun.
# #

# ─── Contoh 0 ───────────────────────────────────────────────────────────────────
program = 'a = 5\nb=10\nprint("Sum =", a+b)'
exec(program)

# Output: Sum = 15
# ────────────────────────────────────────────────────────────────────────────────

# ─── Contoh 1: Python Exec ──────────────────────────────────────────────────────
program = 'a = 5\nb=10\nprint("Sum =", a+b)'
exec(program)
# ────────────────────────────────────────────────────────────────────────────────
"""
Dalam contoh di atas, kita telah melewati objek stringprogramke exec()metode.
Metode mengeksekusi kode python di dalam metode objek dan menghasilkan output Sum = 15 .
"""
# ────────────────────────────────────────────────────────────────────────────────

# ─── Contoh 2: Exec Dengan Input Program Baris Tunggal ──────────────────────────
# get an entire program as input
program = input('Enter a program:')

# execute the program
exec(program)
# ────────────────────────────────────────────────────────────────────────────────
# ────────────────────────────────────────────────────────────────────────────────

# TODO ─── Penggunaan Fungsi float ────────────────────────────────────────────────────
# Metode float()mengembalikan angka floating point dari angka atau string.
# Syntax : float([x])
# Metode float()ini mengambil satu parameter:
#   x (Opsional) - angka atau string yang perlu dikonversi ke angka floating point Jika string, string harus berisi titik desimal
# Metode float()mengembalikan:
#   -Angka floating point yang setara jika argumen dilewatkan
#   -0.0 jika tidak ada argumen yang lolos
#   -OverflowErrorpengecualian jika argumen berada di luar kisaran float Python
# #

# ─── Contoh 1: Bagaimana Float Bekerja Dengan Python ────────────────────────────
# for integers
print(float(10))  # Output : 10.0

# for floats
print(float(11.22))  # Output : 11.22

# for string floats
print(float("-13.33"))  # Output : -13.33

# for string floats with whitespaces
print(float("     -24.45\n"))  # Output : -24.45

# string float error
print(float("abc"))  # Output : ValueError: could not convert string to float: 'abc'

# ────────────────────────────────────────────────────────────────────────────────

# ─── Example 2: Float For Infinity And Not A Number ─────────────────────────────
# for NaN
print(float("nan"))  # Output : nan
print(float("NaN"))  # Output : nan

# for inf/infinity
print(float("inf"))  # Output : inf
print(float("InF"))  # Output : inf
print(float("InFiNiTy"))  # Output : inf
print(float("infinity"))  # Output : inf
print(float("inFinIty"))  # Output : inf
# ────────────────────────────────────────────────────────────────────────────────
# ────────────────────────────────────────────────────────────────────────────────

# TODO ─── Penggunaan Fungsi Format ───────────────────────────────────────────────────
# Metode format()ini mengembalikan representasi terformat dari nilai yang diberikan yang dikontrol oleh penentu format.
# Syntax : format(value[, format_spec])
# Fungsi format()ini mengambil dua parameter:
#   nilai - nilai yang perlu diformat
#   format_spec - Spesifikasi tentang bagaimana nilai harus diformat.
# Fungsi format()mengembalikan representasi terformat dari nilai tertentu yang ditentukan oleh penentu format.
# #

# ─── Contoh 0 ───────────────────────────────────────────────────────────────────

value = 45

# format the integer to binary
binary_value = format(value, 'b')
print(binary_value)

# Output: 101101
# ────────────────────────────────────────────────────────────────────────────────

# ─── Contoh 1: Pemformatan Angka Dengan Format ──────────────────────────────────
# d, f and b are type

# integer
print(format(123, "d"))  # Output : 123 // desimal

# float arguments
print(format(123.4567898, "f"))  # Output : 123.456790 // float

# binary format
print(format(12, "b"))  # Output : 1100 // biner
# ────────────────────────────────────────────────────────────────────────────────

# ─── Contoh 2: Pemformatan Angka Dengan Isian Perataan Tanda Lebar Presisi Dan Tipe
# integer
print(format(1234, "*>+7,d"))  # Output : *+1,234

# float number
print(format(123.4567, "^-09.3f"))  # Output : 0123.4570

# ────────────────────────────────────────────────────────────────────────────────
"""
Di sini, saat memformat integer 1234, kami telah menentukan penentu pemformatan *>+7,d. Mari kita pahami setiap opsi:

*- Ini adalah karakter isian yang mengisi ruang kosong setelah memformat
>- Ini adalah opsi perataan kanan yang menyelaraskan string output ke kanan
+- Ini adalah opsi tanda yang memaksa nomor untuk ditandatangani (memiliki tanda di sebelah kirinya)
7- Ini adalah opsi lebar yang memaksa angka untuk mengambil lebar minimum 7, spasi lainnya akan diisi dengan karakter isian
,- Operator ribuanlah yang menempatkan koma di antara ribuan.
d- Ini adalah opsi tipe yang menentukan nomor adalah bilangan bulat.
# ────────────────────────────────────────────────────────────────────────────────
Saat memformat floating point number 123.4567, kita telah menentukan format specifier ^-09.3f. Ini adalah:

^- Ini adalah opsi penyelarasan tengah yang menyelaraskan string keluaran ke tengah ruang yang tersisa
-- Ini adalah opsi tanda yang memaksa hanya angka negatif untuk menunjukkan tanda
0- Ini adalah karakter yang ditempatkan di tempat kosong.
9- Ini adalah opsi lebar yang menetapkan lebar minimum angka menjadi 9 (termasuk titik desimal, koma ribuan, dan tanda)
.3- Ini adalah operator presisi yang mengatur presisi angka mengambang yang diberikan ke 3 tempat
f- Ini adalah opsi tipe yang menentukan nomor adalah float.
# ────────────────────────────────────────────────────────────────────────────────

"""
# ─── Contoh 3: Menggunakan format() dengan mengganti __format__──────────────────
# custom __format__() method


class Person:
    def __format__(self, format):
        if(format == 'age'):
            return '23'
        return 'None'


print(format(Person(), "age"))

# ────────────────────────────────────────────────────────────────────────────────
"""
Di sini, kami telah mengganti __format__()metode kelas Person.
Sekarang menerima formatparameter dan mengembalikan 23 jika sama dengan 'age'. Jika tidak ada format yang ditentukan, Nonedikembalikan.
Fungsi format()berjalan secara internal Person().__format__("age")untuk mengembalikan 23.
"""
# ────────────────────────────────────────────────────────────────────────────────
"""
Format bawaan() Vs. format string()
format()Fungsinya mirip dengan metode format String . Secara internal, kedua metode memanggil __format__()metode objek.
Sementara format()fungsi bawaan adalah implementasi tingkat rendah untuk memformat objek menggunakan __format__()internal, string format()adalah implementasi tingkat tinggi yang mampu melakukan operasi pemformatan kompleks pada beberapa string objek juga.
"""
# ────────────────────────────────────────────────────────────────────────────────
# ────────────────────────────────────────────────────────────────────────────────

# TODO ─── Penggunaan Fungsi Frozenset ────────────────────────────────────────────────
# Fungsi frozenset() mengembalikan objek frozenset yang tidak dapat diubah
# yang diinisialisasi dengan elemen dari iterable yang diberikan.
# Syntax : frozenset([iterable])
# Fungsi frozenset()ini mengambil satu parameter:
#   -iterable (Opsional) - iterable yang berisi elemen untuk menginisialisasi frozenset.Iterable dapat diatur, kamus, Tuple, dll.
# Fungsi frozenset()mengembalikan yang tidak dapat diubah yang frozensetdiinisialisasi dengan elemen dari iterable yang diberikan.
# #

"""
Set beku hanyalah versi objek set Python yang tidak dapat diubah . Sementara elemen himpunan dapat dimodifikasi kapan saja, elemen himpunan beku tetap sama setelah dibuat.
Karena ini, set beku dapat digunakan sebagai kunci dalam Kamus atau sebagai elemen dari set lain. Tapi seperti set, itu tidak dipesan (elemen dapat diatur pada indeks apa pun).
"""

# ─── Contoh 1: Bekerja Dari Python Frozenset ────────────────────────────────────

# tuple of vowels
vowels = ('a', 'e', 'i', 'o', 'u')

fSet = frozenset(vowels)

print('The frozen set is:', fSet)
# Output : frozenset({'a', 'o', 'i', 'u', 'e'})
print('The empty frozen set is:', frozenset())
# Output : The empty frozen set is: frozenset()

# frozensets are immutable
fSet.add('v')  # Output : AttributeError: 'frozenset' object has no attribute 'add'

# ────────────────────────────────────────────────────────────────────────────────

# ─── Contoh 2: Frozenset Untuk Kamus ────────────────────────────────────────────
# Saat Anda menggunakan kamus sebagai iterable untuk set yang dibekukan, hanya diperlukan kunci kamus untuk membuat set.
# random dictionary
person = {"name": "John", "age": 23, "sex": "male"}

fSet = frozenset(person)

print('The frozen set is:', fSet)
# Output : The frozen set is: frozenset({'name', 'age', 'sex'})
# ────────────────────────────────────────────────────────────────────────────────

# ─── Contoh 3 Operasi Frozenset ─────────────────────────────────────────────────
# Seperti set normal, frozenset juga dapat melakukan operasi yang berbeda seperti copy, difference, intersection, symmetric_difference, dan union.

# Frozensets
# initialize A and B
A = frozenset([1, 2, 3, 4])
B = frozenset([3, 4, 5, 6])

# copying a frozenset
C = A.copy()  # Output: frozenset({1, 2, 3, 4})
print(C)

# union
print(A.union(B))  # Output: frozenset({1, 2, 3, 4, 5, 6})

# intersection
print(A.intersection(B))  # Output: frozenset({3, 4})

# difference
print(A.difference(B))  # Output: frozenset({1, 2})

# symmetric_difference
print(A.symmetric_difference(B))  # Output: frozenset({1, 2, 5, 6})

# ────────────────────────────────────────────────────────────────────────────────
# Demikian pula, metode set lainnya seperti isdisjoint, issubset, dan issupersetjuga tersedia.
# Frozensets
# initialize A, B and C
A = frozenset([1, 2, 3, 4])
B = frozenset([3, 4, 5, 6])
C = frozenset([5, 6])

# isdisjoint() method
print(A.isdisjoint(C))  # Output: True

# issubset() method
print(C.issubset(B))  # Output: True

# issuperset() method
print(B.issuperset(C))  # Output: True
# ────────────────────────────────────────────────────────────────────────────────
# ────────────────────────────────────────────────────────────────────────────────

# TODO ─── Penggunaan Fungsi Getattr ──────────────────────────────────────────────────
# Metode getattr()mengembalikan nilai atribut bernama dari suatu objek. Jika tidak ditemukan,
# itu mengembalikan nilai default yang diberikan ke fungsi.
# Syntax : getattr(object, name[, default])
# syntax is equivalent to: object.name
# getattr()metode membutuhkan beberapa parameter:
# objek - objek yang nilai atributnya akan dikembalikan
# name - string yang berisi nama atribut
# default (Opsional) - nilai yang dikembalikan ketika atribut bernama tidak ditemukan
#
# getattr()metode kembali:
#   -nilai atribut bernama dari objek yang diberikan
#   -default, jika tidak ada atribut bernama yang ditemukan
#   -AttributeErrorpengecualian, jika atribut bernama tidak ditemukan dan defaulttidak didefinisikan
# #


# ─── Contoh 1: Bagaimana Getattr Bekerja Dengan Python ──────────────────────────
class Person:
    age = 23
    name = "Adam"


person = Person()
print('The age is:', getattr(person, "age"))  # Output : The age is: 23
print('The age is:', person.age)  # Output : The age is: 23

# ────────────────────────────────────────────────────────────────────────────────

# ─── Contoh 2: Getattr Ketika Atribut Bernama Tidak Ditemukan ───────────────────


class Person:
    age = 23
    name = "Adam"


person = Person()

# when default value is provided
print('The sex is:', getattr(person, 'sex', 'Male'))
# Output : The sex is: Male
# when no default value is provided

print('The sex is:', getattr(person, 'sex'))
# Output : AttributeError: 'Person' object has no attribute 'sex'
# ────────────────────────────────────────────────────────────────────────────────

"""
Atribut bernamasekstidak hadir di kelasOrang. Jadi, saat memanggil getattr()metode dengan nilai default Male, ia mengembalikan Male.
Namun, jika kita tidak memberikan nilai default, ketika atribut bernama sex tidak ditemukan, maka akan muncul AttributeErrorpepatah bahwa objek tersebut tidak memiliki atribut sex.
"""
# ────────────────────────────────────────────────────────────────────────────────
# ────────────────────────────────────────────────────────────────────────────────

# TODO ─── Pengguanan Fungsi Globals ──────────────────────────────────────────────────
# Metode globals()ini mengembalikan kamus dengan semua variabel dan simbol global untuk program saat ini.
# Syntax : globals()
# Metode globals()ini tidak mengambil parameter apa pun.
# Metode globals()mengembalikan kamus tabel simbol global saat ini.
# #

# ─── Contoh 1 ───────────────────────────────────────────────────────────────────

age = 23

globals()['age'] = 25
print('The age is:', age)
# Output : The age is:

# ────────────────────────────────────────────────────────────────────────────────
# ────────────────────────────────────────────────────────────────────────────────
"""
Kompiler Python memelihara tabel simbol yang berisi informasi yang diperlukan tentang program yang sedang ditulis. Ada dua jenis tabel simbol dalam Python - Loca l dan Global .
Tabel Simbol Global menyimpan semua informasi yang terkait dengan cakupan global program (dalam keseluruhan program). Kita dapat mengakses tabel simbol ini dengan globals()metode.
Biasanya, pemrogram python menggunakan globals()metode untuk memodifikasi variabel global apa pun dalam kode.
Dalam hal ini, kami telah mengubahusiavariabel ke 25 menggunakan globals()metode dengan kunci kamus ['age'].
"""
# ────────────────────────────────────────────────────────────────────────────────
# ────────────────────────────────────────────────────────────────────────────────


# TODO ─── Penggunaan Fungsi Hasattr ──────────────────────────────────────────────────
# Metode hasattr()mengembalikan true jika suatu objek memiliki atribut bernama yang diberikan dan false jika tidak.
# Syntax : hasattr(object, name)
# Metode hasattr()ini mengambil dua parameter:
#   -obyek- objek yang atribut namanya akan diperiksa
#   -nama- nama atribut yang akan dicari
# Metode hasattr()mengembalikan:
# True- jika objek memiliki atribut bernama yang diberikan
# False- jika objek tidak memiliki atribut bernama yang diberikan
# #


# ─── Contoh 0 ───────────────────────────────────────────────────────────────────

class Person:
    age = 23
    name = "Adam"


person = Person()

print("Person's age:", hasattr(person, "age"))
print("Person's salary:", hasattr(person, "salary"))

# Output:
# Person's age: True
# Person's salary: False

# ────────────────────────────────────────────────────────────────────────────────

# ─── Contoh 1: Python Hasattr ───────────────────────────────────────────────────


class Car:
    brand = "Ford"
    number = 7786


car = Car()

print("The car class has brand:", hasattr(Car, "brand"))
print("The car class has specs: ", hasattr(Car, "specs"))
# Output :
# The car class has brand: True
# The car class has specs:  False
# ────────────────────────────────────────────────────────────────────────────────
"""
Dalam contoh di atas, kami memiliki Carkelas dengan dua atribut: branddan number.
Saat kami memeriksa kedua atribut ini menggunakan hasattr()metode, hasilnya adalah True .
Di sisi lain, untuk atribut apa pun yang tidak ada di kelas Carseperti specs , kita mendapatkan False sebagai outputnya.    
"""
# ────────────────────────────────────────────────────────────────────────────────
# ────────────────────────────────────────────────────────────────────────────────


# TODO ─── Penggunaan Fugnsi Hash ─────────────────────────────────────────────────────
# Metode hash()mengembalikan nilai hash suatu objek jika memilikinya.
# Nilai hash hanyalah bilangan bulat yang digunakan untuk membandingkan kunci kamus
# selama kamus terlihat dengan cepat.
#
# Syntax : hash(object)
# Metode hash()ini mengambil satu parameter:
#   -objek - objek yang nilai hashnya akan dikembalikan (integer, string, float)
# Metode hash()mengembalikan nilai hash dari suatu objek.
# #

# ─── Contoh 0 ───────────────────────────────────────────────────────────────────
text = 'Python Programming'

# compute the hash value of text
hash_value = hash(text)
print(hash_value)

# Output: -966697084172663693

# ────────────────────────────────────────────────────────────────────────────────

# ─── Contoh 1: Bagaimana Hash Bekerja Dengan Python ─────────────────────────────
# hash for integer unchanged
print('Hash for 181 is:', hash(181))
# Ouput : Hash untuk 181 adalah: 181

# hash for decimal
print('Hash for 181.23 is:', hash(181.23))
# Ouput : Hash untuk 181,23 adalah: 530343892119126197

# hash for string
print('Hash for Python is:', hash('Python'))
# Ouput : Hash untuk Python adalah: 2230730083538390373

# ────────────────────────────────────────────────────────────────────────────────

# ─── Contoh 2: Hash Untuk Objek Tuple Yang Tidak Dapat Diubah ───────────────────
# hash()metode hanya berfungsi untuk objek yang tidak dapat diubah sebagai Tuple .
# #

# tuple of vowels
vowels = ('a', 'e', 'i', 'o', 'u')

print('The hash is:', hash(vowels))
# Ouput : The hash is: -695778075465126279

# ────────────────────────────────────────────────────────────────────────────────
# ────────────────────────────────────────────────────────────────────────────────

# ─── Contoh 3: Hash Untuk Objek Kustom Dengan Mengganti __hash__ ────────────────


class Person:
    def __init__(self, age, name):
        self.age = age
        self.name = name

    def __eq__(self, other):
        return self.age == other.age and self.name == other.name

    def __hash__(self):
        print('The hash is:')
        return hash((self.age, self.name))


person = Person(23, 'Adam')
print(hash(person))

# Output : Hashnya adalah: 3785419240612877014
#! Catatan: Anda tidak harus mengimplementasikan __eq__()metode untuk hash karena metode ini dibuat secara default untuk semua objek.

# ────────────────────────────────────────────────────────────────────────────────
# ────────────────────────────────────────────────────────────────────────────────


# TODO ─── Penggunaan Fungsi Help ─────────────────────────────────────────────────────
# Metode help() memanggil sistem bantuan Python bawaan.
# Syntax : help(object)
# Metode help()ini mengambil maksimal satu parameter.
#   -objek (opsional) - Anda ingin menghasilkan bantuan yang diberikanobject
# #

# ────────────────────────────────────────────────────────────────────────────────
# ────────────────────────────────────────────────────────────────────────────────

"""
How help() works in Python?
The help() method is used for interactive use. 
It's recommended to try it in your interpreter when you need help to write Python program 
and use Python modules.
#!Note: object is passed to help() (not a string)    
"""

# ? Try these on Python shell.

help(list)
help(dict)
help(print)
help([1, 2, 3])

# Jika string dilewatkan sebagai argumen, nama modul, fungsi, kelas, metode, kata kunci,
# atau topik dokumentasi, dan halaman bantuan dicetak.
#! Catatan: string dilewatkan sebagai argumen kehelp()
# #

"""
Jika stringditeruskan sebagai argumen, string yang diberikan akan dicari sebagai nama modul, 
fungsi, kelas, metode, kata kunci, atau topik dokumentasi, dan halaman bantuan dicetak.    
"""

help('random thing')
help('print')
help('def')
help('math.pow')

#! Catatan: tidak ada argumen yang diteruskan kehelp()


# Jika tidak ada argumen yang diteruskan, utilitas bantuan Python(sistem bantuan interaktif)
# dimulai di konsol.

help()

# Kemudian, Anda dapat memasukkan nama topik untuk mendapatkan bantuan dalam menulis program Python
# dan menggunakan modul Python. Sebagai contoh:

help > True
help > 'print'
help > print

# Untuk keluar dari utilitas bantuan dan kembali ke juru bahasa, Anda perlu mengetik quitdan menekan enter.

help > quit


# ────────────────────────────────────────────────────────────────────────────────
# ────────────────────────────────────────────────────────────────────────────────


# TODO ─── Penggunaan Fungsi Hex ──────────────────────────────────────────────────────
# Fungsi hex() mengonversi bilangan bulat ke string heksadesimal yang sesuai.
# Syntax : hex(x)
# hex()fungsi mengambil satu argumen.
# x - bilangan bulat ( intobjek atau harus mendefinisikan __index__()metode yang mengembalikan bilangan bulat)
#
# hex()fungsi mengonversi bilangan bulat ke bilangan heksadesimal yang sesuai dalam bentuk string dan mengembalikannya.
# String heksadesimal yang dikembalikan dimulai dengan awalan yang 0xmenunjukkan bahwa itu dalam bentuk heksadesimal.
# #


# ─── Contoh 1 Bagaimana Hex Bekerja ─────────────────────────────────────────────
number = 435
print(number, 'in hex =', hex(number))
# Output : 435 dalam hex = 0x1b3
number = 0
print(number, 'in hex =', hex(number))
# Output : 0 dalam hex = 0x0
number = -34
print(number, 'in hex =', hex(number))
# Output : -34 dalam hex = -0x22
returnType = type(hex(number))
print('Return type from hex() is', returnType)
# Output :Jenis pengembalian dari hex() adalah <class 'str'>
# ────────────────────────────────────────────────────────────────────────────────
"""
Jika Anda perlu menemukan representasi heksadesimal dari float, Anda perlu menggunakan float.hex()metode.
"""
# ────────────────────────────────────────────────────────────────────────────────

# ─── Contoh 2: Representasi Heksadesimal Dari Float ─────────────────────────────
number = 2.5
print(number, 'in hex =', float.hex(number))
# Output : 2,5 dalam hex = 0x1.4000000000000p+1
number = 0.0
print(number, 'in hex =', float.hex(number))
# Output : 0,0 dalam heksa = 0x0.0p+0
number = 10.5
print(number, 'in hex =', float.hex(number))
# Output : 10,5 dalam heksa = 0x1.5000000000000p+3
# ────────────────────────────────────────────────────────────────────────────────
# ────────────────────────────────────────────────────────────────────────────────

# TODO ─── Penggunaan Fungsi Id ───────────────────────────────────────────────────────
# Metode id()ini mengembalikan bilangan bulat unik (identitas) dari objek argumen yang diteruskan.
# Sintaks dari id()metode ini adalah: id(object)
# Metode id()ini mengambil satu parameter:
#   -obyek- dapat berupa kelas, variabel, daftar, tupel, set, dll.
# Metode id()mengembalikan:
#   -identitas objek (yang merupakan bilangan bulat unik untuk objek tertentu)
# #

# ─── Contoh 0 ───────────────────────────────────────────────────────────────────
a = 5
b = 6
sum = a + b

# id of sum variable
print("The id of sum is", id(sum))
# Output: The id of sum is 1877287371312
# ────────────────────────────────────────────────────────────────────────────────


# ─── Contoh 1 : Python Id ───────────────────────────────────────────────────────
# id of 5
print("id of 5 =", id(5))
# Output: id of 5 = 2037968011632

a = 5
# id of a
print("id of a =", id(a))
# Output: id of a = 2037968011632

b = a
# id of b
print("id of b =", id(b))
# Output: id of b = 2037968011632

c = 5.0
# id of c
print("id of c =", id(c))
# Output: id of c = 2037968011632
# ────────────────────────────────────────────────────────────────────────────────
"""
Di sini, id()metode mengembalikan nomor integer unik untuk setiap nilai unik yang digunakannya.
Dalam contoh di atas, kami telah menggunakan id()metode dengan variabe a,b dan c dan mendapatkan id yang sesuai.
Seperti yang Anda lihat, id()metode ini mengembalikan bilangan bulat 2037968011632 untuk keduanya a = 5 dan 5.0
Karena kedua nilainya sama, idnya juga sama.
#!Catatan : Karena ID adalah alamat memori yang ditetapkan, ID dapat berbeda di sistem yang berbeda. Jadi, output pada sistem Anda bisa berbeda.
"""

# ─── Contoh 2 : Id dengan kelas dan object ──────────────────────────────────────


class Food:
    banana = 15


dummyFood = Food()

#  id of the object dummyFood
print("id of dummyFoo =", id(dummyFood))
# Output : id of dummyFoo = 3074880666976
# ?Ketika kita menggunakan id()metode dengan dummyFoodobjek, kita mendapatkan hasil 139984002204864 .
# ────────────────────────────────────────────────────────────────────────────────

# ─── Contoh 3: Id Dengan Set ────────────────────────────────────────────────────

fruits = {"apple", "banana", "cherry", "date"}

# id() of the set fruits
print("The id of the fruits set is", id(fruits))
# Output : The id of the fruits set is 1969766393088
# ? Dalam contoh di atas, kami telah menggunakan id()metode dengan set fruit. Dalam hal ini, kami mendapatkan nomor unik sebagai id untuk set- 140533973276928 .
# ────────────────────────────────────────────────────────────────────────────────

# ─── Contoh 4 : Id Dengan Tuples ────────────────────────────────────────────────
vegetables = ("asparagus", "basil", "cabbage")

# id() with vegetable
print("The id of the vegetables set is", id(vegetables))
# The id of the vegetables set is 2283407349376
# ? Metode id()mengembalikan nomor unik 139751433263360 sebagai id dari tuple vegetable.
# ────────────────────────────────────────────────────────────────────────────────
# ────────────────────────────────────────────────────────────────────────────────


# TODO ─── Penggunaan Fungsi Input ────────────────────────────────────────────────────
# Fungsi input()mengambil input dari pengguna dan mengembalikannya.
# Syntax : input([prompt])
# Fungsi input()mengambil satu argumen opsional:
#   -prompt (Opsional) - string yang ditulis ke output standar (biasanya layar) tanpa mengikuti baris baru
# Fungsi input()membaca baris dari input (biasanya dari pengguna), mengubah baris menjadi string dengan menghapus baris baru yang tertinggal, dan mengembalikannya.
# Jika EOF dibaca, itu menimbulkan EOFErrorpengecualian.
# #


# ─── Contoh 0 ───────────────────────────────────────────────────────────────────
name = input("Enter your name: ")
print(name)

# Output:
# Enter your name: James
# James

# ────────────────────────────────────────────────────────────────────────────────

# ─── Contoh 1 Bagaimana Input Bekerja Dengan Python ─────────────────────────────
# get input from user

inputString = input()

print('The inputted string is:', inputString)
# Output : The inputted string is: Risqi
# Risqi
# ────────────────────────────────────────────────────────────────────────────────

# ─── Contoh 2: Dapatkan Masukan Dari Pengguna Dengan Prompt ─────────────────────
# get input from user

inputString = input('Enter a string:')

print('The inputted string is:', inputString)
# Output : Enter a string : risqi
# The inputted string is: risqi
# ────────────────────────────────────────────────────────────────────────────────
# ────────────────────────────────────────────────────────────────────────────────


# TODO ─── Penggunaan Fungs Int ───────────────────────────────────────────────────────
# Metode int()ini mengonversi string apa pun, objek seperti byte, atau angka menjadi bilangan bulat dan kembali.
# Syntax : int(value, base [optional])
# int()metode membutuhkan dua parameter:
#   -nilai- string numerik, objek seperti byte atau angka apa pun
#   -dasar [opsional]- sistem angka tempat nilainya saat ini
# Metode int()mengembalikan:
#   -bagian integer dari nomor - untuk nilai argumen tunggal (nomor apa saja)
#   -0 - tanpa argumen
#   -representasi bilangan bulat dari angka dengan basis yang diberikan (0, 2 ,8 ,10,16)
# #

# ─── Contoh 0 ───────────────────────────────────────────────────────────────────
# returns the integer representation of the binary string 1010
print("For 1010, int is:", int("1010", 2))

# Output: For 1010, int is: 10
# ────────────────────────────────────────────────────────────────────────────────

# ─── Contoh 1 : Python int Argumen Tunggal ──────────────────────────────────────

# int() with an integer value
print("int(123) is:", int(123))
# Output: int(123) is: 123

# int() with a floating point value
print("int(123.23) is:", int(123.23))
# Output: int(123.23) is: 123

# int() with a numeric-string value
print("int('123') is:", int("123"))
# Output: int('123') is: 123

# ────────────────────────────────────────────────────────────────────────────────

# ─── Contoh 2 : Python Int Dua Argumen ──────────────────────────────────────────
# converting a binary to integer with int()
print("For 0b101, int is:", int("0b101", 2))
# Output: For 0b101, int is: 5

# converting a binary to integer with int())
print("For 0o16, int is:", int("0o16", 8))
# Output: For 0o16, int is: 14


# converting a binary to integer with int()
print("For 0xA, int is:", int("0xA", 16))
# Output: For 0xA, int is: 10

# ────────────────────────────────────────────────────────────────────────────────

# ─── Contoh 3: Int Untuk Objek Khusus ───────────────────────────────────────────
"""
Bahkan jika suatu objek bukan angka, kita masih dapat mengubahnya menjadi objek integer.
Kita dapat melakukan ini dengan mudah dengan mengganti __index__()dan __int__()metode kelas untuk mengembalikan angka.
Kedua metode itu identik. Versi Python yang lebih baru menggunakan __index__()metode ini.
"""


class Person:
    age = 23

    def __index__(self):
        return self.age

    # def __int__(self):
    #     return self.age


person = Person()

# int() method with a non integer object person
print("int(person) is:", int(person))
# Output: int(person) is: 23


# ────────────────────────────────────────────────────────────────────────────────
"""
Dalam contoh di atas, kelasnya Personbukan tipe integer.
Tapi kita masih bisa mengembalikanusiavariabel (yang merupakan bilangan bulat) menggunakan int()metode.
"""

# ────────────────────────────────────────────────────────────────────────────────
# ────────────────────────────────────────────────────────────────────────────────


# TODO ─── Penggunaan Fungsi Isinstance ───────────────────────────────────────────────
# Fungsi isinstance()memeriksa apakah objek(argumen pertama) adalah turunan atau subkelas dari kelas classinfo(argumen kedua).
# Syntax : isinstance(object, classinfo)
# isinstance()membutuhkan dua parameter:
#   -objek - objectuntuk diperiksa
#   -classinfo - kelas, tipe, atau tupel kelas dan tipe
# isinstance() mengembalikan:
#   -True jika obyek adalah turunan atau subkelas dari kelas atau elemen apa pun dari Tuple
#   -False jika tidak
#! Jikainfo kelasbukan tipe atau tupel tipe, TypeErrorpengecualian dimunculkan.
# #

# ─── Contoh 0 ───────────────────────────────────────────────────────────────────
numbers = [1, 2, 3, 4, 2, 5]

# check if numbers is instance of list
result = isinstance(numbers, list)
print(result)

# Output: True
# ────────────────────────────────────────────────────────────────────────────────

# ─── Contoh 1 : Cara Kerja Isinstance ───────────────────────────────────────────


class Foo:
    a = 5


fooInstance = Foo()

print(isinstance(fooInstance, Foo))  # True
print(isinstance(fooInstance, (list, tuple)))  # False
print(isinstance(fooInstance, (list, tuple, Foo)))  # True

# ────────────────────────────────────────────────────────────────────────────────

# ─── Contoh 2: Bekerja Dari Isinstance Dengan Native Types ──────────────────────
numbers = [1, 2, 3]

result = isinstance(numbers, list)
print(numbers, 'instance of list?', result)
# Output : [1, 2, 3] instance of list? True

result = isinstance(numbers, dict)
print(numbers, 'instance of dict?', result)
# Output : [1, 2, 3] instance of dict? False

result = isinstance(numbers, (dict, list))
print(numbers, 'instance of dict or list?', result)
# Output : [1, 2, 3] instance of dict or list? True

number = 5
result = isinstance(number, list)
print(number, 'instance of list?', result)
# Output : 5 instance of list? Fals

result = isinstance(number, int)
print(number, 'instance of int?', result)
# Output : 5 instance of int? True

# ────────────────────────────────────────────────────────────────────────────────
# ────────────────────────────────────────────────────────────────────────────────

#TODO ─── Penggunaan Fungsi Issubclass ───────────────────────────────────────────────
# Fungsi issubclass() memeriksa apakah argumen kelas (argumen pertama) adalah subkelas dari kelas classinfo (argumen kedua).
# Syntax : issubclass(class, classinfo)
# issubclass()membutuhkan dua parameter:
#   -kelas - kelas yang akan diperiksa
#   -classinfo - kelas, tipe, atau tupel kelas dan tipe
# issubclass()mengembalikan:
#   -Truejikakelasadalah subclass dari kelas, atau elemen apa pun dari Tuple
#   -Falsejika tidak
# #

# ─── Contoh: Bagaimana Cara Kerja Issubclass ────────────────────────────────────


class Polygon:
    def __init__(polygonType):
        print('Polygon is a ', polygonType)


class Triangle(Polygon):
    def __init__(self):

        Polygon.__init__('triangle')


print(issubclass(Triangle, Polygon))  # True
print(issubclass(Triangle, list))  # False
print(issubclass(Triangle, (list, Polygon)))  # True
print(issubclass(Polygon, (list, Polygon)))  # True

# ────────────────────────────────────────────────────────────────────────────────
# ────────────────────────────────────────────────────────────────────────────────


# TODO ─── Penggunaan Fungsi Iter ─────────────────────────────────────────────────────
# Metode iter()mengembalikan iterator untuk argumen yang diberikan.
# Syntax : iter(object, sentinel [optional])
# Metode iter()ini mengambil dua parameter:
#   -obyek- bisa berupa list, set, tuple, dll.
#   -sentinel [optional] - a special value that is used to represent the end of a sequence
# Metode iter()mengembalikan:
#   -objek iterator untuk argumen yang diberikan sampai karakter sentinel ditemukan
#   -TypeError untuk objek yang ditentukan pengguna yang tidak mengimplementasikan __iter__(), dan __next__()atau__getitem()__
#
# #

# ─── Contoh 0 ───────────────────────────────────────────────────────────────────
# list of vowels
phones = ['apple', 'samsung', 'oneplus']
phones_iter = iter(phones)

print(next(phones_iter))
print(next(phones_iter))
print(next(phones_iter))

# Output:
# apple
# samsung
# oneplus
# ────────────────────────────────────────────────────────────────────────────────

# ─── Contoh 1 : Python Iter ─────────────────────────────────────────────────────
# list of vowels
vowels = ["a", "e", "i", "o", "u"]

# iter() with a list of vowels
vowels_iter = iter(vowels)

print(next(vowels_iter))  # Output : a
print(next(vowels_iter))  # Output : e
print(next(vowels_iter))  # Output : i
print(next(vowels_iter))  # Output : o
print(next(vowels_iter))  # Output :u

# ────────────────────────────────────────────────────────────────────────────────

"""
Dalam contoh di atas, kami telah menggunakan iter()metode dengan daftar vokal.
Metode mengembalikan elemen individu a, e, i, o, u dalam daftar sebagai objek iterator.    
"""
# ────────────────────────────────────────────────────────────────────────────────

# ─── Contoh 2 : Iter Untuk Object Khusus ────────────────────────────────────────


class PrintNumber:
    def __init__(self, max):
        self.max = max

# iter() method in a class
    def __iter__(self):
        self.num = 0
        return self
# next() method in a class

    def __next__(self):
        if(self.num >= self.max):
            raise StopIteration
        self.num += 1
        return self.num


print_num = PrintNumber(3)

print_num_iter = iter(print_num)
print(next(print_num_iter))  # 1
print(next(print_num_iter))  # 2
print(next(print_num_iter))  # 3

# raises StopIteration
print(next(print_num_iter))
""" Output :
Traceback (panggilan terakhir terakhir): 
  File "", baris 23, di 
File "", baris 11, di __next__ 
StopIteration
"""

# ────────────────────────────────────────────────────────────────────────────────

"""
Pada contoh di atas, kami telah mencetak nomor iterator 1 , 2 , 3 menggunakan metode __iter__()and __next__() .
Di sini, __next()__metode di sini memiliki loop yang berjalan hingga self.numlebih besar dari atau sama dengan self.max.
Karena kami telah melewati 3 sebagai parameter ke PrintNumber()objek, self.maxdiinisialisasi ke 3 . Oleh karena itu, loop berhenti di 3 .
Ketika self.nummencapai nilai self.maxyang 3 , next()metode ini memunculkan pengecualian StopIteration .
"""


# ─── Contoh 3 : Iter Dengan Parameter Sentinel ──────────────────────────────────

class DoubleIt:

    def __init__(self):
        self.start = 1

    def __iter__(self):
        return self

    def __next__(self):
        self.start *= 2
        return self.start

    __call__ = __next__


my_iter = iter(DoubleIt(), 16)

for x in my_iter:
    print(x)

# Output :
# 2
# 4
# 8
# ────────────────────────────────────────────────────────────────────────────────
"""
Dalam contoh di atas, kami belum menerapkan StopIterationkondisi.
Sebagai gantinya, kami telah menggunakan iter()metode dengan parameter sentinel untuk menghentikan iterasi:
"""
#my_iter = iter(DoubleIt(), 16)
"""
Nilai parameter sentinel disini adalah 16 sehingga program akan berhenti ketika nilai dari __next__()metode sama dengan angka tersebut.
Pada titik ini dalam kode, program akan menaikkan secara StopIterationotomatis.
"""
# ────────────────────────────────────────────────────────────────────────────────
# ────────────────────────────────────────────────────────────────────────────────


# TODO ─── Penggunaan Fungsi Len ──────────────────────────────────────────────────────
# Fungsi len()mengembalikan jumlah item (panjang) dalam suatu objek.
# Syntax : len(s)
# Fungsi len()mengambil satu argumen s , yang dapat berupa
#   -urutan - string, byte, Tuple, daftar, rentang ATAU,
#   -koleksi - kamus, set, set beku
# len()fungsi mengembalikan jumlah item dari suatu objek.
# Gagal memberikan argumen atau memberikan argumen yang tidak valid akan memunculkan TypeErrorpengecualian.
# #


# ─── Contoh 0 ───────────────────────────────────────────────────────────────────
languages = ['Python', 'Java', 'JavaScript']

# compute the length of languages
length = len(languages)
print(length)

# Output: 3
# ────────────────────────────────────────────────────────────────────────────────

# ─── Contoh 1: Bagaimana Len Bekerja Dengan Tupel Daftar Dan Rentang ────────────
testList = []
print(testList, 'length is', len(testList))
# Output :[] panjangnya adalah 0

testList = [1, 2, 3]
print(testList, 'length is', len(testList))
# Output :[1, 2, 3] panjangnya adalah 3

testTuple = (1, 2, 3)
print(testTuple, 'length is', len(testTuple))
# Output :(1, 2, 3) panjangnya adalah 3

testRange = range(1, 10)
print('Length of', testRange, 'is', len(testRange))
# Output : Panjang jangkauan(1, 10) adalah 9
# ────────────────────────────────────────────────────────────────────────────────

# ─── Contoh 2: Bagaimana Len Bekerja Dengan String Dan Byte ─────────────────────
testString = ''
print('Length of', testString, 'is', len(testString))
# Output : Panjangnya adalah 0

testString = 'Python'
print('Length of', testString, 'is', len(testString))
# Output : Panjang Python adalah 6

# byte object
testByte = b'Python'
print('Length of', testByte, 'is', len(testByte))
# Output :Panjang b'Python' adalah 6

testList = [1, 2, 3]
# converting to bytes object
testByte = bytes(testList)
print('Length of', testByte, 'is', len(testByte))
# Output :Panjang b'\x01\x02\x03' adalah3
# ────────────────────────────────────────────────────────────────────────────────


# ─── Contoh 3: Bagaimana Len Bekerja Dengan Kamus Dan Set ───────────────────────
testSet = {1, 2, 3}
print(testSet, 'length is', len(testSet))
# Ouput : {1, 2, 3} panjangnya adalah 3

# Empty Set
testSet = set()
print(testSet, 'length is', len(testSet))
# Ouput : set() panjangnya 0

testDict = {1: 'one', 2: 'two'}
print(testDict, 'length is', len(testDict))
# Ouput : {1: 'one', 2: 'two'} length is 2

testDict = {}
print(testDict, 'length is', len(testDict))
# Ouput : {} length is 0

testSet = {1, 2}
# frozenSet
frozenTestSet = frozenset(testSet)
print(frozenTestSet, 'length is', len(frozenTestSet))
# Ouput : frozenset({1, 2}) length is 2

# ────────────────────────────────────────────────────────────────────────────────


# ─── Contoh 4: Bagaimana Len Bekerja Untuk Objek Kustom ─────────────────────────
class Session:
    def __init__(self, number=0):
        self.number = number

    def __len__(self):
        return self.number


# default length is 0
s1 = Session()
print(len(s1))  # Output : 0


# giving custom length
s2 = Session(6)
print(len(s2))  # Output : 6
# ────────────────────────────────────────────────────────────────────────────────
# ────────────────────────────────────────────────────────────────────────────────


# TODO ─── Penggunaan Fungsi List ─────────────────────────────────────────────────────
# Konstruktor list()mengembalikan daftar dengan Python.
# Syntax : list([iterable])
# Konstruktor list()mengambil satu argumen:
#   -iterable (opsional) - objek yang bisa berupa urutan ( string , tupel ) atau koleksi ( set , dictionary ) atau objek iterator apa pun
# Konstruktor list()mengembalikan daftar.
#   -Jika tidak ada parameter yang dilewatkan, ia mengembalikan daftar kosong
#   -Jika iterable dilewatkan sebagai parameter, itu membuat daftar yang terdiri dari item iterable.
# #

# ─── Contoh 0 ───────────────────────────────────────────────────────────────────
text = 'Python'

# convert string to list
text_list = list(text)
print(text_list)

# check type of text_list
print(type(text_list))

# Output: ['P', 'y', 't', 'h', 'o', 'n']
#         <class 'list'>
# ────────────────────────────────────────────────────────────────────────────────

# ─── Contoh 1: Buat Daftar Dari String Tupel Dan Daftar ─────────────────────────
# empty list
print(list())  # Output:[]

# vowel string
vowel_string = 'aeiou'
print(list(vowel_string))  # Output:['a', 'e', ​​'i', 'o', 'u']

# vowel tuple
vowel_tuple = ('a', 'e', 'i', 'o', 'u')
print(list(vowel_tuple))  # Output: ['a', 'e', ​​'i', 'o', 'u']

# vowel list
vowel_list = ['a', 'e', 'i', 'o', 'u']
print(list(vowel_list))  # Output: ['a', 'e', 'i', 'o', 'u']
# ────────────────────────────────────────────────────────────────────────────────


# ─── Contoh 2: Buat Daftar Dari Set Dan Kamus ───────────────────────────────────
# vowel set
vowel_set = {'a', 'e', 'i', 'o', 'u'}
print(list(vowel_set))  # Output : ['a', 'o', 'u', 'e', 'i']

# vowel dictionary
vowel_dictionary = {'a': 1, 'e': 2, 'i': 3, 'o': 4, 'u': 5}
print(list(vowel_dictionary))  # Output :['o', 'e', 'a', 'u', 'i']

#!Catatan: Dalam kasus kamus, kunci kamus akan menjadi item dari daftar. Juga, urutan elemen akan acak.

# ────────────────────────────────────────────────────────────────────────────────

# ─── Contoh 3: Buat Daftar Dari Objek Iterator ──────────────────────────────────
# objects of this class are iterators


class PowTwo:
    def __init__(self, max):
        self.max = max

    def __iter__(self):
        self.num = 0
        return self

    def __next__(self):
        if(self.num >= self.max):
            raise StopIteration
        result = 2 ** self.num
        self.num += 1
        return result


pow_two = PowTwo(5)
pow_two_iter = iter(pow_two)

print(list(pow_two_iter))
# Output : [1, 2, 4, 8, 16]
# ────────────────────────────────────────────────────────────────────────────────
# ────────────────────────────────────────────────────────────────────────────────


# TODO ─── Penggunaan Fungsi Local ────────────────────────────────────────────────────
# Metode locals()mengembalikan kamus dengan semua variabel dan simbol lokal untuk program saat ini.
# Syntax : locals()
# Metode locals()ini tidak mengambil parameter apa pun.
# Metode locals()mengembalikan kamus tabel simbol lokal saat ini.
# #

# ─── Contoh 0 ───────────────────────────────────────────────────────────────────
print(locals())
# Output :
"""
{'In': ['', 'locals()'],
 ​​'Out': {},
 '_': '',
 '__': '',
 '___': '',
 '__builtin__':,
 ' __builtins__':,
 '__name__': '__main__',
 '_dh': ['/home/repl'],
 '_i': '',
 '_i1': 'locals()',
 '_ih': ['', 'locals()'],
 ​​'_ii': '',
 '_iii': '',
 '_oh': {},
 '_sh':,
 'exit':,
 'get_ipython': > ,
 'quit': }
"""
# ────────────────────────────────────────────────────────────────────────────────

# ─── Contoh 1 : Locals Python ───────────────────────────────────────────────────


class local:
    l = 50
    # locals inside a class
    print('\nlocals() value inside class\n', locals())


# Output :
# locals() value inside class
 #{'__module__': '__main__', '__qualname__': 'local', 'l': 50}
# ────────────────────────────────────────────────────────────────────────────────
"""
Kompiler Python memelihara tabel simbol yang berisi informasi yang diperlukan tentang program yang sedang ditulis. Ada dua jenis tabel simbol di Python - Lokal dan Global .

Tabel Simbol Lokal menyimpan semua informasi yang terkait dengan cakupan lokal program (di dalam kelas atau metode). Kita dapat mengakses tabel simbol ini dengan locals()metode.

Biasanya, pemrogram python menggunakan locals()metode untuk membatasi variabel dan metode apa pun di dalam lingkup metode atau kelas.

Dalam contoh di atas, kami memiliki kelas bernama local. Di sini, kami telah menggunakan metode locals() untuk mengembalikan variabel dan metode kelas ini.
"""

# ────────────────────────────────────────────────────────────────────────────────

# ─── Contoh 2: Locals Untuk Mengubah Nilai ──────────────────────────────────────


def localsPresent():
    present = True
    print(present)
    locals()['present'] = False
    print(present)


localsPresent()
# Output :
# Benar
# Benar
# ────────────────────────────────────────────────────────────────────────────────
""" 
Dalam contoh di atas, kami telah mengubah nilai presentvariabel di dalam fungsi localsPresentmenggunakan locals()metode.

Sejak locals()mengembalikan kamus, kami telah menggunakan metode dengan item kamus yaitu variabel yang ada dan mengubah nilainya menjadi False.
"""
# ────────────────────────────────────────────────────────────────────────────────
# ────────────────────────────────────────────────────────────────────────────────


# TODO ─── Penggunaan Fungsi Map ──────────────────────────────────────────────────────
# Fungsi tersebut map()menerapkan fungsi yang diberikan ke setiap item dari iterable (daftar, tuple, dll.) dan mengembalikan sebuah iterator.
# Syntax : map(function, iterable, ...)
# Fungsi map()ini mengambil dua parameter:
#   -function - fungsi yang melakukan beberapa tindakan untuk setiap elemen dari iterable
#   -iterable - iterable seperti set , list , tuple , dll
# You can pass more than one iterable to the map() function.
# Fungsi map()mengembalikan objek kelas peta. Nilai yang dikembalikan dapat diteruskan ke fungsi seperti
#   -list() - untuk mengonversi ke daftar
#   -set() - untuk mengonversi ke set, dan seterusnya.
# #

# ─── Contoh 0 ───────────────────────────────────────────────────────────────────
from xml.etree.ElementTree import XML


numbers = [2, 4, 6, 8, 10]

# returns square of a number


def square(number):
    return number * number


# apply square() function to each item of the numbers list
squared_numbers_iterator = map(square, numbers)

# converting to list
squared_numbers = list(squared_numbers_iterator)
print(squared_numbers)

# Output: [4, 16, 36, 64, 100]
# ────────────────────────────────────────────────────────────────────────────────

# ─── Contoh 1 : Cara Kerja Maps ─────────────────────────────────────────────────


def calculateSquare(n):
    return n*n


numbers = (1, 2, 3, 4)
result = map(calculateSquare, numbers)
print(result)

# converting map object to set
numbersSquare = set(result)
print(numbersSquare)
# Output :
# <map object at 0x000001B3EC6FBB80 >
#{16, 1, 4, 9}
# ?Dalam contoh di atas, setiap item dari tupel dikuadratkan.
# ────────────────────────────────────────────────────────────────────────────────
""" 
Karena map()mengharapkan suatu fungsi untuk diteruskan, fungsi lambda biasanya digunakan saat bekerja dengan map()fungsi.
Fungsi lambda adalah fungsi pendek tanpa nama. Kunjungi halaman ini untuk mempelajari lebih lanjut tentang Fungsi lambda Python .
"""
# ────────────────────────────────────────────────────────────────────────────────

# ─── Contoh 2: Bagaimana Cara Menggunakan Fungsi Lamda Dengan Map ───────────────
numbers = (1, 2, 3, 4)
result = map(lambda x: x*x, numbers)
print(result)

# converting map object to set
numbersSquare = set(result)
print(numbersSquare)
# Output :
# <map object at 0x000001B3EC6FBB80 >
#{16, 1, 4, 9}
# ────────────────────────────────────────────────────────────────────────────────
# ?sama kek contoh 1
# ────────────────────────────────────────────────────────────────────────────────

# ─── Contoh 3: Melewati Beberapa Iterator Ke Map Menggunakan Lambda ─────────────
num1 = [4, 5, 6]
num2 = [5, 6, 7]

result = map(lambda n1, n2: n1+n2, num1, num2)
print(list(result))
#Output : [9, 11, 13]
# ────────────────────────────────────────────────────────────────────────────────
# ────────────────────────────────────────────────────────────────────────────────


# TODO ─── Penggunaan Fungsi Map ──────────────────────────────────────────────────────
# Fungsi max()mengembalikan item terbesar dalam iterable. Ini juga dapat digunakan untuk menemukan item terbesar antara dua atau lebih parameter.
# Syntax : max(iterable, *iterables, key, default)
#! max()mengembalikan elemen terbesar dari iterable.
# ────────────────────────────────────────────────────────────────────────────────
# Fungsi max()memiliki dua bentuk:
# to find the largest item in an iterable
#! max(iterable, *iterables, key, default)

# to find the largest item between two or more objects
#! max(arg1, arg2, *args, key)
# ────────────────────────────────────────────────────────────────────────────────

# max() with iterable arguments
# maks() Parameter :
#   -iterable - sebuah iterable seperti daftar, tuple, set, kamus, dll.
#   -* iterables(opsional) - sejumlah iterables bisa lebih dari satu
#   -key(opsional) - fungsi kunci tempat iterable dilewatkan dan perbandingan dilakukan berdasarkan nilai pengembaliannya
#   -default(opsional) - nilai default jika iterable yang diberikan kosong


# ────────────────────────────────────────────────────────────────────────────────

# ? max() dengan argumen yang dapat diubah

#! max bentuk 1 : max(iterable, *iterables, key, default)
# ─── Contoh 0 ───────────────────────────────────────────────────────────────────
numbers = [9, 34, 11, -4, 27]

# find the maximum number
max_number = max(numbers)
print(max_number)

# Output: 34
# ────────────────────────────────────────────────────────────────────────────────

# ─── Contoh 1: Dapatkan Item Terbesar Dalam Daftar Atau List ────────────────────
number = [3, 2, 8, 5, 10, 6]
largest_number = max(number)

print("The largest number is:", largest_number)
# Output : Bilangan terbesar adalah: 10
# ────────────────────────────────────────────────────────────────────────────────
# ?Jika item dalam iterable adalah string, item terbesar (diurutkan berdasarkan abjad) dikembalikan.
# ────────────────────────────────────────────────────────────────────────────────


# ─── Contoh 2: String Terbesar Dalam Daftar ─────────────────────────────────────
languages = ["Python", "C Programming", "Java", "JavaScript"]
largest_string = max(languages)

print("The largest string is:", largest_string)
# Output :String terbesar adalah: Python
# ?Dalam kasus kamus, max()mengembalikan kunci terbesar. Mari kita gunakan keyparameter sehingga kita dapat menemukan kunci kamus yang memiliki nilai terbesar.
# ────────────────────────────────────────────────────────────────────────────────

# ─── Contoh 3: Max Dalam Kamus ──────────────────────────────────────────────────
square = {2: 4, -3: 9, -1: 1, -2: 4}

# the largest key
key1 = max(square)
print("The largest key:", key1)    # 2

# the key whose value is the largest
key2 = max(square, key=lambda k: square[k])

print("The key with the largest value:", key2)    # -3

# getting the largest value
print("The largest value:", square[key2])    # 9

# ────────────────────────────────────────────────────────────────────────────────

# kita telah melewatkan fungsi lambda ke keyparameter.
# key = lambda k: square[k]
# Fungsi mengembalikan nilai kamus. Berdasarkan nilai(bukan kunci kamus), kunci yang memiliki nilai maksimum dikembalikan.
""" 
Catatan:
Jika kita melewati iterator kosong, ValueErrorpengecualian dimunculkan. Untuk menghindarinya, kita bisa melewatibawaanparameter.
Jika kita melewati lebih dari satu iterator, item terbesar dari iterator yang diberikan akan dikembalikan.
"""

# ? max() tanpa iterable
#! max bentuk ke 2 : max(arg1, arg2, *args, key)
# Untuk menemukan objek terbesar di antara dua atau lebih parameter, kita dapat menggunakan sintaks ini:
# Syntax : max(arg1, arg2, *args, key)
# maks() parameter :
#   -arg1 - sebuah objek; dapat berupa angka, string, dll.
#   -arg2 - sebuah objek; dapat berupa angka, string, dll.
#   -*args (opsional) - sejumlah objek
#   -key (opsional) - fungsi kunci di mana setiap argumen dilewatkan, dan perbandingan dilakukan berdasarkan nilai kembaliannya
# Pada dasarnya, max()fungsi menemukan item terbesar di antara dua objek atau lebih.
# max()mengembalikan argumen terbesar di antara beberapa argumen yang diteruskan ke sana.
##

# ─── Contoh 4: Temukan Maksimum Di Antara Angka-angka Yang Diberikan ────────────
# find max among the arguments
result = max(4, -5, 23, 5)
print("The maximum number is:", result)
# Output : Jumlah maksimumnya adalah: 23
# ────────────────────────────────────────────────────────────────────────────────
# ────────────────────────────────────────────────────────────────────────────────


# TODO ─── Penggunaan Fungsi Memory View ──────────────────────────────────────────────
# Fungsi memoryview() mengembalikan objek tampilan memori dari argumen yang diberikan.
# Syntax : memoryview(obj)
# memoryview() Parameter :
#   -obj - objek yang data internalnya akan diekspos. objharus mendukung protokol buffer ( byte , bytearray )
# Fungsi memoryview()mengembalikan objek tampilan memori.
# #

# ?Sebelum kita masuk ke tampilan memori, kita harus terlebih dahulu memahami tentang protokol buffer Python.
""" 
Protokol Penyangga Python
Protokol buffer menyediakan cara untuk mengakses data internal suatu objek. Data internal ini adalah array memori atau buffer.
Protokol buffer memungkinkan satu objek untuk mengekspos data internal (buffer) dan yang lain untuk mengakses buffer tersebut tanpa penyalinan perantara.
Protokol ini hanya dapat diakses oleh kami di level C-API dan tidak menggunakan basis kode normal kami.
Jadi, untuk mengekspos protokol yang sama ke basis kode Python normal, tampilan memori hadir.
"""
# ────────────────────────────────────────────────────────────────────────────────

# ? ─── Apa Itu Tampilan Memori ───────────────────────────────────────────────────
"""
Tampilan memori adalah cara aman untuk mengekspos protokol buffer dengan Python.
Ini memungkinkan Anda untuk mengakses buffer internal suatu objek dengan membuat objek tampilan memori.
"""
# ────────────────────────────────────────────────────────────────────────────────
# ?Mengapa protokol buffer dan tampilan memori penting?
""" 
Kita perlu ingat bahwa setiap kali kita melakukan beberapa tindakan pada suatu objek (panggil fungsi suatu objek, iris array), Python perlu membuat salinan objek tersebut .
Jika kita memiliki data besar untuk digunakan (misalnya, data biner dari suatu gambar), kita tidak perlu membuat salinan potongan data yang sangat besar, yang hampir tidak berguna.
Dengan menggunakan protokol buffer, kita dapat memberikan akses objek lain untuk menggunakan/memodifikasi data besar tanpa menyalinnya. Ini membuat program menggunakan lebih sedikit memori dan meningkatkan kecepatan eksekusi.
"""
# ────────────────────────────────────────────────────────────────────────────────

# Syntax : memoryview(obj)

# ────────────────────────────────────────────────────────────────────────────────


# ─── Contoh 1: Bagaimana Memoryview Bekerja Dengan Python ───────────────────────
# random bytearray
random_byte_array = bytearray('ABC', 'utf-8')

mv = memoryview(random_byte_array)

# access memory view's zeroth index
print(mv[0])  # Output :65

# create byte from memory view
print(bytes(mv[0:2]))  # Output :b'AB'

# create list from memory view
print(list(mv[0:3]))  # Output :[65, 66, 67]
# ────────────────────────────────────────────────────────────────────────────────
""" 
Di sini, kami membuat objek tampilan memorimvdari array byterandom_byte_array.
Kemudian, kami mengaksesmv's 0th index, 'A', dan mencetaknya (yang memberikan nilai ASCII - 65).
Sekali lagi, kami mengaksesmvdari 0 dan 1, 'AB', dan mengubahnya menjadi byte.
Akhirnya, kami mengakses semua indeksmvdan mengubahnya menjadi daftar. Karena secara internal bytearraymenyimpan nilai ASCII untuk alfabet, outputnya adalah daftar nilai ASCII dariSEBUAH,B,danC.
"""
# ────────────────────────────────────────────────────────────────────────────────

# ─── Contoh 2: Ubah Data Internal Menggunakan Tampilan Memori ───────────────────
# random bytearray
random_byte_array = bytearray('ABC', 'utf-8')
print('Before updation:', random_byte_array)
# Output : Sebelum pembaruan: bytearray(b'ABC')

mv = memoryview(random_byte_array)

# update 1st index of mv to Z
mv[1] = 90
print('After updation:', random_byte_array)
# Output :Setelah pembaruan: bytearray(b'AZC')
# ────────────────────────────────────────────────────────────────────────────────
""" 
Di sini, kami memperbarui indeks pertama tampilan memori menjadi 90, nilai ASCII dari Z.
Karena, objek tampilan memorimvreferensi buffer/memori yang sama, memperbarui indeks dimvjuga updaterandom_byte_array.
"""
# ────────────────────────────────────────────────────────────────────────────────
# ────────────────────────────────────────────────────────────────────────────────


# TODO ─── Penggunaan Fungsi Min ──────────────────────────────────────────────────────
# Fungsi min()mengembalikan item terkecil dalam iterable. Ini juga dapat digunakan untuk menemukan item terkecil di antara dua atau lebih parameter.
# Syntax :
# #

# ────────────────────────────────────────────────────────────────────────────────
#!Fungsi min()memiliki dua bentuk:
# ? to find the smallest item in an iterable
# min(iterable, *iterables, key, default)
# ?to find the smallest item between two or more objects
# min(arg1, arg2, *args, key)
# ────────────────────────────────────────────────────────────────────────────────

#?1. min() dengan argumen yang dapat diubah
# Syntax : min(iterable, *iterables, key, default)
#min() Parameter : 
#   -iterable - sebuah iterable seperti daftar, tuple, set, kamus, dll.
#   -* iterables (opsional) - sejumlah iterables; bisa lebih dari satu
#   -key (opsional) - fungsi kunci tempat iterable dilewatkan dan perbandingan dilakukan berdasarkan nilai pengembaliannya
#   -default (opsional) - nilai default jika iterable yang diberikan kosong
# min()mengembalikan elemen terkecil dari iterable.
# #

# ─── Contoh - 0 ─────────────────────────────────────────────────────────────────
numbers = [9, 34, 11, -4, 27]

# find the smallest number
min_number = min(numbers)
print(min_number)

# Output: -4
# ────────────────────────────────────────────────────────────────────────────────

# ─── Contoh 1.1 ─────────────────────────────────────────────────────────────────
number = [3, 2, 8, 5, 10, 6]
smallest_number = min(number)

print("The smallest number is:", smallest_number)
#Output : Bilangan terkecil adalah: 2
# ────────────────────────────────────────────────────────────────────────────────

#?Jika item dalam iterable adalah string, item terkecil (diurutkan berdasarkan abjad) dikembalikan.
# ─── Contoh 1.2 Min Dengan String ───────────────────────────────────────────────
languages = ["Python", "C Programming", "Java", "JavaScript"]
smallest_string = min(languages)

print("The smallest string is:", smallest_string)
#Output : String terkecil adalah: Pemrograman C
# ────────────────────────────────────────────────────────────────────────────────

#?Dalam kasus kamus, min()mengembalikan kunci terkecil. Mari kita gunakan keyparameter sehingga kita dapat menemukan kunci kamus yang memiliki nilai terkecil.
# ─── Contoh 1.3 Min Dalam Kamus ─────────────────────────────────────────────────
square = {2: 4, 3: 9, -1: 1, -2: 4}

# the smallest key
key1 = min(square)
print("The smallest key:", key1)    # -2

# the key whose value is the smallest
key2 = min(square, key=lambda k: square[k])

print("The key with the smallest value:", key2)    # -1

# getting the smallest value
print("The smallest value:", square[key2])    # 1
# ────────────────────────────────────────────────────────────────────────────────

# ────────────────────────────────────────────────────────────────────────────────
#!Pada min()fungsi kedua, kita telah melewatkan fungsi lambda ke keyparameter.
# key = lambda k: square[k]
#Fungsi mengembalikan nilai kamus. Berdasarkan nilai (bukan kunci kamus), kunci yang memiliki nilai minimum dihitung.
""" 
Beberapa Catatan:

Jika kita melewati iterator kosong, ValueErrorpengecualian dimunculkan. Untuk menghindarinya, kita bisa melewatibawaanparameter.
Jika kita melewati lebih dari satu iterator, item terkecil dari iterator yang diberikan akan dikembalikan.
"""
# ────────────────────────────────────────────────────────────────────────────────

#! min tanpa iterable
#Syntax : min(arg1, arg2, *args, key)
# min() Parameter :
#   -arg1 - sebuah objek; dapat berupa angka, string, dll.
#   -arg2 - sebuah objek; dapat berupa angka, string, dll.
#   -*args (opsional) - sejumlah objek
#   -key (opsional) - fungsi kunci di mana setiap argumen dilewatkan, dan perbandingan dilakukan berdasarkan nilai kembaliannya
# Pada dasarnya, min()fungsi dapat menemukan item terkecil di antara dua objek atau lebih.
# min()mengembalikan argumen terkecil di antara beberapa argumen yang diteruskan ke sana.
# #

# ─── Contoh 4: Temukan Minimum Di Antara Angka-angka Yang Diberikan ─────────────
result = min(4, -5, 23, 5)
print("The minimum number is:", result)
# ouput : Jumlah minimumnya adalah -5
# ────────────────────────────────────────────────────────────────────────────────

# TODO ─── Penggunaan Fungsi Next ─────────────────────────────────────────────────────
# Itu next() mengembalikan item berikutnya dari iterator.
# Syntax : next(iterator, default)
# next() Parameter
#   -iteratornext()iterator
#   -default (optional) - this value is returned if the iterator is exhausted (there is no next item)
# next() Return Value
#   -Fungsi next()mengembalikan item berikutnya dari iterator.
#   -Jika iterator habis, ia mengembalikan defaultnilai yang diteruskan sebagai argumen.
#   -If the default parameter is omitted and the iterator is exhausted, it raises the StopIteration exception.
# #

# ─── Contoh 0 ───────────────────────────────────────────────────────────────────
marks = [65, 71, 68, 74, 61]

# convert list to iterator
iterator_marks = iter(marks)

# the next element is the first element
marks_1 = next(iterator_marks)
print(marks_1)

# find the next element which is the second element
marks_2 = next(iterator_marks)
print(marks_2)

# Output: 65
#         71
# ────────────────────────────────────────────────────────────────────────────────

# ─── Contoh 1: Dapatkan Item Berikutnya ─────────────────────────────────────────
random = [5, 9, 'cat']

# converting the list to an iterator
random_iterator = iter(random)
print(random_iterator)

# Output: 5
print(next(random_iterator))

# Output: 9
print(next(random_iterator))

# Output: 'cat'
print(next(random_iterator))

# This will raise Error
# iterator is exhausted
print(next(random_iterator))
"""
Output : 
<list_iterator objek di 0x7feb49032b00> 
5 
9 
cat 
Traceback (panggilan terakhir terakhir): 
  File "python", baris 18, di <module> 
StopIteration
"""
# ────────────────────────────────────────────────────────────────────────────────
""" 
Daftar adalah iterable dan Anda bisa mendapatkan iteratornya darinya dengan menggunakan iter()fungsi di Python.
Kami mendapatkan kesalahan dari pernyataan terakhir dalam program di atas karena kami mencoba untuk mendapatkan item berikutnya ketika tidak ada item berikutnya yang tersedia (iterator habis).
Dalam kasus seperti itu, Anda dapat memberikanbawaannilai sebagai parameter kedua.
"""
# ────────────────────────────────────────────────────────────────────────────────

# ─── Contoh 2: Melewati Nilai Default Ke Next ───────────────────────────────────
random = [5, 9]

# converting the list to an iterator
random_iterator = iter(random)

# Output: 5
print(next(random_iterator, '-1'))

# Output: 9
print(next(random_iterator, '-1'))

# random_iterator is exhausted
# Output: '-1'
print(next(random_iterator, '-1'))
print(next(random_iterator, '-1'))
print(next(random_iterator, '-1'))

# ────────────────────────────────────────────────────────────────────────────────
# ────────────────────────────────────────────────────────────────────────────────

