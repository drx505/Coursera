a = int(input())
b = (((a // 10) // 10) // 10) % 10
c = a % 10
d = ((a // 10) // 10) % 10
e = (a // 10) % 10
a2 = str(d) + str(b)
b2 = str(e) + str(c)
print(int(b2 == a2))
