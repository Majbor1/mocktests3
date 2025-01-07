def f(fnc, prods):
    result = list(map(fnc, prods))

    return ",".join(result)

if __name__ == "__main__":
    prods = ["woda", "ser", "pomidor"]  
    fnc1 = lambda x: "id:" + x[:2]  
    print(f(fnc1, prods))