from math import sqrt

from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

from DatasetLoader.Dataset import Dataset, Example


def compute_distance(e1: Example, e2: Example) -> float:
	return sqrt(sum([(q - p)**2 for q, p in zip(e1.ins, e2.ins)]))


def run():
	ds = Dataset('datasets/ex00.ds')
	for e in ds.examples:
		point = 'bx' if e.outs[0] == 1 else 'rx'
		plt.plot(e.ins[0], e.ins[1], point)
	plt.show()


if __name__ == '__main__':
	run()
