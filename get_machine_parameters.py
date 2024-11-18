import sys
import sqlite3 as sl3

ASSETS_FOLDER = ".\\assets"
DB_FILE = ASSETS_FOLDER + "\\McFit.db"

def getMachineParameters(machineID: str) -> str:
    SQL = "SELECT parameters FROM machines WHERE name = ?"

    connection = sl3.connect(DB_FILE, check_same_thread=False)
    cursor = connection.cursor()
    cursor.execute(SQL, [machineID])
    machine = cursor.fetchone()

    if machine:
        parameterList = []
        for piece in machine[0].split(','):
            parameterList.append(piece.strip("[ ']"))
    else:
        parameterList = None

    return parameterList


def getMachineParameterValues(machines: dict, machineID: str) -> str:
    for machine in machines:
        if machine["machine_id"] == machineID:
            return machine["parameter_values"]

    return None

if __name__ == '__main__':
    print(getMachineParameters(machineID=sys.argv[1]))
