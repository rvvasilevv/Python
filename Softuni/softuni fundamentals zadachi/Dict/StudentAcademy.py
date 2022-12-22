broika=int(input())
ocenki_imena=[]
rechnik={}
for x in range(broika):
    ime=str(input())
    ocenka=float(input())
    if ime not in rechnik.keys():
        rechnik[ime] =ocenka
    elif ime in rechnik.keys():
        rechnik[ime] = (rechnik[ime]+ocenka) / 2
for ime,ocenka in rechnik.items():
    if rechnik[ime] >= 4.5:
        print(f"{ime} ->{rechnik[ime]: .2f}")


