# use of Function inside the another function
def calculate_area(length, width):
    area = length * width
    return area

def calculate_volume(length, width, height):
    base_area = calculate_area(length, width)
    volume = base_area * height
    return volume
length = 2
width = 3
height = 4
volume = calculate_volume(length, width, height)
print("The volume of the rectangular prism is:", volume)

