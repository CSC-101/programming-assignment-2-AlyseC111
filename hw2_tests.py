import data
import hw2
import unittest


# Write your test cases for each part below.

class TestCases(unittest.TestCase):
    # Part 1
    def test_create_rectangle_1(self):
        point1 = data.Point(5, 9)
        point2 = data.Point(2, 0)
        expected = data.Rectangle(data.Point(2, 9), data.Point(5, 0))
        actual = hw2.create_rectangle(point1, point2)
        self.assertEqual(expected, actual)
    def test_create_rectangle_2(self):
        point1 = data.Point(2, 10)
        point2 = data.Point(9, 5)
        expected = data.Rectangle(data.Point(2, 10), data.Point(9, 5))
        actual = hw2.create_rectangle(point1, point2)
        self.assertEqual(expected, actual)

    # Part 2
    def test_shorter_duration_than_1(self):
        d1 = data.Duration(2, 10)
        d2 = data.Duration(9, 5)
        expected = True
        actual = hw2.shorter_duration_than(d1, d2)
        self.assertEqual(expected, actual)
    def test_shorter_duration_than_2(self):
        d1 = data.Duration(10, 39)
        d2 = data.Duration(8, 25)
        expected = False
        actual = hw2.shorter_duration_than(d1, d2)
        self.assertEqual(expected, actual)
    # Part 3
    def test_songs_shorter_than_1(self):
        input = [data.Song("Taylor", "22", data.Duration(5, 22)), data.Song("Justin", "Baby", data.Duration(8, 10)), data.Song("Tyler", "Universal Sound", data.Duration(4, 48))]
        expected = [data.Song("Taylor", "22", data.Duration(5, 22)), data.Song("Tyler", "Universal Sound", data.Duration(4, 48))]
        actual = hw2.songs_shorter_than(input, data.Duration(7, 30))
        self.assertEqual(expected, actual)
    def test_songs_shorter_than_2(self):
        input = [data.Song("Kanye", "Stronger", data.Duration(5, 30))]
        expected = []
        actual = hw2.songs_shorter_than(input, data.Duration(5, 30))
        self.assertEqual(expected, actual)

    # Part 4
    def test_running_time_1(self):
        input = [data.Song("Taylor", "22", data.Duration(5, 22)), data.Song("Justin", "Baby", data.Duration(8, 10)),
                    data.Song("Tyler", "Universal Sound", data.Duration(4, 48))]
        expected = data.Duration(18, 21)
        actual = hw2.running_time(input, [0, 1, 2])
        self.assertEqual(expected, actual)
    def test_running_time_2(self):
        input = [data.Song("Taylor", "22", data.Duration(5, 22)), data.Song("Justin", "Baby", data.Duration(8, 10)),
                    data.Song("Tyler", "Universal Sound", data.Duration(4, 48))]
        expected = data.Duration(18, 54)
        actual = hw2.running_time(input, [0, 1, 0])
        self.assertEqual(expected, actual)

    # Part 5
    def test_validate_route_1(self):
        input = ['san luis obispo', 'santa margarita', 'atascadero']
        expected = True
        actual = hw2.validate_route([['san luis obispo', 'santa margarita'],['san luis obispo', 'pismo beach'],['atascadero', 'santa margarita'],['atascadero', 'creston']], input)
        self.assertEqual(expected, actual)
    def test_validate_route_2(self):
        input = ['san luis obispo', 'atascadero']
        expected = False
        actual = hw2.validate_route([['san luis obispo', 'santa margarita'],['san luis obispo', 'pismo beach'],['atascadero', 'santa margarita'],['atascadero', 'creston']], input)
        self.assertEqual(expected, actual)
    def test_validate_route_3(self):
        input = ['san luis obispo', 'santa margarita', 'atascadero']
        expected = False
        actual = hw2.validate_route([['san luis obispo', 'santa margarita'],['san luis obispo', 'pismo beach'],['atascadero', 'creston']], input)
        self.assertEqual(expected, actual)
    # Part 6
    def test_longest_repetition_1(self):
        input = [1, 1, 2, 2, 1, 1, 1, 3]
        expected = 4
        actual = hw2.longest_repetition(input)
        self.assertEqual(expected, actual)
    def test_longest_repetition_2(self):
        input = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        expected = None
        actual = hw2.longest_repetition(input)
        self.assertEqual(expected, actual)
    def test_longest_repetition_3(self):
        input = [2, 5, 5, 5, 5, 8, 3, 2, 3, 3, 3, 3]
        expected = 1
        actual = hw2.longest_repetition(input)
        self.assertEqual(expected, actual)




if __name__ == '__main__':
    unittest.main()
