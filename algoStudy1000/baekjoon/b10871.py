a, b = map(int, input().split())
k = map(int, input().split())
answer = []
for x in k:
    if x < b:
        answer.append(str(x))

print(' '.join(answer))







