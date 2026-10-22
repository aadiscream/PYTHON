import re
# Define a regular expression pattern
pattern = r"[a-z]+at"
# Match the pattern against a string
text = "Hi this is aditya, cat hat hello hi example@gmail.com"
match = re.findall(pattern, text)
print(match[0],match[1])
match=re.search(pattern,text)
print(match)
match=re.sub(pattern,"dog",text)
print(match)
pattern = r"\w+@\w+\.\w+"
match=re.search(pattern,text)
print(match.group())