#
# 4299
# AFC 윔블던
# https://www.acmicpc.net/problem/4299

a, b = map(int, input().split())

if a < b:
    print(-1)
else:
    x = (a + b) // 2
    y = (a - b) // 2
    if x + y == a and x - y == b:
        print(x, y)
    else:
        print(-1)