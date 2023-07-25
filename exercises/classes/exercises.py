"""An introduction to classes in Python"""

"""
CREATE A CUSTOMER CLASS
-----------------------

In the area below you will create a class called `Customer`, and add to this
class as the exercises go on:

* Uncomment the two print statements at the bottom of this section.

* Define a new class called `Customer`, with no functionality (just use `pass`
  as the class body)

* Replace the Ellipsis (...) so that `customer_instance` is an instance of the
  `Customer` class.
"""

# <<< REPLACE THIS COMMENT WITH A NEW CLASS DEFINITION FOR `Customer` >>>

customer_instance = ...

# print("Customer has type", type(Customer))
# print("customer_instance has type", type(customer_instance))


"""
SETTING ATTRIBUTES ON AN INSTANCE
---------------------------------

Before the `Customer` class existed, customers were represented as dictionaries
like `customer_1` and `customer_2` below. You can now replace these with
instances of the customer class.

* Uncomment the four print statements at the bottom of this section, and run
  the script. You should see:

        customer_1 has type <class 'dict'>
        customer_2 has type <class 'dict'>
        customer_1 is called: Tuna Turner
        customer_2 is called: Eel Pacino

* Replace the definitions of `customer_1` and `customer_2`, so that instead of
  being `dict`s they are `Customer`s, which have `first_name` and `surname`
  as attributes on the class.

* Modify the final two print statements in this section, so that they still run
  successfully, and print out the full names of both customers.
"""

customer_1 = {
    "first_name": "Tuna",
    "surname": "Turner"
}
customer_2 = {
    "first_name": "Eel",
    "surname": "Pacino"
}

# print()
# print("customer_1 has type", type(customer_1))
# print("customer_2 has type", type(customer_2))

# # You'll need to update the two print statements below here:

# print("customer_1 is called:", customer_1["first_name"], customer_1["surname"])
# print("customer_2 is called:", customer_2["first_name"], customer_2["surname"])


"""
ADDING A BASKET TO THE CUSTOMER
--------------------------------

* Give first_name and surname default values of the empty string `''` so that a
  `Customer` can be created without providing any names.

* Add a new class attribute called `basket` in the constructor for `Customer`
  and set it equal to an empty set `set()`

* Uncomment and read the code lines below, but don't edit them in any other way.
  Make sure you understand what each of the lines is doing.
"""

# customer_3 = Customer()
# customer_3.basket.add("Kelp")
# customer_3.basket.add("Seaweed")
# customer_3.basket.add("Krill")
# print()
# print("customer_3's basket contains:", customer_3.basket)


"""
USING CLASSES TOGETHER
----------------------

The code below defines a new class, `Item`, which has a name, and a price. You
will modify the `Customer` class to expect `Item`s to be added to the basket
instead of strings.

* Uncomment the lines of code below. They create a new customer, `customer_4`
  and add some items to the customer's basket.

* Add a new method to the `Customer` class called `basket_items`, which will
  return a list of the names of the items in the basket.

* Add a new method to the `Customer` class called `basket_value`, which will
  return the total value of the items in the basket (the sum of all items'
  individual values)

"""


class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price


kelp = Item("kelp", 19)
seaweed = Item("seaweed", 13)
krill = Item("krill", 11)


# customer_4 = Customer("Ernest", "Herringway")
# customer_4.add_to_basket(kelp)
# customer_4.add_to_basket(seaweed)
# customer_4.add_to_basket(seaweed)
# customer_4.add_to_basket(krill)
# print()
# print("customer_4's basket contains:", customer_4.basket_items())
# print("customer_4's basket value is:", customer_4.basket_value())
