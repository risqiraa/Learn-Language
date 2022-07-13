# TODO ─── Penggunaan Fungsi Complex ──────────────────────────────────────────────────
# Fungsi complex() mengembalikan bilangan kompleks dari argumen riil dan imajiner yang diberikan.
# Syntax : complex([real[, imag])
# Fungsi complex() memiliki dua parameter yaitu:
#   real – bagian real dari bilangan. Bila tidak dimasukkan, defaultnya 0
#   imag – bagian imajiner dari bilangan. Bila tidak dimasukkan, defaultnya 0
# ungsi complex() mengembalikan bilangan dalam bentuk bilangan kompleks yaitu dalam format real+imagj
# #

z = complex(3, 3)
print(z)  # (3+3j)

z = complex(2)
print(z)  # (2+0j)

z = complex()
print(z)  # (0j)

z = complex('5-9j')
print(z)  # (5-9j)

# ────────────────────────────────────────────────────────────────────────────────
# ────────────────────────────────────────────────────────────────────────────────

a = 2+3j
print('a =', a)  # 2+3j
print('Type of a is', type(a))  # Type of a is <class 'complex'>

b = -2j
print('b =', b)  # -0-2j
print('Type of b is', type(a))  # Type of b is <class 'complex'>

c = -1+2j
print('c =', c)  # -1+2j
print('Type of c is', type(c))  # Type of c is <class 'complex'>

d = 2j
print('d =', d)  # 2j
print('Type of c is', type(d))  # Type of d is <class 'complex'>

# ────────────────────────────────────────────────────────────────────────────────
# ────────────────────────────────────────────────────────────────────────────────
