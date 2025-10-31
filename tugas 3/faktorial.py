# input bilangan 
bilangan = int(input("Masukan bilangan : "))

# inisialisasi faktorial
faktorial = 1

# perhitungan faktorial
for i in range(1, bilangan + 1):
    faktorial *= i

# output
print(f"Faktorial dari {bilangan} adalah {faktorial}")