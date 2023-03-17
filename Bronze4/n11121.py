#
# 11121
# Communication Channels
# https://www.acmicpc.net/problem/11121

import sys
input = sys.stdin.readline

for _ in range(int(input())):
    inp, outp = input().split()

    if inp == outp:
        print("OK")
    else:
        print("ERROR")