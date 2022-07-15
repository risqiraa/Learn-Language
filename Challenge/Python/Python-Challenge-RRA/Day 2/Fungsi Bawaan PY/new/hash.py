# ─── Penggunaan Fugnsi Hash ─────────────────────────────────────────────────────
# Metode hash()mengembalikan nilai hash suatu objek jika memilikinya.
# Nilai hash hanyalah bilangan bulat yang digunakan untuk membandingkan kunci kamus
# selama kamus terlihat dengan cepat.
#
# Syntax : hash(object)
# Metode hash()ini mengambil satu parameter:
#   -objek - objek yang nilai hashnya akan dikembalikan (integer, string, float)
# Metode hash()mengembalikan nilai hash dari suatu objek.
# #

# ─── Contoh 0 ───────────────────────────────────────────────────────────────────
text = 'Python Programming'

# compute the hash value of text
hash_value = hash(text)
print(hash_value)

# Output: -966697084172663693

# ────────────────────────────────────────────────────────────────────────────────

# ─── Contoh 1: Bagaimana Hash Bekerja Dengan Python ─────────────────────────────
# hash for integer unchanged
print('Hash for 181 is:', hash(181))
# Ouput : Hash untuk 181 adalah: 181

# hash for decimal
print('Hash for 181.23 is:', hash(181.23))
# Ouput : Hash untuk 181,23 adalah: 530343892119126197

# hash for string
print('Hash for Python is:', hash('Python'))
# Ouput : Hash untuk Python adalah: 2230730083538390373

# ────────────────────────────────────────────────────────────────────────────────

# ─── Contoh 2: Hash Untuk Objek Tuple Yang Tidak Dapat Diubah ───────────────────
# hash()metode hanya berfungsi untuk objek yang tidak dapat diubah sebagai Tuple .
# #

# tuple of vowels
vowels = ('a', 'e', 'i', 'o', 'u')

print('The hash is:', hash(vowels))
# Ouput : The hash is: -695778075465126279

# ────────────────────────────────────────────────────────────────────────────────
# ────────────────────────────────────────────────────────────────────────────────

# ─── Contoh 3: Hash Untuk Objek Kustom Dengan Mengganti __hash__ ────────────────


class Person:
    def __init__(self, age, name):
        self.age = age
        self.name = name

    def __eq__(self, other):
        return self.age == other.age and self.name == other.name

    def __hash__(self):
        print('The hash is:')
        return hash((self.age, self.name))


person = Person(23, 'Adam')
print(hash(person))

#Output : Hashnya adalah: 3785419240612877014
#! Catatan: Anda tidak harus mengimplementasikan __eq__()metode untuk hash karena metode ini dibuat secara default untuk semua objek.

# ────────────────────────────────────────────────────────────────────────────────
# ────────────────────────────────────────────────────────────────────────────────
