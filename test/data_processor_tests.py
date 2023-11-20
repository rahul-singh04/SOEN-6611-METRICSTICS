import unittest
from metricstics.code.data_processor import DataProcessor


class TestDataProcessor(unittest.TestCase):

    def setUp(self):
        # Create a DataProcessor instance for testing
        self.data_processor = DataProcessor()

    def test_generate_random_data(self):
        # Test generating random data
        self.data_processor.generate_random_data()
        self.assertTrue(self.data_processor.original_data)
        self.assertEqual(len(self.data_processor.original_data), 1000)

    def test_get_mean(self):
        # Test calculating the mean
        self.data_processor.original_data = [1, 2, 3, 4, 5]
        mean = self.data_processor.get_mean()
        self.assertEqual(mean, 3.0)

    def test_get_median_odd_length(self):
        # Test calculating the median with odd-length data
        self.data_processor.original_data = [1, 2, 3, 4, 5]
        median = self.data_processor.get_median()
        self.assertEqual(median, 3.0)

    def test_get_median_even_length(self):
        # Test calculating the median with even-length data
        self.data_processor.original_data = [1, 2, 3, 4, 5, 6]
        median = self.data_processor.get_median()
        self.assertEqual(median, 3.5)

    def test_get_mode(self):
        # Test calculating the mode
        self.data_processor.original_data = [1, 2, 2, 3, 4, 4, 4]
        mode = self.data_processor.get_mode()
        self.assertEqual(mode, 4)

    def test_get_standard_deviation(self):
        # Test calculating the standard deviation
        self.data_processor.original_data = [1, 2, 3, 4, 5]
        std_deviation = self.data_processor.get_standard_deviation()
        self.assertAlmostEqual(std_deviation, 1.41, places=2)

    def test_get_mean_absolute_deviation(self):
        # Test calculating the mean absolute deviation
        self.data_processor.original_data = [1, 2, 3, 4, 5]
        mean_abs_dev = self.data_processor.get_mean_absolute_deviation()
        self.assertEqual(mean_abs_dev, 1.2)

    def test_get_min_value(self):
        # Test getting the minimum value
        self.data_processor.original_data = [5, 2, 8, 1, 3]
        min_value = self.data_processor.get_min_value()
        self.assertEqual(min_value, 1)

    def test_get_max_value(self):
        # Test getting the maximum value
        self.data_processor.original_data = [5, 2, 8, 1, 3]
        max_value = self.data_processor.get_max_value()
        self.assertEqual(max_value, 8)


if __name__ == '__main__':
    unittest.main()
