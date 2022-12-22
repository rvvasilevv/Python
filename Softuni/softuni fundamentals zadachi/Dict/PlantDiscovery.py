n=int(input())
cvetq={}
for x in range(n):
    zadanie=input().split("<->")
    plant=zadanie[0]
    rarity=zadanie[1]
    rating=0
    if plant in cvetq.keys():
        cvetq[plant][0]=rarity
    else:
        cvetq[plant]=[rarity,rating]
data=input()
while data != "Exhibition":
    command=data.split