`n=int(input())
stats={}
for x in range(n):
    zadanie=input().split()
    name=zadanie[0]
    HP=int(zadanie[1])
    MP=int(zadanie[2])
    stats[name]=[HP,MP]
data=input()
while data != 'End':
    command=data.split(' - ')
    funkciq=command[0]
    if funkciq == "CastSpell":
        name=command[1]
        MP_needed=int(command[2])
        spell_name=command[3]
        if stats[name][1] >= MP_needed:
            ostavashtamana=stats[name][1]-MP_needed
            stats[name][1]-=MP_needed
            print(f"{name} has successfully cast {spell_name} and now has {ostavashtamana} MP!")
        else:
            print(f"{name} does not have enough MP to cast {spell_name}!")
    if funkciq == "TakeDamage":
        name=command[1]
        damage=int(command[2])
        attacker=command[3]
        current_hp=int(stats[name][0]-damage)
        stats[name][0]-=damage
        if stats[name][0] > 0:
            print(f"{name} was hit for {damage} HP by {attacker} and now has {current_hp} HP left!")
        if stats[name][0] <= 0:
            stats.pop(name)
            print(f"{name} has been killed by {attacker}!")
    if funkciq == "Recharge":
        name=command[1]
        amount=abs(int(command[2]))
        stats[name][1]+=amount
        realnorecharge = abs(200 - stats[name][1])
        obshtorecharge = stats[name][1] + amount
        if obshtorecharge > 200:
            stats[name][1] = 200
            print(f"{name} recharged for {realnorecharge} MP!")
        else:
            print(f"{name} recharged for {amount} MP!")
    if funkciq == "Heal":
        name=command[1]
        amount=int(command[2])
        # stats[name][0] += amount
        realnohealnato=100 -stats[name][0]
        obshto=stats[name][0]+amount
        if obshto > 100:
            stats[name][0] += amount
            stats[name][0] = 100
            print(f"{name} healed for {realnohealnato} HP!")
        else:
            stats[name][0] += amount
            print(f"{name} healed for {amount} HP!")


    data=input()
for k in stats.keys():
    print(f"{k}")
    print(f'  HP: {stats[k][0]}')
    print(f'  MP: {stats[k][1]}')



`