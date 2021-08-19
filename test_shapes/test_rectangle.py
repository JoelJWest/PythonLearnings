import unittest
import shapes

class TestRectangle(unittest.TestCase):
    def test_something(self):
        rect1 = shapes.Rectangle(5, 5, 10)
        self.assertEqual(rect1.area(), 250)

