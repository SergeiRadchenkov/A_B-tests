import scipy.stats as stats
import numpy as np

# Параметры задачи
current_time_spent = 25  # минут
std_dev = 156  # стандартное отклонение
effect_size = 0.10  # предполагаемое изменение в 10%
alpha = 0.05  # уровень значимости
beta = 0.20  # мощность теста (1 - beta)
daily_traffic = 20000 * 0.05  # 5% от среднего трафика в день

# Рассчет минимального числа пользователей, необходимого для эксперимента
effect = current_time_spent * effect_size
z_alpha = stats.norm.ppf(1 - alpha / 2)
z_beta = stats.norm.ppf(1 - beta)

sample_size_per_group = ((z_alpha + z_beta) * std_dev / effect) ** 2
sample_size_per_group = np.ceil(sample_size_per_group)

# Рассчет количества дней
days_needed = sample_size_per_group * 2 / daily_traffic  # умножаем на 2, так как у нас две группы
days_needed = np.ceil(days_needed)

print(days_needed)
