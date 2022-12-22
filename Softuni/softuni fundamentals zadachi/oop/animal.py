class Animal:
    species="humans"
    def __init__(self,name):
        self.name=name
test_obj=Animal("Gosho")
print(test_obj.name)
print(test_obj.species)