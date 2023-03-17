#
# 6825
# Body Mass Index
# https://www.acmicpc.net/problem/6825

import sys
input = sys.stdin.readline

weight = float(input())
height = float(input())

BMI = weight / (height * height)

if BMI >= 25:
    print("Overweight")
elif 18.5 <= BMI < 25.0:
    print("Normal weight")
else:
    print("Underweight")