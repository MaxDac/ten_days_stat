from math import factorial, pow


def binomial(n, x):
    return factorial(n) / (factorial(x) * factorial(n - x))


def binomial_probability(x, n, p):
    return binomial(n, x) * pow(p, x) * pow(1 - p, n - x)


def geometric_probability(n, p):
    return pow(1 - p, n - 1) * p
