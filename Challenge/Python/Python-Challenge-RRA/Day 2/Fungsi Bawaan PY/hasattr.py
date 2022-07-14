# ─── Penggunaan Fungsi Hasattr ──────────────────────────────────────────────────
# Metode hasattr()mengembalikan true jika suatu objek memiliki atribut bernama yang diberikan dan false jika tidak.
# Syntax : hasattr(object, name)
# Metode hasattr()ini mengambil dua parameter:
#   -obyek- objek yang atribut namanya akan diperiksa
#   -nama- nama atribut yang akan dicari
# Metode hasattr()mengembalikan:
# True- jika objek memiliki atribut bernama yang diberikan
# False- jika objek tidak memiliki atribut bernama yang diberikan
# #


# ─── Contoh 0 ───────────────────────────────────────────────────────────────────

class Person:
    age = 23
    name = "Adam"


person = Person()

print("Person's age:", hasattr(person, "age"))
print("Person's salary:", hasattr(person, "salary"))

# Output:
# Person's age: True
# Person's salary: False

# ────────────────────────────────────────────────────────────────────────────────

# ─── Contoh 1: Python Hasattr ───────────────────────────────────────────────────


class Car:
    brand = "Ford"
    number = 7786


car = Car()

print("The car class has brand:", hasattr(Car, "brand"))
print("The car class has specs: ", hasattr(Car, "specs"))
# Output :
# The car class has brand: True
# The car class has specs:  False
# ────────────────────────────────────────────────────────────────────────────────
"""
Dalam contoh di atas, kami memiliki Carkelas dengan dua atribut: branddan number.
Saat kami memeriksa kedua atribut ini menggunakan hasattr()metode, hasilnya adalah True .
Di sisi lain, untuk atribut apa pun yang tidak ada di kelas Carseperti specs , kita mendapatkan False sebagai outputnya.    
"""
# ────────────────────────────────────────────────────────────────────────────────
# ────────────────────────────────────────────────────────────────────────────────



