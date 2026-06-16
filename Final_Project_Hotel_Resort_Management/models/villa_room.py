from models.room import Room


class VillaRoom(Room):

    def calculate_price(self, days):
        return self.price * days

    def get_room_type(self):
        return "Villa"

    def get_services(self):
        return ["WiFi", "TV", "Breakfast", "Private Pool", "Butler Service"]