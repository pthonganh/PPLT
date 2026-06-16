import csv


class ReportService:

    def __init__(
        self,
        room_service,
        booking_service
    ):
        self.room_service = room_service
        self.booking_service = booking_service

    # =========================
    # REVENUE
    # =========================

    def get_total_revenue(self):

        return self.booking_service.get_total_revenue()

    def get_revenue_by_room_type(self):

        return self.booking_service.get_revenue_by_room_type()

    # =========================
    # ROOM REPORTS
    # =========================

    def get_available_rooms(self):

        return self.room_service.get_available_rooms()

    def get_booked_rooms(self):

        return self.room_service.get_booked_rooms()

    def get_room_statistics(self):

        return self.room_service.count_rooms_by_type()

    def get_room_status_statistics(self):

        return self.room_service.count_rooms_by_status()

    # =========================
    # BOOKING REPORTS
    # =========================

    def get_top_bookings(self, limit=3):

        return self.booking_service.get_top_bookings_by_price(
            limit
        )

    # =========================
    # EXPORT CSV
    # =========================

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

    def export_revenue_report_csv(self):

        revenue_data = self.get_revenue_by_room_type()

        with open(
            "revenue_report.csv",
            "w",
            newline="",
            encoding="utf-8"
        ) as file:

            writer = csv.writer(file)

            writer.writerow([
                "Room Type",
                "Revenue"
            ])

            for room_type, revenue in revenue_data.items():

                writer.writerow([
                    room_type,
                    revenue
                ])

        return True