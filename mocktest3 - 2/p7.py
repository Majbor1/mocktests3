def f(d):
    parking_lot = []
    for car in d:
        if car[1] == "in":
            parking_lot.append(car[0])
        elif car[1] == "out":
            parking_lot.remove(car[0])

    parking_lot.sort()
    return parking_lot

cars = [["KR234","in"],["BA123","in"],["GX444","in"],["KR234","out"], ["KR234","in"], ["BA111","in"],["BA123","out"]]
print(f(cars))
cars1 = [["KR234","in"],["KR234","out"]]
print(f(cars1))