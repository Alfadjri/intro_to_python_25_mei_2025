from Person import Person

class Employe(Person):
    def __init__(self, nama, usia,pekerjaan,gaji):
        super().__init__(nama, usia)
        self._pekerjaan = pekerjaan
        self.__gaji = gaji
    
    def getDetail(self):
        return f"Nama Empolye : {self.nama}\nUsia : {self.getUsia()}\nPekerjaan : {self._pekerjaan}\nGaji : {self.__gaji}"
    
    def getWork(self):
        return f"{self.nama} hanya seorang Eployee"