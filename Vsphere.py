# Автор Ігор Хруневич
# Цю міні-програму створено, щоб зацікавити дітей програмуванням
# Користуйтесь, вивчайте, досліджуйте, змінюйте - експериментуйте

from math import sqrt, pi
import turtle
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

print("Розрахуйте V обєм кулі та площу її поверхні - сфери ")

r = float(input("Введіть радіус кулі R см ? = "))

print ("V кулі =  = (4/3)*Пі(3.14)*(R в кубі)")
print ("S сфери = 4*Пі(3.14)*R в квадраті")
print("V кулі = %.2f" % ((4/3)*pi * r**3))
print("S сфери = %.2f" % (4*pi*r**2))
print ("Поки Ви звіряєте свій розв'язок із розв'язком даної програми, matplotlib намалював Вам вашу кулю . Знайдіть її у себе на моніторі.")

# matplotlib
# Create a dark-themed figure
fig = plt.figure()
fig.patch.set_facecolor('white')  # Set background color to dark gray
ax = fig.add_subplot(111, projection='3d')
ax.set_facecolor('white')  # Set plot background color to dark gray

# Sphere parameters
center = (0, 0, 0)
radius = r
phi = np.linspace(0, np.pi, 100)
theta = np.linspace(0, 2 * np.pi, 100)

# Створіть сітчасту сітку для сфери
phi, theta = np.meshgrid(phi, theta)
x = center[0] + radius * np.sin(phi) * np.cos(theta)
y = center[1] + radius * np.sin(phi) * np.sin(theta)
z = center[2] + radius * np.cos(phi)

# Намалюйте сферу кольором
ax.plot_surface(x, y, z, color='grey', alpha=0.7)  # колір та прозорість

# Встановити позначки осей і колір тексту
ax.set_xlabel('X-вісь', color='black')
ax.set_ylabel('Y-вісь', color='black')
ax.set_zlabel('Z-вісь', color='black')
ax.tick_params(axis='x', colors='black')
ax.tick_params(axis='y', colors='black')
ax.tick_params(axis='z', colors='black')

# Встановіть заголовок і колір заголовка
ax.set_title('Python та Matplotlib вивели зображення Вашої сфери', color='black')

# показати малюнок
plt.show()

