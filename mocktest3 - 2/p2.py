def f(x, y, d):
    for i in range(x, y+1):
        if d in str(i):
            return True
    return False

print(f(10,15,"14"))
print(f(100,120,"11"))
print(f(205,215,"04"))