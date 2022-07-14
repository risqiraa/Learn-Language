#TODO ─── Penggunaan Fungsi Frozenset ────────────────────────────────────────────────
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
