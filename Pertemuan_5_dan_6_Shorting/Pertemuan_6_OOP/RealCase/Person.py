from abc import ABC, abstractclassmethod

class Person(ABC):
    def __init__(self,nama , usia):
        self.nama = nama
        self.__usia = usia
        
    def getDetail(self):
        pass
    
    def getUsia(self):
        return f"{self.__usia}"
    
    def setUsia(self,usia):
        if usia != 0 :
            self.__usia = usia
        else:
            raise ValueError("umur tidakb bernilai negatif")