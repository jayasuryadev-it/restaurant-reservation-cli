from db import get_connection
from decimal import Decimal

class Billing:
    def generate_bill(self, reservation_id):
        conn = get_connection()
        cur = conn.cursor()

        query = """
        SELECT item_name, quantity, price
        FROM orders
        WHERE reservation_id=%s
        """
        cur.execute(query, (reservation_id,))
        items = cur.fetchall()

        conn.close()

        if not items:
            print("❌ No orders found")
            return

        total = Decimal("0.00")

        print("\n🧾 BILL")
        print("----------------------")

        for item, qty, price in items:
            cost = price * qty   # Decimal × int ✅
            total += cost
            print(f"{item} x {qty} = ₹{cost}")

        gst = total * Decimal("0.05")
        grand_total = total + gst

        print("----------------------")
        print(f"Subtotal : ₹{total}")
        print(f"GST (5%) : ₹{gst}")
        print(f"Total    : ₹{grand_total}")
