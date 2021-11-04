# Четные и нечетные
a = int(input())
b = int(input())
c = int(input())
a1 = a % 2
b1 = b % 2
c1 = c % 2
if (a1 == 0 or b1 == 0 or c1 == 0) and (a1 == 1 or b1 == 1 or c1 == 1):
    print("YES")
else:
    print("NO")
