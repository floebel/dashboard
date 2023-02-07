
import streamlit as st
import sqlite3
import pandas as pd

"""
SELECT journal, count(journal_id) as count_journal
FROM article
INNER JOIN journal ON article.journal_id = journal.rowid
GROUP BY journal_id
ORDER BY count_journal DESC
LIMIT 10;
"""

#import sqlalchemy
#from sqlalchemy.ext.automap import automap_base
#from sqlalchemy.orm import Session
#from sqlalchemy import create_engine, func, inspect 
#Create engine 





def query(db_name, sql, data):
    with sqlite3.connect(db_name) as db:
        cursor = db.cursor()
        cursor.execute("PRAGMA Foreign_Keys = ON")
        cursor.execute(sql, data)
        result = cursor.fetchall()
        db.commit()
        return result



def main():
   st.title("Sqlite3 Test")
   #st.info(
   #    """
   #    This app is maintained by Fulton Loebel
   #    """
   #)


   conn = sqlite3.connect('millbrae_2019.sqlite')
   cursor = conn.cursor()

   st.write("Connected to the SQLite database")

   query = "SELECT * FROM Lease"

   if 1 == 2:
      result = cursor.execute(query).fetchall()
      st.write("Result of the query:", result)
   else:
      query = "SELECT * FROM Lease"
      df = pd.read_sql_query(query, conn)

      st.write("Result of the query:")
      st.dataframe(df)

   conn.close()

   conn.close()
    
   #from flask import Flask
   #from flask_sqlite3 import SQLite3

   #app = Flask(__name__)
   #app.config['SQLITE3_DATABASE_URI'] = 'sqlite:///test.db'
   #db = SQLite3(app)



   
