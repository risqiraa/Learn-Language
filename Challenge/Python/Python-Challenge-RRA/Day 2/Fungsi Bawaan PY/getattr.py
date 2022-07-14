# ─── Penggunaan Fungsi Getattr ──────────────────────────────────────────────────
# Metode getattr()mengembalikan nilai atribut bernama dari suatu objek. Jika tidak ditemukan,
# itu mengembalikan nilai default yang diberikan ke fungsi.
# Syntax : getattr(object, name[, default])
# syntax is equivalent to: object.name
# getattr()metode membutuhkan beberapa parameter:
# objek - objek yang nilai atributnya akan dikembalikan
# name - string yang berisi nama atribut
# default (Opsional) - nilai yang dikembalikan ketika atribut bernama tidak ditemukan
#
# getattr()metode kembali:
#   -nilai atribut bernama dari objek yang diberikan
#   -default, jika tidak ada atribut bernama yang ditemukan
#   -AttributeErrorpengecualian, jika atribut bernama tidak ditemukan dan defaulttidak didefinisikan
# #


# ─── Contoh 1: Bagaimana Getattr Bekerja Dengan Python ──────────────────────────
class Person:
    age = 23
    name = "Adam"


person = Person()
print('The age is:', getattr(person, "age"))  # Output : The age is: 23
print('The age is:', person.age)  # Output : The age is: 23

# ────────────────────────────────────────────────────────────────────────────────

# ─── Contoh 2: Getattr Ketika Atribut Bernama Tidak Ditemukan ───────────────────


class Person:
    age = 23
    name = "Adam"


person = Person()

# when default value is provided
print('The sex is:', getattr(person, 'sex', 'Male'))
# Output : The sex is: Male
# when no default value is provided

print('The sex is:', getattr(person, 'sex'))
# Output : AttributeError: 'Person' object has no attribute 'sex'
# ────────────────────────────────────────────────────────────────────────────────

"""
Atribut bernamasekstidak hadir di kelasOrang. Jadi, saat memanggil getattr()metode dengan nilai default Male, ia mengembalikan Male.
Namun, jika kita tidak memberikan nilai default, ketika atribut bernama sex tidak ditemukan, maka akan muncul AttributeErrorpepatah bahwa objek tersebut tidak memiliki atribut sex.
"""
# ────────────────────────────────────────────────────────────────────────────────
# ────────────────────────────────────────────────────────────────────────────────
