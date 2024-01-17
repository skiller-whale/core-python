# ============================================
# Printing Multipliers - User Friendly Version
# ============================================
# 
# Change this program so that it asks the user which number they want to see multipliers of.

# For example if the user inputs "25", it will output "Multiples of 25: 25, 50, 75 ..." etc.
# Additionally:
#   * If the user enters "quit" the program should exit.
#   * If the user outputs `0`, there should be no output.


multiples_of = 5

# Print will output on the same line if `end=""`
print(f"Multiples of {multiples_of}: ", end="")

for i in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
    print(f"{i * multiples_of} ", end="")

# Called once to add a line break
print()
