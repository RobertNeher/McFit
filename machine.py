from persistence import MACHINE_TABLE
from persistence import DBConnection

class Machine:
    def __init__(self, machineID = None):
        self.machineID = machineID
        self.description = ""
        self.connection = DBConnection(initialize=False)
        self.cursor = self.connection.cursor

        if machineID != None:
            SQL = f"SELECT * FROM {MACHINE_TABLE} WHERE name = ?"""
            self.cursor.execute(SQL, [machineID])
            row = self.cursor.fetchone()

            self.machines = {}
            for index, col in enumerate(self.cursor.description):
                self.machines[col[0]] = list(row)[index]

        else:
            SQL = f"""SELECT * FROM {MACHINE_TABLE}"""
            self.cursor.execute(SQL)
            self.machines = [dict((self.cursor.description[i][0], value) \
               for i, value in enumerate(row)) for row in self.cursor.fetchall()]

#-------------------------- TEST -------------------------#
if __name__ == "__main__":
    m = Machine("X02")
    print(m.machines["parameters"])
