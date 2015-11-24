temp = input('Adj meg egy szamot 1-99ig!\n')
szam = int(temp)

if szam == 0:
    print("nulla baze")
elif szam % 2 == 0:
    print("paros biza")
else:
    print("paratlan nyugger")
