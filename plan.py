import sys

from persistence import PLAN_TABLE
from persistence import DBConnection
from preferences import Preferences
from machine import Machine
class Plan:
    def __init__(self, customerID:str, validFrom:str = None, machineID:str = None):
        self.customerID = customerID
        self.machineID = machineID
        self.validFrom = validFrom
        self.connection = DBConnection(initialize=False)
        self.cursor = self.connection.cursor

        SQL = f"SELECT * FROM {PLAN_TABLE} WHERE customer_id = \"{self.customerID}\""

        if self.machineID != None:
            SQL += f" AND machine_id = \"{self.machineID}\""

        if self.validFrom == None:
            SQL += " ORDER BY valid_from DESC, machine_id ASC"
            print(SQL)
            self.cursor.execute(SQL)
        else:
            SQL += f" AND valid_from >= {validFrom} ORDER BY valid_from DESC"
            self.cursor.execute(SQL)

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

def main(argv):
    prefs = Preferences()
    p = Plan(customerID=prefs.customerID, validFrom="2024-11-15") #, machineID=sys.argv[1])
    m = Machine()
    a = []
    b = []
    for plan in p.plans:
        a.append(plan["machine_id"] + "p")
    for machine in m.machines:
        a.append(machine["name"] + "m")
    a.sort()
    print(a)
#-------------------------- TEST -------------------------#
if __name__ == "__main__":
    main(sys.argv)
