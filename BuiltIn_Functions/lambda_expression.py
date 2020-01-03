if __name__ == '__main__':
    f = lambda x: 2*x + 1
    print(f(2))

    g = lambda x, y, z: x + y + z
    print(g(1, 2, 3))

    h = lambda iterable: sum(iterable)
    print(h([i for i in range(10)]))

    def Y(m: float, b: float):
        return lambda x: m*x + b


    y = Y(5, 1)
    print(type(y))
    print(y(2))
