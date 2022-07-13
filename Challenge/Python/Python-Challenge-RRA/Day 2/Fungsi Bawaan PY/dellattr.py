#TODO ─── Penggunaan Fungsi Delattr ──────────────────────────────────────────────────
# Delattr() menghapus atribut dari objek (jika objek mengizinkannya).
# Syntax : delattr(objek, nama)
# delattr()membutuhkan dua parameter:
#   -objek - objek dari mana nama atribut harus dihapus
#   -name - string yang harus berupa nama atribut yang akan dihapus dariobyek
# delattr()tidak mengembalikan nilai apa pun(mengembalikan None).
# Itu hanya menghapus atribut(jika objek mengizinkannya).
# #

class Coordinate:
    x = 10
    y = -5
    z = 0


point1 = Coordinate()

print('x = ', point1.x)
print('y = ', point1.y)
print('z = ', point1.z)

delattr(Coordinate, 'z')

print('--After deleting z attribute--')
print('x = ', point1.x)  # x = 10
print('y = ', point1.y)  # y =  -5

# Raises Error
# AttributeError: 'Coordinate' object has no attribute 'z'
print('z = ', point1.z)

# ────────────────────────────────────────────────────────────────────────────────
# ────────────────────────────────────────────────────────────────────────────────


class Coordinate:
    x = 10
    y = -5
    z = 0


point1 = Coordinate()

print('x = ', point1.x)
print('y = ', point1.y)
print('z = ', point1.z)

# Deleting attribute z
del Coordinate.z

print('--After deleting z attribute--')
print('x = ', point1.x)
print('y = ', point1.y)

# Raises Attribute Error
print('z = ', point1.z)

# ────────────────────────────────────────────────────────────────────────────────
# ────────────────────────────────────────────────────────────────────────────────
