f_1 = [19.9, 20.7, 20.5, 20.76, 22.7]
f_2 = [10.6, 10.1, 10.5, 12.62, 19.02]

mean_1 = 20.912
mean_2 = 12.568

mean_dev_1 = 0
mean_dev_2 = 0

for focus in f_1:
    mean_dev_1 += (focus - mean_1)**2

for focus in f_2:
    mean_dev_2 += (focus - mean_2)**2

mean_dev_1 = (1 / (len(f_1) - 1)) * mean_dev_1
mean_dev_2 = (1 / (len(f_1) - 1)) * mean_dev_2

print(f"Standard Deviation of the Mean of Focus 1: {mean_dev_1}")
print(f"Standard Deviation of the Mean of Focus 2: {mean_dev_2}")
