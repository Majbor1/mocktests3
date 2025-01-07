def f(x,y,d):
    for i in range(x, y+1):
        i = str(i)
        if d in i:
            return True
    
    return False

if __name__ == "__main__":
    print(f(10, 15, "14"))
    print(f(100, 120, "11"))
    print(f(205, 210, "04"))