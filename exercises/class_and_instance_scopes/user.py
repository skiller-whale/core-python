class User:
    def __init__(self, name, role, user_id):
        self.validate_role(role)   # Ensure that the role has an allowed value
        self.validate_id(user_id)  # Ensure that the id is a unique integer
        self.user_id = user_id
        self.name = name
        self.role = role
        self.log_user_creation()

    def is_valid_role(self, role):
        # TODO: Update this to correctly implement role checking logic
        return True

    def is_unique(self, user_id):
        return True

    def log_user_creation(self):
        self.log("User", self.user_id, "-", self.name, "created with role:", self.role)

    def log(self, *args):
        print("USER LOG: ", *args)

    # Validation Methods
    # ~~~~~~~~~~~~~~~~~~

    def validate_role(self, role):
        """Raise an exception if role does not have an allowed value"""
        if not self.is_valid_role(role):
            self.log(role, "is not a valid role")
            raise ValueError("Invalid role")

    def validate_id(self, user_id):
        """Raises an exception if user_id is not a unique integer"""
        if not isinstance(user_id, int):
            self.log("User id", user_id, "is not an integer")
            raise TypeError("user_id should be an integer")

        if not self.is_unique(user_id):
            self.log("User cannot be created with a non unique id:", user_id)
            raise ValueError(f"User id is not unique")
