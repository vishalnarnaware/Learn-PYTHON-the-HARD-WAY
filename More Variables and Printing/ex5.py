my_name = 'Zed A. Shaw'
my_age = 35 # not a lie
my_height = 74 # inches
my_weight = 180 # lbs
my_eyes = 'Blue'
my_teeth = 'White'
my_hair = 'Brown'

print("Let's talk about %s." % my_name)
print("He's %d inches tall." % my_height)
print("He's %d pounds heavy." % my_weight)
print("Actually that's not too heavy.")
print("He's got %s eyes and %s hair" % (my_eyes, my_hair))
print("His teeth are usually %s depending on the coffee." % my_teeth)

# this line is tricky, try to get it exactly right
print("If I add %d, %d and %d I get %d." % (my_age, my_height, my_weight,
                                            my_age + my_height + my_weight))


# Study Drills
# 1. Change all the variables so there isn’t the my_ in front.
# Make sure you change the name everywhere, not just where you used = to set them.
# Just remove my_ from everywhere and you'll be fine.

# 2. Try more format characters. %r is a very useful one. It’s like saying
# “print this no matter what.”
# I think r stands for raw...

# 3. Search online for all the Python format characters.
# In docs.python.org Topic = 5.6.2.
# String Formatting Operations http://docs.python.org/library/stdtypes.html#string-formatting
# then further down to the chart (text above chart is "The conversion types are:")#

# 4. Try to write some variables that convert the inches and pounds to centimeters and kilos.
# Do not just type in the measurements. Work out the math in Python.
# 1 inch = 2.54 cm    and     1 pound = 0.45359237 kg
# inch_to_cm = 2.54 * my_height
# pound_to_kg = 0.45359237 * my_weight
