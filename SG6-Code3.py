import math

def calculate_distance(x1,y1,x2,y2):
    d = math.sqrt(math.pow(x2 - x1, 2) + math.pow(y2 - y1, 2))
    return d

x1 = float(input("Enter x1: "))
y1 = float(input("Enter y1: "))
x2 = float(input("Enter x2: "))
y2 = float(input("Enter y2: "))
distance = calculate_distance(x1, y1, x2, y2)
print(f"The distance between the points is: {distance:.2f}")