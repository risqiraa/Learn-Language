#TODO ─── Penggunaan Fungsi Bytearray ────────────────────────────────────────────────
# Fungsi bytearray() mengembalikan objek bytearray dari suatu objek
# Syntax : bytearray([source[, encoding[, errors]]]
# source – objek yang akan diubah jadi byte array
# encoding – encoding string bila sourcenya adalah string
# errors – aksi yang dilakukan bila proses encoding gagal
# Fungsi bytearray() mengembalikan byte array berdasarkan inisialisasi panjang
# dan ukuran awal objek.
#
# String : Mengubah string menjadi byte menggunakan str.encode(),
# bisa juga menggunakan opsi encoding dan opsi errors
#
# Integer : Menciptakan array dengan ukuran tertentu, semuanya diinisialisasi dengan null
#
# Object : Buffer read-only dari objek yang digunakan untuk menginisialisai byte array
#
# Iterable : Menciptakan array dengan ukuran yang sama dengan panjang iterable dan mengisialisasinya menjadi anggota – anggota iterable.
# Harus berisi iterable dari integer antara 0 <= x < 256
#
# Kosong : Menciptakan array berukuran 0
# #


# string
s = "Python is fun"
arr = bytearray(s, 'utf-8')
print(arr)  # bytearray(b'Python is fun')

# integer
# Menciptakan array dengan ukuran tertentu, semuanya diinisialisasi dengan null
size = 9
arr = bytearray(size)
print(arr)  # bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00')

# list
# Menciptakan array dengan ukuran yang sama dengan panjang iterable dan mengisialisasinya menjadi anggota – anggota iterable.
# Harus berisi iterable dari integer antara 0 <= x < 256
l = {1, 2, 3, 4, 5, 6}
arr = bytearray(l)
print(arr)  # bytearray(b'\x01\x02\x03\x04\x05\x06')

# ────────────────────────────────────────────────────────────────────────────────
