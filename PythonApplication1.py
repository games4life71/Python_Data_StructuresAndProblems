class Node:
    def __init__(self , data ):
        self.left  = None 
        self.right = None 
        self.val = data
        _private_data = 21 #Private field 
       
    def insert_node( data ):
         pass

class Anim : 
    """Anim is the base class from which other classes inherit"""
    def __init__(self , age , number ) :
        self._age = age 
        self._number = number 
        
    def print_info(self):
        print('The number is {} and the age is {}'.format(self._number ,self._age))
        print(id(self), '\n')
    
    #TODO implement get and set properties to restrict acces to fields
    
    def get_age(self):
        return self._age
    def set_age(self,age):
        self._age = age

    
    age = property(get_age, set_age)

    def get_number(self):
        return self._number
   
    number = property(get_number)


class Dog (Anim):
    """Dog inherits from Anim class ( which is superior) """
    def __init__(self, age, number , race ):
        super().__init__(age, number)
        self.race = race

    def print_anim_info(self):
        self.print_info()
        print(self.race)
        print('\n')


p1 = Anim(12,31)
p1.age = 2
p1.get_number = 32 # it doesnt work because it doesnt have a setter method !!!!
print(p1.number, "p1.number")








