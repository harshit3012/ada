def string_match(text, pattern):
    n, m = len(text), len(pattern)
    for i in range(0, n-m+1):
        j = 0
        while j < m and text[i+j] == pattern[j]:
            j += 1
        if j == m:
            return i
    return -1

# print(string_match("Cool string matching algo", "string"))
# print(string_match("computer science engineering", "science"))
# print(string_match("working is fun", "work"))
# print(string_match("cabaaabc", "abc"))
# print(string_match("bccdabc", "bc"))
# print(string_match("aaaaabc", "bcd"))
text = print('Enter the text :', end="")
pattern = print('Enter the pattern :', end="")
pos = string_match(text, pattern)
if(pos == -1):
    print("Could not find the pattern in the text!")
else:
    print(f'Pattern found in the text at {pos}th position')
