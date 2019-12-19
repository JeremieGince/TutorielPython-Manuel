import numpy as np
import itertools


def monte_carlo_integration(integrand, bounds: list, domainsize=(0.0, 1.0), n_sample: int = int(1e6)):
    """
    Compute the integral with a monte carlo integration algorithm
    :param integrand: the function to integrate (lambda or func)
    :param bounds:
    :param domainsize: (tuple of len==2)
    :param n_sample: number of sample to use (int)
    :return: the integral of the integrand (float)
    """
    np.random.seed(1)
    total = 0.0
    total_sq = 0.0
    count_in_curve = 0

    def sampler():
        while True:
            yield [np.random.uniform(b0, b1) for [b0, b1] in bounds]

    for x in itertools.islice(sampler(), n_sample):
        f = integrand(x)
        f_rn = np.random.uniform(domainsize[0], domainsize[1])
        total += f
        total_sq += (f ** 2)
        count_in_curve += 1 if 0 <= f_rn <= f else 0
    # Return answer
    # sample_mean = total / n_sample
    # sample_var = (total_sq - ((total / n_sample) ** 2) / n_sample) / (n_sample - 1.0)
    # return domainsize * sample_mean, domainsize * np.sqrt(sample_var / n_sample)
    v = np.prod([b1 - b0 for [b0, b1] in bounds]) * (domainsize[1] - domainsize[0])
    print(100 * (count_in_curve / n_sample), "%")
    return (count_in_curve / n_sample) * v


if __name__ == '__main__':
    pass
