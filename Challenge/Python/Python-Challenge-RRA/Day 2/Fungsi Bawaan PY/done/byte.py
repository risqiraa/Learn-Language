#TODO ─── Penggunaan Fungsi Bytes ────────────────────────────────────────────────────
# Fungsi bytes() mengembalikan objek byte yang bersifat immutable dari suatu objek
# Syntax : bytes([source[, encoding[, errors]]]
# source – objek yang akan diubah jadi byte array
# encoding – encoding string bila sourcenya adalah string
# errors – aksi yang dilakukan bila proses encoding gagal
# Fungsi bytes() mengembalikan byte berdasarkan inisialisasi panjang dan ukuran awal objek.
# #


# string
s = "Python is fun"
arr = bytes(s, 'utf-8')
print(arr)  # b'Python is fun

# integer
size = 5
arr = bytes(size)
print(arr)  # b'\x00\x00\x00\x00\x00'

# list
l = [1, 2, 3, 4, 5]
arr = bytes(l)
print(arr)  # b'\x01\x02\x03\x04\x05'

# ────────────────────────────────────────────────────────────────────────────────
