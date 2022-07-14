# ─── Pengguanan Fungsi Globals ──────────────────────────────────────────────────
# Metode globals()ini mengembalikan kamus dengan semua variabel dan simbol global untuk program saat ini.
# Syntax : globals()
# Metode globals()ini tidak mengambil parameter apa pun.
# Metode globals()mengembalikan kamus tabel simbol global saat ini.
# #

# ─── Contoh 1 ───────────────────────────────────────────────────────────────────

age = 23

globals()['age'] = 25
print('The age is:', age)
# Output : The age is:

# ────────────────────────────────────────────────────────────────────────────────
# ────────────────────────────────────────────────────────────────────────────────
"""
Kompiler Python memelihara tabel simbol yang berisi informasi yang diperlukan tentang program yang sedang ditulis. Ada dua jenis tabel simbol dalam Python - Loca l dan Global .
Tabel Simbol Global menyimpan semua informasi yang terkait dengan cakupan global program (dalam keseluruhan program). Kita dapat mengakses tabel simbol ini dengan globals()metode.
Biasanya, pemrogram python menggunakan globals()metode untuk memodifikasi variabel global apa pun dalam kode.
Dalam hal ini, kami telah mengubahusiavariabel ke 25 menggunakan globals()metode dengan kunci kamus ['age'].
"""
