import unittest
import circle
import rectangle
import square
import triangle


class CircleTestCase(unittest.TestCase):
    def test_area_positive(self):
        res = circle.area(5)
        self.assertEqual(res, 78.53981633974483)

    def test_area_negative(self):
        self.assertRaises(TypeError, circle.area, -5)

    def test_area_string(self):
        self.assertRaises(TypeError, circle.area, "5")

    def test_perimeter_positive(self):
        res = circle.perimeter(5)
        self.assertEqual(res, 31.41592653589793)

    def test_perimeter_negative(self):
        self.assertRaises(TypeError, circle.perimeter, -5)

    def test_perimeter_string(self):
        self.assertRaises(TypeError, circle.perimeter, "5")


class RectangleTestCase(unittest.TestCase):
    def test_area_positive(self):
        res = rectangle.area(10, 5)
        self.assertEqual(res, 50)

    def test_area_negative(self):
        self.assertRaises(TypeError, rectangle.area, -10, 5)

    def test_area_string(self):
        self.assertRaises(TypeError, rectangle.area, "10", "5")

    def test_perimeter_positive(self):
        res = rectangle.perimeter(10, 5)
        self.assertEqual(res, 30)

    def test_perimeter_negative(self):
        self.assertRaises(TypeError, rectangle.perimeter, -10, 5)

    def test_perimeter_string(self):
        self.assertRaises(TypeError, rectangle.perimeter, "10", "5")


class SquareTestCase(unittest.TestCase):
    def test_area_positive(self):
        res = square.area(6)
        self.assertEqual(res, 36)

    def test_area_negative(self):
        self.assertRaises(TypeError, square.area, -6)

    def test_area_string(self):
        self.assertRaises(TypeError, square.area, "6")

    def test_perimeter_positive(self):
        res = square.perimeter(6)
        self.assertEqual(res, 24)

    def test_perimeter_negative(self):
        self.assertRaises(TypeError, square.perimeter, -6)

    def test_perimeter_string(self):
        self.assertRaises(TypeError, square.perimeter, "6")


class TriangleTestCase(unittest.TestCase):
    def test_area_positive(self):
        res = triangle.area(10, 4)
        self.assertEqual(res, 20)

    def test_area_negative(self):
        self.assertRaises(TypeError, triangle.area, -10, 4)

    def test_area_string(self):
        self.assertRaises(TypeError, triangle.area, "10", "4")

    def test_perimeter_positive(self):
        res = triangle.perimeter(3, 4, 5)
        self.assertEqual(res, 12)

    def test_perimeter_negative(self):
        self.assertRaises(TypeError, triangle.perimeter, -3, 4, 5)

    def test_perimeter_string(self):
        self.assertRaises(TypeError, triangle.perimeter, "3", "4", "5")