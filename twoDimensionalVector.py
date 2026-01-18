import math
class Vector:
    def __init__(self, x=0, y=0):
        self.x=x
        self.y=y
    
    def __repr__(self):
        return f'Vector({self.x!r}, {self.y!r})'
    
    def __abs__(self):
        return math.hypot(self.x, self.y)
        # return ((self.x*2)+(self.y*2))**0.5# same result as above
    
    def __bool__(self):
        return bool(abs(self))
    
    def __add__(self, other):
        return Vector(self.x+other.x, self.y+other.y)
    
    def __mul__(self,scalar):
        return Vector(self.x*scalar, self.y*scalar)

    


v1=Vector(1,2)#__init__

print(abs(v1))#__abs__

print(v1)#__repr__

v2=Vector(3,4)#__init__

v3= v1+v2#__add__

print(v3)#__repr__

v4= v3*3#__mul__

print(v4)#__repr__


