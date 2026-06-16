class Customer:

    def __init__(self, customer_id, name, phone, email):
        self.__customer_id = customer_id
        self.name = name
        self.phone = phone
        self.email = email

    @property
    def customer_id(self):
        return self.__customer_id

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if value.strip() == "":
            raise ValueError("Name cannot be empty.")
        self.__name = value

    @property
    def phone(self):
        return self.__phone

    @phone.setter
    def phone(self, value):
        if not value.isdigit():
            raise ValueError("Phone number must contain only digits.")
        self.__phone = value

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, value):
        if "@" not in value:
            raise ValueError("Invalid email format.")
        self.__email = value

    def to_dict(self):
        return {
            "customer_id": self.customer_id,
            "name": self.name,
            "phone": self.phone,
            "email": self.email
        }