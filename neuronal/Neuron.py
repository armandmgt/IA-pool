from functools import reduce
from math import exp, log
from random import uniform

from datasetloader.Dataset import Dataset


def sigmoid(x: float) -> float:
	return 1 / (1 + exp(-x))


class Neuron:
	ins: [float]
	weights: [float]
	out: float

	def __init__(self, nb_ins: int):
		self.weights = [uniform(-2, 2) for _ in range(nb_ins + 1)]

	def activate(self, entries: [float]) -> None:
		sp = reduce(self.ponderate, zip(entries, self.weights[1:]), self.weights[0])
		self.out = sigmoid(sp)

	@staticmethod
	def ponderate(acc: float, e: (float, float)) -> float:
		return acc + e[0] * e[1]

	def calc_loss(self, ds: Dataset) -> float:
		ds.normalize()
		loss = 0
		for e in ds.examples:
			self.activate(e.ins)
			loss += self.loss_func(e.outs, [self.out])
		return loss / len(ds.examples)

	@staticmethod
	def loss_func(yrange: [float], hxrange: [float]) -> float:
		return -sum([
			(y * log(hx) + (1 - y) * log(1 - hx)) for y, hx in zip(yrange, hxrange)
		])
