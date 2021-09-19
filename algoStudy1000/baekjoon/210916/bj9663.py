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
a = int(input())
board = [[0 for col in range(a)] for row in range(a)]

def checkUp(x,y):
    for k in range(x):
        if board[k][y] == 1:
            return False
    return True

def checkLeftUp(x,y):
    for k in range(x):
        if y - ( x - k ) < 0:
            continue
        if board[k][y - ( x - k )] == 1:
            return False
    return True

def checkRightUp(x, y):
    for k in range(x):
        if y + (x - k) >= a:
            continue
        if board[k][y + ( x -k )] == 1:
            return False
    return True
line = 0
x = 0
y = 0
x1 = [0]
total = 0
def drawO(x,y, total):
    if x == a :
        return total
    if y == a :
        return total

    if checkUp(x,y):
        if checkLeftUp(x,y):
            if checkRightUp(x, y):
                board[x][y] = 1
                e = drawO(x+1,0, total+1)
                if e == a:
                    x1[0] += 1
                   # print("-------------------")
                    #for k in board:
                    #    print(k)

                board[x][y] = 0

    if y < a:
        drawO(x, y+1, total)

drawO(0,0,0)
print(x1)