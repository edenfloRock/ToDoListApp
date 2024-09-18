import sqlite3 

# Now the final part, we can implement a database to store the tasks.
# We can create a class for this

class Database:

    def __init__(self):
        """Inicializa la conexión a la base de datos al crear una instancia de Database."""
        self.db = self.ConnectToDatabase()

    def ConnectToDatabase(self):
        """
        Conecta a la base de datos SQLite y crea una tabla de tareas si no existe.

        Esta tabla contiene las columnas:
        - `id`: Entero, clave primaria.
        - `Task`: Tarea (texto).
        - `Date`: Fecha (texto).

        Retorna:
            db (sqlite3.Connection): Objeto de conexión a la base de datos.
        """
        try:
            db = sqlite3.connect("todo.db")
            c = db.cursor()
            c.execute(
                """
                CREATE TABLE if not exists tasks (
                    id INTEGER PRIMARY KEY,
                    Task VARCHAR(255) NOT NULL, Date VARCHAR(255) NOT NULL)
                """
            )
            return db
        except Exception as e:
            print(e)

    def ReadDatabase(self):
        """
        Lee las tareas de la base de datos.

        Retorna:
            records (list): Lista de tuplas con las tareas y sus fechas.
        """
        c = self.db.cursor()
        c.execute("SELECT Task, Date FROM tasks")
        records = c.fetchall()
        return records

    def InsertDatabase(self, values):
        """
        Inserta una nueva tarea en la base de datos.

        Parámetros:
            values (tuple): Tupla que contiene la tarea y la fecha.

        Retorna:
            None
        """
        c = self.db.cursor()
        c.execute("INSERT INTO tasks (Task, Date) VALUES (?, ?)", values)
        self.db.commit()

    def DeleteDatabase(self, value):
        """
        Elimina una tarea de la base de datos.

        Parámetros:
            value (tuple): Tupla que contiene la tarea a eliminar.

        Retorna:
            None
        """
        c = self.db.cursor()
        c.execute("DELETE FROM tasks WHERE Task =?", value)
        self.db.commit()

    def UpdateDatabase(self, value):
        """
        Actualiza una tarea existente en la base de datos.

        Parámetros:
            value (tuple): Tupla que contiene la nueva tarea y la tarea anterior a actualizar.

        Retorna:
            None
        """
        c = self.db.cursor()
        c.execute("UPDATE tasks SET Task=? WHERE Task=?", value)
        self.db.commit()
