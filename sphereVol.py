"""
formula for volume of a sphere:
    https://www.google.ca/search?hl=en&q=formula+for+volume+of+a+sphere&gws_rd=cr&ei=ZLjwVaHHNISNyATJzJXwCg
"""

import math

r = float(input("radius of sphere: "))

v = (4/3) * math.pi * r**3

print("the volume of a sphere of r = ", r, " is: {0:.2f}".format(v))
