from day4.binomial_distribution_common import geometric_probability

if __name__ == '__main__':
    num, den = [int(i) for i in input().rstrip().split()]
    n = int(input())

    result, d_prob = 0, num / den
    for i in range(1, n + 1):
        result += geometric_probability(i, d_prob)

    print(round(result, 3))
