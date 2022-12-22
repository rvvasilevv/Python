n=int(input())
cmf={}
for i in range(n):
    zadanie=input().split("|")
    car=zadanie[0]
    mileage=int(zadanie[1])
    fuel=int(zadanie[2])
    cmf[car]=[mileage,fuel]
# print(cmf.keys())
comanda=input()
while comanda != "Stop":
    tokens=comanda.split(" : ")
    funkciq=tokens[0]
    if funkciq == "Drive":
        car=tokens[1]
        distance=int(tokens[2])
        fuel=int(tokens[3])
        if cmf[car][1] < fuel:
            print("Not enough fuel to make that ride")
        else:
            cmf[car][0]+=distance
            cmf[car][1]-=fuel
            print(f"{car} driven for {distance} kilometers. {fuel} liters of fuel consumed.")
            if cmf[car][0] >= 100000:
                print(f"Time to sell the {car}!")
                cmf.pop(car)
    elif funkciq == "Refuel":
        car=tokens[1]
        fuel=int(tokens[2])
        obshtozaredeno=cmf[car][1] + fuel
        razlika=75 - cmf[car][1]
        if obshtozaredeno > 75:
            cmf[car][1] = 75
            print(f"{car} refueled with {razlika} liters")
        else:
            cmf[car][1] += fuel
            print(f"{car} refueled with {fuel} liters")
    elif funkciq == "Revert":
        car=tokens[1]
        kilometers=int(tokens[2])
        cmf[car][0]-=kilometers
        print(f"{car} mileage decreased by {kilometers} kilometers")
        if cmf[car][0] < 10000:
            cmf[car][0]=10000
    comanda=input()
for k in cmf:
    print(f"{k} -> Mileage: {cmf[k][0]} kms, Fuel in the tank: {cmf[k][1]} lt.")



