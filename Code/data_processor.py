from Code import helper


class DataProcessor:

    def __init__(self, data):
        self.data = data

    def mean(self):
        return helper.calculate_mean(self.data)

    def median(self):
        if not self.data:
            return None  # Return None for empty data

        sorted_data = self.data.copy()  # Create a copy to avoid modifying the original data
        helper.bubble_sort(sorted_data)

        length = len(sorted_data)

        if length % 2 == 1:
            # If the length is odd, return the middle element
            return sorted_data[length // 2]
        else:
            # If the length is even, return the average of the two middle elements
            middle1 = sorted_data[length // 2 - 1]
            middle2 = sorted_data[length // 2]
            return (middle1 + middle2) / 2

    def mode(self):
        if not self.data:
            return None  # Return None for empty data

        # Create a dictionary to store the frequency of each element
        frequency_dict = {}
        for value in self.data:
            frequency_dict[value] = frequency_dict.get(value, 0) + 1

        # Find the mode(s) with the highest frequency
        modes = [key for key, value in frequency_dict.items() if value == max(frequency_dict.values())]

        return modes

    def min_value(self):
        if not self.data:
            return None  # Return None for empty data

        sorted_data = self.data.copy()
        helper.bubble_sort(sorted_data)

        return sorted_data[0]

    def max_value(self):
        if not self.data:
            return None  # Return None for empty data

        sorted_data = self.data.copy()
        helper.bubble_sort(sorted_data)

        return sorted_data[-1]

    def standard_deviation(self):
        if not self.data:
            return None  # Return None for empty data

        mean_value = self.mean()
        variance = helper.calculate_variance(self.data, mean_value)
        std_deviation = variance ** 0.5

        return round(std_deviation, 2)

    def mad(self):
        mean_value = self.mean()
        mad_value = helper.calculate_mad(self.data, mean_value)
        return round(mad_value, 2)
