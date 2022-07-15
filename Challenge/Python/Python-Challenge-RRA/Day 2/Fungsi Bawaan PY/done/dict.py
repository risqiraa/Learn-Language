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
