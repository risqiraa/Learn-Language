# TODO ─── Penggunaan Fungsi Id ───────────────────────────────────────────────────────
# Metode id()ini mengembalikan bilangan bulat unik (identitas) dari objek argumen yang diteruskan.
# Sintaks dari id()metode ini adalah: id(object)
# Metode id()ini mengambil satu parameter:
#   -obyek- dapat berupa kelas, variabel, daftar, tupel, set, dll.
# Metode id()mengembalikan:
#   -identitas objek (yang merupakan bilangan bulat unik untuk objek tertentu)
# #

# ─── Contoh 0 ───────────────────────────────────────────────────────────────────
a = 5
b = 6
sum = a + b

# id of sum variable
print("The id of sum is", id(sum))
# Output: The id of sum is 1877287371312
# ────────────────────────────────────────────────────────────────────────────────


# ─── Contoh 1 : Python Id ───────────────────────────────────────────────────────
# id of 5
print("id of 5 =", id(5))
# Output: id of 5 = 2037968011632

a = 5
# id of a
print("id of a =", id(a))
# Output: id of a = 2037968011632

b = a
# id of b
print("id of b =", id(b))
# Output: id of b = 2037968011632

c = 5.0
# id of c
print("id of c =", id(c))
# Output: id of c = 2037968011632
# ────────────────────────────────────────────────────────────────────────────────
"""
Di sini, id()metode mengembalikan nomor integer unik untuk setiap nilai unik yang digunakannya.
Dalam contoh di atas, kami telah menggunakan id()metode dengan variabe a,b dan c dan mendapatkan id yang sesuai.
Seperti yang Anda lihat, id()metode ini mengembalikan bilangan bulat 2037968011632 untuk keduanya a = 5 dan 5.0
Karena kedua nilainya sama, idnya juga sama.
#!Catatan : Karena ID adalah alamat memori yang ditetapkan, ID dapat berbeda di sistem yang berbeda. Jadi, output pada sistem Anda bisa berbeda.
"""

# ─── Contoh 2 : Id dengan kelas dan object ──────────────────────────────────────


class Food:
    banana = 15


dummyFood = Food()

#  id of the object dummyFood
print("id of dummyFoo =", id(dummyFood))
# Output : id of dummyFoo = 3074880666976
# ?Ketika kita menggunakan id()metode dengan dummyFoodobjek, kita mendapatkan hasil 139984002204864 .
# ────────────────────────────────────────────────────────────────────────────────

# ─── Contoh 3: Id Dengan Set ────────────────────────────────────────────────────

fruits = {"apple", "banana", "cherry", "date"}

# id() of the set fruits
print("The id of the fruits set is", id(fruits))
# Output : The id of the fruits set is 1969766393088
# ? Dalam contoh di atas, kami telah menggunakan id()metode dengan set fruit. Dalam hal ini, kami mendapatkan nomor unik sebagai id untuk set- 140533973276928 .
# ────────────────────────────────────────────────────────────────────────────────

# ─── Contoh 4 : Id Dengan Tuples ────────────────────────────────────────────────
vegetables = ("asparagus", "basil", "cabbage")

# id() with vegetable
print("The id of the vegetables set is", id(vegetables))
# The id of the vegetables set is 2283407349376
# ? Metode id()mengembalikan nomor unik 139751433263360 sebagai id dari tuple vegetable.
# ────────────────────────────────────────────────────────────────────────────────
# ────────────────────────────────────────────────────────────────────────────────
