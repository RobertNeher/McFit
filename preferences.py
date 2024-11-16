from persistence import (
    DATASETS_FOLDER,
    PREFERENCE_TABLE,
    DBConnection
)

class Preferences():
    def __init__(self):
        self.customerID = ""
        self.studio = ""
        self.autoforward = True

        SQL = f"SELECT * FROM {PREFERENCE_TABLE}"

        self.connection = DBConnection(initialize=False)
        self.cursor = self.connection.cursor
        self.cursor.execute(SQL)

        preferences = self.cursor.fetchone()

        if preferences:
            self.customerID = preferences[0]
            self.studio = preferences[1]
            self.autoforward = preferences[2] == "1"


#------------------------ MAIN ------------------------#
if __name__ == "__main__":
    prefs = Preferences()

    print(prefs.customerID)