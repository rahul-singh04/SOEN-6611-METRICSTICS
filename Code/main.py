import csv
import helper
from data_processor import DataProcessor

data1 = helper.generate_random_data()

# with open("list.txt", "r") as f:
#     data = f.read()
#     data_list = data.split(",")
#     integer_data = [int(value.strip()) for value in data_list]
#
# print(integer_data)

with open("random_data.csv", "r") as f:
    # Use csv.reader to read the CSV file
    csv_reader = csv.reader(f)

    # Assuming each row contains a single value, use list comprehension to convert each value to an integer
    integer_data = [int(value.strip()) for row in csv_reader for value in row]

data_processor = DataProcessor(integer_data)

mean_value = data_processor.mean()
median_value = data_processor.median()
mode_value = data_processor.mode()
min_value = data_processor.min_value()
max_value = data_processor.max_value()
std_deviation = data_processor.standard_deviation()
mean_abs_dev = data_processor.mad()
print("Mean:", mean_value)
print("Median: ", median_value)
print("Mode: ", mode_value)
print("min_value: ", min_value)
print("max_value: ", max_value)
print("std_deviation: ", std_deviation)
print("mad :", mean_abs_dev)
