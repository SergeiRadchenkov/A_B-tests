import numpy as np
from scipy import stats

# Данные
n1 = 15550
n2 = 15550
conversions1 = 164
conversions2 = 228

# Конверсии
conv1 = conversions1 / n1
conv2 = conversions2 / n2

# Объединенная пропорция
p_pool = (conversions1 + conversions2) / (n1 + n2)

# Стандартная ошибка
SE = np.sqrt(p_pool * (1 - p_pool) * (1/n1 + 1/n2))

# Z-статистика
Z = (conv1 - conv2) / SE

# p-value
p_value = 2 * (1 - stats.norm.cdf(abs(Z)))

print(f'Z-статистика: {Z}')
print(f'p-value: {p_value}')

# Интерпретация результатов
alpha = 0.05
if p_value < alpha:
    print("Статистически значимые различия обнаружены.")
else:
    print("Статистически значимые различия не обнаружены.")
