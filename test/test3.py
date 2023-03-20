class CookieCutter:
    
 def __init__(self,shape):
    self.shape = shape


 def cut_cookie(self):
     name = input("What is Your Name : ") 
     print(f"A {name}-shaped cookie has been cut!")
  
    

circle_cutter = CookieCutter("circle")

kotak_cutter = CookieCutter("Kotak")

petak_cutter = CookieCutter("Petak")


circle_cutter.cut_cookie()

kotak_cutter.cut_cookie()

petak_cutter.cut_cookie()