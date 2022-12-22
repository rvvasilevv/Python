informaciq={}
while True:
    comanda = input()
    if comanda == "buy":
        break
    tokens = comanda.split()
    ime=tokens[0]
    cena=float(tokens[1])
    cena=round(cena,3)
    kolichestvo=tokens[2]
    if ime not in informaciq.keys():
        informaciq[ime]=[]
        informaciq[ime].append(cena)
        informaciq[ime].append(int(kolichestvo))
print(informaciq)









