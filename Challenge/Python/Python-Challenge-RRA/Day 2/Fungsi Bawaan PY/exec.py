# ─── Penggunaan Fungsi Exec ─────────────────────────────────────────────────────
# Metode exec()mengeksekusi program yang dibuat secara dinamis, yang berupa string atau objek kode.
# Syntax : exec(object, globals, locals)
# The exec() method takes three parameters:
# objek - Baik string atau objek kode
# global (opsional) - kamus
# locals (opsional) - objek pemetaan (biasanya kamus)
# Metode exec()tidak mengembalikan nilai apa pun.
# #

# ─── Contoh 0 ───────────────────────────────────────────────────────────────────
program = 'a = 5\nb=10\nprint("Sum =", a+b)'
exec(program)

# Output: Sum = 15
# ────────────────────────────────────────────────────────────────────────────────

# ─── Contoh 1: Python Exec ──────────────────────────────────────────────────────
program = 'a = 5\nb=10\nprint("Sum =", a+b)'
exec(program)
# ────────────────────────────────────────────────────────────────────────────────
"""
Dalam contoh di atas, kita telah melewati objek stringprogramke exec()metode.
Metode mengeksekusi kode python di dalam metode objek dan menghasilkan output Sum = 15 .
"""
# ────────────────────────────────────────────────────────────────────────────────

# ─── Contoh 2: Exec Dengan Input Program Baris Tunggal ──────────────────────────
# get an entire program as input
program = input('Enter a program:')

# execute the program
exec(program)
# ────────────────────────────────────────────────────────────────────────────────



