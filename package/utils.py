import numpy as np
import matplotlib.pyplot as plt


def gauss():
    """
    Demo gaussian rv
    """
    x = np.random.normal(0, 1, 1000)
    plt.figure()
    plt.hist(x)
    plt.show()
