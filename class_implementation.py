
from object import objectClass


obj1 = objectClass('piesa1' , 1234123112)
obj6 = objectClass('piesa1' , 1234123112)
obj7 = objectClass('piesa1' , 1234123112)
obj2 = objectClass('piesa1')
obj3 = objectClass('piesa2')
obj4 = objectClass('piesa2')

objectClass.print_stock()
objectClass.get_total()