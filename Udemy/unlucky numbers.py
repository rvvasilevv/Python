for chislo in range(1,21):
    if chislo % 2 == 0:
        if chislo == 4 or chislo == 13:
            print(f'{chislo}e unlucky')
        else:
            print(f"{chislo} e chetno")

    elif chislo % 2 != 0 :
        if chislo == 4 or chislo == 13:
            print(f'{chislo}e unlucky')
        else:print(f"{chislo} e nechetno")

