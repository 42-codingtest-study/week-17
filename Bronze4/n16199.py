#
# 16199
# 나이 계산하기
# https://www.acmicpc.net/problem/16199

import sys
input = sys.stdin.readline

y1, m1, d1 = map(int, input().split())
y2, m2, d2 = map(int, input().split())

if m1 < m2:
    year1 = y2 - y1
elif m1 == m2 and d1 <= d2:
        year1 = y2-y1
else:
    year1 = y2 - y1 - 1


print(year1) # 만 나이
print(y2 - y1 + 1) # 세는 나이
print(y2 - y1) # 연 나이