import math


def normal_distribution_fun(mean, std_dev, x):
    err_fun = math.erf((x - mean) / (std_dev * math.sqrt(2)))
    return 0.5 * (1 + err_fun)


def normal_distribution(mean, std_dev):
    return lambda x: normal_distribution_fun(mean, std_dev, x)


def compute_ct_mean_st_dev(mean, std_dev, n):
    normal_mean = n * mean
    normal_std_dev = math.sqrt(n) * std_dev
    return normal_mean, normal_std_dev


def normal_distribution_ct(mean, std_dev, n):
    normal_mean, normal_std_dev = compute_ct_mean_st_dev(mean, std_dev, n)
    return normal_distribution(normal_mean, normal_std_dev)
