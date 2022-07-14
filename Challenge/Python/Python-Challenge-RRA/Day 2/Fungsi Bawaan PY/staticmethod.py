# ─── Penggunaan Fungsi Static Method ────────────────────────────────────────────
# Fungsi staticmethod()bawaan mengembalikan metode statis untuk fungsi tertentu.
# Syntax : staticmethod(function)
#
"""staticmethod()dianggap sebagai cara yang tidak Pythonik untuk membuat fungsi statis. 
Oleh karena itu, dalam versi Python yang lebih baru, 
Anda dapat menggunakan @staticmethoddekorator."""
# Syntax baru :
# @staticmethod
# def func(args, ...)
# Metode staticmethod()ini mengambil satu parameter:
#   fungsi - fungsi yang perlu dikonversi ke metode statis
# staticmethod()Mengembalikan metode statis untuk fungsi yang diteruskan sebagai parameter .
# #

"""
 Apa itu metode statis?
 
 Metode statis, seperti metode kelas , adalah metode yang terikat ke kelas daripada objeknya.

 Mereka tidak memerlukan pembuatan instance kelas. Jadi, mereka tidak tergantung pada keadaan objek.

 Perbedaan antara metode statis dan metode kelas adalah:

 Metode statis tidak tahu apa-apa tentang kelas dan hanya berurusan dengan parameter.
 Metode kelas bekerja dengan kelas karena parameternya selalu kelas itu sendiri.
 Mereka dapat dipanggil baik oleh kelas dan objeknya.
 
    Class.staticmethodFunc() 
    atau bahkan 
    Class().staticmethodFunc()

 """

# ─── Contoh 0 ───────────────────────────────────────────────────────────────────


class Calculator:

    def add_numbers(num1, num2):
        return num1 + num2


# convert add_numbers() to static method
Calculator.add_numbers = staticmethod(Calculator.add_numbers)

sum = Calculator.add_numbers(5, 7)
print('Sum:', sum)

# Output: Sum: 12

# ────────────────────────────────────────────────────────────────────────────────

# ─── Contoh 1 : Buat Metode Statis Menggunakan Staticmethod ─────────────────────


class Mathematics:

    def addNumbers(x, y):
        return x + y


# create addNumbers static method
Mathematics.addNumbers = staticmethod(Mathematics.addNumbers)

print('The sum is:', Mathematics.addNumbers(5, 10))
# The sum is : 15

# ────────────────────────────────────────────────────────────────────────────────


# Kapan Anda menggunakan metode statis?
# ─── 1. Mengelompokkan Fungsi Utilitas Ke Kelas ─────────────────────────────────
"""
Metode statis memiliki kasus penggunaan terbatas karena, seperti metode kelas atau metode lain 
apa pun di dalam kelas, mereka tidak dapat mengakses properti kelas itu sendiri.

Namun, ketika Anda membutuhkan fungsi utilitas yang tidak mengakses properti apa pun dari 
suatu kelas tetapi masuk akal bahwa itu milik kelas, kami menggunakan fungsi statis.
"""
# ─── Contoh 2: Buat Fungsi Utilitas Sebagai Metode Statis ───────────────────────


class Dates:
    def __init__(self, date):
        self.date = date

    def getDate(self):
        return self.date

    @staticmethod
    def toDashDate(date):
        return date.replace("/", "-")


date = Dates("15-12-2016")
dateFromDB = "15/12/2016"
dateWithDash = Dates.toDashDate(dateFromDB)

if(date.getDate() == dateWithDash):
    print("Equal")
else:
    print("Unequal")

# Output is : Equal/setara

# ────────────────────────────────────────────────────────────────────────────────

"""
Di sini, kami memiliki Dateskelas yang hanya berfungsi dengan tanggal dengan tanda hubung. Namun, di database kami sebelumnya, semua tanggal ada dalam garis miring.
Untuk mengonversi slash-dates menjadi dash-dates, kami telah membuat fungsi utilitas toDashDatedi dalam Dates.
Ini adalah metode statis karena tidak perlu mengakses properti Datesitu sendiri dan hanya membutuhkan parameter.
Kami juga dapat membuat toDashDatedi luar kelas, tetapi karena ini hanya berfungsi untuk tanggal, logis untuk menyimpannya di dalam Dateskelas.
"""

# ─── 2. Memiliki Implementasi Tunggal ───────────────────────────────────────────
# Metode statis digunakan ketika kita tidak ingin subkelas dari suatu kelas
# mengubah/menimpa implementasi metode tertentu.


# ─── Contoh 3: Bagaimana Pewarisan Bekerja Dengan Metode Statis ─────────────────
class Dates:
    def __init__(self, date):
        self.date = date

    def getDate(self):
        return self.date

    @staticmethod
    def toDashDate(date):
        return date.replace("/", "-")


class DatesWithSlashes(Dates):
    def getDate(self):
        return Dates.toDashDate(self.date)


date = Dates("15-12-2016")
dateFromDB = DatesWithSlashes("15/12/2016")

if(date.getDate() == dateFromDB.getDate()):
    print("Equal")
else:
    print("Unequal")

# Output is : Equal/Setara

# ────────────────────────────────────────────────────────────────────────────────

"""
Di sini, kami tidak ingin subkelas DatesWithSlashesmenimpa metode utilitas statis toDashDatekarena hanya memiliki satu penggunaan, 
yaitu mengubah tanggal menjadi tanggal putus-putus.
Kita dapat dengan mudah menggunakan metode statis untuk keuntungan kita dengan 
getDate()mengganti metode di subkelas sehingga bekerja dengan baik dengan DatesWithSlasheskelas.
"""

# ────────────────────────────────────────────────────────────────────────────────
# ────────────────────────────────────────────────────────────────────────────────
