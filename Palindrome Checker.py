def is_palindrome(s):
    s = s.lower().replace(" ", "")  # Normalize the string
    return s == s[::-1]

# Example usage
input_str = input("Enter a string: ")
if is_palindrome(input_str):
    print(f"'{input_str}' is a palindrome!")
else:
    print(f"'{input_str}' is not a palindrome.")
