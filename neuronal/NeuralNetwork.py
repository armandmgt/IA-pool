from neuronal.Neuron import Neuron


class NeuralNetwork:
	layers: [[Neuron]] = []

	def __init__(self, layers: [int]):
		prev = 0
		for n in layers:
			print(f'init layer of {n} neurons with {prev} connections')
			self.layers.append([Neuron(prev) for _ in range(n)])
			prev = n

	def activate(self, entries: [float]) -> None:
		inputs = entries
		for layer in self.layers[1:]:
			print(f'activating NN: input {inputs}')
			for neuron in layer:
				print(f'neuron weights {neuron.weights}')
				neuron.activate(inputs)
			inputs = [neuron.out for neuron in layer]
