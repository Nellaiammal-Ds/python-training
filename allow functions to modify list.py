# Function that modifies a list
def modify_list(my_list):
    # Appending an element to the list
    my_list.append(4)

    # Changing an element in the list
    my_list[1] = 'new value'


# Creating a list
original_list = [1, 2, 3]

# Displaying the original list
print("Original list:", original_list)

# Calling the function that modifies the list
modify_list(original_list)

# Displaying the modified list
print("Modified list:", original_list)
