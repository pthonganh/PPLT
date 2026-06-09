from models.room import Room


class StandardRoom(Room):

    def calculate_price(self, days):
        return self.price * days

    def get_room_type(self):
        return "Standard"