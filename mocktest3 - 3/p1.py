def f(n):
    n = str(n)
    odds = []
    for char in n:
        if int(char) % 2 != 0:
            odds.append(int(char))
    
    if len(odds) != 0:
        largest = max(odds)
        smallest = min(odds)

        result = largest - smallest
        return abs(result)
    else:
        return -1

if __name__ == "__main__":
    print(f(10852))
    print(f(7235973))
    print(f(4388))
    print(f(846206))