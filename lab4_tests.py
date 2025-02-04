import data
import lab4
import unittest
import data

# Write your test cases for each part below.

class TestCases(unittest.TestCase):
    # Part 1
    def test_first_element_1(self):
        input = [[1,2], [3,4]]
        result = lab4.first_element(input)
        expected = [1, 3]
        self.assertEqual(expected, result)




    def test_first_element_2(self):
        # write a second test here
        input = [[1, 2], [3, 4], [], [27, 3], [7, 54]]
        result = lab4.first_element(input)
        expected = [1, 3, 27, 7]
        self.assertEqual(expected, result)




    # Part 2

    def test_second_element_1(self):
        # write a second test here
        a = data.Point(1,2)
        b = data.Point(2,3)
        input = [a, b]
        result = lab4.x_coordinate(input)
        expected = [1, 2]
        self.assertEqual(expected, result)

    def test_second_element_2(self):
        # write a second test here
        a = data.Point(8,2)
        b = data.Point(3,3)
        input = [a, b]
        result = lab4.x_coordinate(input)
        expected = [8, 3]
        self.assertEqual(expected, result)





    # Part 3
    def test_third_element_1(self):
        # write a second test here
        a = data.Point(8,2)
        b = data.Point(3,3)
        input = [a, b]
        result = lab4.are_in_positive_quadrant(input)
        expected = [a, b]
        self.assertEqual(expected, result)
    def test_third_element_2(self):
        # write a second test here
        a = data.Point(8,2)
        b = data.Point(-3,3)
        input = [a, b]
        result = lab4.are_in_positive_quadrant(input)
        expected = [a]
        self.assertEqual(expected, result)




    # Part 4
    def test_fourth_element_1(self):
        # write a second test here
        a = data.Point(8,2)
        b = data.Point(3,3)

        result = lab4.distance(a, b)
        expected = 5.0
        self.assertAlmostEqual(expected, result, places = 0)
    def test_fourth_element_2(self):
        # write a second test here
        a = data.Point(8, 2)
        b = data.Point(-3, 3)

        result = lab4.distance(a, b)
        expected = 11.0
        self.assertAlmostEqual(expected, result, places = 0)

    # Part 5
    def test_five_element_1(self):
        # write a second test here
        a = data.Point(15, 8)
        b = data.Point(6, 8)

        result = lab4.manhattan_distance(a,b)
        expected = 9
        self.assertEqual(expected, result)

    def test_five_element_2(self):
        # write a second test here
        a = data.Point(2, 1)
        b = data.Point(6, 8)

        result = lab4.manhattan_distance(a, b)
        expected = 11
        self.assertEqual(expected, result)

    # Part 6

    def test_six_element_1(self):
        # write a second test here
        a = data.Point(15, 8)
        b = data.Point(6, 8)
        c = data.Point(3, 4)
        d = data.Point(12, 5)
        input = [a, b,c,d]
        result = lab4.distance_all(input)
        expected = [17.0,10.0,5.0,13.0]
        self.assertEqual(expected, result)
    def test_six_element_2(self):
        # write a second test here
        a = data.Point(40, 9)
        b = data.Point(24, 7)

        input = [a, b]
        result = lab4.distance_all(input)
        expected = [41.0, 25.0]
        self.assertEqual(expected, result)



if __name__ == '__main__':
    unittest.main()
