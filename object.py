
class objectClass: 
    
    _numberOfinstances =0
    instances_map = dict()
    
    def __init__(self , typeof , serialNO = 123) :
            
            self._typeof = typeof
            self._serialNO = serialNO  
            objectClass._numberOfinstances +=1 
            if (self._typeof in  objectClass.instances_map) : 
                objectClass.instances_map[self._typeof] += 1
            else: 
                objectClass.instances_map[self._typeof] = 1

    @staticmethod
    def print_stock():
       for values in objectClass.instances_map:
           print( 'There are {} {} in the stock'.format(objectClass.instances_map[values] , values), 'n')
    @staticmethod
    def get_total():
        print( 'There is a total of {} pieces in the stock'.format(objectClass._numberOfinstances))

    @property
    def typeof(self):
       return self._typeof
    @typeof.setter
    def typeof(self , val):
        self._typeof = val
    @property 
    def serialNO(self):
        return self._serialNO
    @serialNO.setter
    def serialNO(self, val):
        self._serialNO = val


 
