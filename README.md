# fun_times
Simple program where I learned how to query a SQLite database from Python.

I started by using (this article)[https://docs.python.org/3/sqlite.html] to see how to use the sqlite3 library to execute SQL commands in a Python environment.


Here is what I have learned so far:

1. Need to import 'sqlite3' library
 
3. You need to connect to the database you wish to use

5. After the database has been connected, a cursor is needed to be able to interact with said database

7. To execute a SQL command, you use (the_cursor_variable).execute("some_SQL_command")
   Example: cursor_variable.execute("SELECT * FROM db_table")

8. Use ("...") for single line commands and ("""...""") for multiple lines of commands

9. connection_variable.commit() needs to be made if you wish to commit new information

10. After .execute(), a .fetch***() needs to be executed (.fetchall(), .fetchmany(), .fetchone()) <--- Also need to delve a bit deeper

11. Close out with connection_variable.close()

