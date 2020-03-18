import math
from day5.normal_distribution_common import normal_distribution

if __name__ == '__main__':
    max_load = int(input())
    n = int(input())
    average = int(input())
    st_dev = int(input())

    normal_average = n * average
    normal_st_dev = math.sqrt(n) * st_dev

    normal_fun = normal_distribution(normal_average, normal_st_dev)
    print(round(normal_fun(max_load), 4))
