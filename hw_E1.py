import matplotlib.pyplot as plt
import numpy as np
lam,size = 5, 20000
s = np.random.poisson(lam,size)
count, bins, _, = plt.hist(s, 100, density=True)
plt.show()