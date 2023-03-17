#
# 2083
# 럭비 클럽
# https://www.acmicpc.net/problem/2083

import sys
input = sys.stdin.readline

while 1:
    name, age, weight = input().split()

    if name == '#':
        exit()

    print(name, end=' ')

    if int(age) > 17 or int(weight) >= 80:
        print('Senior')
    else:
        print('Junior')