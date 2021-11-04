# Коровы
n = int(input())
m = n % 10
if m == 1 and n != 11:
    print(n, "korova")
elif (m == 2 or m == 3 or m == 4) and n != 12 and n != 13 and n != 14:
    print(n, "korovy")
else:
    print(n, "korov")
