class CookieCutter:
    
 def __init__(self,shape):
    self.shape = shape


 def cut_cookie(self):
     print(f"A {self.shape}-shaped cookie has been cut!")
    

circle_cutter = CookieCutter("circle")

circle_cutter.cut_cookie()