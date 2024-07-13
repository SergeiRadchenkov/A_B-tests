import scipy.stats as stats
import numpy as np

# Параметры задачи
current_bounce_rate = 0.40  # текущий bounce rate
effect_size = 0.20  # предполагаемое изменение в 20%
alpha = 0.05  # уровень значимости
beta = 0.20  # мощность теста (1 - beta)
daily_traffic = 4000 * 0.05  # 5% от среднего трафика в день

# Конвертируем bounce rate в проценты
p1 = current_bounce_rate
p2 = current_bounce_rate * (1 - effect_size)
pooled_p = (p1 + p2) / 2

# Рассчет минимального числа пользователей, необходимого для эксперимента
z_alpha = stats.norm.ppf(1 - alpha / 2)
z_beta = stats.norm.ppf(1 - beta)

sample_size_per_group = (z_alpha + z_beta) ** 2 * pooled_p * (1 - pooled_p) / (p1 - p2) ** 2
sample_size_per_group = np.ceil(sample_size_per_group)

# Рассчет количества дней
days_needed = sample_size_per_group * 2 / daily_traffic  # умножаем на 2, так как у нас две группы
days_needed = np.ceil(days_needed)

print(days_needed)
