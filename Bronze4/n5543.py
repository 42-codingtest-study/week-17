#
# 5543
# 상근날드
# https://www.acmicpc.net/problem/5543

import sys
input = sys.stdin.readline

sb = int(input())
jb = int(input())
hb = int(input())
cola = int(input())
cider = int(input())

print(min(sb, jb, hb) + min(cola, cider) - 50)