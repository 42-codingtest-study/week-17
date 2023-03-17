#
# 6763
# Speed fines are not fine!
# https://www.acmicpc.net/problem/6763

limit = int(input())
speed = int(input())

cnt = speed - limit

if cnt <= 0:
    print("Congratulations, you are within the speed limit!")
elif 1 <= cnt <= 20:
    print("You are speeding and your fine is $100.")
elif 21 <= cnt <= 30:
    print("You are speeding and your fine is $270.")
else:
    print("You are speeding and your fine is $500.")