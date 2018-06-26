import operator
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


def get_most_present_cat(examples: [Example]) -> int:
	counts = {}
	for e in examples:
		if e.outs[0] in counts.keys():
			counts[e.outs[0]] += 1
		else:
			counts[e.outs[0]] = 1
	return max(counts.items(), key=operator.itemgetter(1))[0]


def run():
	train_ds = Dataset('datasets/trainWine.ds')
	test_ds = Dataset('datasets/testWine.ds')
	colors = ['', 'red', 'blue', 'green']
	plt.subplot(2, 1, 1)
	for e in train_ds.examples:
		plt.plot(e.ins[0], e.ins[1], color=colors[int(e.outs[0])], marker='o')
	plt.subplot(2, 1, 2)
	for e in test_ds.examples:
		nearests = get_nearest_neighbors(e, train_ds, 1)
		most_present = get_most_present_cat(nearests)
		plt.plot(e.ins[0], e.ins[1], color=colors[int(most_present)], marker='x')
	plt.show()


if __name__ == '__main__':
	run()
