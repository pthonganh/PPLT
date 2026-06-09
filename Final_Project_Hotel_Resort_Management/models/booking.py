class Booking:

    def __init__(
        self,
        booking_id,
        customer_id,
        room_id,
        check_in,
        check_out,
        total_price
    ):
        self.__booking_id = booking_id
        self.__customer_id = customer_id
        self.__room_id = room_id
        self.__check_in = check_in
        self.__check_out = check_out
        self.__total_price = total_price

    @property
    def booking_id(self):
        return self.__booking_id

    @property
    def customer_id(self):
        return self.__customer_id

    @property
    def room_id(self):
        return self.__room_id

    @property
    def check_in(self):
        return self.__check_in

    @property
    def check_out(self):
        return self.__check_out

    @property
    def total_price(self):
        return self.__total_price

    def to_dict(self):
        return {
            "booking_id": self.booking_id,
            "customer_id": self.customer_id,
            "room_id": self.room_id,
            "check_in": self.check_in,
            "check_out": self.check_out,
            "total_price": self.total_price
        }