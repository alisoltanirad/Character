import numpy as np
from matplotlib import pyplot as plt
from matplotlib import tri


def triplot():
    n_angles = 34
    n_radii = 8
    min_radius = 0.21
    radii = np.linspace(min_radius, 0.95, n_radii)

    angles = np.linspace(0, 2 * np.pi, n_angles, endpoint=False)
    angles = np.repeat(angles[..., np.newaxis], n_radii, axis=1)
    angles[:, 1::2] += np.pi / n_angles

    x = (radii * np.cos(angles)).flatten()
    y = (radii * np.sin(angles)).flatten()

    triangulation = tri.Triangulation(x, y)

    triangulation.set_mask(
        np.hypot(
            x[triangulation.triangles].mean(axis=1),
            y[triangulation.triangles].mean(axis=1)) < min_radius
    )

    fig = plt.figure()
    ax = fig.add_subplot()
    ax.triplot(triangulation, 'bo-', lw=1)
    ax.set_aspect('equal')
    ax.set_title('Triplot of Delaunay Triangulation')
    plt.show()


def tripcolor():
    n_angles = 55
    n_radii = 13
    min_radius = 0.1
    radii = np.linspace(min_radius, 0.95, n_radii)

    angles = np.linspace(0, 2 * np.pi, n_angles, endpoint=False)
    angles = np.repeat(angles[..., np.newaxis], n_radii, axis=1)
    angles[:, 1::2] += np.pi / n_angles

    x = (radii * np.cos(angles)).flatten()
    y = (radii * np.sin(angles)).flatten()
    z = (np.cos(radii) * np.cos(3 * angles)).flatten()

    triangulation = tri.Triangulation(x, y)

    triangulation.set_mask(
        np.hypot(
            x[triangulation.triangles].mean(axis=1),
            y[triangulation.triangles].mean(axis=1)) < min_radius
    )

    fig = plt.figure()
    ax = fig.add_subplot()
    tpc = ax.tripcolor(triangulation, z, shading='flat')
    fig.colorbar(tpc)
    ax.set_aspect('equal')
    ax.set_title('Tripcolor of Delaunay Triangulation')
    plt.show()


if __name__ == '__main__':
    tripcolor()
