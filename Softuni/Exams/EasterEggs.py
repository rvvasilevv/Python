import re
text = input()
pater = r'(@|#)+([a-z]{3,})(@|#)+(?:\W+)\/+(\d+)\/+'
hidden_eggs = []
for match in re.finditer(pater, text):
    amount=match.group(4)
    color=match.group(2)
    hidden_eggs.append([color, amount])
for dvoika in hidden_eggs:
    print(f"You found {dvoika[1]} {dvoika[0]} eggs!")