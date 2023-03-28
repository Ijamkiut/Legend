class player:
    def __init__(self,nama1,id1,health1,shiels,damage):
        self.nama1 =  nama1
        self.id1 = id1
        self.health1 = health1
        self.shiels = shiels
        self.damage = damage
    def introduction1(self):
        choice = choice
        print(f"Hi {self.nama1}, You Have {self.health} health and {self.shiels} Sheils")

        print("You Are Getting Fire From A enemy,so You Have to choose to run away or take the gun Fight")
        choice = input("Please Choose 1 or 2(1 for run away and 2 to fight)")
        if choice == 1:
            print("You Have Run Away")
            self.health1 -= 5
        elif choice == 2:
            print("You Fight the enemy and taken 10 damage but the enemy also taken 20 damage")
            self.health1 -= 20

class enemy:
    def __init__(self,nama2,id2,health2,shiels):
        self.nama2 = nama2
        self.id2 = id2
        self.health2 = health2
        self.shiels = shiels
    def introduction2(self):
        print(f"Hi {self.nama2}, You Have {self.health} health and {self.shiels} Sheils")