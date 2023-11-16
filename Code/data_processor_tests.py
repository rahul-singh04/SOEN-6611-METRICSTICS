import unittest

from Code.data_processor import DataProcessor


class DataProcessorTests(unittest.TestCase):
    def test_get_median(self):
        processor = DataProcessor()
        data = [1, 2, 3, 4, 5]
        processor.original_data = data
        self.assertEqual(processor.get_median(), 3)

        processor = DataProcessor()
        data = [1, 2, 3, 4]
        processor.original_data = data
        self.assertEqual(processor.get_median(), 2.5)
