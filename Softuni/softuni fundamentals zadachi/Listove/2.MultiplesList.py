chislo=int(input())
faktor=int(input())
list = []
dobavqne=0
for x in range(faktor):
    dobavqne=chislo+dobavqne
    list.append(dobavqne)
print(list)