employe = [
    {
        "nama" : "Alfadjri",
        "pekerjaan" : "IT Trainer", 
        "gaji" : 8000000
    },
    {
        "nama" : "budi",
        "pekerjaan" : "IT Trainer", 
    },
    {
        "nama" : "toni",
        "pekerjaan" : "IT Trainer", 
    }
]

print("========Daftar Pekerja========")
# function void
def detail_pekerja(nama,pekerjaan, gaji = None):
    print(f"Nama : {nama}")
    print(f"Pekerjaan : {pekerjaan}")
    print(f"Gaji : {gaji}")
    print(f"Pekerja yang rajin")

# cara panggil
detail_pekerja(employe[0]['nama'],employe[0]['pekerjaan'],employe[0]['gaji'])
detail_pekerja(employe[1]['nama'],employe[1]['pekerjaan'])
detail_pekerja(employe[2]['nama'],employe[2]['pekerjaan'])


def penjumlahan(a,b):
    return a + b

hasil_penjumlahan = penjumlahan(10,12)
print(f"hasil dari penjumlahan : {hasil_penjumlahan}")
