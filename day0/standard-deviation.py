import math


def compute_mean(n, arr):
    return sum(arr) / n


def compute_variance(n, arr):
    mean = compute_mean(n, arr)
    deviation_from_mean = sum([math.pow(x - mean, 2) for x in arr])
    return deviation_from_mean / n


def compute_standard_deviation(n, arr):
    variance = compute_variance(n, arr)
    return math.sqrt(variance)


if __name__ == '__main__':
    n = int(input())
    arr = [int(x) for x in input().rstrip().split()]
    print(str(round(compute_standard_deviation(n, arr), 1)))
