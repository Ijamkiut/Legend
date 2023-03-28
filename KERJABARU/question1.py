class members:
    def __init__(self,member,total):
        self.member = member
        self.total = total

    def introduction1(self):
        
        match member:
           case "vip":
             discount = total-(total*0.06)
             print(f"Diskaun yang diperolehi : 6 %")
             print(f"Bayaran yang dikenakan : {discount}")

           case "normal":
              discount = total-(total*0.04)
              print(f"Diskaun yang diperolehi : 4 %")
              print(f"Bayaran yang dikenakan : {discount}")

           case "none":
              discount = total-(total*0.00)
              print(f"Diskaun yang diperolehi : 0 %")
              print(f"Bayaran yang dikenakan : {discount}")
    
           case _:
              print("Please Try Again..")

member = input("Masukan keahlian anda (vip/biasa/tiada) : ")
total = float(input("                 Please Enter The Total : "))

dis = members(member,total)

dis.introduction1()