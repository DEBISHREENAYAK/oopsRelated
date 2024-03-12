class A:
    _a = 10
    __b = 20
    def show(self):
        print("a =", self._a)
        print("b =", self.__b) # we can access __b here , because this method is under the class A , by object we can access this private variable.
        
a_obj = A()
a_obj.show()        
print(A._a)
# print(A.__b)  # this give attribute werror ,, as __b is private . you can;t access it out side of class

# _a -> protected , can accss outside of the class
# __a -> private , can't access outside of class
A._a = 29
print(A._a)


#raw string :) # just prac
print("debi\tshree")
print("debi\nshree")
print(r"debi\n\tShree")

#my fev eg 
class Bank:
    def setbalance(self,balance):
        self.__balance = balance
    def getbalance(self):
        return self.__balance
bank_obj = Bank()
bank_obj.setbalance(9000)
print(bank_obj.getbalance())        


        