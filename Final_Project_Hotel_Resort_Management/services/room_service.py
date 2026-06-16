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
        self.save_data()

        return room

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

            if (
                keyword.lower() in room.room_id.lower()
                or keyword.lower() in room.get_room_type().lower()
                or keyword.lower() in room.status.lower()
            ):
                result.append(room)

        return result

    def find_rooms_by_type(self, room_type):

        result = []

        for room in self.rooms:

            if room.get_room_type().lower() == room_type.lower():
                result.append(room)

        return result

    def find_rooms_by_status(self, status):

        result = []

        for room in self.rooms:

            if room.status.lower() == status.lower():
                result.append(room)

        return result

    # =========================
    # UPDATE
    # =========================

    def update_room(
        self,
        room_id,
        new_price=None,
        new_capacity=None,
        new_status=None
    ):

        room = self.find_room_by_id(room_id)

        if room is None:
            return False

        if new_price is not None:
            room.price = new_price

        if new_capacity is not None:
            room.capacity = new_capacity

        if new_status is not None:
            room.status = new_status

        self.save_data()

        return True

    # =========================
    # DELETE
    # =========================

    def delete_room(self, room_id):

        room = self.find_room_by_id(room_id)

        if room is None:
            return False

        if room.status == "Booked":
            raise ValueError("Cannot delete a booked room.")

        self.rooms.remove(room)

        self.save_data()

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

    def sort_by_capacity_ascending(self):

        return sorted(
            self.rooms,
            key=lambda room: room.capacity
        )

    def sort_by_capacity_descending(self):

        return sorted(
            self.rooms,
            key=lambda room: room.capacity,
            reverse=True
        )

    # =========================
    # ROOM STATUS
    # =========================

    def get_available_rooms(self):

        return self.find_rooms_by_status("Available")

    def get_booked_rooms(self):

        return self.find_rooms_by_status("Booked")

    # =========================
    # STATISTICS
    # =========================

    def count_rooms_by_type(self):

        result = {}

        for room in self.rooms:

            room_type = room.get_room_type()

            if room_type not in result:
                result[room_type] = 0

            result[room_type] += 1

        return result

    def count_rooms_by_status(self):

        result = {
            "Available": 0,
            "Booked": 0
        }

        for room in self.rooms:

            if room.status not in result:
                result[room.status] = 0

            result[room.status] += 1

        return result

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

                    room = self.create_room_from_dict(item)

                    if room:
                        self.rooms.append(room)

        except FileNotFoundError:

            self.rooms = []

        except json.JSONDecodeError:

            self.rooms = []

    # =========================
    # HELPER
    # =========================

    def create_room_from_dict(self, item):

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
            return None

        room.status = item.get("status", "Available")

        return room