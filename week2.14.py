a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())
if a < b and c < b:
    x = a
    y = c
elif b < a and c < a:
    x = b
    y = c
else:
    x = a
    y = b
if (x <= d and y <= e) or (y <= d and x <= e):
    print("YES")
else:
    print("NO")
