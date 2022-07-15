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
