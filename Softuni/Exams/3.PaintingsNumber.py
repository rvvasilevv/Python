accession_number=[int(x) for x in input().split(' ')]
comanda=input()
while comanda != "END":
    funkciq=comanda.split(" ")
    if funkciq[0] == "Change":
        paintings_number=int(funkciq[1])
        new_number=int(funkciq[2])
        if paintings_number in accession_number:
            for i in range(len(accession_number)):
                if accession_number[i] == paintings_number:
                    accession_number[i] = new_number
        else:
            pass
    elif funkciq[0] =="Hide":
        paintings_number=int(funkciq[1])
        if paintings_number in accession_number:
            accession_number.remove(paintings_number)
        else:
            pass
    elif funkciq[0] == "Switch":
        paintings_number1=int(funkciq[1])
        paintings_number2=int(funkciq[2])
        if paintings_number1 in accession_number and paintings_number2 in accession_number:
            edno, dve = accession_number.index(paintings_number1), accession_number.index(paintings_number2)
            accession_number[dve], accession_number[edno] = accession_number[edno], accession_number[dve]
        else:
            pass
    elif funkciq[0] == "Insert":
        index=int(funkciq[1])
        resulting_index=index + 1
        paintings_number=int(funkciq[2])
        if resulting_index in range(0,len(accession_number)):
            accession_number.insert(resulting_index, paintings_number)
        else:
            pass
    elif funkciq[0] == "Reverse":
        accession_number.reverse()

    comanda=input()
print(" ".join(map(str,accession_number)))