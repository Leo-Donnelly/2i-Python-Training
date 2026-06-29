class Rectangle:
    def __init__(self,width,height):
        self.width = width
        self.height = height
    
    def __str__(self):
        return f"Rectangle(Width = {self.width}, Height = {self.height})"
    
    def __add__(self, other):
      return Rectangle(self.width + other.width, self.height + other.height)
    
rectangle1 = Rectangle(10, 10)
rectangle2 = Rectangle(20, 20)

print(rectangle1)
print(rectangle2)

print(rectangle1 + rectangle2)