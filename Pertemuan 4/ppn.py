# presentase ppn
ppn_persen = 11 

# meminta input dari penguna
harga = float(input("Masukan harga barang : "))

# menghitung ppn
ppn = (ppn_persen / 100) * harga

# menghitung total harga
total_harga = harga + ppn

# menampilkan hasil nya 
print(f"\nHarga setelah ppn adalah : {harga: .2f}")
print(f"PPN  yang harus dibayar adalah : {ppn: .2f}")
print(f"Total harga yang harus dibayar adalah : {total_harga: .2f}")