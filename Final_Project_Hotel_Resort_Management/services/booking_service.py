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

        check_in_date = datetime.strptime(
            check_in,
            "%Y-%m-%d"
        )

        check_out_date = datetime.strptime(
            check_out,
            "%Y-%m-%d"
        )

        days = (
            check_out_date -
            check_in_date
        ).days

        if days <= 0:
            raise ValueError(
                "Check-out must be after check-in."
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

        return booking

    # =========================
    # READ
    # =========================

    def get_all_bookings(self):
        return self.bookings

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

        return True

    # =========================
    # REVENUE
    # =========================

    def get_total_revenue(self):

        total = 0

        for booking in self.bookings:
            total += booking.total_price

        return total

    # =========================
    # SAVE JSON
    # =========================

    def save_data(self):

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

    def load_data(self):

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

        except FileNotFoundError:

            self.bookings = []

        except json.JSONDecodeError:

            self.bookings = []