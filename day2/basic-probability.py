import itertools

if __name__ == '__main__':
    dice = [1, 2, 3, 4, 5, 6]
    occourences = []

    for i in range(1, 7):
        for j in range(1, 7):
            occourences.append((i, j))

    count = 0
    for i in occourences:
        first, second = i
        if first + second <= 9:
            count += 1

    print(count)
    print(len(occourences))