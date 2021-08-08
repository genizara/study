a = int(input())

cnt = 0

a_1 = a
while True:
    cnt += 1
    b = 0
    c = 0

    if a_1 >= 10:
        b = a_1 // 10

    c = a_1 % 10

    d = (c * 10) + ((b + c) % 10)

    if a == d:
        break
    else:
        a_1 = d

print(str(cnt))


