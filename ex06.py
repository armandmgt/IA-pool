from tkinter import *

from neuronal.NeuralNetwork import NeuralNetwork

entries = [[0, 0, 0], [0, 1, 1], [1, 0, 0], [1, 1, 1]]
nn = NeuralNetwork([3, 5, 5, 2])


def test():
	i = 0
	for l in nn.layers[1:]:
		for n in l:
			for w in range(len(n.weights)):
				n.weights[w] = scales[i].get()
				i += 1
	for e, (o, ov) in zip(entries, outs):
		nn.activate(e)
		ov.set(nn.layers[-1][0].out)
		o.set('True' if nn.layers[-1][0].out >= 0.5 else 'False')


window = Tk()

scales = []
for layer, x in zip(nn.layers[1:], range(1, len(nn.layers))):
	lframe = LabelFrame(window, text=f'layer: {x}', borderwidth=2)
	lframe.pack(fill='x', padx=6, pady=2)
	for neuron, y in zip(layer, range(len(layer))):
		nframe = LabelFrame(lframe, text=f'neuron: {y}')
		nframe.pack(padx=6, pady=2)
		for weight, z in zip(neuron.weights, range(len(neuron.weights))):
			wframe = Frame(nframe)
			wframe.pack()
			Label(wframe, text=f'weight: {z}').pack(side=LEFT, padx=6)
			sc = Scale(wframe, from_=-2, to=2, resolution=0.1, orient=HORIZONTAL, length=400)
			sc.pack(side=LEFT)
			scales.append(sc)

outs = []
for ex in entries:
	rframe = LabelFrame(window, text='Results')
	rframe.pack(padx=10, pady=2, side=LEFT)
	out = StringVar()
	outval = IntVar()
	outdisp = Label(rframe, textvariable=out).pack(side=LEFT)
	outvaldisp = Label(rframe, textvariable=outval).pack(side=RIGHT)
	outs.append((out, outval))


test_btt = Button(window, text='Compute', command=test)
test_btt.pack(side=RIGHT)


if __name__ == '__main__':
	window.mainloop()
