def ispallindrome(s):
    return s == s[::-1]

s = "MalayalaM"
ans = ispallindrome(s)

if ans:
    print("Yes")
else:
    print("No")