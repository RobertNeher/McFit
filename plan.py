from persistence import PLAN_TABLE
from persistence import DBConnection
from preferences import Preferences
from machine import Machine
from datetime import datetime

class Plan:
    def __init__(self, customerID:str, validFrom:str = None, machineID:str = None):
        self.customerID = customerID
        self.machineID = machineID
        self.validFrom = validFrom
        self.connection = DBConnection(initialize=False)
        self.cursor = self.connection.cursor

        SQL = f"SELECT * FROM {PLAN_TABLE} WHERE customer_id = ?"

        if validFrom == None:
            SQL += "ORDER BY valid_from DESC, machine_id ASC"

            self.cursor.execute(SQL, [self.customerID])
        else:
            SQL += "AND valid_from >= ? ORDER BY valid_from DESC"
            self.cursor.execute(SQL, [self.customerID, self.validFrom])

        self.plans = [dict((self.cursor.description[i][0], value) \
            for i, value in enumerate(row)) for row in self.cursor.fetchall()]

    def planHistory(self, mostActual: bool = False) -> list:
        SQL = f"SELECT DISTINCT valid_from FROM {PLAN_TABLE} WHERE customer_id = ? ORDER BY valid_from DESC"
        self.cursor.execute(SQL, [self.customerID])

        if mostActual:
            dates = self.cursor.fetchone()
        else:
            dates = self.cursor.fetchall()

        return dates

#-------------------------- TEST -------------------------#
if __name__ == "__main__":
    prefs = Preferences()
    # today = datetime.today().strftime("%Y-%m-%d")
    p = Plan(customerID=prefs.customerID, validFrom="2024-10-27")
    print(p.plans)
