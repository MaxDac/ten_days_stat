if __name__ == '__main__':
    n = int(input())

    arr = sorted([int(x) for x in input().rstrip().split()])
    l = len(arr)

    # Mean
    print(round(sum(arr) / l, 2))

    # Median
    if l % 2 == 0:
        print(round((arr[l // 2 - 1] + arr[l // 2]) / 2, 1))
    else:
        print(arr[l // 2])

    # Mode
    mode = 1
    max_mode = 1
    min_mode = arr[0]

    for i in range(1, l):
        if arr[i - 1] == arr[i]:
            mode += 1
            if max_mode < mode:
                max_mode = mode
                min_mode = arr[i]

        else:
            mode = 1

    print(min_mode)

