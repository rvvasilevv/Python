class Person:
    def __init__(self, name):
        self.name=nam
class Party:
    def __init__(self):
        self.hora=[]
party=Party()
comanda=input()
while comanda != "End":
    party.hora.append(comanda)
    comanda=input()
    name=comanda
print(f"Going: {', '.join(party.hora)}")
print(f"Total:{len(party.hora)}")