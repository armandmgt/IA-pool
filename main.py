import numpy as np
import matplotlib.pyplot as mpl

xrange = np.linspace(-10, 10)
yrange = 1 / (1 + np.exp(-1 * xrange))


def run():
	mpl.plot(xrange, yrange)
	mpl.show()


if __name__ == '__main__':
	run()
