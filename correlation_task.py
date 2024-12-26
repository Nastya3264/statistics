# Чему равен коэффициент корреляции в данной выборке (попробуйте построить график для нахождения верного ответа):
#
# X Y
# 4 2
# 5 1
# 2 4
# 3 3
# 1 5

# (с помощью графика)
import matplotlib.pyplot as plt
import numpy as np

x = np.array([4, 5, 2, 3, 1])
y = np.array([2, 1, 4, 3, 5])

plt.scatter(x, y, alpha=0.5)  # alpha - прозрачность
plt.show()

# (с помощью вычислений)
# 1 способ
import pandas as pd
df = pd.DataFrame({'x': [4, 5, 2, 3, 1], 'y': [2, 1, 4, 3, 5]})
print(df.corr())

# 2 способ
import scipy.stats as stats
x = [4, 5, 2, 3, 1]
y = [2, 1, 4, 3, 5]
print(stats.pearsonr(x, y))



