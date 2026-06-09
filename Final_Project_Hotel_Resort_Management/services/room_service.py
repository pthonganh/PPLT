import json

from models.standard_room import StandardRoom
from models.vip_room import VIPRoom
from models.villa_room import VillaRoom


class RoomService:

    def __init__(self):
        self.rooms = []
        self.load_data()

    # =========================
    # CREATE
    # =========================

    def add_room(self, room):

        if self.find_room_by_id(room.room_id):
            raise ValueError("Room ID already exists.")

        self.rooms.append(room)

    # =========================
    # READ
    # =========================

    def get_all_rooms(self):
        return self.rooms

    # =========================
    # SEARCH
    # =========================

    def find_room_by_id(self, room_id):

        for room in self.rooms:

            if room.room_id == room_id:
                return room

        return None

    def search_room(self, keyword):

        result = []

        for room in self.rooms:

            if keyword.lower() in room.room_id.lower():
                result.append(room)

        return result

    # =========================
    # UPDATE
    # =========================

    def update_room(
        self,
        room_id,
        new_price,
        new_capacity
    ):

        room = self.find_room_by_id(room_id)

        if room is None:
            return False

        room.price = new_price
        room.capacity = new_capacity

        return True

    # =========================
    # DELETE
    # =========================

    def delete_room(self, room_id):

        room = self.find_room_by_id(room_id)

        if room is None:
            return False

        self.rooms.remove(room)

        return True

    # =========================
    # SORT
    # =========================

    def sort_by_price_ascending(self):

        return sorted(
            self.rooms,
            key=lambda room: room.price
        )

    def sort_by_price_descending(self):

        return sorted(
            self.rooms,
            key=lambda room: room.price,
            reverse=True
        )

    # =========================
    # ROOM STATUS
    # =========================

    def get_available_rooms(self):

        return [
            room
            for room in self.rooms
            if room.status == "Available"
        ]

    def get_booked_rooms(self):

        return [
            room
            for room in self.rooms
            if room.status == "Booked"
        ]

    # =========================
    # SAVE JSON
    # =========================

    def save_data(self):

        data = []

        for room in self.rooms:
            data.append(room.to_dict())

        with open(
            "data/rooms.json",
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
                "data/rooms.json",
                "r",
                encoding="utf-8"
            ) as file:

                data = json.load(file)

                for item in data:

                    room_type = item["room_type"]

                    if room_type == "Standard":

                        room = StandardRoom(
                            item["room_id"],
                            item["price"],
                            item["capacity"]
                        )

                    elif room_type == "VIP":

                        room = VIPRoom(
                            item["room_id"],
                            item["price"],
                            item["capacity"]
                        )

                    elif room_type == "Villa":

                        room = VillaRoom(
                            item["room_id"],
                            item["price"],
                            item["capacity"]
                        )

                    else:
                        continue

                    room.status = item["status"]

                    self.rooms.append(room)

        except FileNotFoundError:

            self.rooms = []

        except json.JSONDecodeError:

            self.rooms = []