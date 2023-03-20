class animal_name:
 def __init__(self,animal,type):
  
  self.animal = animal
  self.type = type

 def nama(self):
  print(f"A {self.animal} is a animal that is {self.type}")

black_pyhton = animal_name("Black Pyhton","carnivore")
black_tiger = animal_name("Black Tiger","carnivore")

black_pyhton.nama()
black_tiger.nama()