# ─── Penggunaan Fungsi Filter ───────────────────────────────────────────────────
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
