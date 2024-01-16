#with temp
a = 5
b = 10
print(f"before swap: {a,b}")
tmp = b
b = a
a = tmp
print(f"after swap: {a,b}")


#without temp variable
a = 25
b = 0
print(f"before swap: {a,b}")
a, b = b, a
print(f"after swap: {a,b}")
