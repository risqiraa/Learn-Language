# TODO ─── Penggunaan Fungsi Local ────────────────────────────────────────────────────
# Metode locals()mengembalikan kamus dengan semua variabel dan simbol lokal untuk program saat ini.
# Syntax : locals()
# Metode locals()ini tidak mengambil parameter apa pun.
# Metode locals()mengembalikan kamus tabel simbol lokal saat ini.
# #

# ─── Contoh 0 ───────────────────────────────────────────────────────────────────
print(locals())
# Output :
"""
{'In': ['', 'locals()'],
 ​​'Out': {},
 '_': '',
 '__': '',
 '___': '',
 '__builtin__':,
 ' __builtins__':,
 '__name__': '__main__',
 '_dh': ['/home/repl'],
 '_i': '',
 '_i1': 'locals()',
 '_ih': ['', 'locals()'],
 ​​'_ii': '',
 '_iii': '',
 '_oh': {},
 '_sh':,
 'exit':,
 'get_ipython': > ,
 'quit': }
"""
# ────────────────────────────────────────────────────────────────────────────────

# ─── Contoh 1 : Locals Python ───────────────────────────────────────────────────


class local:
    l = 50
    # locals inside a class
    print('\nlocals() value inside class\n', locals())


# Output :
# locals() value inside class
 #{'__module__': '__main__', '__qualname__': 'local', 'l': 50}
# ────────────────────────────────────────────────────────────────────────────────
"""
Kompiler Python memelihara tabel simbol yang berisi informasi yang diperlukan tentang program yang sedang ditulis. Ada dua jenis tabel simbol di Python - Lokal dan Global .

Tabel Simbol Lokal menyimpan semua informasi yang terkait dengan cakupan lokal program (di dalam kelas atau metode). Kita dapat mengakses tabel simbol ini dengan locals()metode.

Biasanya, pemrogram python menggunakan locals()metode untuk membatasi variabel dan metode apa pun di dalam lingkup metode atau kelas.

Dalam contoh di atas, kami memiliki kelas bernama local. Di sini, kami telah menggunakan metode locals() untuk mengembalikan variabel dan metode kelas ini.
"""

# ────────────────────────────────────────────────────────────────────────────────

# ─── Contoh 2: Locals Untuk Mengubah Nilai ──────────────────────────────────────


def localsPresent():
    present = True
    print(present)
    locals()['present'] = False
    print(present)


localsPresent()
# Output :
# Benar
# Benar
# ────────────────────────────────────────────────────────────────────────────────
""" 
Dalam contoh di atas, kami telah mengubah nilai presentvariabel di dalam fungsi localsPresentmenggunakan locals()metode.

Sejak locals()mengembalikan kamus, kami telah menggunakan metode dengan item kamus yaitu variabel yang ada dan mengubah nilainya menjadi False.
"""
# ────────────────────────────────────────────────────────────────────────────────
# ────────────────────────────────────────────────────────────────────────────────
