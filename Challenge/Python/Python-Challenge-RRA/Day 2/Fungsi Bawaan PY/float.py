# ─── Penggunaan Fungsi float ────────────────────────────────────────────────────
# Metode float()mengembalikan angka floating point dari angka atau string.
# Syntax : float([x])
# Metode float()ini mengambil satu parameter:
#   x (Opsional) - angka atau string yang perlu dikonversi ke angka floating point Jika string, string harus berisi titik desimal
# Metode float()mengembalikan:
#   -Angka floating point yang setara jika argumen dilewatkan
#   -0.0 jika tidak ada argumen yang lolos
#   -OverflowErrorpengecualian jika argumen berada di luar kisaran float Python
# #

# ─── Contoh 1: Bagaimana Float Bekerja Dengan Python ────────────────────────────
# for integers
print(float(10))  # Output : 10.0

# for floats
print(float(11.22))  # Output : 11.22

# for string floats
print(float("-13.33"))  # Output : -13.33

# for string floats with whitespaces
print(float("     -24.45\n"))  # Output : -24.45

# string float error
print(float("abc"))  # Output : ValueError: could not convert string to float: 'abc'

# ────────────────────────────────────────────────────────────────────────────────

# ─── Example 2: Float For Infinity And Not A Number ─────────────────────────────
# for NaN
print(float("nan"))  # Output : nan
print(float("NaN"))  # Output : nan

# for inf/infinity
print(float("inf"))  # Output : inf
print(float("InF"))  # Output : inf
print(float("InFiNiTy"))  # Output : inf
print(float("infinity"))  # Output : inf
print(float("inFinIty"))  # Output : inf
# ────────────────────────────────────────────────────────────────────────────────

