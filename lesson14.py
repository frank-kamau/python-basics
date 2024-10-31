#cylinder
class Cylinder:
    def __init__(self,radius,height, color):
        self.r = radius
        self.h= height
        self.rangi = color

    def calc_area(self, is_closed):
        if is_closed == True:
            area = 2 * 22/7 * self.r ** 2 + 2 * 22/7 * self.r * self.h
            print(f'The area of the closed cylinder is: {area}')
        else:
            area = 22/7 * self.r ** 2 + 2 * 22/7 * self.r * self.h
            print(f'The area of the open cylinder is: {area}')

    def calc_volume (self):
        v = 22/7 * self.r ** 2 * self.h
        print(f'The volume of the cylinder is: {v}')


c1 = Cylinder(10, 11, 'Red')
c2 = Cylinder(7.8, 22.6, 'Blue')
c1.calc_volume()
c1.calc_area(is_closed=False)


# classes in python/ oop in python
# intro to oop in python -----check youtube