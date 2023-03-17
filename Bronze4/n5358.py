#
# 5358
# Football Team
# https://www.acmicpc.net/problem/5358

while 1:
    try:
        name = input()

        # maketrans
        ori = 'eiEI'
        cha = 'ieIE'

        rule = name.maketrans(ori, cha)

        print(name.translate(rule))

    except:
        exit()