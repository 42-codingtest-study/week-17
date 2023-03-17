#
# 8718
# Bałwanek
# https://www.acmicpc.net/problem/8718

x, k = map(int, input().split())

if k * 7 <= x: # Kasia가 만든 공이 가장 작은 공일 경우
    print(k * 7000)
elif k * 3.5 <= x: # Kasia가 만든 공이 중간 크기의 공일 경우
    print(k * 3500)
elif k * 1.75 <= x: # Kasia가 만든 공이 가장 큰 공일 경우
    print(k * 1750)
else:
    print(0)