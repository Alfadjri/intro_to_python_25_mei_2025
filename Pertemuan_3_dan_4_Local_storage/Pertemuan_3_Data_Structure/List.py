# inisialisasi
# teknik program menyediakan memoery yang akan di pakai
makanan = ["nasi","","ayam"]

# Read (R)
print(f"List Makanan : {makanan}")

# Read Spesifik
print(f"Index of 1 : {makanan[1]}")
print(f"Index of -1 : {makanan[-1]}")

# Update(U)
makanan[1] = "daging"
print(f"List Makanan setelah di update: {makanan}")

# tambah data append (a)
makanan.append("sayur")
print(f"List Makanan setelah di add: {makanan}")

makanan.remove("nasi")
print(f"List Makanan setelah di delete: {makanan}")

buah = ["semangka","Melon","nanas"]
makanan += buah
print(f"List Makanan setelah di add list: {makanan}")