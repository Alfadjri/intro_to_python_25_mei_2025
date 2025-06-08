import datetime

nama_pt = "PT.Bintang Jaya"
alamat = "JL.Kedoya 30 No 1 , Jakarta Timur"
waktu_dibuat = datetime.datetime.now()

# pisisonal Argumen 
print("=======Posisional Argument=======")
print("\t\t\t{0}\nKepada,\nHRD Manager {1}\n{2}".format(nama_pt,alamat,waktu_dibuat))
print("=======Keword Argument=======")
print("\t\t\t{waktu}\nKepada,\nHRD Manager {nama_pt}\n{alamat}".format(nama_pt = nama_pt,alamat = alamat, waktu=waktu_dibuat))
print("=======Cara Singkat=========")
print(f"\t\t\t{waktu_dibuat}\nKepada,\nHRD Manager {nama_pt}\n{alamat}")
# \t ini untuk tab  sama dengan 4 kali spasi (indentasi) atau sebutanya unique simbol
# \n ini untuk new line atau enter
