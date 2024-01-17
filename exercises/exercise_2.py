# ========================================== 
# Printing Multipliers    
# ========================================== 
# 
# Edit this program so that it prints the first 10 multiples of 
#       each of the numbers from 1 to 5.
# Print each set of multiples on a new row like this:
#
#   ```
#   Multiples of 1: 1 2 3 4 5 6 7 8 9 10
#   Multiples of 2: 2 4 6 8 10 12 14 16 18 20
#   etc.
#   ```

multiples_of = 5

# Print will output on the same line if `end=""`
print(f"Multiples of {multiples_of}: ", end="")

for i in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
    print(f"{i * multiples_of} ", end="")

# Called once to add a line break
print()
