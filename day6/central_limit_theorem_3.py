import math

if __name__ == '__main__':
    n = int(input())
    mean = int(input())
    std_dev = int(input())
    percentage = float(input())
    z_score = float(input())

    # dist = normal_distribution_ct(mean, std_dev, n)
    sample_std_dev = std_dev / math.sqrt(n)
    sample_mean = mean
    print(round(sample_mean - sample_std_dev * z_score, 2))
    print(round(sample_mean + sample_std_dev * z_score, 2))
