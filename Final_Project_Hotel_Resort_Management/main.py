from services.room_service import RoomService
from services.customer_service import CustomerService
from services.booking_service import BookingService
from services.report_service import ReportService

from views.menu_view import MenuView


def main():

    room_service = RoomService()

    customer_service = CustomerService()

    booking_service = BookingService(
        room_service,
        customer_service
    )

    report_service = ReportService(
        room_service,
        booking_service
    )

    menu = MenuView(
        room_service,
        customer_service,
        booking_service
    )

    menu.report_service = report_service

    menu.run()


if __name__ == "__main__":
    main()