"""
The class `Company` below is initialized with a list of the contractors and
employees who work there, and it can print their details using the
`list_people()` method.

At the moment, all contractors and employees have the class `Person`.
You will change this so that contractors have the class `Contractor` and
employees have the class `Employee`.

1. Create two new classes `Contractor` and `Employee` which are subclasses of
  `Person`.

2. Update:

  * The employees 'Geri Hallibut' and 'Free Willy Nelson' so they have the
    newly defined `Employee` class.

  * The contractors 'Sealion Dion' and 'Goldie Prawn' so they have the
    newly defined `Contractor` class.
"""


class Company:
    def __init__(self, name, employees, contractors):
        self.name = name
        self.employees = employees      # A list of employees
        self.contractors = contractors  # A list of contractors

    def list_people(self):
        """Print details of the people working at the company"""
        print("People working at", self.name + ":")

        for employee in self.employees:
            print('* ', employee.description())

        for contractor in self.contractors:
            print('* ', contractor.description())


class Person:
    def __init__(self, name, job_title):
        self.name = name
        self.job_title = job_title

    def description(self):
        """Return a description string e.g. 'Dave the engineer"""
        return self.name + ", the " + self.job_title


# < DEFINE `Contractor` AND `Employee` CLASSES HERE >


# TODO Change these employees to have the Employee class
employees = [
    Person("Geri Hallibut", "Sea.E.O"),
    Person("Free Willy Nelson", "Digital Sharketing Intern"),
]

# TODO Change these contractors to have the Contractor class
contractors = [
    Person("Sealion Dion", "Regional Seals Manager"),
    Person("Goldie Prawn", "Sea Sharp Engineer"),
]

company = Company("Clamazon", employees=employees, contractors=contractors)
company.list_people()
