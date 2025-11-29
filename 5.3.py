###
# A program that calculates the volume
# and surface area of ​​a cuboid with sides a, b, and c.
# Read the dimensions of the cuboid from the keyboard.
#
a = int(input('a='))
b = int(input('b='))
c = int(input('c='))
print(f'volume = {a*b*c}, surface area = {a*b*2+b*c*2+a*c*2}')