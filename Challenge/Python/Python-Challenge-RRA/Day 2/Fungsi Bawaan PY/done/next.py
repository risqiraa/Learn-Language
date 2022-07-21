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
