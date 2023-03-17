#
# 2752
# 세수정렬
# https://www.acmicpc.net/problem/2752

import sys
input = sys.stdin.readline

a, b, c = map(int, input().split())
li = [a, b, c]

print(min(a, b, c), end=' ')
li.remove(min(a, b, c))

print(min(li), end=' ')
print(max(a, b, c))