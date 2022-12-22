import random
dni_sedmica=["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"]
def return_day():
    izbor=random.randint(1,7)
    if izbor == 1:
        return dni_sedmica[0]
    elif izbor == 2:
        return dni_sedmica[1]
    elif izbor == 3:
        return dni_sedmica[2]
    elif izbor == 4:
        return dni_sedmica[3]
    elif izbor == 5:
        return dni_sedmica[4]
    elif izbor == 6:
        return dni_sedmica[5]
    else:
        return None
