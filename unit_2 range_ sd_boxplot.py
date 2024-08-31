# 1. Расчет размаха

import numpy as np
sample = np.array([185, 175, 170, 169, 171, 175, 157, 172, 170, 172, 167, 173, 168, 167, 166,
              167, 169, 172, 177, 178, 165, 161, 179, 159, 164, 178, 172, 170, 173, 171])

# The name "ptp" of the function comes from the acronym for ‘peak to peak’
print(f'Range: {np.ptp(sample)} is equal max - min: {np.max(sample)- np.min(sample)}')

# 2. Расчет стандартного отклонения
# ddof - Delta Degrees of Freedom
print(f'Standard deviation: {np.std(sample, ddof=1):.1f}')

# (способ расчета через цикл for)
sum_deviation = 0
for x in sample:
    sum_deviation += (x - np.mean(sample)) ** 2
print(sum_deviation)

print(np.sqrt(sum_deviation/len(sample)))
print(np.sqrt(sum_deviation/(len(sample)-1)))

# (способ расчета через матрично-векторные вычисления)
X = np.array([185, 175, 170, 169, 171, 175, 157, 172, 170, 172, 167, 173, 168, 167, 166,
              167, 169, 172, 177, 178, 165, 161, 179, 159, 164, 178, 172, 170, 173, 171])
n = len(sample)
m = np.mean(sample)

print(np.sqrt(np.dot((X - m), (X - m)) / (n-1)))


# 3. Построение box-plot
import matplotlib.pyplot as plt

plt.boxplot(sample, showfliers=1) # показывает выбросы
plt.show()