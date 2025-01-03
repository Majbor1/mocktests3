def f(uid):
    unique = []
    for name in uid:
        if name not in unique:
            unique.append(name)
        else:
            return False
    
    return True

print(f(["john5","ann123","JOHN5","xxx","abc333","a10"]))
print(f(["john5","ann123","JOHN5","xxx","abc333","a10", "abc333"]))