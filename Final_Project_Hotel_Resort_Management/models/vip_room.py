from models.room import Room


class VIPRoom(Room):

    def calculate_price(self, days):
        return self.price * days * 1.1

    def get_room_type(self):
        return "VIP"