#
# 14038
# Tournament Selection
# https://www.acmicpc.net/problem/14038

score = []

for _ in range(6):
    x = input()

    if x == 'W':
        score.append(1)
    else:
        score.append(0)

judge = score.count(1)

if judge == 5 or judge == 6:
    print(1)
elif judge == 3 or judge == 4:
    print(2)
elif judge == 1 or judge == 2:
    print(3)
else:
    print(-1)