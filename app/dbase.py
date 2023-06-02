import sqlite3


class Database:
    def __init__(self, db_file):
        self.con = sqlite3.connect(db_file, check_same_thread=False)
        self.con.cursor().execute("CREATE TABLE IF NOT EXISTS user_theme(theme TEXT)") and self.con.cursor().execute("CREATE TABLE IF NOT EXISTS user_terms(terms TEXT)")

    def check_theme(self):
        with self.con:
            return self.con.cursor().execute("SELECT theme FROM user_theme").fetchone()

    def add_theme(self, theme):
        with self.con:
            self.con.cursor().execute("INSERT INTO user_theme VALUES (?)", (theme,))

    def update_theme(self, theme):
        with self.con:
            self.con.cursor().execute("UPDATE user_theme SET theme = ?", (theme,))

    def check_terms(self):
        with self.con:
            return self.con.cursor().execute("SELECT terms FROM user_terms").fetchone()

    def add_terms(self, terms):
        with self.con:
            self.con.cursor().execute("INSERT INTO user_terms VALUES (?)", (terms,))