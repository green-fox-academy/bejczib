
num = 0
l = 1
i = 1
while i < 100:
    c = l + num;
    num = l
    l = c
    print(c)
    i += 1
