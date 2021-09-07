

def lcm(m, n, r):
    maxNum = max(m, n, r)
    while True:
        if maxNum % m == 0 and maxNum % n == 0 and maxNum % r == 0:
            break
        maxNum = maxNum+1
    return f"The LCM of {m} and  {n} and {r} is {maxNum}"


# taking inputs
m = int(input("Enter the first Number: "))
n = int(input("Enter the second number: "))
r = int(input("Enter the third number: "))
# print(m, n)
Num = lcm(m, n, r)
print(Num)
# maxNum = max(m, n)
# while True:
#     if maxNum % m == 0 and maxNum % n == 0:
#         break
#     maxNum = maxNum+1
# print(f"The lcm of {m} and {n} is {maxNum}")
