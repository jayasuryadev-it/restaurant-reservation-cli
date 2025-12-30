from customer import Customer
from reservation import Reservation
from order import Order
from billing import Billing

customer = Customer()
reservation = Reservation()
order = Order()
billing = Billing()

while True:
    print("\n--- Restaurant Reservation System (CLI) ---")
    print("1. Add Customer")
    print("2. Book Table")
    print("3. Add Order")
    print("4. Generate Bill")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        name = input("Customer Name: ")
        phone = input("Phone: ")
        email = input("Email: ")
        customer.add_customer(name, phone, email)

    elif choice == "2":
        cid = int(input("Customer ID: "))
        table_no = int(input("Table No: "))
        date = input("Date (YYYY-MM-DD): ")
        time = input("Time (HH:MM:SS): ")
        reservation.book_table(cid, table_no, date, time)

    elif choice == "3":
        rid = int(input("Reservation ID: "))
        item = input("Item Name: ")
        qty = int(input("Quantity: "))
        price = float(input("Price: "))
        order.add_order(rid, item, qty, price)

    elif choice == "4":
        rid = int(input("Reservation ID: "))
        billing.generate_bill(rid)

    elif choice == "5":
        print("👋 Exiting application")
        break

    else:
        print("❌ Invalid choice")
