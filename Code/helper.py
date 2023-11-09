import csv
import random


class Helper:

    def __init__(self):
        pass

    def read_txt_file(self, file_path):
        """
        Read data from a text file and return it as a list of floats.

        :param file_path:Path of the file
        :return:
        """
        with open(file_path, "r") as f:
            # Read the content of the file
            data = f.read()
            # Split the data by commas
            data_list = data.split(",")
            # Convert values to float
            integer_data = [float(value.strip()) for value in data_list]
            print(integer_data)
            return integer_data

    def read_csv_file(self, file_path):
        """
        Read data from a csv file and return it as a list of floats.
        :param file_path: Path of the file
        :return:
        """
        with open(file_path, "r") as f:
            # Use csv.reader to read the CSV file
            csv_reader = csv.reader(f)

            # Convert values to float
            integer_data = [float(value.strip()) for row in csv_reader for value in row]
            return integer_data

    def calculate_mean(self, data):
        """
        Calculate the mean of a list of numbers.
        :param data: List of values
        :return: Mean of the data
        """
        if not data:
            # Return None for empty data
            return None

        sum_of_numbers = 0
        count = 0

        for number in data:
            sum_of_numbers += number
            count += 1

        # Calculate and return the mean
        return round(sum_of_numbers / count, 2)


    def calculate_variance(self,data, mean):
        """
        Calculate the variance of a list of numbers.
        :param data: List of numbers
        :param mean: Mean of data
        :return:
        """
        if not data or mean is None:
            # Return None for empty data or undefined mean
            return None

        sum_squared_diff = sum((value - mean) ** 2 for value in data)
        variance = sum_squared_diff / len(data)
        return variance


    def bubble_sort(self,data):
        """
        Sort a list of numbers in ascending order using the bubble sort algorithm.
        :param data: List of numbers
        :return:
        """
        length = len(data)

        for i in range(length):
            for j in range(0, length - i - 1):
                if data[j] > data[j + 1]:
                    # Swap elements if they are in the wrong order
                    data[j], data[j + 1] = data[j + 1], data[j]


    def calculate_mean_absolute_deviation(self,data, mean):
        """
        Calculate the mean absolute deviation (MAD) of a list of numbers from their mean.

        :param data:List of numbers
        :param mean:Mean of given data
        :return:
        """
        if not data or mean is None:
            # Return None for empty data or undefined mean
            return None

        absolute_diff_sum = 0
        count = 0

        for value in data:
            absolute_diff_sum += value - mean if value >= mean else mean - value
            count += 1

        mean_absolute_deviation = absolute_diff_sum / count
        return mean_absolute_deviation


    def generate_random_data(self):
        """
        Genrate random data ranging from 1 to 1000
        :return:
        """
        return [random.randint(1, 1000) for _ in range(1000)]
