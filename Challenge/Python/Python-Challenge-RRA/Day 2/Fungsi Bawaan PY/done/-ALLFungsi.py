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