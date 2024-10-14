def mean(data):
    return sum(data) / len(data)

x_values = [0.3, 0.35, 0.41, 0.45, 0.56, 0.65, 0.7, 0.79, 0.825]
y_values = [1.28, 1.42, 1.64, 1.66, 2.25, 2.62, 2.96, 3.17, 3.20]

avg_x = mean(x_values)
avg_y = mean(y_values)

xx = []
yy = []

for value in x_values:
    xx.append((avg_x - value)**2)

for idx, value in enumerate(y_values):
    yy.append((avg_x - x_values[idx]) * (avg_y - value))

sum_xx = sum(xx)
sum_yy = sum(yy)

regression_slope = round(sum_yy / sum_xx, 5)

print(f"Correlation Coefficient: {regression_slope}")
