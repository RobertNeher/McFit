from plan import Plan
from preferences import Preferences

from flet import (
    Column,
    DataCell,
    DataColumn,
    DataRow,
    DataTable,
    Divider,
    FontWeight,
    MainAxisAlignment,
    Tab,
    Text,
    TextStyle,
    colors
)
def trainingPlan(validFrom: str) -> list:
    prefs = Preferences()
    plan = Plan(customerID=prefs.customerID, validFrom=validFrom)
    stationTabs = []

    for station in plan.plans:
        stationTabs.append(
                Tab(
                    tab_content=Text(station["machine_id"],
                                        weight=FontWeight.BOLD,
                                        bgcolor=colors.AMBER_400,
                                        color=colors.BLACK,
                                ),
                    content=Column(
                        alignment=MainAxisAlignment.START,
                        controls=[
                            Text(station["comments"]),
                            Divider(color=colors.AMBER_400),
                            DataTable(
                                heading_text_style=TextStyle(
                                    weight=FontWeight.BOLD,
                                    color=colors.BLACK,
                                    size=16
                                ),
                                columns=[
                                    DataColumn(label=Text("Einstellung")),
                                    DataColumn(label=Text("Wert"))
                                ],
                                rows=[
                                    DataRow(
                                        cells=[
                                            DataCell(content=Text("Sätze"),
                                            ),
                                            DataCell(content=Text(station["sets"])
                                            )
                                        ]
                                    ),
                                    DataRow(
                                        cells=[
                                            DataCell(content=Text("Wiederholungen"),
                                            ),
                                            DataCell(content=Text(station["repeats"])
                                            )
                                        ]
                                    ),
                                    DataRow(
                                        cells=[
                                            DataCell(content=Text("Pause"),
                                            ),
                                            DataCell(content=Text(station["break"])
                                            )
                                        ]
                                    )
                                ]
                            )
                        ]
                    )
            )
        )

    return stationTabs
