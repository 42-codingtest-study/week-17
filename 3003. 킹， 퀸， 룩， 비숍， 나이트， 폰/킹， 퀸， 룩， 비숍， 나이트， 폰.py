perfect = [1,1,2,2,2,8]

find = list(map(int, input().split()))
result = []
for i in range(0, 6):
    result.append(perfect[i] - find[i])

for a in result:
    print(a, end = ' ')