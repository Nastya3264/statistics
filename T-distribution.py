'''График показывает, как меняется форма распределения при увеличении количества степеней свободы
А также показывает приближение t-распредееления к нормальному по мере увеличения степеней свободы '''

from scipy.stats import t, norm
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-5, 5, 100)
y1, y2, y3, y4 = t.pdf(x, df=1), t.pdf(x, df=3), t.pdf(x, df=8), t.pdf(x, df=30)
y5 = norm.pdf(x)

plt.title('Графики t-распределения с разными степенями свободы')
plt.plot(x, y1)
plt.plot(x, y2)
plt.plot(x, y3)
plt.plot(x, y4)
plt.plot(x, y5, 'r:') # красная пунктирная линия
plt.legend(('df=1', 'df=3', 'df=8', 'df=30', 'norm'))
plt.show()
