def is_palindrome(s):
    # Jika string memiliki 0 atau 1 karakter, itu adalah palindrom.
    if len(s) <= 1:
        return True
    
    # Periksa apakah karakter pertama dan terakhir sama.
    if s[0] == s[-1]:
        # Periksa rekursif substring tanpa karakter pertama dan terakhir.
        return is_palindrome(s[1:-1])
    
    # Jika karakter pertama dan terakhir berbeda, maka bukan palindrom.
    return False

# Contoh:
input_str = "katak"
if is_palindrome(input_str):
    print(f"{input_str} adalah palindrom.")
else:
    print(f"{input_str} bukan palindrom.")
    
input_str = "balapan"
if is_palindrome(input_str):
    print(f"{input_str} adalah palindrom.")
else:
    print(f"{input_str} bukan palindrom.")
