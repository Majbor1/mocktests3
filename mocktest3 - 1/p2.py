def f(x, y, digit):
    result = 0
    for i in range(x, y+1):
        i = str(i)
        for char in i:
            if int(char) == digit:
                result += 1
    
    return result

print(f(10,15,1))
print(f(28,32,2))
print(f(100,105,6))
print(f(100,103,0))

