import math

with open("focus_2.txt", 'r') as f:
    data = f.read().splitlines()

data = list(map(float, data))

mean = sum(data) / len(data)
print(f"Mean: {mean}")

mod_data = [(value - mean)**2 for value in data]
print(f"Modified data: {mod_data}")

std_dev = sum(mod_data) / (len(mod_data) - 1)
print(f"Standard Deviation: {std_dev}")

std_dev_mean = std_dev / math.sqrt(len(mod_data))
print(f"Standard Deviation of Mean: {std_dev_mean}")
