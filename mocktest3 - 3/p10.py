def f(s):
    """Zwraca najdłuższy podciąg znaków w s, który jest palindromem."""
    if not s:
        return ""
    
    def is_palindrome(substr):
        """Sprawdza, czy podciąg substr jest palindromem."""
        return substr == substr[::-1]
    
    longest_palindrome = ""
    
    for i in range(len(s)):
        for j in range(i + 1, len(s) + 1):
            current_substr = s[i:j]
            if is_palindrome(current_substr) and len(current_substr) > len(longest_palindrome):
                longest_palindrome = current_substr
    
    return longest_palindrome

# Przykłady użycia:
print(f("babad"))  # Output: "bab" lub "aba"
print(f("cbbd"))   # Output: "bb"
print(f("abcde"))  # Output: "a"
print(f("racecar"))  # Output: "racecar"
print(f(""))        # Output: ""