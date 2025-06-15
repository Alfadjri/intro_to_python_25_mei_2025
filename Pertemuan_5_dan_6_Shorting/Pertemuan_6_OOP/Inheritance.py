# case Ibu dan anak

class Ibu:
    panggilan = "Iya, Ada Apa ?"
    _sifat = "Lembut"
    
    def setSifat(self,sifat):
        self._sifat = sifat
    
    def getSifat(self):
        return f"Sifat dari tokoh : {self._sifat}"
    
    def getPanggilan(self):
        return f"{self.panggilan}"

class Anak(Ibu): #ini yag di sebut encapsulation
    def disurush(self):
        return f"Nanti dulu deh !!!!"
    

# Cara memanggil
Toni = Anak()
Toni.panggilan = "Ton Ton"
Toni.setSifat("Pemarah")
print(Toni.getPanggilan())
print(Toni.getSifat())
