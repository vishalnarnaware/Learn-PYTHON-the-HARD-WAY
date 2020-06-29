cars = 100
space_in_a_car = 4.0
drivers = 30
passengers = 90
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_a_car
average_passenger_per_car = passengers / cars_driven


print("There are", cars, "cars available.")
print("There are only", drivers, "drivers available.")
print("There will be", cars_not_driven, "empty cars today.")
print("We can transport", carpool_capacity, "people today.")
print("We have", passengers, "to carpool today.")
print("We need to put about", average_passenger_per_car, "in each car.")


# Study Drills
# 1. I used 4.0 for space_in_a_car, but is that necessary? What happens if it’s just 4?
# Actually that wouold work fineand yield the same output. (Python 3)

# 2. Remember that 4.0 is a “floating point” number. Find out what that means.
# Floating point number means it has values after decimal. Eg.: 3.00, 6.9

# 3. Write comments above each of the variable assignments.
# Idk name seem to be self explanatory. But still is a good practice.

# 4. Make sure you know what = is called (equals) and that it’s making names for things.
# Yeah. '=' is called equals and is an assignment operator.

# 5. Remember that _ is an underscore character.
# Without '_' it would be really hard for us to define meaningfull variable names.

# 6. Try running Python as a calculator like you did before and use variable names
# to do your calculations. Popular variable names are also i, x, and j.
# Good Luck (*.*)
