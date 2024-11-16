from  persistence import ASSETS_FOLDER
# from preferences import Preferences
# from plan import Plan
from trainings_plan import trainingPlan

from flet import (
    Column,
    Container,
    FontWeight,
    Icon,
    MainAxisAlignment,
    Page,
    Tabs,
    Text,
    app,
    colors
)

APP_NAME = "McFit Trainingsbegleiter"

def main(page: Page):
    page.title = APP_NAME

    stationTabs = Tabs(
        selected_index=0,
        animation_duration=300,
        tabs=trainingPlan(validFrom="2024-10-27"),
    )

    page.window.width=500
    page.add(Column(
        alignment=MainAxisAlignment.CENTER,
        controls=[
            Container(
                content=Text(
                    "Dein Trainingsplan",
                    size=24,
                    color=colors.BLACK,
                    weight=FontWeight.BOLD
                ),
            ),
            stationTabs
        ],
        expand=1
    ))
    page.update()


app(main, assets_dir=ASSETS_FOLDER,name=APP_NAME)
