import numpy as np
import matplotlib.pyplot as plt

# создаём объект fig
fig = plt.figure()

ax = plt.axes(projection ='3d')

# определяем значение для каждой из оси
x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)
z = np.sin(x * y)

# вывод на экран
ax.plot3D(x, y, z, 'green')
ax.set_title('3D chart
plt.show()
