import os

from Code import helper
from Code.helper import Helper


class DataProcessor:

    def __init__(self):
        self.sorted_data = None
        self.mode = None
        self.median = None
        self.mean = None
        self.original_data = None
        self.helper = Helper()

    def read_data(self, file_path):
        file_extension = os.path.splitext(file_path)[1]
        if file_extension == ".txt":
            self.original_data = self.helper.read_txt_file(file_path)
        elif file_extension == ".csv":
            self.original_data = self.helper.read_csv_file(file_path)

    def get_mean(self):
        self.mean = self.helper.calculate_mean(self.original_data)
        return self.mean

    def get_median(self):
        if not self.original_data:
            return None  # Return None for empty data

        if self.sorted_data is None:
            sorted_data = self.original_data.copy()  # Create a copy to avoid modifying the original data
            self.helper.bubble_sort(sorted_data)
            self.sorted_data = sorted_data

        length = len(self.sorted_data)

        if length % 2 == 1:
            # If the length is odd, return the middle element
            self.median = self.sorted_data[length // 2]
        else:
            # If the length is even, return the average of the two middle elements
            middle1 = self.sorted_data[length // 2 - 1]
            middle2 = self.sorted_data[length // 2]
            self.median = (middle1 + middle2) / 2
        return self.median

    def get_mode(self):
        if not self.original_data:
            return None  # Return None for empty data

        # Create a dictionary to store the frequency of each element
        frequency_dict = {}
        for value in self.original_data:
            frequency_dict[value] = frequency_dict.get(value, 0) + 1

        # Find the mode(s) with the highest frequency
        modes = [key for key, value in frequency_dict.items() if value == max(frequency_dict.values())]
        self.mode = modes[0]
        return self.mode

    def get_min_value(self):
        if not self.original_data:
            return None  # Return None for empty data

        if self.sorted_data is None:
            sorted_data = self.original_data.copy()
            self.sorted_data = self.helper.bubble_sort(sorted_data)

        return self.sorted_data[0]

    def get_max_value(self):
        if not self.original_data:
            return None  # Return None for empty data

        if self.sorted_data is None:
            sorted_data = self.original_data.copy()
            self.sorted_data = self.helper.bubble_sort(sorted_data)

        return self.sorted_data[-1]

    def get_standard_deviation(self):
        if not self.original_data:
            return None  # Return None for empty data

        if self.mean is None:
            self.get_mean()

        variance = self.helper.calculate_variance(self.original_data, self.mean)
        std_deviation = variance ** 0.5

        return round(std_deviation, 2)

    def get_mean_absolute_deviation(self):
        if self.mean is None:
            self.get_mean()

        mad_value = self.helper.calculate_mean_absolute_deviation(self.original_data, self.mean)
        return round(mad_value, 2)
