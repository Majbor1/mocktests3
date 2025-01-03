def f(fnc, prods):
    return ", ".join(map(fnc, prods))
    

prods = ["woda", "ser", "pomidor"]
fnc1 = lambda x: "id: "+x[:2]
print(f(fnc1, prods))
fnc2 = lambda x: (x[0]+x[-1]).upper()
print(f(fnc2, prods))