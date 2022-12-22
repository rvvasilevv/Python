import re
text=input()
patern=r'\b(\d{2})([-.V])([A-Z][a-z]{2})\2(\d{4})\b'
resultat=re.findall(patern,text)
for match in resultat:
    print(f"Day: {match[0]}, Month: {match[2]}, Year: {match[3]}")