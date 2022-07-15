# ─── Penggunaan Fungsi Help ─────────────────────────────────────────────────────
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

from math import *
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
