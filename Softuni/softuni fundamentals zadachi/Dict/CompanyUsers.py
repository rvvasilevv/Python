rechnik={}
while True:
    command = input()
    if command == "End":
        break
    else:
        tokens=command.split('->')
        ime=tokens[0]
        id=tokens[1]
        if ime not in rechnik.keys():
            rechnik[ime]=[]
        rechnik[ime].append(id)
for ime in rechnik.keys():
    print(f"{ime} ")
    for i in rechnik[ime]:
        print(f'--{i}')
