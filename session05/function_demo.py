import math


def area_of_circle(whatever):
    """returns the area of circle with parameter, which is a float"""
    # print(math.pi * whatever ** 2)
    return math.pi * whatever ** 2
    


r1 = 10
# area_of_circle(r1)
a1 = area_of_circle(r1)
print(f'the area of the circle is {a1}.')

r2 = 100
a2 = area_of_circle(r2)
print(a2)

print(a1 > a2)


def give_me_a_break():
    str1 = 'break'
    return str1
    print('another break')
    
print(give_me_a_break())