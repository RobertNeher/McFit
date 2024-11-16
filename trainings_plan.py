from plan import Plan
from preferences import Preferences

from flet import (
    Container,
    FontWeight,
    Page,
    Tab,
    Tabs,
    Text,
)
def trainingPlan(validFrom: str) -> list:
    prefs = Preferences()
    plan = Plan(customerID=prefs.customerID, validFrom=validFrom)
    stationTabs = []

    for station in plan.plans:
        stationTabs.append(
                Tab(
                    tab_content=Text(station["machine_id"],
                                        weight=FontWeight.BOLD
                                ),
                    content=Text(station["machine_comments"])
                    # content=getMachineDetail(station)
                )
        )

    return stationTabs
