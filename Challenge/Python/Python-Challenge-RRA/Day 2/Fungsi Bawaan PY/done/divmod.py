# TODO ─── Penggunaan Fungsi Divmod ───────────────────────────────────────────────────
# Metode divmod()ini mengambil dua angka sebagai argumen dan mengembalikan hasil bagi dan sisanya dalam sebuah tupel.
# Syntax : divmod(number1, number2)
# Metode divmod()ini mengambil dua parameter:
#   -number1 - pembilang, bisa berupa bilangan bulat atau bilangan floating point
#   -number2 - penyebut, bisa berupa bilangan bulat atau bilangan floating point
# Metode divmod()mengembalikan:
#   -(quotient, remainder)- Tuple yang berisi hasil bagi dan sisa pembagian
#   -TypeError - untuk argumen non-numerik
# #

# ─── Contoh 0 ───────────────────────────────────────────────────────────────────
# returns the quotient and remainder of 8/3
result = divmod(8, 3)

print('Quotient and Remainder = ', result)

# Output: Quotient and Remainder =  (2, 2)

# ────────────────────────────────────────────────────────────────────────────────

# ─── Contoh 1 : Python divmod() dengan Argumen Integer ──────────────────────────
# divmod() with integer arguments
print('divmod(8, 3) = ', divmod(8, 3))
# Output : divmod(8, 3) =  (2, 2)

# divmod() with integer arguments
print('divmod(3, 8) = ', divmod(3, 8))
# Output : divmod(3, 8) =  (0, 3)

# divmod() with integer arguments
print('divmod(5, 5) = ', divmod(5, 5))
# Output : divmod(5, 5) =  (1, 0)

# ────────────────────────────────────────────────────────────────────────────────

# ─── Contoh 2: Python divmod() dengan Float Arguments ───────────────────────────
# divmod() with float arguments
print('divmod(8.0, 3) = ', divmod(8.0, 3))
# Output : divmod(8.0, 3) =  (2.0, 2.0)

# divmod() with float arguments
print('divmod(3, 8.0) = ', divmod(3, 8.0))
# Output : divmod(3, 8.0) =  (0.0, 3.0)

# divmod() with float arguments
print('divmod(7.5, 2.5) = ', divmod(7.5, 2.5))
# Output : divmod(7.5, 2.5) =  (3.0, 0.0)

# divmod() with float arguments
print('divmod(2.6, 0.5) = ', divmod(2.6, 0.5))
# Output : divmod(2.6, 0.5) =  (5.0, 0.10000000000000009)

# ────────────────────────────────────────────────────────────────────────────────
