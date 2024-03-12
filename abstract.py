#Abstraction
# The process of hiding th implementation details from the users 
#only the highlighted set of services provided to the user 
#eg : phone , red button , green button -> receive , end , but how,, not our issu
#eg2 : mobile camera
from abADD import add
import abSUB

print(add(1,2))
print(abSUB.sub(56,6))

# WE can implement abstraction with 2 types
# -> abstact class
# -> interface