import matplotlib.pyplot as plt
import numpy as np

def draw_circle_fractal_3d(ax, x, y, z, size, depth, count):
    min_size = 5
    m = 6
    n = 3

    if size > min_size:
        s1 = size / n
        s2 = size * (n - 1) / n

        # Рисуем центральную окружность перед циклом
        u = np.linspace(0, 2 * np.pi, 100)
        v = np.linspace(0, np.pi, 50)
        x_circle = x + size * np.outer(np.cos(u), np.sin(v))
        y_circle = y + size * np.outer(np.sin(u), np.sin(v))
        z_circle = z + size * np.outer(np.ones(np.size(u)), np.cos(v))
        ax.plot_surface(x_circle, y_circle, z_circle, color='b', alpha=0.5)

        for i in range(1, m + 1):
            new_x = x - s2 * np.sin(2 * np.pi / m * i)
            new_y = y + s2 * np.cos(2 * np.pi / m * i)

            draw_circle_fractal_3d(ax, new_x, new_y, z, s1, depth - 1, count)

def fractal_3d_main():
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.set_title('3D Circle Fractal')

    x, y, z, initial_size, initial_depth, circles_count = 0, 0, 0, 20, 3, 5

    draw_circle_fractal_3d(ax, x, y, z, initial_size, initial_depth, circles_count)

    plt.show()

if __name__ == "__main__":
    fractal_3d_main()
