from day4.binomial_distribution_common import binomial_probability

if __name__ == '__main__':
    p, n = [int(i) for i in input().rstrip().split()]
    p_broken = p / 100
    result_1, result_2 = 0, 0

    # No more than 2
    for x in range(3):
        result_1 += binomial_probability(x, n, p_broken)

    for x in range(2, n + 1):
        result_2 += binomial_probability(x, n, p_broken)

    print(round(result_1, 3))
    print(round(result_2, 3))
