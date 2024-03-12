from abc import ABC,abstractmethod

#when action common but implementation deffierent --> then use abstract class
class Car(ABC):
    def show(self):
        print("Every car has 4 wheels")
    @abstractmethod
    def speed(self):
        pass

class Maruti(Car):
    def speed(self):
        print("The speed of the car is 120km/hr")
       
class Suzuki(Car):
    def speed(self):
        print("The speed of the car is 90km/hr")       
   
obj_Maruti = Maruti()
obj_Maruti.show()
obj_Maruti.speed()

obj_Suzuki = Suzuki()
obj_Suzuki.show()
obj_Suzuki.speed()

# # my experiment  #yeahhhhh
# for i in (obj_Maruti,obj_Suzuki):
#     i.speed()
#     i.show()
    
          
    
        