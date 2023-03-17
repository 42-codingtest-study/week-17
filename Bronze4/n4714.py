#
# 4714
# Lunacy
# https://www.acmicpc.net/problem/4714

while 1:
    x = float(input())

    if x == -1:
        break

    print("Objects weighing %.2f on Earth will weigh %.2f on the moon." % (x, x * 0.167))