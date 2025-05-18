import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D

def f(x1, x2):
    w1 = 1 + (x1 - 1) / 4
    w2 = 1 + (x2 - 1) / 4
    term1 = np.sin(np.pi * w1) ** 2
    term2 = (w1 - 1) ** 2 * (1 + 10 * np.sin(np.pi * w1 + 1) ** 2)
    term3 = (w2 - 1) ** 2 * (1 + np.sin(2 * np.pi * w2) ** 2)
    return term1 + term2 + term3

x1_min, x1_max = -10.0, 10.0
x2_min, x2_max = -10.0, 10.0
x10, x20 = 1.0, 1.0  

x1 = np.linspace(x1_min, x1_max, 200)
x2 = np.linspace(x2_min, x2_max, 200)
X1, X2 = np.meshgrid(x1, x2)
Z = f(X1, X2)

fig = plt.figure(figsize=(16, 12))
fig.suptitle('Графики функции f(x1, x2)', fontsize=16)

ax1 = fig.add_subplot(221, projection='3d')
ax1.plot_surface(X1, X2, Z, cmap=cm.viridis)
ax1.set_title('1. 3D поверхность (изометрический вид)')
ax1.set_xlabel('x1')
ax1.set_ylabel('x2')
ax1.set_zlabel('f(x1, x2)')

ax2 = fig.add_subplot(222)
contour = ax2.contourf(X1, X2, Z, levels=30, cmap=cm.viridis)
plt.colorbar(contour, ax=ax2)
ax2.set_title('2. Вид сверху (контурный график)')
ax2.set_xlabel('x1')
ax2.set_ylabel('x2')

ax3 = fig.add_subplot(223)
y_x1 = f(x1, x20)
ax3.plot(x1, y_x1)
ax3.set_title(f'3. График y = f(x1) при x2 = {x20}')
ax3.set_xlabel('x1')
ax3.set_ylabel('f(x1, x2)')
ax3.grid(True)

ax4 = fig.add_subplot(224)
y_x2 = f(x10, x2)
ax4.plot(x2, y_x2)
ax4.set_title(f'4. График y = f(x2) при x1 = {x10}')
ax4.set_xlabel('x2')
ax4.set_ylabel('f(x1, x2)')
ax4.grid(True)

plt.tight_layout()
plt.subplots_adjust(top=0.92)

plt.show()
