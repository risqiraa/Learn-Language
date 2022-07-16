# TODO ─── Penggunaan Fungs Int ───────────────────────────────────────────────────────
# Metode int()ini mengonversi string apa pun, objek seperti byte, atau angka menjadi bilangan bulat dan kembali.
# Syntax : int(value, base [optional])
# int()metode membutuhkan dua parameter:
#   -nilai- string numerik, objek seperti byte atau angka apa pun
#   -dasar [opsional]- sistem angka tempat nilainya saat ini
# Metode int()mengembalikan:
#   -bagian integer dari nomor - untuk nilai argumen tunggal (nomor apa saja)
#   -0 - tanpa argumen
#   -representasi bilangan bulat dari angka dengan basis yang diberikan (0, 2 ,8 ,10,16)
# #

# ─── Contoh 0 ───────────────────────────────────────────────────────────────────
# returns the integer representation of the binary string 1010
print("For 1010, int is:", int("1010", 2))

# Output: For 1010, int is: 10
# ────────────────────────────────────────────────────────────────────────────────

# ─── Contoh 1 : Python int Argumen Tunggal ──────────────────────────────────────

# int() with an integer value
print("int(123) is:", int(123))
# Output: int(123) is: 123

# int() with a floating point value
print("int(123.23) is:", int(123.23))
# Output: int(123.23) is: 123

# int() with a numeric-string value
print("int('123') is:", int("123"))
# Output: int('123') is: 123

# ────────────────────────────────────────────────────────────────────────────────

# ─── Contoh 2 : Python Int Dua Argumen ──────────────────────────────────────────
# converting a binary to integer with int()
print("For 0b101, int is:", int("0b101", 2))
# Output: For 0b101, int is: 5

# converting a binary to integer with int())
print("For 0o16, int is:", int("0o16", 8))
# Output: For 0o16, int is: 14


# converting a binary to integer with int()
print("For 0xA, int is:", int("0xA", 16))
# Output: For 0xA, int is: 10

# ────────────────────────────────────────────────────────────────────────────────

# ─── Contoh 3: Int Untuk Objek Khusus ───────────────────────────────────────────
"""
Bahkan jika suatu objek bukan angka, kita masih dapat mengubahnya menjadi objek integer.
Kita dapat melakukan ini dengan mudah dengan mengganti __index__()dan __int__()metode kelas untuk mengembalikan angka.
Kedua metode itu identik. Versi Python yang lebih baru menggunakan __index__()metode ini.
"""


class Person:
    age = 23

    def __index__(self):
        return self.age

    # def __int__(self):
    #     return self.age


person = Person()

# int() method with a non integer object person
print("int(person) is:", int(person))
# Output: int(person) is: 23


# ────────────────────────────────────────────────────────────────────────────────
"""
Dalam contoh di atas, kelasnya Personbukan tipe integer.
Tapi kita masih bisa mengembalikanusiavariabel (yang merupakan bilangan bulat) menggunakan int()metode.
"""

# ────────────────────────────────────────────────────────────────────────────────
# ────────────────────────────────────────────────────────────────────────────────
