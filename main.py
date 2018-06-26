from math import sqrt

from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

from DatasetLoader.Dataset import Dataset, Example


def compute_distance(e1: Example, e2: Example) -> float:
	return sqrt(sum([(q - p)**2 for q, p in zip(e1.ins, e2.ins)]))


def get_nearest_neighbors(e: Example, train_ds: Dataset, k: int) -> [Example]:
	distances = [(compute_distance(e, te), te) for te in train_ds.examples]
	distances = sorted(distances, key=lambda t: t[0])[:k]
	distances, trains = zip(*distances)
	return trains


def run():
	ds = Dataset('datasets/ex03.ds')
	for e in ds.examples:
		point = 'bx' if e.outs[0] == 1 else 'rx'
		plt.plot(e.ins[0], e.ins[1], point)
	nearest = get_nearest_neighbors(Example([0.4, 0.4], [0]), ds, 3)
	print(nearest)
	plt.show()


if __name__ == '__main__':
	run()
