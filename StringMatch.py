def string_match(text, pattern):
    n, m = len(text), len(pattern)
    for i in range(0, n-m+1):
        j = 0
        while j < m and text[i+j] == pattern[j]:
            j += 1
        if j == m:
            return i
    return -1

print(string_match("computer science", "science"))
print(string_match("aaaaaaabc", "bc"))
print(string_match("aabcaaabc", "bc"))
print(string_match("aaaaaaabc", "bcd"))
