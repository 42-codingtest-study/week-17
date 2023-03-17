#
# 5554
# 심부름 가는 길
# https://www.acmicpc.net/problem/5554

import sys
input = sys.stdin.readline

hometoschool = int(input())
schooltopc = int(input())
pctowork = int(input())
worktohome = int(input())

all = hometoschool + schooltopc + pctowork + worktohome

print(all // 60)
print(all % 60)