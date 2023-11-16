import os

from code.metricstics.helper import Helper


class DataProcessor:

    def __init__(self):
        self.sorted_data = None
        self.mode = None
        self.median = None
        self.mean = None
        self.original_data = None
        self.helper = Helper()

    def read_data(self, file_path):
        """
        Reads data from a file specified by 'file_path' and stores it in 'self.original_data'.

        :param file_path: The path to the file to be read.
        :return:
        """
        try:
            # Extract the file extension from the file path
            file_extension = os.path.splitext(file_path)[1]

            # Check the file extension and read data accordingly
            if file_extension == ".txt":
                self.original_data = self.helper.read_txt_file(file_path)
            elif file_extension == ".csv":
                self.original_data = self.helper.read_csv_file(file_path)
            else:
                raise ValueError(f"Unsupported file format: {file_extension}")
        except FileNotFoundError:
            print(f"File not found: {file_path}")
        except Exception as e:
            print(f"An error occurred while reading the file: {e}")

    def generate_random_data(self):
        """
        This method generates random data ranging from 1 to 1000
        :return:
        """
        try:
            self.original_data = self.helper.generate_random_data()
        except Exception as e:
            print(f"An error occurred while generating random data: {e}")

    def get_mean(self):
        """
        Calculate the mean of the given data.
        :return: Mean of the dataset.
        """
        try:
            self.mean = self.helper.calculate_mean(self.original_data)
            return self.mean
        except Exception as e:
            print(f"An error occurred while calculating the mean: {e}")

    def get_median(self):
        """
        Calculate the median of the given dataset.
        :return: Median of the dataset.
        """
        try:
            if not self.original_data:
                # Return None for empty data.
                return None

            if self.sorted_data is None:
                # Create a copy to avoid modifying the original data.
                self.sorted_data = self.original_data.copy()
                self.helper.merge_sort(self.sorted_data)

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
        except Exception as e:
            print(f"An error occurred while calculating the median: {e}")

    def get_mode(self):
        """
        Calculate the mode of the given dataset.
        :return: Mode of the dataset.
        """
        try:
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
        except Exception as e:
            print(f"An error occurred while calculating the mode: {e}")

    def get_min_value(self):
        """
        This method returns the minimum value present in the dataset
        :return: Minimum value
        """
        try:
            if not self.original_data:
                # Return None for empty data
                return None

            if self.sorted_data is None:
                self.sorted_data = self.original_data.copy()
                self.helper.merge_sort(self.sorted_data)

            # Return the minimum value, which is the first element of the sorted data
            return self.sorted_data[0]
        except Exception as e:
            print(f"An error occurred while getting the minimum value: {e}")

    def get_max_value(self):
        """
        This method returns the maximum value present in the dataset
        :return: Maximum value
        """
        try:
            if not self.original_data:
                # Return None for empty data
                return None

            if self.sorted_data is None:
                self.sorted_data = self.original_data.copy()
                self.helper.merge_sort(self.sorted_data)

            # Return the maximum value, which is the last element of the sorted data
            return self.sorted_data[-1]
        except Exception as e:
            print(f"An error occurred while getting the maximum value: {e}")

    def get_standard_deviation(self):
        """
        This method calculates the standard deviation
        :return: The standard deviation of the data
        """
        try:
            if not self.original_data:
                # Return None for empty data
                return None

            if self.mean is None:
                self.get_mean()

            # Calculate the variance and standard deviation
            variance = self.helper.calculate_variance(self.original_data, self.mean)
            std_deviation = variance ** 0.5

            # Round the standard deviation to 2 decimal places
            return round(std_deviation, 2)
        except Exception as e:
            print(f"An error occurred while calculating the standard deviation: {e}")

    def get_mean_absolute_deviation(self):
        """
        This method calculates the mean absolute deviation
        :return: The mean absolute deviation of the data
        """
        try:
            if self.mean is None:
                self.get_mean()

            mean_absolute_deviation_value = self.helper.calculate_mean_absolute_deviation(self.original_data, self.mean)

            # Round the mean absolute deviation to 2 decimal places
            return round(mean_absolute_deviation_value, 2)
        except Exception as e:
            print(f"An error occurred while calculating the mean absolute deviation: {e}")
