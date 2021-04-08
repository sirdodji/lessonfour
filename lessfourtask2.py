count = 0
summ_num = 0
avg = 0
max_numb = 0
scnd_max_num = 0
max_numb_indx = 0
cnt_even_num = 0
cnt_odd_num = 0
all_max_num = -1
comp = 1

while True:
    n = int(input())
    if n == max_numb:
        all_max_num += 1
    if n == 0:
        break
    elif n != 0:
        count += 1
        summ_num += n
        comp *= n
        avg = summ_num / count
        if n >= max_numb:
            scnd_max_num = max_numb
            max_numb = n
            max_numb_indx = count
        if scnd_max_num < n < max_numb:
            scnd_max_num = n
        if n % 2 == 0:
            cnt_even_num += 1
        else:
            cnt_odd_num += 1

print(count)
print(summ_num)
print(comp)
print(avg)
print(max_numb)
print(max_numb_indx)
print(scnd_max_num)
print(cnt_even_num)
print(cnt_odd_num)
print(all_max_num)

