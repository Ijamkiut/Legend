class animal_name:
 def __init__(self,animal,type,bikaki):
  
  self.animal = animal
  self.type = type
  self.bikaki = bikaki

 def nama(self):
  self.animal = input("What is Your animal")
  self.type = input("What Is The Type of Your Animal")
    
  print(f"A {self.animal} is a animal that is {self.type}")

 def kaki(self):
  self.bikaki =  int (input("How many Leg does Your animal has"))
  if self.bikaki == 0:
   print(f"{self.animal}it sliding on the ground")
  elif self.bikaki < 2:
    print(f"{self.animal} walk on 2 feet")
  else:
    print(f"{self.animal} walk on 4 feet") 
 


black_pyhton = animal_name(animal,type,bikaki)

black_pyhton.nama()







# black_pyhton = animal_name("Black Pyhton","carnivore",0)
# black_tiger = animal_name("Black Tiger","carnivore",4)
# black_sheep = animal_name("Black Sheep","Hermivore",4)

# black_pyhton.nama()
# black_pyhton.kaki()
# black_tiger.nama()
# black_tiger.kaki()
# black_sheep.nama()
# black_sheep.kaki()
