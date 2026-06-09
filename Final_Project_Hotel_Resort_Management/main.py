from services.room_service import RoomService
from services.customer_service import CustomerService
from services.booking_service import BookingService

from views.menu_view import MenuView


def main():

    room_service = RoomService()

    customer_service = CustomerService()

    booking_service = BookingService(
        room_service,
        customer_service
    )

    menu = MenuView(
        room_service,
        customer_service,
        booking_service
    )

    menu.run()


if __name__ == "__main__":
    main()