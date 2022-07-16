# TODO ─── Penggunaan Fungsi Input ────────────────────────────────────────────────────
# Fungsi input()mengambil input dari pengguna dan mengembalikannya.
# Syntax : input([prompt])
# Fungsi input()mengambil satu argumen opsional:
#   -prompt (Opsional) - string yang ditulis ke output standar (biasanya layar) tanpa mengikuti baris baru
# Fungsi input()membaca baris dari input (biasanya dari pengguna), mengubah baris menjadi string dengan menghapus baris baru yang tertinggal, dan mengembalikannya.
# Jika EOF dibaca, itu menimbulkan EOFErrorpengecualian.
# #


# ─── Contoh 0 ───────────────────────────────────────────────────────────────────
name = input("Enter your name: ")
print(name)

# Output:
# Enter your name: James
# James

# ────────────────────────────────────────────────────────────────────────────────

# ─── Contoh 1 Bagaimana Input Bekerja Dengan Python ─────────────────────────────
# get input from user

inputString = input()

print('The inputted string is:', inputString)
# Output : The inputted string is: Risqi
# Risqi
# ────────────────────────────────────────────────────────────────────────────────

# ─── Contoh 2: Dapatkan Masukan Dari Pengguna Dengan Prompt ─────────────────────
# get input from user

inputString = input('Enter a string:')

print('The inputted string is:', inputString)
# Output : Enter a string : risqi
# The inputted string is: risqi
# ────────────────────────────────────────────────────────────────────────────────
