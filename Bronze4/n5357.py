# 질문
#
# 5357
# Dedupe
# https://www.acmicpc.net/problem/5357

for _ in range(int(input())):
    word = input()

    check= []
    prev = ''

    for i in word:
        if prev != i:
            check.append(i)
            prev = i

    for i in check:
        print(i, end='')
        print()