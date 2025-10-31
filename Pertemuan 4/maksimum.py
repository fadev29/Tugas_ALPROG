# input tiga bilangan 
a = int(input("Masukan bilangan pertama : "))
b = int(input("Masukan bilangan kedua : "))
c = int(input("Masukan bilangan ketiga : "))

# mencari bilangan terbesar
maks = a
if b > maks:
    maks = b
if c > maks:
    maks = c

# output
print(f"Bilangan terbesar adalah {maks}")