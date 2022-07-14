#TODO ─── Penggunaan Fungsi Eval ─────────────────────────────────────────────────────
# Metode eval()ini mem-parsing ekspresi yang diteruskan ke metode ini dan menjalankan ekspresi python (kode) di dalam program.
# Syntax : eval(expression, globals=None, locals=None)
# The eval() function takes three parameters:
# ekspresi - string diuraikan dan dievaluasi sebagai ekspresi Python
# global (opsional) - kamus
# penduduk setempat(opsional) - objek pemetaan. Kamus adalah tipe pemetaan standar dan umum digunakan dalam Python.
# penggunaan dari global dan locals akan dibahas nanti di artikel ini.
#
# Metode eval()mengembalikan hasil yang dievaluasi dariekspresi.
# #

# ─── Contoh 0 ───────────────────────────────────────────────────────────────────

number = 9

# eval performs the multiplication passed as argument
square_number = eval('number * number')
print(square_number)

# Output: 81

# ─── Contoh 1 Bagaimana Eval Bekerja ────────────────────────────────────────────
x = 1
print(eval('x + 1'))
# Output = 2
# ────────────────────────────────────────────────────────────────────────────────
# ? Di sini, eval()fungsi mengevaluasi ekspresi x + 1dan printdigunakan untuk menampilkan nilai ini.

# ─── Contoh 2: Contoh Praktis Untuk Mendemonstrasikan Penggunaan Eval ───────────

# Perimeter of Square


def calculatePerimeter(l):
    return 4*l

# Area of Square


def calculateArea(l):
    return l*l


expression = input("Type a function: ")

for l in range(1, 5):
    if (expression == 'calculatePerimeter(l)'):
        print("If length is ", l, ", Perimeter = ", eval(expression))
    elif (expression == 'calculateArea(l)'):
        print("If length is ", l, ", Area = ", eval(expression))
    else:
        print('Wrong Function')
        break
# Output :
# Ketikkan fungsi: countArea(l)
# Jika panjangnya 1, Luas = 1
# Jika panjangnya 2, Luas = 4
# Jika panjangnya 3, Luas = 9
# Jika panjangnya 4, Luas = 16

# ────────────────────────────────────────────────────────────────────────────────

