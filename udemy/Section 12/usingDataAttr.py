class Kettle(object):
    power_source = "electricity" # class attribute, shared by all instances of the class
    def __init__(self, make, price):
        self.make = make
        self.price = price
        self.on = False

    def switch_on(self):
        self.on = True
    
kenwood = Kettle("Kenwood", 8.99)
print(kenwood.make)
print(kenwood.price)

kenwood.price = 12.75
print(kenwood.price)
hamilton = Kettle("Hamilton", 14.55)
print("Models: {} = {}, {} = {}".format(kenwood.make, kenwood.price, hamilton.make, hamilton.price))
print("Models: {0.make} = {0.price}, {1.make} = {1.price}".format(kenwood, hamilton))   
# using the idx of the objects as to represent them and accessing their attributes

"""
Class: template for creating objects. All objects created using the same class will have the same characteristics
Object: an instance of a class
Instantiate: creating an instance of a class
Method: a function defined in a class
Attribute: a variable bound to an instance of a class
"""

print(kenwood.on)
kenwood.switch_on()
print(kenwood.on)

print(hamilton.on)
Kettle.switch_on(hamilton)  
# pass the object to class instance method, allows the code init to access all the attrs of the object passed
print(hamilton.on)

print("*"*80)

kenwood.power = 1.8 # adding a new attribute to the object, althought it wasn't part of the definition of the class
print(kenwood.power)
# print(hamilton.power)

print(Kettle.power_source)
print(kenwood.power_source)
print(hamilton.power_source)

print('*'*80)

print(Kettle.__dict__)
print(kenwood.__dict__)
print(hamilton.__dict__)

print('*'*80)
Kettle.power_source = "atomic"

print(kenwood.power_source)
print(hamilton.power_source)

print('*'*80)

kenwood.power_source = "gas"    
# updating the power_source attribute of the kenwood object doesn't affect the class attribute
print(Kettle.power_source)
print(kenwood.power_source)
print(hamilton.power_source)

