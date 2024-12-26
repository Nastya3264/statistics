# Имитация доски Гальтона в коде

import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt

data = dict()
# количество шариков
N = 10000
# количество уровней
level = 20
for _ in range(N):
    index = 0
    for _ in range(level):
        index += np.random.choice([-1, 1])
    data.setdefault(index, 0)
# Метод setdefault возвращает элемент словаря по указанному ключу.
# Если такого ключа нет, то в словарь запишется указанный ключ и значение по умолчанию, и вернется это значение.
# В первом параметре метода указываем нужный нам ключ, во втором необязательном параметре - значение по умолчанию.
    data[index] += 1
sns.barplot(x=list(data.keys()), y=list(data.values()))
plt.show()
