# case mobil

class Mobil: #Mobil itu di sebut nama Kelas
    # instastiasi
    # memerpsiapkan object apa yang akan di save oleh komputer
    roda = 4 # roda di sebutnya object yang memiliki property public 
    #propery public adalah nilai yang bisa di ubah dari luar kelas se maunya
    _warna = "default" # warna memiliki property private (_)
    #property private adalah nilai yang hanya bisa di ubah jika di izinkan
    __merek = "default" # merek memiliki property protected (_ _)
    #property protexted adalah nilai yang tidak bisa di ganti di luar kelas apa pun
    
    def __init__(self,brand:str = None ,merek:str = None, warna:str = None): #ini di sebutnya construktor
        self.__merek = merek
        self._brand = brand
        self._warna = warna
    
    # method
    def getDetail(self):
        print(f"Nama brand : {self._brand}")
        print(f"Merek : {self.__merek}")
        print(f"Warna : {self._warna}")
        print(f"Jumlah roda : {self.roda}")
        

# Cara menggilnya 
gakJelas = Mobil() #ini contoh tidak menggunakan contruktor
gakJelas.getDetail()


toyota = Mobil("Toyota","supra","hitam")
toyota.roda = 2 # ini pemanggilan variabel atau object public
toyota.getDetail()
