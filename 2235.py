x = input().split(" ")
a = int(x[0])
b = int(x[1])
c = int(x[2])


if a-b == 0 or b-c == 0 or c- a == 0:
    print("S")
elif a+c == b or a+b == c or b+c == a:
    print("S")

else:
    print("N")