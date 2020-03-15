if __name__ == '__main__':
    n = int(input())

    arr = [int(x) for x in input().rstrip().split()]
    weight = [int(x) for x in input().rstrip().split()]
    l = len(arr)

    n, d = 0, sum(weight)
    for i in range(l):
        n += arr[i] * weight[i]

    print(round(n / d, 1))

