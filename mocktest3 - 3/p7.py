from math import sqrt

def f(arr):
    num_of_primary = 0
    for char in arr:
        if is_primary(char):
            num_of_primary += 1

    return num_of_primary


def is_primary(n):
    primary = 0
    if n > 1:
        for i in range(2, int(sqrt(n))+1):
            if n % i == 0:
                primary = 1
        if primary == 0:
            return True
        else:
            return False
    else:
        return False
        
if __name__ == "__main__":
    print(f([2, 3, 4, 5, 6, 7, 8, 9, 10]))  
    print(f([1, 13, 15, 17]))
    print(f([0, 1, 4, 6]))
