#
# 13866
# 팀 나누기
# https://www.acmicpc.net/problem/13866

import sys
input = sys.stdin.readline

level = list(map(int, input().split()))

team1 = max(level) + min(level)
level.remove(max(level))
level.remove(min(level))

team2 = 0
for i in level:
    team2 += i

print(abs(team1 - team2))