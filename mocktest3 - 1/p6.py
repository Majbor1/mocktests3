import re

def f(vname):
    pattern = r"^[a-zA-Z_]\w{0,4}$"
    
    # Use bool() to convert the match result to True or False
    return bool(re.match(pattern, vname))

# Test the function
print(f("abc"))      # True
print(f("Abc"))
print(f("_ab_c"))
print(f("abcdef"))
print(f("8anc"))
print(f("_aB8_"))
print(f("_4x"))
