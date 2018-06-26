import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

from DatasetLoader.Dataset import Dataset


def run():
	figure = plt.figure()
	ax = figure.add_subplot(111, projection='3d')
	ds = Dataset('datasets/xor.ds')
	xvalues = []
	yvalues = []
	zvalues = []
	for example in ds.examples:
		print(example.entries)
		xvalues.append(example.entries[0])
		yvalues.append(example.entries[1])
		zvalues.append(example.outs[0])
	ax.scatter(xvalues, yvalues, zvalues)
	plt.show()


if __name__ == '__main__':
	run()
