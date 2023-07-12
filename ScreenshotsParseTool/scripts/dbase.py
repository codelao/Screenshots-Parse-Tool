import sqlite3


class Database:
    def __init__(self, db_file):
        self.con = sqlite3.connect(db_file, check_same_thread=False)
        self.con.cursor().execute("CREATE TABLE IF NOT EXISTS user_theme(theme TEXT)") and self.con.cursor().execute("CREATE TABLE IF NOT EXISTS user_terms(terms TEXT)") and self.con.cursor().execute("CREATE TABLE IF NOT EXISTS stats(screens INTEGER, last_parse TEXT)")

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

    def add_stats(self, screens, last_parse):
        with self.con:
            self.con.cursor().execute("INSERT INTO stats VALUES (?, ?)", (screens, last_parse))
    
    def update_stats(self, screens, last_parse):
        with self.con:
            self.con.cursor().execute("UPDATE stats SET screens = ?, last_parse = ?", (screens, last_parse))
        
    def get_screens_count(self):
        with self.con:
            return self.con.cursor().execute("SELECT screens FROM stats").fetchone()
        
    def get_last_parse_date(self):
        with self.con:
            return self.con.cursor().execute("SELECT last_parse FROM stats").fetchone()
