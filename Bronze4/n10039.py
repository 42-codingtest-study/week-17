#
# 10039
# 평균 점수
# https://www.acmicpc.net/problem/10039

score = 0

for _ in range(5):
    s = int(input())
    if s < 40:
        s = 40

    score += s


print(score // 5)