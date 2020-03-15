from day4.binomial_distribution_common import geometric_probability

if __name__ == '__main__':
    num, den = [int(i) for i in input().rstrip().split()]
    n = int(input())

    print(round(geometric_probability(n, num / den), 3))
