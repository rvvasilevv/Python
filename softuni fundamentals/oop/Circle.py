class Circle:
    __pi=3.14
    def __init__(self,diameter):
        self.diameter=diameter
        self.radius=diameter/2
    def calculate_circumference(self):
        self.circumference=Circle.__pi*self.diameter
        return self.circumference
    def calculate_area(self):
        self.area= ((1 / 4) * Circle.__pi * (self.diameter * self.diameter))
        return self.area
    def calculate_area_of_sector(self,angle):
        return (angle/360)*Circle.__pi*self.radius*self.radius

comanda=float(input())
circle=Circle(comanda)
angle=float(input())
print(f"{circle.calculate_circumference():.2f}")
print(f"{circle.calculate_area():.2f}")
print(f"{circle.calculate_area_of_sector(angle):.2f}")

