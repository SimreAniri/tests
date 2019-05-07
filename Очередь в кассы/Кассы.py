from datetime import timedelta

sum = [0 for i in range(16)]


def sum_of_customers(filename):
    i = 0
    with open(filename) as cashbox:
        for line in cashbox:
            customers = int(line.strip())
            sum[i] += customers
            i += 1


start_time = timedelta(hours=8)
print(start_time)


sum_of_customers('1.txt')
sum_of_customers('2.txt')
sum_of_customers('3.txt')
sum_of_customers('4.txt')
sum_of_customers('5.txt')

print(sum)

max_customers = max(sum)

print('Максимальное количество посетителей:', max_customers)
print('Было в магазине:')

index = -100

for i in range(len(sum)):

    if (sum[i] == max_customers) and (i != index+1):

        delta = timedelta(minutes=i*30)
        current_time = start_time + delta
        index = i
        print('с', current_time, 'до', end=' ')

        if i == len(sum) - 1:
                delta = timedelta(minutes=(i+1)*30)
                current_time = start_time + delta
                print(current_time)

        elif sum[i] != sum[i+1]:
            delta = timedelta(minutes=(i+1)*30)
            current_time = start_time + delta
            print(current_time)

    elif (sum[i] == max_customers) and (i == index+1):
        index = i

        if i == len(sum) - 1:
            delta = timedelta(minutes=(i+1)*30)
            current_time = start_time + delta
            print(current_time)

        elif sum[i] != sum[i + 1]:
            delta = timedelta(minutes=(i+1)*30)
            current_time = start_time + delta
            print(current_time)

