#
# 1264
# 모음의 개수
# https://www.acmicpc.net/problem/1264

while 1:
    sen =input()

    if sen == "#":
        exit()

    count = 0

    for x in sen:
        if x in 'aeiouAEIOU':
            count += 1

    print(count)