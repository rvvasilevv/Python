import random
print("......Kamyk.......")
print("......Nojica.......")
print("......Hartiq.........")
izbor = input("Kvo izbirash")
izbornacpu=random.randint(0, 2)
if izbornacpu == 0:
    poziciq = "Kamyk"
elif izbornacpu == 1:
    poziciq = "Nojica"
elif izbornacpu == 2:
    poziciq = "Hartiq"
print(f"Kompa izbra {poziciq}")
if izbor == poziciq:
    print("Ravni")
elif izbor == "Kamyk":
    if poziciq == "Nojica":
        print("Ti biesh")
    elif poziciq == "Hartiq":
        print("Cpu bie")
elif izbor == "Nojica":
    if poziciq == "Kamyk":
        print("CPUto te prusna ")
    elif poziciq == "Hartiq":
        print("ti biesh kurvo")
elif izbor == "Hartiq":
    if poziciq == "Kamyk":
        print("Ti biesh ")
    elif poziciq == "Nojica":
        print("Cputo bie")


