# TODO ─── Penggunaan Fungsi Memory View ──────────────────────────────────────────────
# Fungsi memoryview() mengembalikan objek tampilan memori dari argumen yang diberikan.
# Syntax : memoryview(obj)
# memoryview() Parameter :
#   -obj - objek yang data internalnya akan diekspos. objharus mendukung protokol buffer ( byte , bytearray )
# Fungsi memoryview()mengembalikan objek tampilan memori.
# #

# ?Sebelum kita masuk ke tampilan memori, kita harus terlebih dahulu memahami tentang protokol buffer Python.
""" 
Protokol Penyangga Python
Protokol buffer menyediakan cara untuk mengakses data internal suatu objek. Data internal ini adalah array memori atau buffer.
Protokol buffer memungkinkan satu objek untuk mengekspos data internal (buffer) dan yang lain untuk mengakses buffer tersebut tanpa penyalinan perantara.
Protokol ini hanya dapat diakses oleh kami di level C-API dan tidak menggunakan basis kode normal kami.
Jadi, untuk mengekspos protokol yang sama ke basis kode Python normal, tampilan memori hadir.
"""
# ────────────────────────────────────────────────────────────────────────────────

# ? ─── Apa Itu Tampilan Memori ───────────────────────────────────────────────────
"""
Tampilan memori adalah cara aman untuk mengekspos protokol buffer dengan Python.
Ini memungkinkan Anda untuk mengakses buffer internal suatu objek dengan membuat objek tampilan memori.
"""
# ────────────────────────────────────────────────────────────────────────────────
# ?Mengapa protokol buffer dan tampilan memori penting?
""" 
Kita perlu ingat bahwa setiap kali kita melakukan beberapa tindakan pada suatu objek (panggil fungsi suatu objek, iris array), Python perlu membuat salinan objek tersebut .
Jika kita memiliki data besar untuk digunakan (misalnya, data biner dari suatu gambar), kita tidak perlu membuat salinan potongan data yang sangat besar, yang hampir tidak berguna.
Dengan menggunakan protokol buffer, kita dapat memberikan akses objek lain untuk menggunakan/memodifikasi data besar tanpa menyalinnya. Ini membuat program menggunakan lebih sedikit memori dan meningkatkan kecepatan eksekusi.
"""
# ────────────────────────────────────────────────────────────────────────────────

# Syntax : memoryview(obj)

# ────────────────────────────────────────────────────────────────────────────────


# ─── Contoh 1: Bagaimana Memoryview Bekerja Dengan Python ───────────────────────
# random bytearray
random_byte_array = bytearray('ABC', 'utf-8')

mv = memoryview(random_byte_array)

# access memory view's zeroth index
print(mv[0])  # Output :65

# create byte from memory view
print(bytes(mv[0:2]))  # Output :b'AB'

# create list from memory view
print(list(mv[0:3]))  # Output :[65, 66, 67]
# ────────────────────────────────────────────────────────────────────────────────
""" 
Di sini, kami membuat objek tampilan memorimvdari array byterandom_byte_array.
Kemudian, kami mengaksesmv's 0th index, 'A', dan mencetaknya (yang memberikan nilai ASCII - 65).
Sekali lagi, kami mengaksesmvdari 0 dan 1, 'AB', dan mengubahnya menjadi byte.
Akhirnya, kami mengakses semua indeksmvdan mengubahnya menjadi daftar. Karena secara internal bytearraymenyimpan nilai ASCII untuk alfabet, outputnya adalah daftar nilai ASCII dariSEBUAH,B,danC.
"""
# ────────────────────────────────────────────────────────────────────────────────

# ─── Contoh 2: Ubah Data Internal Menggunakan Tampilan Memori ───────────────────
# random bytearray
random_byte_array = bytearray('ABC', 'utf-8')
print('Before updation:', random_byte_array)
# Output : Sebelum pembaruan: bytearray(b'ABC')

mv = memoryview(random_byte_array)

# update 1st index of mv to Z
mv[1] = 90
print('After updation:', random_byte_array)
# Output :Setelah pembaruan: bytearray(b'AZC')
# ────────────────────────────────────────────────────────────────────────────────
""" 
Di sini, kami memperbarui indeks pertama tampilan memori menjadi 90, nilai ASCII dari Z.
Karena, objek tampilan memorimvreferensi buffer/memori yang sama, memperbarui indeks dimvjuga updaterandom_byte_array.
"""
# ────────────────────────────────────────────────────────────────────────────────
# ────────────────────────────────────────────────────────────────────────────────
