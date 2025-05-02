# Импортируем модуль pyplot из библиотеки matplotlib, который используется для создания графиков и визуализаций
import matplotlib.pyplot as plt
# Импортируем модуль nile из библиотеки statsmodels.datasets, который содержит набор данных о годовом расходе воды в реке Нил
from statsmodels.datasets import nile

data = nile.load_pandas().data

# Устанавливаем столбец 'year' (год) в качестве индекса DataFrame.
data.set_index('year', inplace=True)

# Создаем новое окно для графика 
plt.figure(figsize=(10, 6))

# По оси x будет индекс DataFrame (год), а по оси y - значения из столбца 'volume' (годовой расход воды).
plt.plot(data['volume'], label='Годовой расход воды в реке Нил')


plt.title('Годовой расход воды в реке Нил (1871-1970)')
plt.xlabel('Год')
plt.ylabel('Годовой расход воды (кубические гектометры)')

plt.legend()

# Включаем отображение сетки на графике для облегчения чтения значений.
plt.grid(True)

plt.show()

