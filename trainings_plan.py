from machine import Machine
from plan import Plan
from preferences import Preferences
from helpers import splitString2List
from flet import (
    Column,
    Container,
    DataCell,
    DataColumn,
    DataTable,
    DataRow,
    Divider,
    FontWeight,
    Icon,
    MainAxisAlignment,
    Tab,
    TextStyle,
    Text,
    alignment,
    colors,
)

def exerciseDetails(station: dict) -> DataTable:
    return DataTable(
        data_text_style=TextStyle(
            weight=FontWeight.NORMAL,
            size=14,
            color=colors.BLACK
        ),
        heading_text_style=TextStyle(
            weight=FontWeight.BOLD,
            size=14,
            color=colors.BLACK
        ),
        columns=[
            DataColumn(
                label=Text("Übung"),
            ),
            DataColumn(
                label=Text("Wert"),
            )
        ],
        rows=[
            DataRow(
                cells=[
                    DataCell(
                        content=Text("Sätze")
                    ),
                    DataCell(
                        content=Text(station["sets"])
                    ),
                ]
            ),
            DataRow(
                cells=[
                    DataCell(
                        content=Text("Wiederholungen")
                    ),
                    DataCell(
                        content=Text(station["repeats"])
                    ),
                ]
            ),
            DataRow(
                cells=[
                    DataCell(
                        content=Text("Pause")
                    ),
                    DataCell(
                        content=Text(station["break"])
                    ),
                ]
            )
        ]
    )

def machineSettings(station: dict) -> DataTable:
    parameterRows = []
    machine = Machine(station["machine_id"])
    parameterValues = splitString2List(station["parameters"])
    index = 0

    for parameter in splitString2List(machine.machines["parameters"]):
        parameterRows.append(
            DataRow(
                cells=[
                    DataCell(
                        content=Text(parameter),
                    ),
                    DataCell(
                        content=Text(parameterValues[index]),
                    )
                ]
            )
        )
        index += 1

    return DataTable(
        data_text_style=TextStyle(
            weight=FontWeight.NORMAL,
            size=14,
            color=colors.BLACK
        ),
        heading_text_style=TextStyle(
            weight=FontWeight.BOLD,
            size=14,
            color=colors.BLACK
        ),
        columns=[
            DataColumn(
                label=Text("Parameter"),
            ),
            DataColumn(
                label=Text("Wert"),
            )
        ],
        rows=parameterRows,
        expand=1,
    )

def trainingPlan(validFrom: str) -> list:
    prefs = Preferences()
    plan = Plan(customerID=prefs.customerID, validFrom=validFrom)
    stationTabs = []

    for station in plan.plans:
        stationTabs.append(
                Tab(
                    tab_content=Text(
                        station["machine_id"],
                        style=TextStyle(
                            size=16,
                            weight=FontWeight.BOLD
                        )
                    ),
                    # icon=Icon(
                    #     "icons/gymMachine.png",
                    #     size=10,
                    #     semantics_label=f"Gym Machine: {station["machine_id"]}"
                    # ),
                    content=Column(
                        alignment=MainAxisAlignment.START,
                        controls=[
                            Text(station["comments"]),
                            Divider(
                                height=15,
                                color=colors.BLUE_500
                            ),
                            exerciseDetails(station=station),
                            machineSettings(station=station)
                        ],
                        expand=1
                    )
                ),
        )

    return stationTabs
