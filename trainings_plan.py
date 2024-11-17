from machine import Machine
from plan import Plan
from preferences import Preferences

from flet import (
    Column,
    DataCell,
    DataColumn,
    DataTable,
    DataRow,
    FontWeight,
    MainAxisAlignment,
    Tab,
    TextStyle,
    Text,
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
                label=Text("Einstellung"),
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

def machineDetails(station: dict) -> list:
    parameterRows = []
    machine = Machine(station["machine_id"])
    for parameter in machine.machines["parameters"]:
        parameterRows.append(
            DataRow(
                cells=[
                    DataCell(
                        content=Text(parameter),
                    )
                ]
            )
        )
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

def trainingPlan(validFrom: str) -> list:
    prefs = Preferences()
    plan = Plan(customerID=prefs.customerID, validFrom=validFrom)
    stationTabs = []

    for station in plan.plans:
        stationTabs.append(
                Tab(
                    tab_content=Text(station["machine_id"],
                                    style=TextStyle(
                                        size=16,
                                        weight=FontWeight.BOLD
                                    )
                                ),
                    content=Column(
                        alignment=MainAxisAlignment.CENTER,
                        controls=[
                            Text(station["comments"]),
                            exerciseDetails(station=station),
                            machineDetails(station=station)
                        ]
                    )
                )
        )

    return stationTabs
