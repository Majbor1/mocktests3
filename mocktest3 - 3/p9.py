def f(arr):
    suma = []
    for i in arr:
        if i % 3 == 0 or i % 5 == 0:
            suma.append(i)

    return sum(suma)

if __name__ == "__main__":
    print(f([1, 2, 3, 4, 5, 6, 10, 15]))
    print(f([7, 11, 13]))
    print(f([30, 60, 90]))
