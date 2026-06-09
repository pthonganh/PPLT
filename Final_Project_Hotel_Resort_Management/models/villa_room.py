from models.room import Room


class VillaRoom(Room):

    def calculate_price(self, days):
        return self.price * days * 1.2

    def get_room_type(self):
        return "Villa"