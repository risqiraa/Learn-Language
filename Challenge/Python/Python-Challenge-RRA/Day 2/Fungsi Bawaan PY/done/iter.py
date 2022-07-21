# TODO ─── Penggunaan Fungsi Iter ─────────────────────────────────────────────────────
# Metode iter()mengembalikan iterator untuk argumen yang diberikan.
# Syntax : iter(object, sentinel [optional])
# Metode iter()ini mengambil dua parameter:
#   -obyek- bisa berupa list, set, tuple, dll.
#   -sentinel [optional] - a special value that is used to represent the end of a sequence
# Metode iter()mengembalikan:
#   -objek iterator untuk argumen yang diberikan sampai karakter sentinel ditemukan
#   -TypeError untuk objek yang ditentukan pengguna yang tidak mengimplementasikan __iter__(), dan __next__()atau__getitem()__
#
# #

# ─── Contoh 0 ───────────────────────────────────────────────────────────────────
# list of vowels
phones = ['apple', 'samsung', 'oneplus']
phones_iter = iter(phones)

print(next(phones_iter))
print(next(phones_iter))
print(next(phones_iter))

# Output:
# apple
# samsung
# oneplus
# ────────────────────────────────────────────────────────────────────────────────

# ─── Contoh 1 : Python Iter ─────────────────────────────────────────────────────
# list of vowels
vowels = ["a", "e", "i", "o", "u"]

# iter() with a list of vowels
vowels_iter = iter(vowels)

print(next(vowels_iter))  # Output : a
print(next(vowels_iter))  # Output : e
print(next(vowels_iter))  # Output : i
print(next(vowels_iter))  # Output : o
print(next(vowels_iter))  # Output :u

# ────────────────────────────────────────────────────────────────────────────────

"""
Dalam contoh di atas, kami telah menggunakan iter()metode dengan daftar vokal.
Metode mengembalikan elemen individu a, e, i, o, u dalam daftar sebagai objek iterator.    
"""
# ────────────────────────────────────────────────────────────────────────────────

# ─── Contoh 2 : Iter Untuk Object Khusus ────────────────────────────────────────


class PrintNumber:
    def __init__(self, max):
        self.max = max

# iter() method in a class
    def __iter__(self):
        self.num = 0
        return self
# next() method in a class

    def __next__(self):
        if(self.num >= self.max):
            raise StopIteration
        self.num += 1
        return self.num


print_num = PrintNumber(3)

print_num_iter = iter(print_num)
print(next(print_num_iter))  # 1
print(next(print_num_iter))  # 2
print(next(print_num_iter))  # 3

# raises StopIteration
print(next(print_num_iter))
""" Output :
Traceback (panggilan terakhir terakhir): 
  File "", baris 23, di 
File "", baris 11, di __next__ 
StopIteration
"""

# ────────────────────────────────────────────────────────────────────────────────

"""
Pada contoh di atas, kami telah mencetak nomor iterator 1 , 2 , 3 menggunakan metode __iter__()and __next__() .
Di sini, __next()__metode di sini memiliki loop yang berjalan hingga self.numlebih besar dari atau sama dengan self.max.
Karena kami telah melewati 3 sebagai parameter ke PrintNumber()objek, self.maxdiinisialisasi ke 3 . Oleh karena itu, loop berhenti di 3 .
Ketika self.nummencapai nilai self.maxyang 3 , next()metode ini memunculkan pengecualian StopIteration .
"""


# ─── Contoh 3 : Iter Dengan Parameter Sentinel ──────────────────────────────────

class DoubleIt:

    def __init__(self):
        self.start = 1

    def __iter__(self):
        return self

    def __next__(self):
        self.start *= 2
        return self.start

    __call__ = __next__


my_iter = iter(DoubleIt(), 16)

for x in my_iter:
    print(x)

# Output :
# 2
# 4
# 8
# ────────────────────────────────────────────────────────────────────────────────
"""
Dalam contoh di atas, kami belum menerapkan StopIterationkondisi.
Sebagai gantinya, kami telah menggunakan iter()metode dengan parameter sentinel untuk menghentikan iterasi:
"""
#my_iter = iter(DoubleIt(), 16)
"""
Nilai parameter sentinel disini adalah 16 sehingga program akan berhenti ketika nilai dari __next__()metode sama dengan angka tersebut.
Pada titik ini dalam kode, program akan menaikkan secara StopIterationotomatis.
"""
# ────────────────────────────────────────────────────────────────────────────────
# ────────────────────────────────────────────────────────────────────────────────
