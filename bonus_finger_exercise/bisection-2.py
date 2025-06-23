secret = 99 # 3, 11, 42, work
            # 2, 4, 12, 99, 100 do not work
a = 0
b = 100
times = 1
m = a + (b-a) // 3  # note the floor division by 3
while True:
    if m < secret:
        a = m + 1
    elif m > secret:
        b = m - 1
    else:
        print(f'found {m} after {times} times')
        break
    m = a + (b-a) // 3  # note the floor division by 3
    times += 1