import csv


class ReportService:

    def __init__(
        self,
        room_service,
        booking_service
    ):
        self.room_service = room_service
        self.booking_service = booking_service

    def get_total_revenue(self):

        return self.booking_service.get_total_revenue()

    def get_available_rooms(self):

        return self.room_service.get_available_rooms()

    def get_booked_rooms(self):

        return self.room_service.get_booked_rooms()

    def export_bookings_csv(self):

        bookings = self.booking_service.get_all_bookings()

        with open(
            "booking_report.csv",
            "w",
            newline="",
            encoding="utf-8"
        ) as file:

            writer = csv.writer(file)

            writer.writerow([
                "Booking ID",
                "Customer ID",
                "Room ID",
                "Check In",
                "Check Out",
                "Total Price"
            ])

            for booking in bookings:

                writer.writerow([
                    booking.booking_id,
                    booking.customer_id,
                    booking.room_id,
                    booking.check_in,
                    booking.check_out,
                    booking.total_price
                ])

        return True