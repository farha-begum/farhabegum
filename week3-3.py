def palindrome(s):
    rev=''.join(reversed(s))
    return s==rev

print(palindrome("racecar"))
print(palindrome("farha"))
