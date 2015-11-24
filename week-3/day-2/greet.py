def greet(hi, name):
    print (hi + ", " +name)
greet ("hi", "Balint")

def greet2(hi, name):
    if hi is None:
        hi = "Hello"
    print(hi + " ," + name)

greet2(None ,"Balint")

def add(a, b, res = []):
    if res is None:
        res = []
    r = a + b
    res.append(r)
    print(res)
    return r

add(2,3)
