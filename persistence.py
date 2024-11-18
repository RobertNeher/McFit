import os
import json
import sqlite3 as sl

from helpers import (
    getMachineParameterValues
)

ASSETS_FOLDER = ".\\assets"
DATASETS_FOLDER = ASSETS_FOLDER + "\\datasets"
DB_FILE = ASSETS_FOLDER + "\\McFit.db"
IMAGE_FOLDER = ASSETS_FOLDER + "\\images"
# Table names in local SQLite DB and expected bootstrapping content
PREFERENCE_TABLE = "preferences"
SETTING_TABLE = "settings"
CUSTOMER_TABLE = "customers"
MACHINE_TABLE = "machines"
PLAN_TABLE = "plans"

class DBConnection:
    def __init__(self, initialize: bool):
        self.connection = sl.connect(DB_FILE, check_same_thread=False)
        self.cursor = self.connection.cursor()

        with self.connection as connection:
            if initialize:
                connection.execute(f"""DROP TABLE IF EXISTS {PREFERENCE_TABLE}
                                        """)
                connection.execute(f"""DROP TABLE IF EXISTS {MACHINE_TABLE}
                                        """)
                connection.execute(f"""DROP TABLE IF EXISTS {PLAN_TABLE}
                                        """)
                connection.execute(f"""CREATE TABLE {PREFERENCE_TABLE} (
                                        customer_id REFERENCES {CUSTOMER_TABLE} (customer_id),
                                        studio TEXT NOT NULL,
                                        auto_forward INTEGER NOT NULL);
                                    """)

                connection.execute(f"""CREATE TABLE {MACHINE_TABLE}
                                        (name PRIMARY KEY,
                                        title TEXT NOT NULL,
                                        parameters TEXT,
                                        description TEXT,
                                        image BLOB);
                                    """)
                connection.execute(f"""CREATE UNIQUE INDEX MACHINE1 ON {MACHINE_TABLE}
                                        (name);""")

                connection.execute(f"""CREATE TABLE {PLAN_TABLE}
                                        (customer_id REFERENCES {CUSTOMER_TABLE}(customer_id),
                                        valid_from TEXT NOT NULL,
                                        machine_id REFERENCES {MACHINE_TABLE}(name),
                                        sets INTEGER,
                                        repeats INTEGER,
                                        break INTEGER,
                                        parameters TEXT,
                                        comments TEXT);
                                    """)
                connection.execute(f"""CREATE UNIQUE INDEX PLAN1 ON {PLAN_TABLE}
                                        (customer_id, valid_from DESC, machine_id ASC);""")

                connection.commit()

                self.initialize_preferences()
                self.initialize_machines()
                self.initialize_plans()

    def initialize_preferences(self) -> None:
        settings_init_file = os.path.join(DATASETS_FOLDER, PREFERENCE_TABLE + ".json")
        SQL = f"""INSERT INTO {PREFERENCE_TABLE} (
                        customer_id,
                        studio,
                        auto_forward
                )
                VALUES (?, ?, ?)"""

        if os.path.isfile(settings_init_file):
            with open(settings_init_file, "r", encoding="UTF-8") as json_file:
                preferences = json.load(json_file)["Preferences"][0]
                self.cursor.execute(SQL, list(preferences.values()))
                self.connection.commit()

            self.preferences = {
                "customer_id": preferences['customer_id'],
                "studio": preferences['studio'],
                "auto_forward": preferences['auto_forward']
            }

    def initialize_machines(self) -> None:
        logo_file = open(f"{IMAGE_FOLDER}\\McFit-weisserHG-hochkant.png", "rb")

        machine_init_file = os.path.join(DATASETS_FOLDER, MACHINE_TABLE + ".json")

        SQL = f"""INSERT INTO {MACHINE_TABLE} (
                        name,
                        title,
                        parameters,
                        description,
                        image
                    )
                    VALUES (
                        ?, ?, ?, ?, ?
                    )"""
        if os.path.isfile(machine_init_file):
            with open(machine_init_file, "r", encoding="UTF-8") as json_file:
                machines = json.load(json_file)

            for machine in machines["Machines"]:
                try:
                    with open(f"{IMAGE_FOLDER}\\{machine['name'].strip(' ')}.jpg", "rb") as image_file:
                        blob_data = image_file.read()
                except OSError:
                    blob_data = logo_file.read()
                data_tuple = (
                    machine['name'],
                    machine['title'],
                    str(machine['parameters']),
                    machine['description'],
                    blob_data
                )

                self.cursor.execute(SQL, data_tuple)

            self.connection.commit()

    def initialize_plans(self) -> None:
        plan_init_file = os.path.join(DATASETS_FOLDER, PLAN_TABLE + ".json")
        if os.path.isfile(plan_init_file):
            with open(plan_init_file, "r", encoding="UTF-8") as json_file:
                plans = json.load(json_file)

            for plan in plans["Plans"]:
                for machine in plan["machines"]:
                    # self.connection.execute(f"""INSERT INTO {PLAN_TABLE} (
                    SQL = f"""INSERT INTO {PLAN_TABLE} (
                                                customer_id,
                                                valid_from,
                                                machine_id,
                                                sets,
                                                repeats,
                                                break,
                                                parameters,
                                                comments
                                            )
                                            VALUES (?, ?, ?, ?, ?, ?, ?, ?)"""
                    self.cursor.execute(SQL, [plan['customer_id'],
                                              plan['valid_from'],
                                              machine['machine_id'],
                                              machine['sets'],
                                              machine['repeats'],
                                              machine['break'],
                                              str(getMachineParameterValues(plan['machines'], machine['machine_id'])),
                                              machine['comments']
                    ])
                    self.connection.commit()

    def __del__(self):
        self.connection.close()


#------------------------ MAIN ------------------------#
if __name__ == "__main__":
    db = DBConnection(initialize=True)
    db.connection.commit()
