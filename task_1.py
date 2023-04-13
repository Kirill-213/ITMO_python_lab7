# Vasilev Kirill, ISU: 367964, group: R3135. variant: 4
import numpy as np
import random
from time import perf_counter

# задаём начальное время
time_start = perf_counter()

# задаём переменные
mass_1 = []
mass_2 = []
mass_3 = []
million = 1_000_000

# перемножение списков без numpy
for i in range(million):
    # заполнение списков
    mass_1.append(random.randint(1, million))
    mass_2.append(random.randint(1, million))
    # перемножение списков
    mass_3.append(mass_1[i] * mass_2[i])

time_now = perf_counter() - time_start
print(time_now, 'сек, обычное перемножение')


# перемножение списков через numpy

time_now = perf_counter()
# заполнение списков
mass_1 = np.random.randint(0, million, million)
mass_2 = np.random.randint(0, million, million)
# перемножение списков
product = np.multiply(mass_1, mass_2)

print(perf_counter() - time_now, 'сек, numpy')
