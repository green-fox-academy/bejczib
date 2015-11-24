temp = input('Adj meg egy szamot 1-99ig!\n')
szam = int(temp)

if szam == 0:
    print("zero")
elif szam % 2 == 0:
    print("even")
else:
    print("odd")
