#TODO ─── Penggunaan Fungsi Format ───────────────────────────────────────────────────
# Metode format()ini mengembalikan representasi terformat dari nilai yang diberikan yang dikontrol oleh penentu format.
# Syntax : format(value[, format_spec])
# Fungsi format()ini mengambil dua parameter:
#   nilai - nilai yang perlu diformat
#   format_spec - Spesifikasi tentang bagaimana nilai harus diformat.
# Fungsi format()mengembalikan representasi terformat dari nilai tertentu yang ditentukan oleh penentu format.
# #

# ─── Contoh 0 ───────────────────────────────────────────────────────────────────

value = 45

# format the integer to binary
binary_value = format(value, 'b')
print(binary_value)

# Output: 101101
# ────────────────────────────────────────────────────────────────────────────────

# ─── Contoh 1: Pemformatan Angka Dengan Format ──────────────────────────────────
# d, f and b are type

# integer
print(format(123, "d"))  # Output : 123 // desimal

# float arguments
print(format(123.4567898, "f"))  # Output : 123.456790 // float

# binary format
print(format(12, "b"))  # Output : 1100 // biner
# ────────────────────────────────────────────────────────────────────────────────

# ─── Contoh 2: Pemformatan Angka Dengan Isian Perataan Tanda Lebar Presisi Dan Tipe
# integer
print(format(1234, "*>+7,d"))  # Output : *+1,234

# float number
print(format(123.4567, "^-09.3f"))  # Output : 0123.4570

# ────────────────────────────────────────────────────────────────────────────────
"""
Di sini, saat memformat integer 1234, kami telah menentukan penentu pemformatan *>+7,d. Mari kita pahami setiap opsi:

*- Ini adalah karakter isian yang mengisi ruang kosong setelah memformat
>- Ini adalah opsi perataan kanan yang menyelaraskan string output ke kanan
+- Ini adalah opsi tanda yang memaksa nomor untuk ditandatangani (memiliki tanda di sebelah kirinya)
7- Ini adalah opsi lebar yang memaksa angka untuk mengambil lebar minimum 7, spasi lainnya akan diisi dengan karakter isian
,- Operator ribuanlah yang menempatkan koma di antara ribuan.
d- Ini adalah opsi tipe yang menentukan nomor adalah bilangan bulat.
# ────────────────────────────────────────────────────────────────────────────────
Saat memformat floating point number 123.4567, kita telah menentukan format specifier ^-09.3f. Ini adalah:

^- Ini adalah opsi penyelarasan tengah yang menyelaraskan string keluaran ke tengah ruang yang tersisa
-- Ini adalah opsi tanda yang memaksa hanya angka negatif untuk menunjukkan tanda
0- Ini adalah karakter yang ditempatkan di tempat kosong.
9- Ini adalah opsi lebar yang menetapkan lebar minimum angka menjadi 9 (termasuk titik desimal, koma ribuan, dan tanda)
.3- Ini adalah operator presisi yang mengatur presisi angka mengambang yang diberikan ke 3 tempat
f- Ini adalah opsi tipe yang menentukan nomor adalah float.
# ────────────────────────────────────────────────────────────────────────────────

"""
# ─── Contoh 3: Menggunakan format() dengan mengganti __format__──────────────────
# custom __format__() method


class Person:
    def __format__(self, format):
        if(format == 'age'):
            return '23'
        return 'None'


print(format(Person(), "age"))

# ────────────────────────────────────────────────────────────────────────────────
"""
Di sini, kami telah mengganti __format__()metode kelas Person.
Sekarang menerima formatparameter dan mengembalikan 23 jika sama dengan 'age'. Jika tidak ada format yang ditentukan, Nonedikembalikan.
Fungsi format()berjalan secara internal Person().__format__("age")untuk mengembalikan 23.
"""
# ────────────────────────────────────────────────────────────────────────────────
"""
Format bawaan() Vs. format string()
format()Fungsinya mirip dengan metode format String . Secara internal, kedua metode memanggil __format__()metode objek.
Sementara format()fungsi bawaan adalah implementasi tingkat rendah untuk memformat objek menggunakan __format__()internal, string format()adalah implementasi tingkat tinggi yang mampu melakukan operasi pemformatan kompleks pada beberapa string objek juga.
"""
# ────────────────────────────────────────────────────────────────────────────────
