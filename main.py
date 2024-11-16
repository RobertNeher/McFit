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
    alignment,
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
                content=Row(
                    alignment=MainAxisAlignment.SPACE_BETWEEN,
                    controls=[
                        Image(
                            src=f"{IMAGE_FOLDER}\\McFit-weisserHG-hochkant.png",
                            height=50
                        ),
                        Container(
                            height=75,
                            content=Text(
                                "Mein Trainingsplan",
                                size=24,
                                color=colors.BLACK,
                                weight=FontWeight.BOLD
                            ),
                            alignment=alignment.center,
                            expand=1
                        ),
                    ]
                )
            ),
            Divider(
                height=5,
                color=colors.AMBER_400
            ),
            stationTabs
        ],
        expand=1
    ))
    page.update()


app(main, assets_dir=ASSETS_FOLDER,name=APP_NAME)
