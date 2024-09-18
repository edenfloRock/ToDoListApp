# app.py
import flet
from flet import *

from datetime import datetime
from database.Database import Database
from ui.form import FormContainer
from ui.task import CreateTask

def main(page: Page):
    page.horizontal_alignment = "center"
    page.vertical_alignment = "center"

    def AddTaskToScreen(e):
        # now, everytime the users adds a task, we need to fecth the data and output it to the main column...
        # there are 2 data we need: the task and the date
        dateTime = datetime.now().strftime("%b %d, %Y %I:%M")

        # we can use the db here for the starters...
        # first, open a conneccion to the database
        db_instance = Database()
        db = db_instance.ConnectToDatabase() # this returns the db
        db_instance.InsertDatabase((form.content.controls[0].value, dateTime))
        # we have both values, one the date and time and the other user task
        #finally close the connect
        db.close()

        # we could also place the db functions within the if statement



        # now recall that we set the form container to form variable.
        # We can use now to see if there's any content in the textfield
        if form.content.controls[0].value: # this checks the textfield's value
            _main_column_.controls.append(
                #here, we can create an instance od CreateTask() class...
                CreateTask(
                    #Now, it takes two arguments
                    form.content.controls[0].value, # task description...
                    dateTime,
                    # now, the instance takes  two more arguments when called...
                    DeleteFunction,
                    UpdateFunciton,
                )
            )
            _main_column_.update()

            # we can recall the show.hide function for the form here
            CreateToDoTask(e)
        else:
            db.close() # make sure it closes even if there is no user input
            pass


    def DeleteFunction(e):
        # when we want to delete, recall that these instances are in a list => so that means we can simply remove them when we want to
        print(e)
        _main_column_.controls.remove(e) # e is the instance itself
        _main_column_.update()        

    def UpdateFunciton(e):
        print(e)
        # The update needs a little bit more work...
        # we want ti update from the form, so we need to pass whatever the user had from the instance back to the form, 
        # then change the functions and pass it back again...
        form.height, form.opacity = 200, 1
        (
            form.content.controls[0].value,
            # here we are chaning the button function and name...
            # we need to change it from add task to update and so on...
            form.content.controls[1].content.value,
            form.content.controls[1].on_click,
        ) = (
            e.controls[0]
            .content.controls[0]
            .controls[0]
            .value, # this is the instance value of the task
            "Update",
            lambda _: FinalizeUpdate(e),
        )
        form.update()

        # once the user edits, we need to send the correct data back

    def FinalizeUpdate(e):
        # we can simply reverse the values from above
        e.controls[0].content.controls[0].controls[0].value = form.content.controls[0].value
        e.controls[0].content.update()
        # so we can hide the container
        CreateToDoTask(e)

    # function to show/hide form container
    def CreateToDoTask(e):
        
        # when we click the ADD iconbutton...
        if form.height != 200:
            form.height, form.opacity = 200, 1
        else:
            form.height, form.opacity = 80, 0
            # we can remove the values from the texfield to...
            form.content.controls[0].value =  None
            form.content.controls[1].content.value =  "Add Text"
            form.content.controls[1].on_click = lambda e: AddTaskToScreen(e)
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
                                #main column here...
                                _main_column_,

                                # form class here...
                                # pass in the argument
                                FormContainer(lambda e: AddTaskToScreen(e)),
                            ],
                        ),
                    )
                ],
            ),

        )
    )
    page.update()
    
    # The form container index is as follows. 
    # We can set the long element index as a variable so it can be called faster and easier.
    form = page.controls[0].content.controls[0].content.controls[1].controls[0]
    # now we can call form whenever we want to do something with it...

    # now to display it, we need to read the database
    # another note: Flet keeps on refreshing when we call the database functions, this could be from the code or from flet itself, but i should be adressed...
    db_instance = Database()

    db = db_instance.ConnectToDatabase
    
    #now remember that the ReadDatabase function returns the records...
    # note: return is a tuple data type
    # note: we may want to display the records in reverse order, meaning the new records first followed by the oldest last...
    # using [::-1] revereses a list
    for task in db_instance.ReadDatabase()[::-1]:
        # let's see if the task are being saved...
        print (task)
        # let's add these the to the screen now
        _main_column_.controls.append(
            # same process as before: we create an instance of this class...
            CreateTask(
                task[0], # first item of the returned tuple
                task[1],
                DeleteFunction,
                UpdateFunciton,
            )
        )
    _main_column_.update()




if __name__ == '__main__':
    flet.app(target=main)   
