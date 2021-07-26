import random
import random as rd
num = random.randrange(100) + 1
while True:

    a = int(input('점수를 입력하세요'))
    if a > num:
        print("너무 높아요")
    elif a < num:
        print("너무 낮아요")
    else:
        print('정답입니다')
        break

print('프로그램을 종료합니다')
