from parent_class import Base

class Child(Base):
    def __init__(self,name,age):
        Base.__init__(self,name)
        self.age=age
    def get_age(self):
        return self.age
