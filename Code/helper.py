import csv
import random


class Helper:

    def __init__(self):
        pass

    def read_txt_file(self, file_path):
        integer_data = []
        with open(file_path, "r") as f:
            data = f.read()
            data_list = data.split(",")
            integer_data = [int(value.strip()) for value in data_list]
        print(integer_data)
        return integer_data

    def read_csv_file(self, file_path):
        integer_data = []
        with open("random_data.csv", "r") as f:
            # Use csv.reader to read the CSV file
            csv_reader = csv.reader(f)

            # Assuming each row contains a single value, use list comprehension to convert each value to an integer
            integer_data = [int(value.strip()) for row in csv_reader for value in row]
        return integer_data

    def calculate_mean(self, data):
        if not data:
            return None  # Return None for empty data

        sum_of_numbers = 0
        count = 0

        for number in data:
            sum_of_numbers += number
            count += 1

        return round(sum_of_numbers / count, 2)


    def calculate_variance(self,data, mean):
        if not data or mean is None:
            return None  # Return None for empty data or undefined mean

        sum_squared_diff = sum((value - mean) ** 2 for value in data)
        variance = sum_squared_diff / len(data)
        return variance


    def bubble_sort(self,data):
        length = len(data)

        for i in range(length):
            for j in range(0, length - i - 1):
                if data[j] > data[j + 1]:
                    data[j], data[j + 1] = data[j + 1], data[j]


    def calculate_mean_absolute_deviation(self,data, mean):
        if not data or mean is None:
            return None  # Return None for empty data or undefined mean

        absolute_diff_sum = 0
        count = 0

        for value in data:
            absolute_diff_sum += value - mean if value >= mean else mean - value
            count += 1

        mad = absolute_diff_sum / count
        return mad


    def generate_random_data(self):
        return [random.randint(1, 1000) for _ in range(1000)]
