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

    # =========================
    # UPDATE
    # =========================

    def update_customer(
        self,
        customer_id,
        new_name,
        new_phone,
        new_email
    ):

        customer = self.find_customer_by_id(customer_id)

        if customer is None:
            return False

        customer.name = new_name
        customer.phone = new_phone
        customer.email = new_email

        return True

    # =========================
    # DELETE
    # =========================

    def delete_customer(self, customer_id):

        customer = self.find_customer_by_id(customer_id)

        if customer is None:
            return False

        self.customers.remove(customer)

        return True

    # =========================
    # SORT
    # =========================

    def sort_by_name(self):

        return sorted(
            self.customers,
            key=lambda customer: customer.name.lower()
        )

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
            