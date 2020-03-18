if __name__ == '__main__':
    mean, std_dev = [float(x) for x in input().rstrip().split()]
    distribution = cumulative_normal(mean, std_dev)

    less_1 = float(input())
    low_2, high_2 = [float(x) for x in input().rstrip().split()]

    first = distribution(less_1)
    second = distribution(high_2) - distribution(low_2)

    print(round(first, 3))
    print(round(second, 3))
