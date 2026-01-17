import sqlite3

class Database:
    def __init__(self, db_file):
        self.conn = sqlite3.connect(db_file)
        self.cur = self.conn.cursor()
        self.create_table()

    def create_table(self):
        with self.conn:
            self.cur.execute('''CREATE TABLE IF NOT EXISTS users (
                                id INTEGER PRIMARY KEY autoincrement,
                                user_id INTEGER NOT NULL UNIQUE,
                                referrer_id INTEGER)''')

    def user_exists(self, user_id):
        with self.conn:
            result = self.cur.execute("SELECT * FROM users WHERE user_id = ?", (user_id,)).fetchone()
            return bool(result)

    def add_user(self, user_id, referrer_id=None):
        try:
            with self.conn:
                if referrer_id is not None:
                    self.cur.execute("INSERT INTO users (user_id, referrer_id) VALUES (?, ?)", (user_id, referrer_id))
                else:
                    self.cur.execute("INSERT INTO users (user_id) VALUES (?)", (user_id,))
        except sqlite3.IntegrityError:
            pass
        except Exception as e:
            print(f"An error occurred: {e}")

    def count_referrals(self, user_id):
        referral_list = self.cur.execute("SELECT user_id FROM users WHERE referrer_id = ?", (user_id,))
        return "\n".join([str(referral[0]) for referral in referral_list.fetchall()])


    def close(self):
        self.conn.close()
