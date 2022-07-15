#TODO ─── Penggunaan Fungsi Hex ──────────────────────────────────────────────────────
# Fungsi hex() mengonversi bilangan bulat ke string heksadesimal yang sesuai.
# Syntax : hex(x)
# hex()fungsi mengambil satu argumen.
# x - bilangan bulat ( intobjek atau harus mendefinisikan __index__()metode yang mengembalikan bilangan bulat)
#
# hex()fungsi mengonversi bilangan bulat ke bilangan heksadesimal yang sesuai dalam bentuk string dan mengembalikannya.
# String heksadesimal yang dikembalikan dimulai dengan awalan yang 0xmenunjukkan bahwa itu dalam bentuk heksadesimal.
# #


# ─── Contoh 1 Bagaimana Hex Bekerja ─────────────────────────────────────────────
number = 435
print(number, 'in hex =', hex(number))
# Output : 435 dalam hex = 0x1b3
number = 0
print(number, 'in hex =', hex(number))
# Output : 0 dalam hex = 0x0
number = -34
print(number, 'in hex =', hex(number))
# Output : -34 dalam hex = -0x22
returnType = type(hex(number))
print('Return type from hex() is', returnType)
# Output :Jenis pengembalian dari hex() adalah <class 'str'>
# ────────────────────────────────────────────────────────────────────────────────
"""
Jika Anda perlu menemukan representasi heksadesimal dari float, Anda perlu menggunakan float.hex()metode.
"""
# ────────────────────────────────────────────────────────────────────────────────

# ─── Contoh 2: Representasi Heksadesimal Dari Float ─────────────────────────────
number = 2.5
print(number, 'in hex =', float.hex(number))
# Output : 2,5 dalam hex = 0x1.4000000000000p+1
number = 0.0
print(number, 'in hex =', float.hex(number))
# Output : 0,0 dalam heksa = 0x0.0p+0
number = 10.5
print(number, 'in hex =', float.hex(number))
# Output : 10,5 dalam heksa = 0x1.5000000000000p+3
# ────────────────────────────────────────────────────────────────────────────────
# ────────────────────────────────────────────────────────────────────────────────
