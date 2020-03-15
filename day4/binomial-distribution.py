from day4.binomial_distribution_common import binomial_probability

if __name__ == '__main__':
    b, g = [float(i) for i in input().rstrip().split()]
    n, r = 6, 3

    boy_probability = b / (b + g)

    # Applying binomial distribution with cumulative probability (sum)
    cumulative = 0
    for i in range(r, n + 1):
        cumulative += binomial_probability(i, n, boy_probability)

    print(round(cumulative, 3))
