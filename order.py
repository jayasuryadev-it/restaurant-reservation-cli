from db import get_connection

class Order:
    def add_order(self, reservation_id, item, quantity, price):
        conn = get_connection()
        cur = conn.cursor()

        query = """
        INSERT INTO orders (reservation_id, item_name, quantity, price)
        VALUES (%s, %s, %s, %s)
        """
        cur.execute(query, (reservation_id, item, quantity, price))

        conn.commit()
        conn.close()
        print("✅ Order added successfully")
