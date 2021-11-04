# Шоколадка
n = int(input())
m = int(input())
k = int(input())
# n = 2
# m = 10
# k = 7
if ((k % m == 0) or (k % n == 0)) and k <= (m * n):
    print("YES")
else:
    print("NO")
