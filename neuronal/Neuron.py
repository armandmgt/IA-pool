from functools import reduce
from math import exp
from random import uniform


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
