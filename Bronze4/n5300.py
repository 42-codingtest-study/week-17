#
# 5300
# Fill the Rowboats!
# https://www.acmicpc.net/problem/5300

n = int(input())

cnt = 0
for i in range(1, n + 1):
    print(i, end=' ')
    cnt += 1

    if cnt == 6 or i == n:
        print("Go!", end=' ')
        cnt = 0