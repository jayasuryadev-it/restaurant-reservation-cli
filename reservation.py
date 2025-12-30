from db import get_connection

class Reservation:

    def check_availability(self, date, time, table_no):
        conn = get_connection()
        cur = conn.cursor()

        query = """
        SELECT * FROM reservation
        WHERE date=%s AND time=%s AND table_no=%s AND status='Booked'
        """
        cur.execute(query, (date, time, table_no))
        result = cur.fetchone()

        conn.close()
        return result is None

    def book_table(self, customer_id, table_no, date, time):
        if not self.check_availability(date, time, table_no):
            print("❌ Table already booked")
            return

        conn = get_connection()
        cur = conn.cursor()

        query = """
        INSERT INTO reservation (customer_id, table_no, date, time, status)
        VALUES (%s, %s, %s, %s, 'Booked')
        """
        cur.execute(query, (customer_id, table_no, date, time))

        conn.commit()
        conn.close()
        print("✅ Table booked successfully")
