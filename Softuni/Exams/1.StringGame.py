wordsanddefefinitions=input().split(" | ")
dictionary = {}
listDef=[]
for x in wordsanddefefinitions:
    token = x.split(": ")
    word=token[0]
    definition=token[1]
    if word not in dictionary.keys():
        dictionary[word]=[definition]
    else:
        dictionary[word].append(definition)
dumi_za_test=input().split(" | ")

comanda=input()
if comanda == "Test":
    for duma in dumi_za_test:

        if duma in dictionary.keys():
            print(f'{duma}:')
            for definitions in dictionary[duma]:
                print(f' -{definitions}')
elif comanda == "Hand Over":
    list_of_the_keys = list(dictionary.keys())
    print(" ".join(list_of_the_keys))