import re
text=input()
pattern=r'\b[A-Z][a-z]+ [A-Z][a-z]+\b'
resultata=re.findall(pattern,text)
print(" ".join(resultata))