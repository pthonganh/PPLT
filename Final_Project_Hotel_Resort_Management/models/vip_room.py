from models.room import Room


class VIPRoom(Room):

    def calculate_price(self, days):
        return self.price * days

    def get_room_type(self):
        return "VIP"

    def get_services(self):
        return ["WiFi", "TV", "Breakfast", "Gym Access"]