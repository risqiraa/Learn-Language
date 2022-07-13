# TODO ─── Penggunaan Fungsi Ascii ────────────────────────────────────────────────────
# Fungsi ascii() mengembalikan string yang berisi representasi objek yang dapat dicetak.
# Fungsi ascii() mengembalikan karakter escape dari karakter non-ASCII menggunakan karakter escape \x, \u, atau \U.
# ASCII singkatan dari American Standard Code for Information Interchange atau Kode Standar Amerika untuk Pertukaran Informasi

text_normal = 'Python is very interesting'
print(ascii(text_normal))  # 'Python is very interesting'

other_text = 'Pythön is very interesting'
print(ascii(other_text))  # 'Pyth\xf6n is very interesting'

print('Pyth\xf6n is very interesting')  # Pyth�n is very interesting

# ────────────────────────────────────────────────────────────────────────────────
