import math
class Circle:
  radius = 1.0
  color = "red"

  def __init__(self, radius=1.0):
    self.radius = radius 
    self.color = "red"

  def getRadius(self):
    return self.radius

  def getArea(self):
    return math.pi * self.radius * self.radius
