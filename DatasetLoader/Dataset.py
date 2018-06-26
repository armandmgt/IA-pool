

class Example:
	entries: list
	outs: list

	def __init__(self, entries: list, outs: list):
		self.entries = entries
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
				entries = [int(x) for x in file.readline().split()]
				outs = [int(x) for x in file.readline().split()]
				self.examples.append(Example(entries, outs))
