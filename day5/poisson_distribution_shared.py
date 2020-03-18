import math


def evaluate_poisson(k, l):
    return pow(l, k) * pow(math.e, -l) / math.factorial(k)


def evaluate_poisson_range(range_k, l):
    prob = 0
    for r in range_k:
        prob += evaluate_poisson(r, l)
