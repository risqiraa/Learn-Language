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
