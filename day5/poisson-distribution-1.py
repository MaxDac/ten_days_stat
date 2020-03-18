from day5.poisson_distribution_shared import evaluate_poisson

if __name__ == '__main__':
    mean = float(input())
    value = float(input())
    print(round(evaluate_poisson(value, mean), 3))
