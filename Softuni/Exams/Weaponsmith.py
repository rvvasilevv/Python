parts=input().split('|')
comanda=input()
even=[]
while comanda != "Done":

    funkciq=comanda.split(" ")
    if funkciq[0] == "Add":
        particle=funkciq[1]
        index=int(funkciq[2])
        if index in range(len(parts)):
            parts.insert(index, particle)
    elif funkciq[0] == "Remove":
        index=int(funkciq[1])
        if index in range(len(parts)):
            parts.pop(index)
    elif funkciq[0] == "Check":
        if funkciq[1] == "Even":
            print(' '.join(parts[::2]))
        elif funkciq[1] == "Odd":
            print(' '.join(parts[1::2]))
    comanda= input()
print(f"You crafted {''.join(parts)}!")