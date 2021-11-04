x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
d1 = abs(x1 - x2)
d2 = abs(y1 - y2)
if d1 > 1 or d2 > 1:
    print("NO")
else:
    print("YES")
