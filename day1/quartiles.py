def compute_median(n, arr):
    if n % 2 == 0:
        return round((arr[n // 2 - 1] + arr[n // 2]) / 2, 1)
    else:
        return arr[n // 2]


if __name__ == '__main__':
    n = int(input())
    arr = sorted([int(x) for x in input().rstrip().split()])
    median = int(compute_median(n, arr))

    first_quartile, second_quartile = [], []
    if n % 2 == 0:
        first_quartile, second_quartile = arr[0:n // 2], arr[n // 2:]
    else:
        first_quartile, second_quartile = arr[0:n // 2], arr[n // 2 + 1:]

    first_quartile_median = int(compute_median(n // 2, first_quartile))
    second_quartile_median = int(compute_median(n // 2, second_quartile))

    print(str(first_quartile_median))
    print(str(median))
    print(str(second_quartile_median))
