# Мода, медиана и среднее

# 1. Расчет медианы, среднего и моды с помощью numpy
import numpy as np
sample = np.array([185, 175, 170, 169, 171, 175, 157, 172, 170, 172, 167, 173, 168, 167, 166,
              167, 169, 172, 177, 178, 165, 161, 179, 159, 164, 178, 172, 170, 173, 171])
print('median:', np.median(sample))
print('mean:', np.mean(sample))

vals, counts = np.unique(sample, return_counts = True) # ищем уникальные значения и их количество
mode_value = np.argwhere(counts == np.max(counts))
print('mode:', *vals[mode_value].flatten().tolist(), 'count:', np.max(counts)) # flatten() возвращает копию массива, свернутую в одно измерение


# 2. Расчет моды с помощью scipy
from scipy import stats
print('mode:', stats.mode(sample))

# 3. Расчет медианы, среднего и моды с помощью pandas
import pandas as pd
sample = pd.Series([185, 175, 170, 169, 171, 175, 157, 172, 170, 172, 167, 173, 168, 167, 166,
              167, 169, 172, 177, 178, 165, 161, 179, 159, 164, 178, 172, 170, 173, 171])
# series - структура, используемая для работы с последовательностью одномерных данных
# дополнительно: Dataframe — более сложная и подходит для нескольких измерений
print('mode:', sample.mode())
print('median:', sample.median())
print('mean:', sample.mean())
