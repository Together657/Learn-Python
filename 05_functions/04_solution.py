import math

def circle_stats(radius):
    area = math.pi * radius ** 2
    circumference = 2 * math.pi * radius
    return area , circumference

a, c = circle_stats(3)
print("The area of the circle is {} and its circumference is {}".format(a,c))
