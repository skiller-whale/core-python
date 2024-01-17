import time

# ========================================== 
# Do programmers dream of electric sheep?    
# ========================================== 
# 
#  Alan tries to fall asleep by counting 'electric sheep'.
#  For any nth sheep, if n is even then Alan counts n in decimal.
#  Otherwise, it is an electric sheep and he counts n in binary.
#  For example, Alan would count six sheep as follows:
#
#  0 sheep
#  1 sheep
#  2 sheep
#  11 sheep
#  4 sheep
#  101 sheep
#  6 sheep
#
#  Using a while loop and if statements, write a program that will print Alan's counting while he is awake.
#  The loop should stop when Alan falls asleep.
#  Usually he falls asleep when he reaches a count of ten.
#
# NOTE: To convert a number to a binary string use the function `convert_to_binary(number)`.
# 


def convert_to_binary(number):
    return bin(number)[2:]


count = 0
awake = True

while awake:
    # Sleep for 1 second between counts
    time.sleep(1)
