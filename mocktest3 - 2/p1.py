def f(n):
    n = str(n)
    odds = []
    for char in n:
        if int(char) % 2 != 0:
            odds.append(int(char))

    if len(odds) == 0:
        return -1
    elif len(odds) == 1:
        return 0
    else:
        smallest = min(odds)
        largest = max(odds)
        return largest - smallest
        
print(f(10852))
print(f(4388))
print(f(2222))
