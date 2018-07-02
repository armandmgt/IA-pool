import matplotlib.pyplot as plt


if __name__ == '__main__':
	data_x = [-2, -1, 0, 1, 2.5, 3.5, 4, 5, 6, 7]
	data_y = [202.5, 122.5, 62.5, 22.5, 0, 10.0, 22.5, 62.5, 122.5, 202.5]
	data_der = [-45, -35, -25, -15, 0, 10, 15, 25, 35, 45]

	for x, y, d in zip(data_x, data_y, data_der):
		plt.plot(x, y, marker='x', color='red' if d < 0 else 'blue')
	plt.show()
