def greet(name):
    return "Hello, " + name

result = greet("Balint")
print(result)

g = []
def add(a,b):
    res = a + b
    g.append(res)
    return res

print(add(1,2))
print(add(2,7))
print(g)


n = 1
def my_print():
    n = 2
    print(n)
print(n)
my_print()
