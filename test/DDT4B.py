class DDT4b:
    def __init__(self,nama,bangsa,nom,umur):
        self.nama = nama
        self.bangsa = bangsa
        self.nom = nom
        self.umur = umur
    
    def introduction(self):
        print(f"Hi {self.nama} , Kamu Berbangsa {self.bangsa} Dan Nom kmu ialah {self.nom} dan Berumur {self.umur}")

a = input("What Is Your Name : ")
b = input("What Is Your Race : ")
c = input("What Is Your Nom : ")
d = input("What Is Your Umur : ")

nama = DDT4b(a,b,c,d)

nama.introduction()

