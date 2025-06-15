from Manager import Manager


def main():
    list_data = [
        {
            "nama_lengkap" : "Alfadjri Dwi Fadhilah",
            "usia" : 24,
            "pekerjan" : "Cybersecurity",
            "gaji" : 8500000,
            "jumlah_tim" : 0
        },
        {
            "nama_lengkap" : "Toni",
            "usia" : 24,
            "pekerjan" : "Programmer",
            "gaji" : 5000000,
            "jumlah_tim" : 2
        },
        {
            "nama_lengkap" : "Siti",
            "usia" : 24,
            "pekerjan" : "Ui and UX",
            "gaji" : 3000000,
            "jumlah_tim" : 3
        },
    ]
    print("===== Detail Karian ======")
    for person in list_data:
        print("===== Profile ======")
        employe = Manager(person['nama_lengkap'],person['usia'],person['pekerjan'],person["gaji"],person["jumlah_tim"])
        print(employe.getDetail())
        print('======= detai Pekerjaan ======')
        print(employe.getWork())
    
if __name__ == "__main__":
    main()