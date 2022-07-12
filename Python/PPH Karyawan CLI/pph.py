from ast import If
from cgi import print_arguments


ketetapantanggungan = 4500000
tidakkenapajak = 54000000
claster0 = 54000000
claster1 = claster0 + 60000000
claster2 = claster1 + 250000000
claster3 = claster2 + 500000000
claster4 = claster3 + 5000000000

pph = 0
tunjangan = 0


print("\n\n\n============================================\n")
print("PENGHITUNG PPH KARYAWAN PT MAKMUR JAYA ABADI\n")
print("============================================\n")

gajipokok = input("input gaji pokok     : ")
iuranasuransi = input("input iuran asuransi : ")
iuranpensiun = input("input iuran pensiun  : ")
statuspernikahan = input("input status pernikahan K(Kawin)/TK(Tidak Kawin) : ")

if(statuspernikahan == "K"):
    tanggungan = input("input jumlah tanggungan (selain istri)             : ")
    if(int(tanggungan) <= 3):
        tunjangan = (int(tanggungan)+1)*ketetapantanggungan
    else:
        tunjangan = (3+1)*ketetapantanggungan

elif(statuspernikahan == "TK"):
    tanggungan = input("input jumlah tanggungan : ")
    if(int(tanggungan) <= 3):
        tunjangan = int(tanggungan)*ketetapantanggungan
    else:
        tunjangan = 3*ketetapantanggungan
else:
    print("maaf format yang anda masukkan tidak sesuai")

gajibulanan = int(gajipokok)-int(iuranasuransi)-int(iuranpensiun)
#biayajabatan = int(gajipokok)*5/100
gajitahunan = int(gajibulanan)*12
ptkp = tidakkenapajak+tunjangan
pajak = int(gajitahunan)-ptkp

if(gajitahunan <= claster0):  # <0juta
    ptkp = gajitahunan
    pajak = 0
    pph = pajak * 0/100
elif(gajitahunan <= claster1):  # 0-60juta
    pph = (pajak * 5/100)
elif(gajitahunan <= claster2):  # 60juta - 250juta
    pajak2 = pajak - 60000000
    pph = (pajak2 * 15/100)+3000000
elif(gajitahunan <= claster3):  # 250juta-500juta
    pajak2 = pajak - 190000000
    pph = (pajak * 25/100)+28500000+3000000
elif(gajitahunan <= claster4):  # 500juta-5miliar
    pajak2 = pajak - 2500000000
    pph = (pajak * 30/100)+62500000+28500000+3000000
elif(gajitahunan > claster4):  # >5miliar
    pajak2 = pajak - 4500000000
    pph = (pajak * 35/100)+1350000000+62500000+28500000+3000000
else:
    print("maaf format yang anda masukkan tidak sesuai\n")

print("\n============================================\n")
print("gaji anda                            = Rp "+str(gajibulanan)+"")
print("total gaji anda 12 bulan             = Rp "+str(gajitahunan)+"")
print("penghasilan tidak kena pajak anda    = Rp "+str(ptkp)+"")
print("penghasilan kena pajak               = Rp "+str(pajak)+"")
print("pph anda                             = Rp "+str(pph)+"")
print("\n============================================\n")

