from day5.normal_distribution_common import normal_distribution

if __name__ == '__main__':
    mean, std_dev = [float(x) for x in input().rstrip().split()]
    distribution = normal_distribution(mean, std_dev)

    plus_score = float(input())
    pass_score = float(input())

    top_class = 1 - distribution(plus_score)
    not_passed = distribution(pass_score)
    passed = 1 - not_passed

    print(round(top_class * 100, 2))
    print(round(passed * 100, 2))
    print(round(not_passed * 100, 2))
