from services.room_service import RoomService
from services.customer_service import CustomerService
from services.booking_service import BookingService
from services.report_service import ReportService

from views.menu_view import MenuView
from views.gui_view import GUIView


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

    print("========== RUN MODE ==========")
    print("1. CLI")
    print("2. GUI")

    choice = input("Choose mode: ")

    if choice == "2":

        gui = GUIView(
            room_service,
            customer_service,
            booking_service,
            report_service
        )

        gui.run()

    else:

        menu = MenuView(
            room_service,
            customer_service,
            booking_service,
            report_service
        )

        menu.run()


if __name__ == "__main__":
    main()