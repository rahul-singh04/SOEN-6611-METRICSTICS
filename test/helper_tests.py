import unittest
from metricstics.code.helper import Helper


class TestHelper(unittest.TestCase):

    def setUp(self):
        # Create a Helper instance for testing
        self.helper = Helper()

    def test_calculate_mean(self):
        # Test calculating mean
        data = [1, 2, 3, 4, 5]
        mean = self.helper.calculate_mean(data)
        self.assertEqual(mean, 3.0)

    def test_calculate_variance(self):
        # Test calculating variance
        data = [1, 2, 3, 4, 5]
        mean = self.helper.calculate_mean(data)
        variance = self.helper.calculate_variance(data, mean)
        self.assertEqual(variance, 2.0)

    def test_merge_sort(self):
        # Test the merge sort algorithm
        unsorted_data = [5, 3, 1, 4, 2]
        self.helper.merge_sort(unsorted_data)
        self.assertEqual(unsorted_data, [1, 2, 3, 4, 5])

    def test_calculate_mean_absolute_deviation(self):
        # Test calculating mean absolute deviation
        data = [1, 2, 3, 4, 5]
        mean = self.helper.calculate_mean(data)
        mean_abs_dev = self.helper.calculate_mean_absolute_deviation(data, mean)
        self.assertEqual(mean_abs_dev, 1.2)

    def test_generate_random_data(self):
        # Test generating random data
        random_data = self.helper.generate_random_data()
        self.assertTrue(random_data)
        self.assertEqual(len(random_data), 1000)


if __name__ == '__main__':
    unittest.main()
