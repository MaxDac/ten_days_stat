def compute_median(n, arr):
    if n % 2 == 0:
        return round((arr[n // 2 - 1] + arr[n // 2]) / 2, 1)
    else:
        return round(float(arr[n // 2]), 1)


def compute_quartiles(n, arr):
    median = int(compute_median(n, arr))

    # first_quartile, second_quartile = [], []
    if n % 2 == 0:
        first_quartile, second_quartile = arr[0:n // 2], arr[n // 2:]
    else:
        first_quartile, second_quartile = arr[0:n // 2], arr[n // 2 + 1:]

    first_quartile_median = compute_median(n // 2, first_quartile)
    second_quartile_median = compute_median(n // 2, second_quartile)

    return first_quartile_median, median, second_quartile_median


def build_arr_freq(n, arr, freq):
    buffer = []
    for i in range(n):
        for _ in range(freq[i]):
            buffer.append(arr[i])

    return sorted(buffer)


if __name__ == '__main__':
    n = int(input())
    arr = [int(x) for x in input().rstrip().split()]
    freq = [int(x) for x in input().rstrip().split()]
    arr_freq = build_arr_freq(n, arr, freq)
    first, _, second = compute_quartiles(len(arr_freq), arr_freq)
    print(str(round(second - first, 1)))
