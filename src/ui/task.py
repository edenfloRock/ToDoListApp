# /ui/task.py
from flet import *


class CreateTask(UserControl):
    def __init__(self, task:str, date:str, func1, func2):
        # create two arguments, so we can pass in the delete function and edit function when we create an instance of this
        self.task = task
        self.date = date
        self.func1 = func1
        self.func2 = func2
        super().__init__()

    def TaskDeleteEdit(self, name, color, func):
        return IconButton(
            icon=name,
            width=30,
            icon_size=18,
            icon_color=color,
            opacity=0,
            animate_opacity=200,
            # to use it, we need to keep it in our delete and edit iconbuttons
            on_click=lambda e: func(self.GetContainerInstance()),
        )

    # we need a final thing from here, and that is the instance itself.
    # we need the instande identifier so that we can delete it needs to be delete
    def GetContainerInstance(self):
        return self # we return the self instance

    def ShowIcons(self, e):
        if e.data == "true":
            # these are the index's of each icon
            (
                e.control.content.controls[1].controls[0].opacity,
                e.control.content.controls[1].controls[1].opacity,
            ) = (1,1)        
        else:
            (
                e.control.content.controls[1].controls[0].opacity,
                e.control.content.controls[1].controls[1].opacity,
            ) = (0,0)
        e.control.content.update()

    def build(self):
        return Container(
            width=280,
            height=60,
            border=border.all(0.85, "white54"),
            border_radius=8,
            on_hover=lambda e: self.ShowIcons(e), # Change later
            clip_behavior=ClipBehavior.HARD_EDGE,
            padding=10,
            content=Row(
                alignment=MainAxisAlignment.SPACE_BETWEEN,
                controls=[
                    Column(
                        spacing=1,
                        alignment=MainAxisAlignment.CENTER,
                        controls=[
                            Text(value=self.task, size=10),
                            Text(value=self.date, size=9, color='white54'),
                        ],
                    ),
                    # Icons Delete and Edit
                    Row(
                        spacing=0,
                        alignment=MainAxisAlignment.CENTER,
                        controls=[
                            self.TaskDeleteEdit(icons.DELETE_ROUNDED, 'red500', self.func1),
                            self.TaskDeleteEdit(icons.EDIT_ROUNDED, 'white70', self.func2),
                        ]
                    )
                ],
            ),
        )
