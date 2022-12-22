class Catalogue:
    def __init__(self,name):
        self.name=name
        self.products=[]
    def add_product(self,product_name):
        self.products.append(product_name)
    def get_by_letter(self,first_letter):
        self.first_letter=first_letter
        return [x for x in self.products if x[0]==self.first_letter]
    def __repr__(self):
        for x in range(len(self.products)):
            return self.products.pop()

catalogue = Catalogue("Furniture")
catalogue.add_product("Sofa")
catalogue.add_product("Mirror")
catalogue.add_product("Desk")
catalogue.add_product("Chair")
catalogue.add_product("Carpet")
print(catalogue.get_by_letter("M"))
print(catalogue)



