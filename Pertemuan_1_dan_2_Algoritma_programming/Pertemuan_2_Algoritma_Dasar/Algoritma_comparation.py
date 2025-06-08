x = 3
y = 3

# besar dari
hasil = (x > y)
print(f"Apakah nilai {x} besar dari (>) {y} adalah {hasil}")
# besar dari sama dengan
hasil = (x >= y)
print(f"Apakah nilai {x} besar dari sama dengan (>=) {y} adalah {hasil}")

# kecil dari
hasil = (x < y)
print(f"Apakah nilai {x} kecil dari (<) {y} adalah {hasil}")
# kecil dari sama dengan
hasil = (x <= y)
print(f"Apakah nilai {x} kecil dari sama dengan (<=) {y} adalah {hasil}")


kondisi = False
hasil = kondisi != False # ! not ini adalah kondisi yang di balikkan 

print(f"Apa yang akan terjadi dari kondisi di atas : {hasil}")

x = "1"
y = 1
hasil = x == str(y)
# kalau jumlah sama dengan ada 3 (===) program akan check ke akuratan tipe data
print(f"Hasil dari {x} apakah sama dengan {y} adalah {hasil}")