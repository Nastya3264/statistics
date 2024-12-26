from scipy import stats
from math import sqrt

# Task 3

mean = 89.9
sd = 11.3
n = 20

# степень свободы
df = n - 1

# 95% доверительный интервал
p = 0.95
alpha = 1-p  # то, что осталось

# стандартная ошибка
se = sd/sqrt(n)
print(se)

# ppf - Percent point function
# делим на два, т.к. по умолчанию функция считает для одного конца, а нам надо для двух
t_value = stats.t(df).ppf(1-(alpha/2))
print(t_value)

# доверительный интервал
сonfidence_interval = (mean-t_value*se, mean+t_value*se)
print('[%.2f; %.2f]' % сonfidence_interval)


# Task 4
from scipy.stats import t
from numpy import sqrt

mean_m, mean_f = 45, 34
sd_m, sd_f = 9, 10

N = 100

se = sqrt((sd_m ** 2)/N + (sd_f ** 2)/N)
print(se)
t_value = (mean_m - mean_f)/se
print(t_value)

p = t.sf(t_value, N+N-2)
print(f'p={p}')
if p >= 0.05:
    print('Мы НЕ можем отклонить нулевую гипотезу')
else:
    print('Мы можем отклонить нулевую гипотезу')
