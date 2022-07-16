#TODO ─── Penggunaan Fungsi Issubclass ───────────────────────────────────────────────
# Fungsi issubclass() memeriksa apakah argumen kelas (argumen pertama) adalah subkelas dari kelas classinfo (argumen kedua).
# Syntax : issubclass(class, classinfo)
# issubclass()membutuhkan dua parameter:
#   -kelas - kelas yang akan diperiksa
#   -classinfo - kelas, tipe, atau tupel kelas dan tipe
# issubclass()mengembalikan:
#   -Truejikakelasadalah subclass dari kelas, atau elemen apa pun dari Tuple
#   -Falsejika tidak
# #

# ─── Contoh: Bagaimana Cara Kerja Issubclass ────────────────────────────────────
class Polygon:
    def __init__(polygonType):
        print('Polygon is a ', polygonType)


class Triangle(Polygon):
    def __init__(self):

        Polygon.__init__('triangle')


print(issubclass(Triangle, Polygon))  # True
print(issubclass(Triangle, list))  # False
print(issubclass(Triangle, (list, Polygon)))  # True
print(issubclass(Polygon, (list, Polygon)))  # True

# ────────────────────────────────────────────────────────────────────────────────
# ────────────────────────────────────────────────────────────────────────────────
