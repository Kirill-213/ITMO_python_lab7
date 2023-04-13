
import pandas as pd
import matplotlib.pyplot as plt

# читаем csv файл
file = pd.read_csv('data2.csv', delimiter=',')
data = file['Hardness']
# выводим среднеквадратичное отклонение
print(round(data.std(), 2), 'среднеквадратичное отклонение')

# создаём объект fig
fig = plt.figure()
# создаём 2 гистограммы
gs = fig.add_gridspec(2, hspace = 1)
axes = gs.subplots()

# вводим обозначения для 1й гистограммыvalue
axes[0].hist(data, bins = 80)
axes[0].set_title('Hardness')
axes[0].set_xlabel('number')
axes[0].set_ylabel('value')

# вводим обозначения для 2й гистограммыvalue
axes[1].hist(data,bins = 80, density=True)
axes[1].set_title('Normalized hardness')
axes[1].set_xlabel('number')
axes[1].set_ylabel('value')

# выводим гистограммы на экран
plt.show()









