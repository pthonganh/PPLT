import json
from datetime import datetime

from models.booking import Booking


class BookingService:

    def __init__(
        self,
        room_service,
        customer_service
    ):

        self.bookings = []
        self.room_service = room_service
        self.customer_service = customer_service

        self.load_data()

    # =========================
    # CREATE BOOKING
    # =========================

    def create_booking(
        self,
        booking_id,
        customer_id,
        room_id,
        check_in,
        check_out
    ):

        if self.find_booking_by_id(booking_id):
            raise ValueError("Booking ID already exists.")

        customer = self.customer_service.find_customer_by_id(
            customer_id
        )

        if customer is None:
            raise ValueError("Customer not found.")

        room = self.room_service.find_room_by_id(
            room_id
        )

        if room is None:
            raise ValueError("Room not found.")

        if room.status != "Available":
            raise ValueError("Room is already booked.")

        days = self.calculate_days(
            check_in,
            check_out
        )

        total_price = room.calculate_price(
            days
        )

        booking = Booking(
            booking_id,
            customer_id,
            room_id,
            check_in,
            check_out,
            total_price
        )

        room.status = "Booked"

        self.bookings.append(
            booking
        )

        self.save_data()
        self.room_service.save_data()

        return booking

    # =========================
    # READ
    # =========================

    def get_all_bookings(self):
        return self.bookings

    # =========================
    # UPDATE BOOKING
    # =========================

    def update_booking(
        self,
        booking_id,
        new_customer_id=None,
        new_room_id=None,
        new_check_in=None,
        new_check_out=None
    ):

        booking = self.find_booking_by_id(
            booking_id
        )

        if booking is None:
            raise ValueError("Booking not found.")

        customer_id = (
            new_customer_id
            if new_customer_id is not None
            else booking.customer_id
        )

        room_id = (
            new_room_id
            if new_room_id is not None
            else booking.room_id
        )

        check_in = (
            new_check_in
            if new_check_in is not None
            else booking.check_in
        )

        check_out = (
            new_check_out
            if new_check_out is not None
            else booking.check_out
        )

        customer = self.customer_service.find_customer_by_id(
            customer_id
        )

        if customer is None:
            raise ValueError("Customer not found.")

        old_room = self.room_service.find_room_by_id(
            booking.room_id
        )

        new_room = self.room_service.find_room_by_id(
            room_id
        )

        if new_room is None:
            raise ValueError("Room not found.")

        if (
            room_id != booking.room_id
            and new_room.status != "Available"
        ):
            raise ValueError("New room is already booked.")

        days = self.calculate_days(
            check_in,
            check_out
        )

        total_price = new_room.calculate_price(
            days
        )

        if old_room and room_id != booking.room_id:
            old_room.status = "Available"
            new_room.status = "Booked"

        updated_booking = Booking(
            booking_id,
            customer_id,
            room_id,
            check_in,
            check_out,
            total_price
        )

        index = self.bookings.index(
            booking
        )

        self.bookings[index] = updated_booking

        self.save_data()
        self.room_service.save_data()

        return updated_booking

    # =========================
    # SEARCH
    # =========================

    def find_booking_by_id(
        self,
        booking_id
    ):

        for booking in self.bookings:

            if booking.booking_id == booking_id:
                return booking

        return None

    def find_bookings_by_customer_id(
        self,
        customer_id
    ):

        result = []

        for booking in self.bookings:

            if booking.customer_id == customer_id:
                result.append(
                    booking
                )

        return result

    def find_bookings_by_room_id(
        self,
        room_id
    ):

        result = []

        for booking in self.bookings:

            if booking.room_id == room_id:
                result.append(
                    booking
                )

        return result

    # =========================
    # SORT
    # =========================

    def sort_bookings_by_total_price(
        self,
        descending=True
    ):

        return sorted(
            self.bookings,
            key=lambda booking: booking.total_price,
            reverse=descending
        )

    def sort_bookings_by_check_in(
        self
    ):

        return sorted(
            self.bookings,
            key=lambda booking: booking.check_in
        )

    # =========================
    # DELETE / CANCEL
    # =========================

    def cancel_booking(
        self,
        booking_id
    ):

        booking = self.find_booking_by_id(
            booking_id
        )

        if booking is None:
            return False

        room = self.room_service.find_room_by_id(
            booking.room_id
        )

        if room:
            room.status = "Available"

        self.bookings.remove(
            booking
        )

        self.save_data()
        self.room_service.save_data()

        return True

    # =========================
    # BUSINESS LOGIC
    # =========================

    def calculate_days(
        self,
        check_in,
        check_out
    ):

        try:

            check_in_date = datetime.strptime(
                check_in,
                "%Y-%m-%d"
            )

            check_out_date = datetime.strptime(
                check_out,
                "%Y-%m-%d"
            )

        except ValueError:

            raise ValueError(
                "Date format must be YYYY-MM-DD."
            )

        days = (
            check_out_date -
            check_in_date
        ).days

        if days <= 0:
            raise ValueError(
                "Check-out must be after check-in."
            )

        return days

    def get_total_revenue(
        self
    ):

        total = 0

        for booking in self.bookings:
            total += booking.total_price

        return total

    def get_revenue_by_room_type(
        self
    ):

        revenue = {}

        for booking in self.bookings:

            room = self.room_service.find_room_by_id(
                booking.room_id
            )

            if room:
                room_type = room.get_room_type()
            else:
                room_type = "Unknown"

            if room_type not in revenue:
                revenue[room_type] = 0

            revenue[room_type] += booking.total_price

        return revenue

    def get_top_bookings_by_price(
        self,
        limit=3
    ):

        sorted_bookings = self.sort_bookings_by_total_price(
            descending=True
        )

        return sorted_bookings[:limit]

    # =========================
    # SAVE JSON
    # =========================

    def save_data(
        self
    ):

        data = []

        for booking in self.bookings:
            data.append(
                booking.to_dict()
            )

        with open(
            "data/bookings.json",
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

    def load_data(
        self
    ):

        try:

            with open(
                "data/bookings.json",
                "r",
                encoding="utf-8"
            ) as file:

                data = json.load(file)

                for item in data:

                    booking = Booking(
                        item["booking_id"],
                        item["customer_id"],
                        item["room_id"],
                        item["check_in"],
                        item["check_out"],
                        item["total_price"]
                    )

                    self.bookings.append(
                        booking
                    )

                    room = self.room_service.find_room_by_id(
                        booking.room_id
                    )

                    if room:
                        room.status = "Booked"

        except FileNotFoundError:

            self.bookings = []

        except json.JSONDecodeError:

            self.bookings = []