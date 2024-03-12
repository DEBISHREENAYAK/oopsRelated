from abc import ABC, abstractmethod

class Car(ABC):
    def name(self):
        print("Every car has 4 wheels")
    
    @abstractmethod    
    def speed(self):
        pass
    
#We cant crete the obj of abstrsct class
#have to inherit it in any other class
#Where implementation is many , work same

class A(Car):
        # def name(self):
        #   print("Maruti")
          
        def speed(self):
            print("100")
            
class B(Car):
        def name(self):
          print("Suzuki")
          
        def speed(self):
            print("80")     
            
obj_A = A()
obj_B = B()

obj_A.name()
obj_A.speed()  


obj_B.name()
obj_B.speed()                 
              
    
                