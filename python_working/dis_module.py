import dis

def add(a, b):
    return a + b

print(add(10, 5))

dis.dis(add)