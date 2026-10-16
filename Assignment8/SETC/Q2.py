# Q2. Create a Flask application to store vehicle details, update vehicle price and delete a 
# vehicle using Vehicle ID.

from flask import Flask
import psycopg2

app = Flask(__name__)

# Database connection
def db_connect():
    return psycopg2.connect(
        dbname="vehicle",
        user="postgres",
        password="root",
        host="localhost",
        port="5432"
    )


# Store vehicle details
@app.route('/insert')
def insert_vehicles():
    try:
        conn = db_connect()
        cur = conn.cursor()

        # Create Vehicle table
        cur.execute("""
            CREATE TABLE IF NOT EXISTS Vehicle (
                vehicle_id SERIAL PRIMARY KEY,
                name VARCHAR(100),
                model VARCHAR(100),
                price FLOAT
            );
        """)

        # Insert sample records only if table is empty
        cur.execute("SELECT COUNT(*) FROM Vehicle")
        count = cur.fetchone()[0]

        if count == 0:
            vehicles = [
                ("Tata", "Nexon", 900000),
                ("Hyundai", "Creta", 1200000),
                ("Maruti", "Swift", 700000),
                ("Honda", "City", 1100000),
                ("Mahindra", "Thar", 1500000)
            ]

            cur.executemany("""
                INSERT INTO Vehicle (name, model, price)
                VALUES (%s, %s, %s)
            """, vehicles)

            conn.commit()
            message = "5 Vehicle Records Inserted Successfully!"
        else:
            message = "Vehicle records already exist."

        cur.close()
        conn.close()

        return message

    except Exception as e:
        return f"Error: {e}"


# Update vehicle price using Vehicle ID
@app.route('/update/<int:vid>')
def update_price(vid):
    try:
        conn = db_connect()
        cur = conn.cursor()

        new_price = 1000000

        cur.execute("""
            UPDATE Vehicle
            SET price = %s
            WHERE vehicle_id = %s
            RETURNING vehicle_id, name, model, price
        """, (new_price, vid))

        vehicle = cur.fetchone()
        conn.commit()

        cur.close()
        conn.close()

        if vehicle:
            return (
                f"Vehicle Price Updated Successfully!<br>"
                f"Vehicle ID: {vehicle[0]}<br>"
                f"Name: {vehicle[1]}<br>"
                f"Model: {vehicle[2]}<br>"
                f"New Price: ₹{vehicle[3]:.2f}"
            )
        else:
            return "Vehicle Not Found!"

    except Exception as e:
        return f"Error: {e}"


# Delete vehicle using Vehicle ID
@app.route('/delete/<int:vid>')
def delete_vehicle(vid):
    try:
        conn = db_connect()
        cur = conn.cursor()

        cur.execute("""
            DELETE FROM Vehicle
            WHERE vehicle_id = %s
            RETURNING vehicle_id, name, model
        """, (vid,))

        vehicle = cur.fetchone()
        conn.commit()

        cur.close()
        conn.close()

        if vehicle:
            return (
                f"Vehicle Deleted Successfully!<br>"
                f"Vehicle ID: {vehicle[0]}<br>"
                f"Name: {vehicle[1]}<br>"
                f"Model: {vehicle[2]}"
            )
        else:
            return "Vehicle Not Found!"

    except Exception as e:
        return f"Error: {e}"


# Display all vehicle records
@app.route('/display')
def display_vehicles():
    try:
        conn = db_connect()
        cur = conn.cursor()

        cur.execute("""
            SELECT vehicle_id, name, model, price
            FROM Vehicle
            ORDER BY vehicle_id
        """)

        vehicles = cur.fetchall()

        cur.close()
        conn.close()

        if not vehicles:
            return "No Vehicle Records Found!"

        output = "<h2>Vehicle Details</h2>"

        for vehicle in vehicles:
            output += f"""
                Vehicle ID: {vehicle[0]}<br>
                Name: {vehicle[1]}<br>
                Model: {vehicle[2]}<br>
                Price: ₹{vehicle[3]:.2f}<br>
                <hr>
            """

        return output

    except Exception as e:
        return f"Error: {e}"


if __name__ == '__main__':
    app.run(debug=True, use_reloader=False)
