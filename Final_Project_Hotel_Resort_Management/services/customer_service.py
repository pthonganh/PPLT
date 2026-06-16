import json

from models.customer import Customer


class CustomerService:

    def __init__(self):
        self.customers = []
        self.load_data()

    # =========================
    # CREATE
    # =========================

    def add_customer(self, customer):

        if self.find_customer_by_id(customer.customer_id):
            raise ValueError("Customer ID already exists.")

        self.customers.append(customer)

        self.save_data()

        return customer

    # =========================
    # READ
    # =========================

    def get_all_customers(self):
        return self.customers

    # =========================
    # SEARCH
    # =========================

    def find_customer_by_id(self, customer_id):

        for customer in self.customers:

            if customer.customer_id == customer_id:
                return customer

        return None

    def search_customer_by_name(self, keyword):

        result = []

        for customer in self.customers:

            if keyword.lower() in customer.name.lower():
                result.append(customer)

        return result

    def search_customer_by_phone(self, phone):

        result = []

        for customer in self.customers:

            if phone in customer.phone:
                result.append(customer)

        return result

    # =========================
    # UPDATE
    # =========================

    def update_customer(
        self,
        customer_id,
        new_name=None,
        new_phone=None,
        new_email=None
    ):

        customer = self.find_customer_by_id(customer_id)

        if customer is None:
            return False

        if new_name is not None:
            customer.name = new_name

        if new_phone is not None:
            customer.phone = new_phone

        if new_email is not None:
            customer.email = new_email

        self.save_data()

        return True

    # =========================
    # DELETE
    # =========================

    def delete_customer(self, customer_id):

        customer = self.find_customer_by_id(customer_id)

        if customer is None:
            return False

        self.customers.remove(customer)

        self.save_data()

        return True

    # =========================
    # SORT
    # =========================

    def sort_by_name(self):

        return sorted(
            self.customers,
            key=lambda customer: customer.name.lower()
        )

    def sort_by_name_descending(self):

        return sorted(
            self.customers,
            key=lambda customer: customer.name.lower(),
            reverse=True
        )

    # =========================
    # STATISTICS
    # =========================

    def count_customers(self):

        return len(self.customers)

    # =========================
    # SAVE JSON
    # =========================

    def save_data(self):

        data = []

        for customer in self.customers:
            data.append(customer.to_dict())

        with open(
            "data/customers.json",
            "w",
            encoding="utf-8"
        ) as file:

            json.dump(
                data,
                file,
                indent=4,
                ensure_ascii=False
            )

    # =========================
    # LOAD JSON
    # =========================

    def load_data(self):

        try:

            with open(
                "data/customers.json",
                "r",
                encoding="utf-8"
            ) as file:

                data = json.load(file)

                for item in data:

                    customer = Customer(
                        item["customer_id"],
                        item["name"],
                        item["phone"],
                        item["email"]
                    )

                    self.customers.append(customer)

        except FileNotFoundError:

            self.customers = []

        except json.JSONDecodeError:

            self.customers = []