from circle import Circle
import unittest
import math

class TestCircle(unittest.TestCase):
  def setUp(self):
    self.circle = Circle()

  def test_circle_radius(self):
    self.assertEqual(self.circle.radius, 1.0)

  def test_circle_color(self):
    self.assertEqual(self.circle.color, "red")

  def test_circle_color(self):
    self.assertEqual(self.circle.color, "red")


class TestCircleOverloading(unittest.TestCase):
  def setUp(self):
    self.radius = 2.0
    self.circle = Circle(self.radius)

  def test_circle_overloading(self):
    self.assertEqual(self.circle.radius, self.radius)

class TestGetRadius(unittest.TestCase):
  def setUp(self):
    self.radius = 3.0
    self.circle = Circle(self.radius)

  def test_get_radius(self):
    self.assertEqual(self.circle.getRadius(), self.radius)

class TestGetArea(unittest.TestCase):
  def setUp(self):
    self.radius = 3.0
    self.circle = Circle(self.radius)

  def test_get_area(self):
    self.assertEqual(self.circle.getArea(), math.pi * self.radius * self.radius)

if __name__ == '__main__':
  unittest.main()
