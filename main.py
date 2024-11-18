from training import Training
from  persistence import (
    ASSETS_FOLDER,
    IMAGE_FOLDER
)
from trainings_plan import trainingPlan
from datetime import datetime

from flet import (
    AlertDialog,
    BottomAppBar,
    Column,
    Container,
    Divider,
    FloatingActionButton,
    FloatingActionButtonLocation,
    FontWeight,
    Image,
    MainAxisAlignment,
    NotchShape,
    Page,
    Row,
    Tabs,
    Text,
    TextButton,
    app,
    alignment,
    colors,
    icons
)

APP_NAME = "McFit Trainingsbegleiter"


def main(page: Page):
    today = datetime.now()

    def resetIcon(e):
        if stationTabs.selected_index <= len(stationTabs.tabs) - 1:
            page.floating_action_button.icon = icons.ARROW_FORWARD
            page.update()

    def nextTab(e):
        stationTabs.selected_index += 1
        page.update()

        if stationTabs.selected_index == len(stationTabs.tabs) - 2:
            page.floating_action_button.icon = icons.SAVE
            page.update()
        elif stationTabs.selected_index == len(stationTabs.tabs) - 1:
            page.open(confirmSave)

    def handleClose(e):
        if (e.control.text == "Ja"):
            training = Training()
            training.storeTraining()
            page.close(confirmSave)


    confirmSave = AlertDialog(
        modal=True,
        title=Text("Bitte bestätigen"),
        content=Text(f"Soll das heutige Datum {today.strftime('%d.%m.%Y (%H:%M)')} als Trainingsdatum gespeichert werden?"),
        actions=[
            TextButton("Ja", on_click=handleClose),
            TextButton("Nein", on_click=handleClose),
        ],
        actions_alignment=MainAxisAlignment.END,
    )

    page.title = APP_NAME

    stationTabs = Tabs(
        selected_index=0,
        on_click=resetIcon,
        divider_color=colors.AMBER_400,
        animation_duration=300,
        tabs=trainingPlan(validFrom="2024-11-15"),
        expand=1
    )

    page.window.width=400
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
                            width=300,
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

    page.horizontal_alignment = page.vertical_alignment = "center"

    page.floating_action_button = FloatingActionButton(
        autofocus=True,
        bgcolor=colors.AMBER_400,
        icon=icons.ARROW_FORWARD,
        on_click=nextTab)
    page.floating_action_button_location = FloatingActionButtonLocation.END_CONTAINED
    page.bottom_appbar = BottomAppBar(
        bgcolor=colors.GREY_300,
        shape=NotchShape.CIRCULAR,
    )
    page.update()


app(main, assets_dir=ASSETS_FOLDER,name=APP_NAME)
