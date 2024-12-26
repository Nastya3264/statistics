import pandas as pd
from scipy.stats import t
import matplotlib.pyplot as plt

#выставляем уровень значимости
p = 0.95

#обрабатываем сырые данные из csv файла, находим объем, среднее и стандартное отклонение выборки
data = pd.read_csv("..//genetherapy.csv", sep=',')
print(data)

data_agg = data.groupby(['Therapy']).agg(['count', 'mean', 'std'])
print(data_agg)

# для каждой выборки высчитываем доверительный интервал по формуле для t-распределения: (K * se), где
# коэффициент K t-value, зависит от степеней свободы df = n-1 и целевого значения вероятности p,
# se - стандартная ошибка среднего = std/sqrt(n), std - стандартное отклонение выборки, n - количество элементов
K = t.ppf((1 + p)/2, data_agg['expr']['count']-1)
se = data_agg['expr']['std']/(data_agg['expr']['count'] ** .5)
data_agg['interval'] = K * se

# строим доверительные интервалы с помощью ErrorBar
plt.errorbar(x='Therapy ' + data_agg.index, y=data_agg['expr']['mean'], yerr=data_agg['interval'], color='black',
             capsize=3,  markersize=4, mfc="red", mec="black", fmt ='o')
plt.title('Уровень экспрессии гена при различной терапии')
plt.grid()
plt.xlabel('Therapy')
plt.ylabel('Уровень экспрессии')
plt.show()