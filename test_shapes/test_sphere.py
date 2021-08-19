import unittest
import shapes

class TestRectangle(unittest.TestCase):
    def test_something(self):
        sphere1 = shapes.Sphere(2)
        self.assertAlmostEqual(sphere1.area(), 33.51, 2)
