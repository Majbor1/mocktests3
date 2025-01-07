def f(nums):
    reverse = {}
    for num in nums:
        num = str(num)
        reverse[num] = num[::-1]
    
    palindroms = []
    for key, value in reverse.items():
        if key == value:
            palindroms.append(int(value))
    
    return palindroms


if __name__ == "__main__":
    print(f([121, 232, 345, 11, 90]))
    print(f([10, 20, 30]))
    print(f([7, 44, 1221, 154984]))