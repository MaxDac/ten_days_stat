if __name__ == '__main__':
    X, Y = [float(x) for x in input().rstrip().split()]

    mean_x_2 = X + pow(X, 2)
    mean_y_2 = Y + pow(Y, 2)

    print(160.0 + 40.0 * mean_x_2)
    print(128.0 + 40.0 * mean_y_2)
