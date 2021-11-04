# Упорядочить три числа
a, b, c = int(input()), int(input()), int(input())
if a >= b >= c:
    print(c, b, a)
elif a >= c >= b:
    print(b, c, a)
elif b >= a >= c:
    print(c, a, b)
elif b >= c >= a:
    print(a, c, b)
elif c >= a >= b:
    print(b, a, c)
else:
    print(a, b, c)
