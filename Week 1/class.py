class Example:
    def __init__(self,x,y):#constructor
        self.x = x
        self.y = y
    
    def point(self):#method for printing x and y
        print(self.x,self.y)
    
    def change(self, a, b):#method for setting x and y
        self.x = a
        self.y = b

p=Example(5,7)
print(p.x)
Example.point(p)
Example.change(p, 6, 9)
Example.point(p)