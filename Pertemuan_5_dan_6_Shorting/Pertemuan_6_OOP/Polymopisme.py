from abc import ABC,abstractclassmethod
class Kendaraan(ABC):
    @abstractclassmethod
    def menyalakanMesin(self):
        pass
    

class Motor(Kendaraan):
    def menyalakanMesin(self):
        print("Status Motor : Mogok")
    
class Mobil(Kendaraan):
    def menyalakanMesin(self):
        print("Status Mobil : Abis Bensin")
        
class Pesawat(Kendaraan):
    def menyalakanMesin(self):
        print("Status Pesawat : Kurang Oli")
        
class Kereta(Kendaraan):
    def menyalakanMesin(self):
        print("Status Pesawat : Batu bara gak ada yang jual !!!!")
        
    

# Polymopisme
def menyalakanMesin(Kendaraan):
    Kendaraan.menyalakanMesin()
    
    
    
bebek = Motor()
supra = Mobil()
boing = Pesawat()
kai = Kereta()


menyalakanMesin(bebek)
menyalakanMesin(supra)
menyalakanMesin(boing)
menyalakanMesin(kai)
