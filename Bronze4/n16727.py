#
# 16727
# ICPC
# https://www.acmicpc.net/problem/16727

p1, s1 = map(int, input().split())
s2, p2 = map(int, input().split())

p = p1 + p2
s = s1 + s2

if p > s:
    print("Persepolis")
elif s > p:
    print("Esteghlal")
else:
    if p1 == s2:
        print("Penalty")
    elif p1 > s2:
        print("Esteghlal")
    else:
        print("Persepolis")