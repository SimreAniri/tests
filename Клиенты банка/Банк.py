from datetime import time


time_in = []
time_out = []

with open('Посетители.txt') as file:
    for line in file:
        client, time1, time2 = line.split()
        time_in.append(time.fromisoformat(time1))
        time_out.append(time.fromisoformat(time2))


time_out = sorted(time_out)

index_in = 0
index_out = 0

max_client = 0
cur_max_time = [time_in[0],time_in[0]]

max_time = {max_client:[cur_max_time]}
count = 0

for i in time_in:
    k = time_out[index_out]


    if i <time_out[index_out]:
        index_in += 1
        cur_max_time = [i, i]

        if index_in > max_client:
            count = 0
            max_client = index_in
            max_time[max_client] = [cur_max_time]

        elif index_in == max_client:
            max_time[max_client][count] = cur_max_time


    elif i == time_out[index_out]:
        index_out += 1
        if index_in == max_client:
            cur_max_time[1] = i
            max_time[max_client][count] = cur_max_time


    else:

        if index_in == max_client:
            cur_max_time[1] = time_out[index_out]
            max_time[max_client][count] = cur_max_time
            max_time[max_client].append([0, 0])
            count += 1

        while i > time_out[index_out]:
            index_out += 1
            index_in -= 1

        if i == time_out[index_out]:
            index_out += 1

        elif i < time_out[index_out]:
            index_in += 1
            cur_max_time = [i, i]

            if index_in > max_client:
                count = 0
                max_client = index_in
                max_time[max_client] = [cur_max_time]

            elif index_in == max_client:
                max_time[max_client][count] = cur_max_time

if index_out <= len(time_out)-1:
    if index_in == max_client:
        cur_max_time[1] = time_out[index_out]
        max_time[max_client][count] = cur_max_time


print('Наибольшее количество клиентов:', max_client)
print('Было в банке:')
for i in max_time[max_client]:
    if i[0] != 0:
        print('с', i[0], 'до', i[1])