# 문제
# N-Queen 문제는 크기가 N × N인 체스판 위에 퀸 N개를 서로 공격할 수 없게 놓는 문제이다.
#
# N이 주어졌을 때, 퀸을 놓는 방법의 수를 구하는 프로그램을 작성하시오.
#
# 입력
# 첫째 줄에 N이 주어진다. (1 ≤ N < 15)
#
# 출력
# 첫째 줄에 퀸 N개를 서로 공격할 수 없게 놓는 경우의 수를 출력한다.
#
# 예제 입력 1
# 8
# 예제 출력 1
# 92
# 힌트

# 내 윗줄에 나와 겹치는 라인에 퀸이 있는가?
def adjacent(x):
    for i in range(x):
        if row[x] == row[i] or abs(row[x] - row[i]) == x - i:
            return False
    return True


# 한줄씩 재귀하며 DFS를 실행
def dfs(x):
    global result

    if x == N:
        result += 1

    else:
        for i in range(N):
            row[x] = i
            if adjacent(x):
                dfs(x + 1)


N = int(input())
row = [0] * N
result = 0
dfs(0)
print(result)