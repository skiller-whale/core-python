"""
BOOLEAN OPERATORS
-------------------
"""
upstairs_switch_up   = True
downstairs_switch_up = True

light_on = upstairs_switch_up or downstairs_switch_up

# print("upstairs_switch_up is", str(upstairs_switch_up))
# print("downstairs_switch_up is", str(downstairs_switch_up))
# print("light_on is", str(light_on))

"""
IF BLOCKS
---------
"""
# print()

age = 21
height = 172

# print("Entry is allowed")
# print("Entry is not allowed")
# print("Age:", age, ";", "Height:", height)

"""
WHITESPACE
----------
"""
# print()

print_extra_line = False

# print("print_extra_line is", print_extra_line)

if print_extra_line:
    pass
# print("This line should only print if print_extra_line is True")
# print("This line should print in any case")

"""
IF, ELSE, ELIF
--------------
"""
# print()

age = 18

# print("One or younger: a baby")
# print("Under 4: a toddler")
# print("Up to 12: a child")
# print("Up to 19: a teenager")
# print("20 or older: an adult")

# print("The person is", age, "years old")


"""
FALSY AND TRUTHY
----------------
"""
# print()

password = "password"

allowed_1 = "skiller"
allowed_2 = "whale"

# print("Allowed passwords:", allowed_1, ";", allowed_2)
# print("Entered password:", password)
if password == allowed_1 or allowed_2:
    pass
    # print("Password match successful")
else:
    pass
    # print("Password match unsuccessful")
