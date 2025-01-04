import re

def f(mnumbers):
    pattern = r"^[a-dA-D1-7+-][a-dA-D1-7]{0,}$"

    matches = []
    for i in mnumbers:
        if re.match(pattern, i):
            matches.append(i)

    return len(matches)

print(f(["A15","-31","7abC","+D1","-gH"]))
print(f(["A05","-3+1","7ab8C","+D1","-22k"]))