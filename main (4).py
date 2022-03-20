#class method or static variable 

class Mobile:
  fp = 'yes'     #class variable 
  def __init__(self):
    self.model = "RealmeX"   # instance variable
  def show_model(self):  #instance method
    print("model:",self.model)  
  @classmethod
  def is_fp(cls):         #class method
    print("finger print:",cls.fp)


realme = Mobile()
realme.show_model()
print(Mobile.fp)   #Accessing class variable 
Mobile.is_fp()
Mobile.fp = 'no'#modifying class variable
Mobile.is_fp()