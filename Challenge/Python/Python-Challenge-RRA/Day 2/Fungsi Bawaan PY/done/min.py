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





