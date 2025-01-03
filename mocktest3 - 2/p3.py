def f(d):
    suma = sum(d.values())
    amounts = len(d)
    avg = suma/amounts

    result = 0
    for value in d.values():
        if value >= avg:
            result += 1
    return result

print(f({"LO231":150,"BA787":120,"NZ15":30}))