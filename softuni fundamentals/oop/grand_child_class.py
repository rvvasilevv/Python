from child_class import Child
class GrandChildClass(Child):
    def __init__(self,name,age,addres):
        Child.__init__(self,name,age)
        self.addres=addres
    def get_addres(self):
        return self.addres



obj=GrandChildClass('Ivan Nikolov', 45, 'Sofia')
print(obj.get_name(), obj.get_age(), obj.get_addres())

