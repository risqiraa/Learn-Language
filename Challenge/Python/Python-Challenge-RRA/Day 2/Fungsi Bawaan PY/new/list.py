# TODO ─── Penggunaan Fungsi List ─────────────────────────────────────────────────────
# Konstruktor list()mengembalikan daftar dengan Python.
# Syntax : list([iterable])
# Konstruktor list()mengambil satu argumen:
#   -iterable (opsional) - objek yang bisa berupa urutan ( string , tupel ) atau koleksi ( set , dictionary ) atau objek iterator apa pun
# Konstruktor list()mengembalikan daftar.
#   -Jika tidak ada parameter yang dilewatkan, ia mengembalikan daftar kosong
#   -Jika iterable dilewatkan sebagai parameter, itu membuat daftar yang terdiri dari item iterable.
# #

# ─── Contoh 0 ───────────────────────────────────────────────────────────────────
text = 'Python'

# convert string to list
text_list = list(text)
print(text_list)

# check type of text_list
print(type(text_list))

# Output: ['P', 'y', 't', 'h', 'o', 'n']
#         <class 'list'>
# ────────────────────────────────────────────────────────────────────────────────

# ─── Contoh 1: Buat Daftar Dari String Tupel Dan Daftar ─────────────────────────
# empty list
print(list())  # Output:[]

# vowel string
vowel_string = 'aeiou'
print(list(vowel_string))  # Output:['a', 'e', ​​'i', 'o', 'u']

# vowel tuple
vowel_tuple = ('a', 'e', 'i', 'o', 'u')
print(list(vowel_tuple))  # Output: ['a', 'e', ​​'i', 'o', 'u']

# vowel list
vowel_list = ['a', 'e', 'i', 'o', 'u']
print(list(vowel_list))  # Output: ['a', 'e', 'i', 'o', 'u']
# ────────────────────────────────────────────────────────────────────────────────


# ─── Contoh 2: Buat Daftar Dari Set Dan Kamus ───────────────────────────────────
# vowel set
vowel_set = {'a', 'e', 'i', 'o', 'u'}
print(list(vowel_set))  # Output : ['a', 'o', 'u', 'e', 'i']

# vowel dictionary
vowel_dictionary = {'a': 1, 'e': 2, 'i': 3, 'o': 4, 'u': 5}
print(list(vowel_dictionary))  # Output :['o', 'e', 'a', 'u', 'i']

#!Catatan: Dalam kasus kamus, kunci kamus akan menjadi item dari daftar. Juga, urutan elemen akan acak.

# ────────────────────────────────────────────────────────────────────────────────

# ─── Contoh 3: Buat Daftar Dari Objek Iterator ──────────────────────────────────
# objects of this class are iterators


class PowTwo:
    def __init__(self, max):
        self.max = max

    def __iter__(self):
        self.num = 0
        return self

    def __next__(self):
        if(self.num >= self.max):
            raise StopIteration
        result = 2 ** self.num
        self.num += 1
        return result


pow_two = PowTwo(5)
pow_two_iter = iter(pow_two)

print(list(pow_two_iter))
# Output : [1, 2, 4, 8, 16]
# ────────────────────────────────────────────────────────────────────────────────
# ────────────────────────────────────────────────────────────────────────────────
