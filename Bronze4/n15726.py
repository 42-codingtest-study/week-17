#
# 15726
# 이칙연산
# https://www.acmicpc.net/problem/15726

a, b, c = map(int, input().split())

print(a * max(b, c) // min(b, c))