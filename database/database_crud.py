import sqlite3

def setup_connection(db_name):
    """Connects to the database and returns a connection"""
    try:
        return sqlite3.connect(db_name)
    except sqlite3.Error as e:
        print("error")
        return None


def close_connection(connection: sqlite3.Connection):
    """Closes the connection"""
    connection.close()


def setup_database(table_name, con: sqlite3.Connection):
    """Creates the jokes table if it doesn't exist."""
    try:
        c = con.cursor()
        c.execute("""CREATE TABLE IF NOT EXISTS jokes (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        setup TEXT,
                        punchline TEXT )""")
        con.commit()
        #print("jokes table created successfully")
    except sqlite3.Error as e:
        print("error")


def store_joke(joke, con: sqlite3.Connection):
    """Stores a joke in the database"""
    try:
        c = con.cursor()
        c.execute("INSERT INTO jokes (setup, punchline) VALUES (?, ?)", (joke["setup"], joke["punchline"]))
        con.commit()
        #print("joke stored successfully!")
    except sqlite3.Error as e:
        print("error")


def get_jokes(con: sqlite3.Connection):
    """gets a joke from the database"""
    try:
        c = con.cursor()
        c.execute("SELECT id, setup, punchline FROM jokes")
        jokes = c.fetchall()
        return jokes
    except sqlite3.Error as e:
        print("error")


def update_joke(joke_id, new_punchline, con: sqlite3.Connection):
    """updates a joke from the database"""
    try:
        c = con.cursor()
        c.execute("UPDATE jokes SET punchline = ? WHERE id = ?", (new_punchline, joke_id))
        con.commit()
        print(f"joke {joke_id} updated!")
    except sqlite3.Error as e:
        print("error")


def delete_joke(joke_id, con: sqlite3.Connection):
    """deletes a joke from the database"""
    try:
        c = con.cursor()
        c.execute("DELETE FROM jokes WHERE id=?", (joke_id,))
        con.commit()
        print(f"joke {joke_id} deleted!")
    except sqlite3.Error as e:
        print("error")
