# Автор Ігор Хруневич
# Цю міні-програму створено, щоб зацікавити дітей програмуванням
# Користуйтесь, вивчайте, досліджуйте, змінюйте - експериментуйте

from math import sqrt, pi
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import sys
from vispy import scene
from vispy.visuals.transforms import STTransform

print("Розрахуйте V обєм кулі та площу її поверхні - сфери ")
r = float(input("Введіть радіус кулі R см ? = "))
print("V кулі = %.2f" % ((4/3)*pi * r**3))
print("S сфери = %.2f" % (4*pi*r**2))
print ("Поки Ви звіряєте свій розв'язок, дана програма виведе Вам зображення вашої кулі ")
print("У графічному сервісі\n1-Matplotlib\n2-VisPy")
figure = input("Оберіть графічний сервіс : ")
if figure == '1':
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

elif figure == '2':
    canvas = scene.SceneCanvas(keys='interactive', bgcolor='white',
                           size=(r*40+200, r*40+200), show=True)
    view = canvas.central_widget.add_view()
    view.camera = 'arcball'
    sphere= scene.visuals.Sphere(radius=r, method='ico', parent=view.scene,
                               edge_color='yellow')
    view.camera.set_range(x=[-3, 3])

    if __name__ == '__main__' and sys.flags.interactive == 0:
        canvas.app.run()

else:
    print("Помилка введення ???")
        



