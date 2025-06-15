from abc import ABC , abstractclassmethod

class Hewan (ABC):
    @abstractclassmethod
    def suara(self): #ini sebutanya abstack jadi nilainya tidak jelas
        print("ini punya hewan")


class Kucing(Hewan):
    def suara(self):
        print("Meow !!!!!")
    

Tom = Kucing()
Tom.suara()