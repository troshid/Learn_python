import sqlite3


def create_and_insert_data():
    try:
        # Connect to SQLite database (or create it)
        conn = sqlite3.connect('example.db')
        cursor = conn.cursor()

        # Create table
        cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            name TEXT NOT NULL,
                            age INTEGER NOT NULL)''')

        # Insert data
        cursor.execute("INSERT INTO users (name, age) VALUES ('Alice', 30)")
        cursor.execute("INSERT INTO users (name, age) VALUES ('Bob', 25)")
        conn.commit()

        # Query data
        cursor.execute("SELECT * FROM users")
        rows = cursor.fetchall()
        for row in rows:
            print(row)

        # Close connection
        conn.close()
    except sqlite3.Error as e:
        print(f"Database error: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")


# Example usage
create_and_insert_data()
