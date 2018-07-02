from numpy.ma import log

outs = [0, 1]
results = [0.8, 0.4]


def loss(yrange: [float], hxrange: [float]) -> float:
	return -sum([
		(y * log(hx) + (1 - y) * log(1 - hx)) for y, hx in
		zip(yrange, hxrange)
	])


print(loss(outs, results))
