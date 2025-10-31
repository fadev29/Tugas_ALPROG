# nilai terbesar

angka1 = int(input("Masukan angka pertama: "))
angka2 = int(input("Masukan angka kedua: "))
angka3 = int(input("Masukan angka ketiga: "))

if angka1 > angka2 and angka1 > angka3:
    print("Angka terbesar adalah:", angka1)
elif angka2 > angka1 and angka2 > angka3:
    print("Angka terbesar adalah:", angka2)
else:
    print("Angka terbesar adalah:", angka3)