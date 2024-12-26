'''Демонстрация работы ковариации и корреляции (1 способ)'''
import numpy as np
import random as r
import matplotlib.pyplot as plt

def cov(x, y):
    assert x.size == y.size
    return ((x - x.mean()) * (y - y.mean())).sum()/(x.size - 1)
# инструкции assert в Python — это булевы выражения, которые проверяют, является ли условие истинным

def cor(x, y):
    return cov(x, y)/(np.std(x, ddof=1)*np.std(y, ddof=1))

# функция имитирущая случайные факторы
# р - настолько существенным будет случайный фактор
def randomize(arr, p):
    peak_to_peak = np.max(arr) - np.min(arr)
    res = np.zeros(arr.shape)
    # функция numpy.zeros() применяется для создания нулевой матрицы
    # обращаясь к массиву через атрибут (или поле) .shape, получим размерность массива arr (тип данных: tuple)
    # т.е. получили нулевой массив такой размерности
    for i, v in enumerate(arr):
        sign = 1 if r.choice([True, False]) else -1
        res[i] = v + (sign * peak_to_peak * r.random() * p)
    # random() - функция с равномерным распределением, которая выдает рандомное число на отрезке [0, 1]
    return res

# идея в том, что изначально мы мысленно дорисовали график (x, x) - биссектриса первого координатного угла
# теперь нужен массив у, который мы будем создавать с помощью генератора случайных чисел, сдвигая вверх или вниз (sign)
# peak_to_peak - задает "коридор" значений (чтобы не вылететь за рамки)
# если р = 1, то в коридоре мы от начала до конца, а если р = 1/2 то коридор уменьшится в 2 раза
# на random домножили, чтобы шум был распределен случайным образом


x = np.array(range(30))
y = randomize(x, 0.1)
y1 = randomize(x, 0.5)
y2 = randomize(x, 1)


fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(16, 3))
ax1.scatter(x, y)
ax2.scatter(x, y1)
ax3.scatter(x, y2)
ax1.set_title('высокая корреляция')
ax2.set_title('средняя корреляция')
ax3.set_title('низкая корреляция')
plt.show()

print(f'''
cov1: {cov(x, y):.2f}
cov2: {cov(x, y1):.2f}
cov3: {cov(x, y2):.2f}

cor1: {cor(x, y):.2f}
cor2: {cor(x, y1):.2f}
cor3: {cor(x, y2):.2f}
''')


'''Демонстрация работы ковариации и корреляции (2 способ)'''
import numpy as np
import random as r
import matplotlib.pyplot as plt

n = 30
x = np.array(range(n))

# Добавим к каждой компоненте вектора икс случайный шум из нормального
# распределения (random.gauss) с разным параметром sigma (стандартное отклонение)
y1 = x + [r.gauss(mu=0, sigma=0.7) for _ in range(n)]
y2 = x + [r.gauss(mu=0, sigma=2) for _ in range(n)]
y3 = x + [r.gauss(mu=0, sigma=10) for _ in range(n)]

fig1, axes = plt.subplots(1, 3, figsize=(12, 3))
axes[0].scatter(x, y1)
axes[1].scatter(x, y2)
axes[2].scatter(x, y3)
ax1.set_title('высокая корреляция')
ax2.set_title('средняя корреляция')
ax3.set_title('низкая корреляция')
plt.show()

''' Пример расчета коэффициента корреляции '''
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import pearsonr

# Генерация данных
N = 50
x = np.random.rand(N)  # Пример генерации случайных данных для x
y = np.random.rand(N)  # Пример генерации случайных данных для y
# rand(N) возвращает N случайных чисел из равномерного распределения на [0, 1]

# Построение графика
plt.scatter(x, y, linewidth=5)
plt.xlabel('x')
plt.ylabel('y')
plt.title('График зависимости x и y')
plt.grid(True)
plt.show()


# Вычисление корреляции
pearsonr_result = pearsonr(x, y)
# На выходе функции будет объект класса PearsonRResult с двумя атрибутами:
# 1. Расчитанный коэффициент корреляции по (x, y)
# 2. p-value
# А также у объекта этого класса есть метод confidence_interval() для рассчета доверительного интервала
correlation_coefficient = pearsonr_result.correlation
p_value = pearsonr_result.pvalue
confidence_interval = pearsonr_result.confidence_interval()

print(f'Коэффициент корреляции: {correlation_coefficient}, p-значение: {p_value}')
print(f'Доверительный интервал: {confidence_interval}')