from abc import ABC, abstractmethod


class Room(ABC):

    def __init__(self, room_id, price, capacity):
        self.__room_id = room_id
        self.__price = price
        self.__capacity = capacity
        self.__status = "Available"

    @property
    def room_id(self):
        return self.__room_id

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError("Price cannot be negative.")
        self.__price = value

    @property
    def capacity(self):
        return self.__capacity

    @capacity.setter
    def capacity(self, value):
        if value <= 0:
            raise ValueError("Capacity must be greater than 0.")
        self.__capacity = value

    @property
    def status(self):
        return self.__status

    @status.setter
    def status(self, value):
        self.__status = value

    @abstractmethod
    def calculate_price(self, days):
        pass

    @abstractmethod
    def get_room_type(self):
        pass

    def to_dict(self):
        return {
            "room_id": self.room_id,
            "price": self.price,
            "capacity": self.capacity,
            "status": self.status,
            "room_type": self.get_room_type()
        }