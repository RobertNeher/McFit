from  persistence import (
    ASSETS_FOLDER,
    IMAGE_FOLDER
)
# from preferences import Preferences
# from plan import Plan
from trainings_plan import trainingPlan

from flet import (
    Column,
    Container,
    Divider,
    FontWeight,
    Image,
    MainAxisAlignment,
    Page,
    Row,
    Tabs,
    Text,
    app,
    alignment,
    colors
)

APP_NAME = "McFit Trainingsbegleiter"

def main(page: Page):
    page.title = APP_NAME

    stationTabs = Tabs(
        selected_index=0,
        divider_color=colors.AMBER_400,
        animation_duration=300,
        tabs=trainingPlan(validFrom="2024-11-15"),
    )

    page.window.width=500
    page.add(
        Column(
            alignment=MainAxisAlignment.CENTER,
            controls=[
                Row(
                    alignment=MainAxisAlignment.CENTER,
                    controls=[
                        Image(
                            src=f"{IMAGE_FOLDER}\\McFit-weisserHG-hochkant.png",
                            height=75
                        ),
                        Container(
                            width=350,
                            height=75,
                            content=Text(
                                "Trainingsplan",
                                size=24,
                                color=colors.BLACK,
                                weight=FontWeight.BOLD
                            ),
                            alignment=alignment.center,
                        )
                    ]
                ),
                Divider(
                    height=5,
                    color=colors.AMBER_400
                ),
                stationTabs
            ],
            expand=1
        )
    )
    page.update()


app(main, assets_dir=ASSETS_FOLDER,name=APP_NAME)
