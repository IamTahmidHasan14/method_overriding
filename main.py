#METHOD OVERRIDING
from math import pi


class Rec:

  def __init__(self, x, y):
    self.x = x
    self.y = y

  def area(self):
    return self.x * self.y


class Circle(Rec):

  def __init__(self, r):
    # self.r = r
    super().__init__(r, r)

  def area(self):
    return pi * super().area()


r = Rec(5, 6)
print(r.area())
c = Circle(7)
print(c.area())