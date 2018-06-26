from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

from DatasetLoader.Dataset import Dataset


def run():
	figure = plt.figure()
	ax = figure.add_subplot(111, projection='3d')
	ds = Dataset('datasets/xor.ds')
	ds.normalize()
	x = []
	y = []
	z = []
	for example in ds.examples:
		x.append(example.ins[0])
		y.append(example.ins[1])
		z.append(example.outs[0])
	ax.scatter(x, y, z)
	plt.show()


if __name__ == '__main__':
	run()
