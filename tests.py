import unittest
import math
import circle
import rectangle
import square
import triangle


class CircleTestCase(unittest.TestCase):
    def test_area(self):
        res = circle.area(5)
        self.assertEqual(res, 78.53981633974483)

    def test_perimeter(self):
        res = circle.perimeter(5)
        self.assertEqual(res, 31.41592653589793)

    def test_negative(self):
        res = circle.area(-5)
        self.assertEqual(res, "Error")

    def test_string(self):
        res = circle.perimeter("5")
        self.assertEqual(res, "Error")


class RectangleTestCase(unittest.TestCase):
    def test_area(self):
        res = rectangle.area(10, 5)
        self.assertEqual(res, 50)

    def test_perimeter(self):
        res = rectangle.perimeter(10, 5)
        self.assertEqual(res, 30)

    def test_negative(self):
        res = rectangle.area(-10, 5)
        self.assertEqual(res, "Error")

    def test_string(self):
        res = rectangle.perimeter("10", "5")
        self.assertEqual(res, "Error")


class SquareTestCase(unittest.TestCase):
    def test_area(self):
        res = square.area(6)
        self.assertEqual(res, 36)

    def test_perimeter(self):
        res = square.perimeter(6)
        self.assertEqual(res, 24)

    def test_negative(self):
        res = square.area(-6)
        self.assertEqual(res, "Error")

    def test_string(self):
        res = square.perimeter("6")
        self.assertEqual(res, "Error")


class TriangleTestCase(unittest.TestCase):
    def test_area(self):
        res = triangle.area(10, 4)
        self.assertEqual(res, 20)

    def test_perimeter(self):
        res = triangle.perimeter(3, 4, 5)
        self.assertEqual(res, 12)

    def test_negative(self):
        res = triangle.area(-10, 4)
        self.assertEqual(res, "Error")

    def test_string(self):
        res = triangle.perimeter("3", "4", "5")
        self.assertEqual(res, "Error")
