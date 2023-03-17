#
# 6764
# Sounds fishy!
# https://www.acmicpc.net/problem/6764

fish = []

for _ in range(4):
    fish.append(int(input()))

if max(fish) == min(fish):
    print("Fish At Constant Depth.")
else:
    if sorted(fish) == fish:
        print("Fish Rising")
    elif sorted(fish, reverse=True) == fish:
        print("Fish Diving")
    else:
        print("No Fish")
