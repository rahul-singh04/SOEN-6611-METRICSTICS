import random


# def calculate_mean(data, index=0, current_sum=0):
#     if not data or index >= len(data):
#         if index == 0:
#             return None  # Return None for empty data
#         return current_sum / index
#
#     current_sum += data[index]
#     return calculate_mean(data, index + 1, current_sum)

def calculate_mean(data):
    if not data:
        return None  # Return None for empty data

    sum_of_numbers = 0
    count = 0

    for number in data:
        sum_of_numbers += number
        count += 1

    return round( sum_of_numbers / count,2)


def calculate_variance(data, mean):
    if not data or mean is None:
        return None  # Return None for empty data or undefined mean

    sum_squared_diff = sum((value - mean) ** 2 for value in data)
    variance = sum_squared_diff / len(data)
    return variance


def bubble_sort(data):
    length = len(data)

    for i in range(length):
        for j in range(0, length - i - 1):
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]


def calculate_mad(data, mean):
    if not data or mean is None:
        return None  # Return None for empty data or undefined mean

    absolute_diff_sum = 0
    count = 0

    for value in data:
        absolute_diff_sum += value - mean if value >= mean else mean - value
        count += 1

    mad = absolute_diff_sum / count
    return mad


def generate_random_data():
    return [random.randint(1, 1000) for _ in range(1000)]
