"""
Matthew
Created: 04/15/2023
Directions from: https://docs.python.org/3/sqlite.html
Purpose: Get started learning how to use SQLite using Python to 
        execute SQL commands
"""

#%%
# Import sqlite3 library to be able to communicate between SQLite and Python
import sqlite3

#%%
# Connect to database that you want to pull information from
con = sqlite3.connect("tutorial.db")

#%%
# Create a cursor to be able to execute SQL statements
cur = con.cursor()

#%%
# Create a table to store data
# This table will be a table about movies
cur.execute("CREATE TABLE movie(title, year, score)")
"""
#%%
# Call all the information from the table
call = cur.execute("SELECT * FROM movie")
# ###.fetchone() fetches the results of the query
call.fetchone()
"""
# Appereantly you need to use sqlite_master instead of the table name 'movie'
# That also didn't produce expected results

#%%
# Insert info into table
cur.execute("""
        INSERT INTO movie VALUES
                ('Monty Python and the Holy Grail', 1975, 8.2),
                ('Star Wars: A New Hope', 1977, 8.7),
                ('Iron Man', 2008, 9.0)

""")
# Changes must be committed
con.commit()

#%%
call = cur.execute("SELECT * FROM movie")
# Appereantly you need to use ###.fetchall(), instead of ###.fetchone()
call.fetchall()

#%%
# Insert more rows
data = [
    ("Monty Python Live at the Hollywood Bowl", 1982, 7.9),
    ("The Office", 2006, 9.2),
    ("Second Hand Lions", 2000, 7.9)
]
cur.executemany("INSERT INTO movie VALUES(?, ?, ?)", data)
con.commit()

#%%
call = cur.execute("SELECT * FROM movie")
call.fetchall()

#%%
"""rem = cur.execute('DELETE FROM movie')
con.commit()"""

#%%
"""call = cur.execute("SELECT * FROM movie")
call.fetchall()"""

#%%
# Close connection to db
con.close()

#%% 
# Start a new connection
new_con = sqlite3.connect("tutorial.db")
new_cur = new_con.cursor()

#%%
# SQL query
res = new_cur.execute("SELECT title, year FROM movie")
res.fetchall()

#%%
# More queries
res_1 = new_cur.execute("""
                        SELECT
                        title, year
                        FROM movie
                        ORDER BY score DESC""")
res_1.fetchall()

#%%
# Attach title and year to a variable
res_2 = new_cur.execute("SELECT title, year FROM movie ORDER BY score DESC")
title, year = res.fetchone()
print(f'Highest scoring movie is {title!r}, released in {year}') # the !r in {title!r} puts a quote around the title
print(f'Highest scoring movie is {title}, released in {year}') # here it shows what happens when the '' are left out

