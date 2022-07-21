# TODO ─── Penggunaan Fungsi Len ──────────────────────────────────────────────────────
# Fungsi len()mengembalikan jumlah item (panjang) dalam suatu objek.
# Syntax : len(s)
# Fungsi len()mengambil satu argumen s , yang dapat berupa
#   -urutan - string, byte, Tuple, daftar, rentang ATAU,
#   -koleksi - kamus, set, set beku
# len()fungsi mengembalikan jumlah item dari suatu objek.
# Gagal memberikan argumen atau memberikan argumen yang tidak valid akan memunculkan TypeErrorpengecualian.
# #


# ─── Contoh 0 ───────────────────────────────────────────────────────────────────
languages = ['Python', 'Java', 'JavaScript']

# compute the length of languages
length = len(languages)
print(length)

# Output: 3
# ────────────────────────────────────────────────────────────────────────────────

# ─── Contoh 1: Bagaimana Len Bekerja Dengan Tupel Daftar Dan Rentang ────────────
testList = []
print(testList, 'length is', len(testList))
# Output :[] panjangnya adalah 0

testList = [1, 2, 3]
print(testList, 'length is', len(testList))
# Output :[1, 2, 3] panjangnya adalah 3

testTuple = (1, 2, 3)
print(testTuple, 'length is', len(testTuple))
# Output :(1, 2, 3) panjangnya adalah 3

testRange = range(1, 10)
print('Length of', testRange, 'is', len(testRange))
# Output : Panjang jangkauan(1, 10) adalah 9
# ────────────────────────────────────────────────────────────────────────────────

# ─── Contoh 2: Bagaimana Len Bekerja Dengan String Dan Byte ─────────────────────
testString = ''
print('Length of', testString, 'is', len(testString))
# Output : Panjangnya adalah 0

testString = 'Python'
print('Length of', testString, 'is', len(testString))
# Output : Panjang Python adalah 6

# byte object
testByte = b'Python'
print('Length of', testByte, 'is', len(testByte))
# Output :Panjang b'Python' adalah 6

testList = [1, 2, 3]
# converting to bytes object
testByte = bytes(testList)
print('Length of', testByte, 'is', len(testByte))
# Output :Panjang b'\x01\x02\x03' adalah3
# ────────────────────────────────────────────────────────────────────────────────


# ─── Contoh 3: Bagaimana Len Bekerja Dengan Kamus Dan Set ───────────────────────
testSet = {1, 2, 3}
print(testSet, 'length is', len(testSet))
# Ouput : {1, 2, 3} panjangnya adalah 3

# Empty Set
testSet = set()
print(testSet, 'length is', len(testSet))
# Ouput : set() panjangnya 0

testDict = {1: 'one', 2: 'two'}
print(testDict, 'length is', len(testDict))
# Ouput : {1: 'one', 2: 'two'} length is 2

testDict = {}
print(testDict, 'length is', len(testDict))
# Ouput : {} length is 0

testSet = {1, 2}
# frozenSet
frozenTestSet = frozenset(testSet)
print(frozenTestSet, 'length is', len(frozenTestSet))
# Ouput : frozenset({1, 2}) length is 2

# ────────────────────────────────────────────────────────────────────────────────


# ─── Contoh 4: Bagaimana Len Bekerja Untuk Objek Kustom ─────────────────────────
class Session:
    def __init__(self, number=0):
        self.number = number

    def __len__(self):
        return self.number


# default length is 0
s1 = Session()
print(len(s1))  # Output : 0


# giving custom length
s2 = Session(6)
print(len(s2))  # Output : 6
# ────────────────────────────────────────────────────────────────────────────────
# ────────────────────────────────────────────────────────────────────────────────
