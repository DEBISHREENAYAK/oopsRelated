class A:
    _a = 10
    __b = 20
    
    def show(self):
        print("a =",self._a, "b =",self.__b)
        
a = A()
a.show()        
print(A._a)

# print(A.__b)  # error
        
        