# function name should be lowercase with underscore
def calculate_square_area(side_length):
    return side_length ** 2

# variable name should be lowercase
radius = 5

# class name should be uppercase
class Circle:
    def __init__(self, radius):
        self.radius = radius
# function name should be lowercase with underscore
    def calculate_circumference(self):
        return 2 * 3.14 * self.radius
# 
if __name__ == "__main__":
    

    square_area = calculate_square_area(4)
    print("Square Area:", square_area)

    # objectname should be lowercase
    circle_obj = Circle(radius)
    circumference = circle_obj.calculate_circumference()
    print("Circle Circumference:", circumference)
    
    # constant should be uppercase with underscore
   MY_CONSTANT = 100
