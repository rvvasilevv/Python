import random

number=random.randint(1, 10)
poznato= None

while True:
    poznato = int(input("Guess a number between 1 and 10:"))
    if poznato < number:
        print("tvurde malko batko")
    elif poznato > number:
        print("tvurde golqmo ")
    else:
        print("specheli!")
        cukalitisepak=input("igrae li ti se pak")
        if cukalitisepak == "y":
            number=random.randint(1, 10)
            poznato = None
        else:
            print("mersi che igra!")
            break

