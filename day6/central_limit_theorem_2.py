from day5.normal_distribution_common import normal_distribution_ct

if __name__ == '__main__':
    tickets = int(input())
    students = int(input())
    mean = float(input())
    std_dev = float(input())

    dist = normal_distribution_ct(mean, std_dev, students)
    print(round(dist(tickets), 4))
