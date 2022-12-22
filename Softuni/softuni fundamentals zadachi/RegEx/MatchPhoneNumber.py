import re

phonenumbers=input()
pattern=r'\+359-2-\d{3}-\d{4}\b|\+359 2 \d{3} \d{4}\b'
resultat=re.findall(pattern,phonenumbers)
print(", ".join(resultat))
