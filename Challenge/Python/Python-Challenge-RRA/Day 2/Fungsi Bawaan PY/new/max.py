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
