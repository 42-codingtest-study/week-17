#
# 4589
# Gnome Sequencing
# https://www.acmicpc.net/problem/4589

n = int(input())

print("Gnomes:")

for _ in range(n):
    book = list(map(int, input().split()))

    if sorted(book, reverse=False) == book or sorted(book, reverse=True) == book:
       print("Ordered")
    else:
       print("Unordered")
