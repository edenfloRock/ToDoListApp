#Modules
import flet
from flet import *
from datetime import datetime
import sqlite3 

# Let's create the form class first so we can get some data
class FormContainer(UserControl):
    def __init__(self):
        super().__init__()

    def build(self):
        return Container(
            width=280,
            height=80,
            bgcolor="bluegrey500",
            opacity=1,
            border_radius=40,
            margin=margin.only(left=-20, right=-20),
            animate=animation.Animation(400,"decelerate"),
            animate_opacity=200,
            padding=padding.only(top=45,bottom=45),
        )
            
def main(page: Page):
    page.horizontal_alignment = "center"
    page.vertical_alignment = "center"

    # function to show/hide form container
    def CreateToDoTask(e):
        
        # when we click the ADD iconbutton...
        if form.height != 200:
            form.height = 200            
        else:
            form.height = 80
        form.update()
        
        



    _main_column_ = Column(
        scroll="hidden",
        expand=True,
        alignment=MainAxisAlignment.START,
        controls=[
            Row(
                alignment=MainAxisAlignment.SPACE_BETWEEN,
                controls=[
                    #Some title stuff
                    Text("To-Do Items", size=18, weight="bold"),
                    IconButton(
                        icons.ADD_CIRCLE_ROUNDED,
                        icon_size=18,
                        on_click=lambda e: CreateToDoTask(e)
                    ),
                ],
            ),
            Divider(height=8, color="white24"),
        ],
    )

    #Set up somb bg and main container
    # The general UI will copy that of a mobile app

    page.add(
        # This is just a bg container
        Container(
            width=1500,
            height=800,
            margin=-10,
            bgcolor="bluegrey900",
            alignment=alignment.center,
            content=Row(
                alignment=MainAxisAlignment.CENTER,
                vertical_alignment=CrossAxisAlignment.CENTER,
                controls=[
                    #Main container
                    Container(
                        width=280,
                        height=600,
                        bgcolor="#0f0f0f",
                        border_radius=40,
                        border=border.all(0.5, "white"),
                        padding=padding.only(top=35, left=20, right=20),
                        clip_behavior=ClipBehavior.HARD_EDGE, # Clip contents to container
                        content=Column(
                            alignment=MainAxisAlignment.CENTER,
                            expand=True,
                            controls=[
                                #main column here
                                _main_column_,

                                # form class here
                                FormContainer()
                            ]
                        )
                    )
                ]
            )

        )
    )
    page.update()
    
    # The form container index is as follows. 
    # We can set the long element index as a variable so it can be called faster and easier.
    form = page.controls[0].content.controls[0].content.controls[1].controls[0]
    # now we can call form whenever we want to do something with it...


if __name__ == '__main__':
    flet.app(target=main)   
