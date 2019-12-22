from matplotlib import pyplot as plt
import numpy as np
import os


if __name__ == '__main__':
    def y(x):
        return 3*x + 2

    X = np.linspace(0, 10, 1_000)

    plt.plot(X, y(X), c="r", label="y curve")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.grid()
    plt.legend()
    plt.savefig(os.getcwd()+"/mcint_exemple_y.png", dpi=300)
    plt.show()

    # generate 100 random points
    X_rn = np.random.uniform(0, 10, 100)

    # evaluate y for X_rn
    Y = y(X_rn)

    # generate 100 y random points
    Y_rn = np.random.uniform(np.min(Y), np.max(Y), 100)

    in_ensemble: list = list()
    out_ensemble: list = list()

    for i, x in enumerate(X_rn):
        y_ref = y(x)
        if Y_rn[i] <= y_ref:
            in_ensemble.append([x, Y_rn[i]])
        else:
            out_ensemble.append([x, Y_rn[i]])

    plt.plot(X, y(X), c="r", label="y curve")
    plt.scatter(np.array(in_ensemble)[:, 0], np.array(in_ensemble)[:, 1], label="random points in the curve")
    plt.scatter(np.array(out_ensemble)[:, 0], np.array(out_ensemble)[:, 1], label="random points out of the curve")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.grid()
    plt.legend()
    plt.savefig(os.getcwd() + "/mcint_exemple_y_with_random_points.png", dpi=300)
    plt.show()

    count_in_curve: int = len(in_ensemble)
    print(f"count_in_curve = {count_in_curve}")
    n_samples: int = 100
    A = 10 * (y(10) - y(0))
    print(f"P = {(count_in_curve/n_samples) * A}")