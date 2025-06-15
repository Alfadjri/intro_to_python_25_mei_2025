# case mobil

class Mobil: 
    roda = 4 
    _warna = "default"  #ini sudah termasuk teknik encapsulation
    __merek = "default"
    def __init__(self,brand:str = None ,merek:str = None, warna:str = None): #ini di sebutnya construktor
        self.__merek = merek
        self._brand = brand
        self._warna = warna
    
    def getDetail(self):
        print(f"Nama brand : {self._brand}")
        print(f"Merek : {self.__merek}")
        print(f"Warna : {self.getWarna()}")
        print(f"Jumlah roda : {self.roda}")
        
    
    # Set and Get
    # set
    # kalau ada kata awalan set ini sifatnya untuk merubah nilai private
    def setWarna(self,warna):
        self._warna = warna
    
    # get
    # kalau ada kata awalan get ini sifatnya untuk mengambil nilai private
    def getWarna(self):
        return f"{self._warna} Gross"



toyota = Mobil("Toyota","supra","hitam")
toyota.roda = 2
toyota.setWarna("Merah")
toyota.getDetail()
