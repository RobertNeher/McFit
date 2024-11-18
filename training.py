from datetime import datetime
from persistence import (
    TRAINING_TABLE,
    DBConnection
)
from preferences import Preferences

class Training:
    def __init__(self, trainingDate:str = None, studio:str = None):
        self.connection = DBConnection(initialize=False).connection()
        self.cursor = self.connection.cursor()

        self.preferences = Preferences()

        if studio == None:
            self.studio = self.preferences.studio

        if trainingDate != None:
            self.trainingDate = trainingDate
        else:
            self.trainingDate = datetime.now().strftime("%Y-%m-%d")

    def storeTraining(self):
        SQL = f"""INSERT INTO {TRAINING_TABLE}
                (date, studio)
                VALUES(?, ?)"""
        self.cursor.execute(SQL, self.trainingDate, self.studio)
        self.connection.connection.commit()
