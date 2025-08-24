from datetime import datetime

class Room:
    def __init__(self, name, price, total):
        self.name = name
        self.price = price
        self.total = total
        self.booked = 0

    def available(self):
        return self.total - self.booked

    def book(self, count):
        if count <= self.available():
            self.booked += count
            return True
        else:
            return False

def generate_booking_id():
    return "B" + datetime.now().strftime("%H%M%S")

# Hotel room setup
room_data = {
    1: Room("Standard", 1800, 5),
    2: Room("Deluxe", 2500, 8),
    3: Room("Suite", 3500, 12)
}

# Program Start
print("\nWelcome to THE GRAND ROYAL HOTEL")
answer = input("Would you like to check the room availability? (Yes/No): ").strip().lower()

if answer != "yes":
    print("Thank you for visiting us!")
    exit()

while True:
    print("\nOur hotel offers:")
    for i, room in room_data.items():
        print(f"{i}. {room.name}")

    try:
        choice = int(input("Which type of room do you want? (1-3): "))
        selected = room_data[choice]
    except (ValueError, KeyError):
        print("Invalid choice. Try again.")
        continue

    print(f"\nOur {selected.name} rooms are available for Rs.{selected.price} / night.")
    print(f"Total available rooms: {selected.available()}")

    confirm = input("Is this okay for you? (Yes / Reselect): ").strip().lower()
    if confirm == "yes":
        break

# Collect customer details
print("\nPlease enter your booking details:")
booking_id = generate_booking_id()
name = input("Customer Name: ")
mobile = input("Mobile Number: ")

try:
    num_rooms = int(input("Number of rooms: "))
    if num_rooms > selected.available():
        print("Not enough rooms available. Try again.")
        exit()
    checkin = input("Check-in date (YYYY-MM-DD): ")
    checkout = input("Check-out date (YYYY-MM-DD): ")

    # Convert to date and calculate days
    d1 = datetime.strptime(checkin, "%Y-%m-%d")
    d2 = datetime.strptime(checkout, "%Y-%m-%d")
    days = (d2 - d1).days
    total_price = days * selected.price * num_rooms
except:
    print("Invalid input. Booking failed.")
    exit()

# Final confirmation
selected.book(num_rooms)

print("\nBooking Confirmed!")
print(f"Booking ID     : {booking_id}")
print(f"Customer Name  : {name}")
print(f"Room Type      : {selected.name}")
print(f"Number of Rooms: {num_rooms}")
print(f"Check-in Date  : {checkin}")
print(f"Check-out Date : {checkout}")
print(f"Total Price    : ₹{total_price}")
print("\nThank you for choosing us!")
print("Hope you will enjoy your stay in our hotel!")
