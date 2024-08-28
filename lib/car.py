from vehicle import Vehicle
# from car import Car 


class Car(Vehicle):
    def go(self):
        return "VRRROOOOOOOOOOOOOOOOOOOOOOOM!!!!!"
    pass

print('__bases__     ',Car.__bases__)
print('int.__bases__ ',int.__bases__)
print('__class__     ',Car.__class__)
print('_class__      ',int.__class__)