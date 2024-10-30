# functions
from datetime import date


def calc_area_triangle(b, h):
    area = 0.5 * b * h
    print(area)


def calc_area_circle(radius):
    area = 22/7 * radius * radius #one can use math.pi as 22/7
    area = round(area, 2)
    print('Area of circle is', area, 'cm^2')


def print_todays_date():
    today = date.today()
    print(today)


def add(*args):
    total = 0
    for num in args:
        total += num
        print('Total is ',total)

def sayHi(name, age=21):
    print('Hello ', name, 'I am ', age, 'years old.')

sayHi('Frank')
sayHi('Kish', 23)

# use a fun == calling
calc_area_triangle(8, 13)
calc_area_triangle(40, 66)

triangles = [[8, 9], [6, 13], [21, 27], [16, 41], [31.5, 66.97]]

for t in triangles:
    calc_area_triangle(t[0], t[1])


calc_area_circle(2.76)

print_todays_date()

add(1, 2)
add(7, 8, 9)
add(76, 34, 23, 45, 56)
