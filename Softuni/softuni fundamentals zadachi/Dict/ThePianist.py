n=int(input())
rechnik={}
for x in range(n):
    command=input().split("|")
    piece=command[0]
    composer=command[1]
    key=command[2]
    rechnik[piece]=[composer,key]
data=input()
while data != "Stop":
    commanda=data.split("|")
    funkciq=commanda[0]
    if funkciq == "Add":
        piece = commanda[1]
        composer = commanda[2]
        key = commanda[3]
        if piece in rechnik.keys():
            print(f"{piece} is already in the collection!")
        else:
            rechnik[piece]=[composer,key]
            print(f"{piece} by {composer} in {key} added to the collection!")
    if funkciq == "Remove":
        piece = commanda[1]
        if piece in rechnik.keys():
            rechnik.pop(piece)
            print(f"Successfully removed {piece}!")
        else:
            print(f"Invalid operation! {piece} does not exist in the collection.")
    if funkciq == "ChangeKey":
        piece = commanda[1]
        new_key=commanda[2]
        if piece in rechnik.keys():
            rechnik[piece][1]=new_key
            print(f"Changed the key of {piece} to {new_key}!")
        else:
            print(f"Invalid operation! {piece} does not exist in the collection.")
    data=input()
for k in rechnik.keys():
    print(f"{k} -> Composer: {rechnik[k][0]}, Key: {rechnik[k][1]}")







