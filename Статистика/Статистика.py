def average(list):
    sum = 0
    for i in list:
        sum += i
    return sum/len(list)


def median(list):
    lens = len(list)
    med = lens//2
    if not lens%2:
        return (list[med] + list[med-1]) / 2
    else:
        return list[med]


def percentile(P, list):
    x = P * (len(list)-1) / 100 + 1
    n = int(x)
    n_x = x - n

    if P == 100:
        return list[n]

    else:
        return list[n] + n_x * (list[n-1] - list[n])


num_list = []

with open('Последовательность_test.txt') as file:
    for line in file:
        num = int(line.strip())
        num_list.append(num)

print('Последовательность:')
print(num_list)
print('Длина последовательности:')
print(len(num_list))

sort_list = sorted(num_list)

print('Отсортированная последовательность:')
print(sort_list)


print('Статистика:')
print('90 percentile', percentile(90, sort_list))
print('median', median(sort_list))
print('average', average(num_list))
print('max', max(num_list))
print('min', min(num_list))