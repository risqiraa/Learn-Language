#TODO ─── Penggunaan Fungsi Callable ─────────────────────────────────────────────────
# Fungsi callable() mengembalikan True jika objek yang menjadi argumennya bisa dipanggil (callable).
# Jika tidak maka kembaliannya adalah False.
# Syntax : callable(object)
# Fungsi callable() akan mengembalikan:
# True – jika objek bisa dipanggil
# False – jika objek tidak bisa dipanggil
# TODO Note : meskipun kembalian dari callable() adalah True, bisa saja pemanggilan terhadap objek masih gagal.
# #

x = 10
print(callable(x)) # False


def tes_fungsi():
    print("tes")
    print("tes")
    print("tes")


y = tes_fungsi
print(callable(y)) # True

# ────────────────────────────────────────────────────────────────────────────────
