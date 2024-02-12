import matplotlib.pyplot as plt
import numpy as np


def draw_3d_fractal(ax, center, radius, depth):
    if depth == 0:
        return
    else:
        u = np.linspace(0, 2 * np.pi, 100)
        v = np.linspace(0, np.pi, 50)
        x = center[0] + radius * np.outer(np.cos(u), np.sin(v))
        y = center[1] + radius * np.outer(np.sin(u), np.sin(v))
        z = center[2] + radius * np.outer(np.ones(np.size(u)), np.cos(v))

        ax.plot_surface(x, y, z, color='b', alpha=0.3)

        new_radius = radius * 0.6
        new_depth = depth - 1

        for i in range(6):
            angle = i * (np.pi / 3)
            new_center = center + np.array([new_radius * np.cos(angle), new_radius * np.sin(angle), 0])
            draw_3d_fractal(ax, new_center, new_radius, new_depth)


def main():
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.grid(False)

    center = np.array([0, 0, 0])
    radius = 1.0
    depth = 3

    draw_3d_fractal(ax, center, radius, depth)

    plt.show()


if __name__ == "__main__":
    main()
