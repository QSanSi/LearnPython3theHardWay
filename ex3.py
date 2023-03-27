print("I will now conut my chickens:")

print("Hens", 25.0 + 30.0 / 6.0)
print("Roosters", 100.0 - 25.0 * 3.0 % 4.0)

print("Now I will count the eggs:")

print(3.0 + 2.0 + 1.0 - 5.0 + 4.0 % 2.0 - 1.0 / 4.0 + 6.0)

print("Is it true that 3 + 2 < 5 - 7?")

print(3 + 2 < 5 - 7)

print("What is 3 + 2?", 3 + 2)
print("What is 5 - 7?", 5 - 7)

print("Oh, that's why it's False.")

print("Hello about some more.")

print("Is it greater?", 5 > -2)
print("Is it greater or equal?", 5 >= -2)
print("Is it less or equal?", 5 <= -2)

# Python取模运算与取余运算区别
# 第一步：求整数商c：
#   进行求模运算时：c = [a/b] = -7 / 4 = -2（向负无穷方向舍入），
#   进行求余运算时：c = [a/b] = -7 / 4 = -1（向0方向舍入）；
a = -7
b = 4
c = a // b # "//"为求整商, "/"求商为浮点数
print(c)
# 第二步：计算模和余数的公式相同，但因c的值不同，
#   求模时：r = a - c*b =-7 - (-2)*4 = 1，
#   求余时：r = a - c*b = -7 - (-1)*4 =-3。
r = a - c * b
print(r)





