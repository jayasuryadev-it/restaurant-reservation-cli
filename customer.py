from db import get_connection

class Customer:
    def add_customer(self, name, phone, email):
        conn = get_connection()
        cur = conn.cursor()

        query = """
        INSERT INTO customer (name, phone, email)
        VALUES (%s, %s, %s)
        """
        cur.execute(query, (name, phone, email))

        conn.commit()
        conn.close()
        print("✅ Customer added successfully")
