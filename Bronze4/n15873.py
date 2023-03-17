#
# 15873
# 공백 없는 A+B
# https://www.acmicpc.net/problem/15873

num = list(map(int, input()))

if len(num) == 3:
    if num[1] == 0:
        a = 10
        b = num[2]
    else:
        a = num[0]
        b = 10

elif len(num) == 4:
    a = b = 10

else:
    a = num[0]
    b = num[1]

print(a + b)