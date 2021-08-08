# 소수 구하기
# 시간 제한	메모리 제한	제출	정답	맞은 사람	정답 비율
# 2 초	256 MB	113239	31622	22406	27.174%
# 문제
# M이상 N이하의 소수를 모두 출력하는 프로그램을 작성하시오.
#
# 입력
# 첫째 줄에 자연수 M과 N이 빈 칸을 사이에 두고 주어진다. (1 ≤ M ≤ N ≤ 1,000,000) M이상 N이하의 소수가 하나 이상 있는 입력만 주어진다.
#
# 출력
# 한 줄에 하나씩, 증가하는 순서대로 소수를 출력한다.
#
# 예제 입력 1
# 3 16
# 예제 출력 1
# 3
# 5
# 7
# 11
# 13
a, b = map(int, input().split())

sosu = [True]*(b+1)
sosu[0] = False
sosu[1] = False
root = int(b ** (1/2))
#print(root)
for x in range(1, root):
    c = x + 1
    y = 1
    if not sosu[c]:
        continue

    while True:
        y += 1
        k = c * y


        if  k > b:
            break

        if not sosu[k]:
            continue

        sosu[c*y] = False

#print(sosu)
result = []
l = len(sosu)
for k in range(l):
    if k >= a and sosu[k]:
        result.append(str(k))

print('\n'.join(result))





















