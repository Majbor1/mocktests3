def f(fnc, res):
    result = list(filter(fnc, res))
    smallest = min(result)
    largest = max(result)

    return largest - smallest

res = [95,90,20,50,70] 
fnc1 = lambda x: x>50
print(f(fnc1,res))
fnc2 = lambda x: x>30 and x<90
print(f(fnc2,res))
