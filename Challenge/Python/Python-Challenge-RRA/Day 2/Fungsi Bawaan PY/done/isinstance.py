# TODO ─── Penggunaan Fungsi Isinstance ───────────────────────────────────────────────
# Fungsi isinstance()memeriksa apakah objek(argumen pertama) adalah turunan atau subkelas dari kelas classinfo(argumen kedua).
# Syntax : isinstance(object, classinfo)
# isinstance()membutuhkan dua parameter:
#   -objek - objectuntuk diperiksa
#   -classinfo - kelas, tipe, atau tupel kelas dan tipe
# isinstance() mengembalikan:
#   -True jika obyek adalah turunan atau subkelas dari kelas atau elemen apa pun dari Tuple
#   -False jika tidak
#! Jikainfo kelasbukan tipe atau tupel tipe, TypeErrorpengecualian dimunculkan.
# #

# ─── Contoh 0 ───────────────────────────────────────────────────────────────────
numbers = [1, 2, 3, 4, 2, 5]

# check if numbers is instance of list
result = isinstance(numbers, list)
print(result)

# Output: True
# ────────────────────────────────────────────────────────────────────────────────

# ─── Contoh 1 : Cara Kerja Isinstance ───────────────────────────────────────────


class Foo:
    a = 5


fooInstance = Foo()

print(isinstance(fooInstance, Foo))  # True
print(isinstance(fooInstance, (list, tuple)))  # False
print(isinstance(fooInstance, (list, tuple, Foo)))  # True

# ────────────────────────────────────────────────────────────────────────────────

# ─── Contoh 2: Bekerja Dari Isinstance Dengan Native Types ──────────────────────
numbers = [1, 2, 3]

result = isinstance(numbers, list)
print(numbers, 'instance of list?', result)
# Output : [1, 2, 3] instance of list? True

result = isinstance(numbers, dict)
print(numbers, 'instance of dict?', result)
# Output : [1, 2, 3] instance of dict? False

result = isinstance(numbers, (dict, list))
print(numbers, 'instance of dict or list?', result)
# Output : [1, 2, 3] instance of dict or list? True

number = 5
result = isinstance(number, list)
print(number, 'instance of list?', result)
# Output : 5 instance of list? Fals

result = isinstance(number, int)
print(number, 'instance of int?', result)
# Output : 5 instance of int? True

# ────────────────────────────────────────────────────────────────────────────────
# ────────────────────────────────────────────────────────────────────────────────
