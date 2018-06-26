from functools import reduce
from math import sqrt


class Example:
	ins: list
	outs: list

	def __init__(self, ins: list, outs: list):
		self.ins = ins
		self.outs = outs


class Dataset:
	nbExamples: int
	nbEntries: int
	nbOuts: int
	examples: list

	def __init__(self, filename: str):
		self.examples = []
		with open(filename) as file:
			self.nbExamples, self.nbEntries, self.nbOuts = file.readline().split()
			self.nbExamples = int(self.nbExamples)
			self.nbEntries = int(self.nbEntries)
			self.nbOuts = int(self.nbOuts)
			for i in range(self.nbExamples):
				ins = [int(x) for x in file.readline().split()]
				outs = [int(x) for x in file.readline().split()]
				self.examples.append(Example(ins, outs))

	def normalize(self) -> None:
		mean_in, mean_out = self.compute_means()
		devi_ins, devi_outs = self.compute_deviations(mean_in, mean_out)
		for e in self.examples:
			map(lambda x: (x - mean_in) / devi_ins, e.ins)
			map(lambda x: (x - mean_out) / devi_outs, e.outs)

	def compute_means(self) -> (float, float):
		ins = reduce(self.concat_ins, self.examples, [])
		outs = reduce(self.concat_outs, self.examples, [])
		ins_mean = sum(ins) / self.nbEntries
		outs_mean = sum(outs) / self.nbOuts
		return ins_mean, outs_mean

	def compute_deviations(self, ins_mean: float, outs_mean: float) -> (float, float):
		ins = reduce(self.concat_ins, self.examples, [])
		outs = reduce(self.concat_outs, self.examples, [])
		return (
			sqrt(sum(map(lambda x: (x - ins_mean)**2, ins)) / self.nbEntries),
			sqrt(sum(map(lambda x: (x - outs_mean)**2, outs)) / self.nbOuts)
		)

	@staticmethod
	def concat_ins(l: list, e: Example) -> list:
		l.extend(e.ins)
		return l

	@staticmethod
	def concat_outs(l: list, e: Example) -> list:
		l.extend(e.outs)
		return l
