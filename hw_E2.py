import numpy as np
a, m = 3, 2  # shape and mode
s = (np.random.pareto(a, 1000) + 1) * m
import matplotlib.pyplot as plt
count, bins, _ = plt.hist(s, 100, density=True)
fit = a*m**a / bins**(a+1)
plt.plot(bins, max(count)*fit/max(fit), linewidth=2, color='r')
plt.show()