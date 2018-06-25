

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
			for x in range(self.nbExamples):
				self.examples.append(Example(file.readline().split(), file.readline().split()))
