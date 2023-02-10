

#!/usr/bin/env python
# -*- coding: utf-8 -*-

print("starting fdl_maintenance_sqlite.py")

"""
publications = pd.read_sql(sql = 'SELECT * FROM publication_citations_per_year LIMIT 100000', con=con) #Set connection
pub = publications.pivot(index = 'year', columns = 'publication_id', values = 'citations').cumsum() #Get a pivot table of pub
pub.plot(legend=False, logy = True, alpha=0.2) #Create logarthmic plot
pub.plot(legend=False, logy = False, alpha=0.2) #Create non-log plot
"""


"""
# df_articles["KEEP_DELETE"] = df_articles.apply(lambda row: Fig_KEEP_DELETE(row), axis=1)
def Fig_KEEP_DELETE(row):

   one_pmcid = row["PMCID"]
   if len(one_pmcid) >= 4:
      return "KEEP"
   else:
      return "DELETE"
""" 


"""
# Average Death per Country
# df = pd.read_sql_query("
SELECT Country_Region, AVG(Deaths) AS avg_deaths
FROM covid_19
GROUP BY Country_Region
", con)
df
"""


"""
# Covid_19 Statistics per Country
df = pd.read_sql_query("
SELECT Country_Region, SUM(Confirmed) AS Total_Cases, SUM(Deaths) AS Total_Deaths, 
SUM(Recovered) AS Total_Recovered 
FROM covid_19
GROUP BY Country_Region
ORDER BY Country_Region
", con)
"""


# Running this query we can know which clients have spent more than 200,000, between 200k and 100k and less than 100k

query = """SELECT a.name, SUM(o.total_amt_usd) total_spent,
                 CASE
                 WHEN SUM(o.total_amt_usd) > 200000 THEN 'Greater than 200,000'
                 WHEN SUM(o.total_amt_usd) > 100000 AND SUM(o.total_amt_usd) < 200000 THEN '200,000 and 100,000'
                 ELSE 'under 100,000' END AS level
                 FROM orders o
                 JOIN accounts a
                 ON o.account_id = a.id
                 GROUP BY 1
                 ORDER BY 2 DESC;"""

# pd.read_sql(query, conn)


                 
# Running this query we can know which channels were the most used to contact the clients

query = """SELECT web_events.channel, COUNT(accounts.name)
 FROM web_events
 JOIN accounts
 ON web_events.account_id = accounts.id
 GROUP BY web_events.channel
 ORDER BY COUNT(accounts.name) DESC
 LIMIT 8;"""

#pd.read_sql(query, conn)                 

# Running this query we can see how many times each client was contacted using "facebook"
query = """
SELECT accounts.name, COUNT(web_events.channel)
 FROM accounts
 JOIN web_events
 ON web_events.account_id = accounts.id
 WHERE web_events.channel LIKE 'facebook'
 GROUP BY accounts.name
 HAVING COUNT(web_events.channel) > 6
 ORDER BY 2
 LIMIT 10;"""

#pd.read_sql(query, conn)


# Running this query we can see how many times each channel was used in each region

query = """
SELECT region.name, web_events.channel, COUNT(web_events.channel) number_of_times
 FROM web_events
 JOIN accounts
 ON accounts.id = web_events.account_id
 JOIN sales_reps
 ON sales_reps.id = accounts.sales_rep_id
 JOIN region
 ON sales_reps.region_id = region.id
 GROUP BY region.name, web_events.channel
 ORDER BY 3 DESC
 LIMIT 10;
 """

# pd.read_sql(query, conn)

"""
/* pour récupérer les abstracts des auteurs ayant été publié au moins deux fois  */
SELECT author.author, abstract 
FROM article 
INNER JOIN author ON article.author_id = author.rowid
GROUP BY author_id 
HAVING count(author_id) > 1 AND abstract IS NOT NULL
WHERE author_id in (SELECT author_id
                    FROM article
                    GROUP BY author_id
                    HAVING count(author_id) > 1) AND abstract IS NOT NULL
ORDER BY author_id DESC;

/* pour récupérer un classement des journaux scientifiques par rapport aux nombres d'articles publiés */
SELECT journal, count(journal_id) as count_journal
FROM article
INNER JOIN journal ON article.journal_id = journal.rowid
GROUP BY journal_id
ORDER BY count_journal DESC
LIMIT 10;

/* pour récupérer le nombre d'articles publiés par an */
SELECT strftime('%Y', publication_date.date) as pub_year, count(publication_date_id) as count_date
FROM article
INNER JOIN publication_date ON article.publication_date_id = publication_date.rowid
GROUP BY pub_year;
"""




"""
DROP TABLE IF EXISTS pubmed;
DROP TABLE IF EXISTS pmc;
DROP TABLE IF EXISTS mesh;

CREATE TABLE pubmed (
pmid INTEGER,
journal  VARCHAR(100),
year INTEGER,
title VARCHAR(200),
abst VARCHAR(5000),
url VARCHAR(100)
);

CREATE TABLE pmc (
pmid INTEGER,
pmcid VARCHAR(20),
pdfurl VARCHAR(100),
FOREIGN KEY (pmid) REFERENCES pubmed (pmid)
);

CREATE TABLE mesh (
meshid INTEGER,
pmid INTEGER,
mesh_term  VARCHAR(200),
FOREIGN KEY (pmid) REFERENCES pubmed (pmid)
);

.separator \t
.import pubmed.txt pubmed
.import pmc.txt pmc
.import mesh.txt mesh

.exit
"""



"""
 cursor.execute("INSERT INTO fish VALUES ('Sammy', 'shark', 1)")
 cursor.execute("INSERT INTO fish VALUES ('Jamie', 'cuttlefish', 7)")
"""

"""
 new_tank_number = 2
   moved_fish_name = "Sammy"
   cursor.execute(
      "UPDATE fish SET tank_number = ? WHERE name = ?",
      (new_tank_number, moved_fish_name)
   )
"""

   
#        return self.cursor.execute("""drop table {}""".format(table_name))
#        return self.cursor.execute("""alter table {} rename to {}""".format(old_table_name, new_table_name))

#from fdl_sub_sqlite_display import *
#from fdl_sub_sqlite_utilities import *

#import pyodbc

from fdl_sub_html_small import *



import pandas as pd
pd.set_option('display.max_rows', 100)       
pd.set_option('display.max_columns', 100)    
pd.set_option('display.width', 1000)         
pd.set_option('display.max_colwidth', 40)    

#from config import CONFIG
pd.set_option('display.max_colwidth', 1000)



import numpy as np
import os
#import os.path
#import os.remove

import sqlite3
import sqlalchemy
#from sqlalchemy.ext.automap import automap_base
#from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func, inspect 
#Create engine 




    

"""
    SQLite3 does not check for foreign key constraints by defautl,
    you must turn this feature on using SQL: PRAGMA Foreign_Keys = ON

"""

list_1 = [1,5,10,20,50,100,200,500,1000,2000,5000,10000,20000,50000,100000]
list_2 = [200000,300000,400000,500000,600000,700000,800000,900000]
list_3 = [1000000,1100000,1200000,1300000,1400000,1500000,1600000,1700000,1800000,1900000]
list_4 = [2000000,2100000,2200000,2300000,2400000,2500000,2600000,2700000,2800000,2900000]

list_display = list_1 + list_2 + list_3 + list_4



#######################################################################################################################################


"""      
   if 1 == 2:
      cur.execute("CREATE TABLE IF NOT EXISTS articles (pmid text PRIMARY KEY, xml_file text, pmcid text, doi text, title text, year text, country text, journal text, abstract text)")
   else:
      #cur.execute("CREATE TABLE IF NOT EXISTS citations (pmid text PRIMARY KEY, citationid text)")
      #cur.execute("CREATE TABLE IF NOT EXISTS citations (pmid text, citationid text)")
      cur.execute("CREATE TABLE IF NOT EXISTS lookups (pmid text PRIMARY KEY, initial_author text, final_author text)")

   oSQLITE.commit()
"""



"""
   if 1 == 1:  # WORKS ONE FIELD AT A TIME 
      sql = "UPDATE citations SET first_author = ( SELECT initial_author FROM lookups WHERE lookups.pmid = citations.pmid )"    
      sql_within_database(oSQLITE, sql)
      sql = "UPDATE citations SET last_author = ( SELECT final_author FROM lookups WHERE lookups.pmid = citations.pmid )"    
      sql_within_database(oSQLITE, sql)
"""



#   if 1 == 1:   
#      cur.execute("CREATE INDEX IF NOT EXISTS lookups_pmid ON lookups(pmid)")
#      oSQLITE.commit()

"""
import sqlalchemy as sa
import pandas as pd

engine = sa.create_engine(...)
with engine.connect() as conn:
   result = conn.execute("SELECT * FROM foo;")
   df = pd.DataFrame(result.all(), columns=result.keys())
"""



def database_to_df(oENGINE, sql):  # WORKS

   print("in database_to_df(oENGINE, sql)")
   print("sql = ", sql)
   #print("db_sqlite = ", db_sqlite)
   #print("drop_table = ", drop_table)    
   #engine = create_engine(database)
   
   cnx = oENGINE.connect()
   df = pd.read_sql(sql, cnx)
   nrows = len(df)
   #print("rows in df = ", nrows)
   #print()
   #print("df.head(10)")
   #print(df.head(10))   
   #print("df.dtypes")
   #print(df.dtypes)  
   #print()
   #input("wait")
   return df



if 1 == 2:
   db_sqlite = 'hz_oklahoma.sqlite'
   database = 'sqlite:///' + db_sqlite   
   oENGINE = create_engine(database)
   print("oENGINE object is connected to", database)
   #Another way to get all indexes from a database is to query from the sqlite_master table:
   sql = "SELECT LeaseID, SurfaceLatitude, sqrt(SurfaceLatitude) FROM Lease"
   df = database_to_df(oENGINE, sql)
   df_to_webbrowser("df", df)
   #print("df.head(100) of INDEXES")
   #print(df.head(100))
   input("STOP")





if 1 == 2:
   db_sqlite = 'hz_oklahoma.sqlite'
   database = 'sqlite:///' + db_sqlite   
   oENGINE = create_engine(database)
   print("oENGINE object is connected to", database)
   #Another way to get all indexes from a database is to query from the sqlite_master table:
   sql = "SELECT type, name, tbl_name, sql FROM sqlite_master WHERE type= 'index'"
   df = database_to_df(oENGINE, sql)
   print("df.head(100) of INDEXES")
   print(df.head(100))
   input("STOP")



# sqlite_execute(db_sqlite, cSQL) 
def sqlite_execute(oSQLITE, cSQL): 

    cur = oSQLITE.cursor()
    #print("sqlite_execute", cSQL)
    cur.execute(cSQL)
    oSQLITE.commit()
    return ""
      
 



def open_sqlite_conn(any_state):

   if any_state == "OK":
      oSQLITE = sqlite3.connect('hz_oklahoma.sqlite')
      #cursor = conn.cursor()
   elif any_state == "KS":
      oSQLITE = sqlite3.connect('hz_kansas.sqlite')
      #cursor = conn.cursor()
    
   return oSQLITE

# sql = "UPDATE citations SET first_author = ( SELECT initial_author FROM lookups WHERE lookups.pmid = citations.pmid )"    



def df_from_sqlite(any_state, query):

   if any_state == "OK":
      conn = sqlite3.connect('hz_oklahoma.sqlite')
      #cursor = conn.cursor()
   elif any_state == "KS":
      conn = sqlite3.connect('hz_kansas.sqlite')
      #cursor = conn.cursor()

   #result = cursor.execute(query).fetchall()
   #st.write("Result of the query:", result)    
   df = pd.read_sql_query(query, conn)

   #   st.write("Result of the query:")
   #   st.dataframe(df)

   conn.close()
   return df


# CREATE INDEXES ...
if 1 == 2:
   any_state = "KS"
   oSQLITE = open_sqlite_conn(any_state)
   cSQL = "CREATE INDEX IF NOT EXISTS Lease_LeaseID ON Lease(LeaseID)"
   sqlite_execute(oSQLITE, cSQL) 
   cSQL = "CREATE INDEX IF NOT EXISTS LeaseProduction_LeaseID_Year_Month ON LeaseProduction(LeaseID, Year, Month)"
   sqlite_execute(oSQLITE, cSQL) 
   input("STOP created indexes")

   
# CREATE COLUMNS ...
if 1 == 2:
   any_state = "OK"
   oSQLITE = open_sqlite_conn(any_state)
   #cSQL = "ALTER TABLE LeaseProduction ADD COLUMN LAT_LENGTH"  # float text integer
   #cSQL = "ALTER TABLE LeaseProduction ADD COLUMN First_Year"
   #cSQL = "ALTER TABLE Lease ADD COLUMN First_Year"
   cSQL = "ALTER TABLE Lease ADD COLUMN MAX_MONTHS"
   sqlite_execute(oSQLITE, cSQL)
   #cSQL = "ALTER TABLE LeaseProduction ADD COLUMN First_Month"
   #cSQL = "ALTER TABLE Lease ADD COLUMN First_Month"
   #sqlite_execute(oSQLITE, cSQL) 
   input("STOP created columns")   
 
   





if 1 == 1:    # Update Lease with single command
   any_state = "OK"     
   df_lease = df_from_sqlite(any_state, "SELECT * FROM Lease")
   df_to_webbrowser("df_lease BEFORE", df_lease)

   oSQLITE = open_sqlite_conn(any_state)
   
   #sql = "on ...
   #  	cSelect += "ROUND(2000.01 + DATEDIFF( 'd',  DateSerial(2000, 01, 01),  DateSerial(P.Year, P.Month, 28)  ) / 365.25,3) AS 'CALENDAR YEARS', "   // 2005 ..............

   if 1 == 2:
      #cUpdate = "UPDATE LeaseProduction "
      #cUpdate += " SET PRODDATE = DateSerial(Year, Month, 15) "
      # cursor.execute("UPDATE mytable SET date_field = strftime('%Y-%m-%d', ?, '+10 day') WHERE date_field = ?", (current_date, current_date))
      cUpdate = "UPDATE LeaseProduction "
      cUpdate += " SET PRODDATE = strftimeDateSerial(Year, Month, 15) " 
   elif 1 == 2:   
      cUpdate  = "UPDATE LeaseProduction "
      cUpdate += " SET LeaseProduction.FIRSTDATE = #01/01/1970# "
      cUpdate += " WHERE LeaseProduction.FIRSTDATE is null "
   elif 1 == 2:   
      cUpdate  = "UPDATE LeaseProduction "
      cUpdate += " SET LeaseProduction.NORMFIFF = DateDiff('d',LeaseProduction.FIRSTDATE,LeaseProduction.PRODDATE) "
   elif 1 == 2:
      cUpdate = "UPDATE LeaseProduction "
      cUpdate += " SET LeaseProduction.PRODDATE = DateSerial(Year, Month, 15) "
   elif 1 == 2:
      cUpdate = "UPDATE LeaseProduction "
      cUpdate += " SET LeaseProduction.NORMALDATE = DateAdd('d', DateDiff('d',LeaseProduction.FIRSTDATE,LeaseProduction.PRODDATE),#01/01/1970#) "
   elif 1 == 2:
      cUpdate  = "UPDATE LeaseProduction "
      cUpdate += " SET LeaseProduction.NORMMONTH = MONTH(LeaseProduction.NORMALDATE), LeaseProduction.NORMYEAR = YEAR(LeaseProduction.NORMALDATE) "
   elif 1 == 2:
      cUpdate  = "UPDATE LeaseProduction "
      cUpdate += " SET LeaseProduction.NORMMONTH = MONTH(LeaseProduction.NORMALDATE), LeaseProduction.NormYear = YEAR(LeaseProduction.NORMALDATE) "
   elif 1 == 2:
      cUpdate  = "UPDATE LeaseProduction "
      cUpdate += " SET LeaseProduction.CUMUL_MONTHS = (12.0 * (LeaseProduction.NORMYEAR - 1970.0)) + LeaseProduction.NORMMONTH "

   if 1 == 2: # WORKS
      cUpdate = "UPDATE LeaseProduction SET LAT_LENGTH = ( SELECT LAT_LENGTH FROM Lease WHERE LeaseProduction.LeaseID = Lease.LeaseID )"    
   elif 1 == 2:
      #cUpdate = "UPDATE LeaseProduction SET PRODDATE = datetime('" + str(Year) + "-" + str(Month) + "-15)" 
      cUpdate  = "UPDATE LeaseProduction SET PRODDATE = datetime( CAST(Year AS TEXT) || '-' || CAST(Month AS TEXT) || '-' || '15') "
   elif 1 == 2:  # WORKS
      cUpdate = "UPDATE Lease SET FieldDirEntityType = printf('%08d', User14)"  # WORKS
   elif 1 == 2:  # WORKS
      cUpdate = "UPDATE Lease SET LAT_LENGTH = ( SELECT LAT_LENGTH FROM Lease WHERE LeaseProduction.LeaseID = Lease.LeaseID )"    
   elif 1 == 2:  # WORKS
     #cUpdate = "UPDATE Lease SET FirstProdDate = (SELECT min(FIRSTDATE) FROM LeaseProduction WHERE LeaseProduction.LeaseID = Lease.LeaseID) "
     cUpdate  = "UPDATE Lease SET FirstProdDate = (SELECT min(FIRSTDATE) FROM LeaseProduction "
     cUpdate += "WHERE LeaseProduction.LeaseID = Lease.LeaseID AND (LeaseProduction.Oil > 0 OR LeaseProduction.Gas > 0)) "
   elif 1 == 2:  # WORKS
     #cUpdate = "UPDATE Lease SET First_Year = year(FirstProdDate) "  # FAILS
     cUpdate = "UPDATE Lease SET First_Year = strftime('%Y', FirstProdDate) "  # WORKS
   elif 1 == 2:
     #cUpdate = "UPDATE Lease SET First_Year = year(FirstProdDate) "  # FAILS
     cUpdate = "UPDATE Lease SET First_Month = strftime('%m', FirstProdDate) "  # WORKS
   elif 1 == 1:  # WORKS
      cUpdate = "UPDATE Lease SET MAX_MONTHS = ( SELECT max(CUMUL_MONTHS) FROM LeaseProduction WHERE LeaseProduction.LeaseID = Lease.LeaseID )"    
   elif 1 == 2:  # WORKS
      fdl = 1  

   if 1 == 1:
      print(cUpdate)
      sqlite_execute(oSQLITE, cUpdate) 

   df_lease = df_from_sqlite(any_state, "SELECT * FROM Lease")
   df_to_webbrowser("df_lease AFTER", df_lease)

   input("STOP")



if 1 == 1:    # Update LeaseProduction with single command
   any_state = "OK"     
   df_prod = df_from_sqlite(any_state, "SELECT * FROM LeaseProduction")
   df_to_webbrowser("df_prod BEFORE", df_prod)

   oSQLITE = open_sqlite_conn(any_state)
   
   #sql = "on ...
   #  	cSelect += "ROUND(2000.01 + DATEDIFF( 'd',  DateSerial(2000, 01, 01),  DateSerial(P.Year, P.Month, 28)  ) / 365.25,3) AS 'CALENDAR YEARS', "   // 2005 ..............

   if 1 == 2:
      #cUpdate = "UPDATE LeaseProduction "
      #cUpdate += " SET PRODDATE = DateSerial(Year, Month, 15) "
      # cursor.execute("UPDATE mytable SET date_field = strftime('%Y-%m-%d', ?, '+10 day') WHERE date_field = ?", (current_date, current_date))
      cUpdate = "UPDATE LeaseProduction "
      cUpdate += " SET PRODDATE = strftimeDateSerial(Year, Month, 15) " 
   elif 1 == 2:   
      cUpdate  = "UPDATE LeaseProduction "
      cUpdate += " SET LeaseProduction.FIRSTDATE = #01/01/1970# "
      cUpdate += " WHERE LeaseProduction.FIRSTDATE is null "
   elif 1 == 2:   
      cUpdate  = "UPDATE LeaseProduction "
      cUpdate += " SET LeaseProduction.NORMFIFF = DateDiff('d',LeaseProduction.FIRSTDATE,LeaseProduction.PRODDATE) "
   elif 1 == 2:
      cUpdate = "UPDATE LeaseProduction "
      cUpdate += " SET LeaseProduction.PRODDATE = DateSerial(Year, Month, 15) "
   elif 1 == 2:
      cUpdate = "UPDATE LeaseProduction "
      cUpdate += " SET LeaseProduction.NORMALDATE = DateAdd('d', DateDiff('d',LeaseProduction.FIRSTDATE,LeaseProduction.PRODDATE),#01/01/1970#) "
   elif 1 == 2:
      cUpdate  = "UPDATE LeaseProduction "
      cUpdate += " SET LeaseProduction.NORMMONTH = MONTH(LeaseProduction.NORMALDATE), LeaseProduction.NORMYEAR = YEAR(LeaseProduction.NORMALDATE) "
   elif 1 == 2:
      cUpdate  = "UPDATE LeaseProduction "
      cUpdate += " SET LeaseProduction.NORMMONTH = MONTH(LeaseProduction.NORMALDATE), LeaseProduction.NormYear = YEAR(LeaseProduction.NORMALDATE) "
   elif 1 == 2:
      cUpdate  = "UPDATE LeaseProduction "
      cUpdate += " SET LeaseProduction.CUMUL_MONTHS = (12.0 * (LeaseProduction.NORMYEAR - 1970.0)) + LeaseProduction.NORMMONTH "

   elif 1 == 2: # WORKS
      cUpdate = "UPDATE LeaseProduction SET LAT_LENGTH = ( SELECT LAT_LENGTH FROM Lease WHERE LeaseProduction.LeaseID = Lease.LeaseID )"    
   elif 1 == 2:
      #cUpdate = "UPDATE LeaseProduction SET PRODDATE = datetime('" + str(Year) + "-" + str(Month) + "-15)" 
      cUpdate  = "UPDATE LeaseProduction SET PRODDATE = datetime( CAST(Year AS TEXT) || '-' || CAST(Month AS TEXT) || '-' || '15') "
   elif 1 == 2:  # WORKS
      cUpdate = "UPDATE Lease SET FieldDirEntityType = printf('%08d', User14)"  # WORKS
   elif 1 == 2:  # WORKS
      cUpdate = "UPDATE LeaseProduction SET First_Year = ( SELECT First_Year FROM Lease WHERE LeaseProduction.LeaseID = Lease.LeaseID )"    
   elif 1 == 2:  # WORKS
      cUpdate = "UPDATE LeaseProduction SET First_Month = ( SELECT First_Month FROM Lease WHERE LeaseProduction.LeaseID = Lease.LeaseID )"    
       
   elif 1 == 1:
      cUpdate  = "UPDATE LeaseProduction SET CUMUL_MONTHS = "
      cUpdate += "12.0 * (Year - First_Year) + (Month - First_Month) "
      #cUpdate = "UPDATE LeaseProduction SET CUMUL_MONTHS = (12.0 * (First_Year - Year)) + LeaseProduction.NormMonth "

  
   #cUpdate = "ALTER TABLE LeaseProduction ADD COLUMN LAT_LENGTH"  # float text integer
   #cUpdate = "ALTER TABLE Lease DROP COLUMN SurfaceLatitudeIHS"


   if 1 == 1:
      print(cUpdate)
      sqlite_execute(oSQLITE, cUpdate) 

   df_prod = df_from_sqlite(any_state, "SELECT * FROM LeaseProduction")
   df_to_webbrowser("df_prod AFTER", df_prod)

   input("STOP")



if 1 == 2:     # Update LeaseProduction row by row 
   any_state = "KS"
   df_prod = df_from_sqlite(any_state, "SELECT * FROM LeaseProduction")
   #df_prod = df_from_sqlite(any_state, "SELECT * FROM LeaseProduction LIMIT 30")
   
   #select_query = "SELECT lower(name) FROM SqliteDb_developers where id = ?"
   
   df_to_webbrowser("df_prod BEFORE", df_prod)
   #input("WAIT")

   
   oSQLITE = open_sqlite_conn(any_state)

   nToDo = len(df_prod)
   nDone = 0  
   for index, row in df_prod.iterrows():
      nDone = nDone + 1
      c_leaseid = row["LeaseID"]
      
      n_year = row["Year"]
      n_month = row["Month"]
      c_year = str(n_year)
      c_month = str(n_month)
      
      #str_date = "2023-02-15"        # YYYY-MM-DD
      str_date = c_year + "-" + c_month.zfill(2) + "-15"
      
      #print()
      #print(lat_length)
      #print()
      #any_lat_length = part1 + part2 - 800.0
      if nDone in list_display:
         print("Updating", c_leaseid, "LeaseID", nDone, "done", nToDo, "to do")
      
      #cSQL = "UPDATE LeaseProductuion SET PRODDATE = " + str(lat_length) + " WHERE LeaseID = " + next_leaseid
      #cSQL = "UPDATE LeaseProduction SET PRODDATE = " + str_date   # e_field = ?", (current_date, current_date))
      #cursor.execute("UPDATE mytable SET date_field = strftime('%Y-%m-%d') WHERE date_field = ?", (current_date, current_date))


      # Get the text input
      #current_date = "2023-02-15" # input("Enter the current date (YYYY-MM-DD): ")
      #number_of_days = 15         # input("Enter the number of days to add: ")

      # Update the date field
      #cSQL = "UPDATE mytable SET PRODDATE = strftime('%Y-%m-%d', ?, '+' || ? || ' day') WHERE date_field = ?", (current_date, number_of_days, current_date)
      #cSQL = "UPDATE LeaseProduction SET PRODDATE = strftime('%Y-%m-%d', ?, '+' || ? || ' day') WHERE date_field = ?", (current_date, number_of_days, current_date)
      #cSQL = "UPDATE LeaseProduction SET PRODDATE = datetime('2023-02-15')"  # WORKS
      cSQL  = "UPDATE LeaseProduction SET PRODDATE = datetime('" + str_date + "')" 
      cWhere = " WHERE LeaseID = " + c_leaseid + " AND Year = " + c_year + " AND Month = " + c_month  

      sqlite_execute(oSQLITE, cSQL) 


   df_prod = df_from_sqlite(any_state, "SELECT * FROM LeaseProduction")
   df_to_webbrowser("df_prod AFTER", df_prod)

   input("STOP")

   

#def sqlite_power(x,n):
#    return int(x)**n
#print(sqlite_power(2,3))
# 8

#def upper(string):
#    return str(string).upper()


if 1 == 2:     # Update Lease row by row 
   any_state = "OK"
   df_lease = df_from_sqlite(any_state, "SELECT * FROM Lease")
   #df_lease = df_from_sqlite(any_state, "SELECT * FROM Lease LIMIT 30")
  
   #select_query = "SELECT lower(name) FROM SqliteDb_developers where id = ?"
   
   df_to_webbrowser("df_lease BEFORE", df_lease)
   oSQLITE = open_sqlite_conn(any_state)

   nToDo = len(df_lease)
   nDone = 0  
   for index, row in df_lease.iterrows():
      nDone = nDone + 1
      next_leaseid = row["LeaseID"]
      
      surf_lat = row["SurfaceLatitude"]
      bot_lat = row["BottomLatitude"]
      surf_long = row["SurfaceLongitude"]
      bot_long = row["BottomLongitude"] 
  
      #next_word = next_word.lower()  # lower case 
      #next_count = row["Count"]

      #cSQL = "ALTER TABLE Lease ADD COLUMN LAT_LENGTH"  # float text integer
      #cSQL  = "UPDATE Lease SET first_author = ( SELECT initial_author FROM lookups WHERE lookups.pmid = citations.pmid )"    
      #cSQL  = "UPDATE Lease SET Analyzed = 'Yes'"
      if surf_lat == 0.0 or surf_long == 0.0:
         lat_length = 0.0
      elif bot_lat == 0.0 or bot_long == 0.0:
         lat_length = 0.0    
      else:   
         lat_length = abs(5280.0 * 69.1* np.sqrt (( bot_lat - surf_lat ) ** 2  + 0.6 * ( bot_long - surf_long ) ** 2 ) ) - 800.0

      lat_length = int(lat_length)
      lat_length = abs(lat_length)
      
      #  cSelect += " ABS(5280.0 * 69.1* SQR (( BottomLatitude - SurfaceLatitude ) ^ 2  + 0.6 * ( BottomLongitude - SurfaceLongitude ) ^ 2 ) ) - 800.0 AS 'LAT_LENGTH', "
      #  cSelect += " ABS(5280.0 * 69.1* SQR ( delta_lat ^ 2  + 0.6 * ( delta_long ^ 2 ) ) - 800.0 AS 'LAT_LENGTH', "

      #part1 = ABS( 5280.0 * 69.1 * SQR (         ( BottomLatitude - SurfaceLatitude ) ^ 2   
      #c_delta_lat_squared = "( (BottomLatitude - SurfaceLatitude) * (BottomLatitude - SurfaceLatitude) )"
   
      #part1 = abs( 5280.0 * 69.1 * sqrt ( power ( delta_lat, 2 )

      #c_delta_long_squared = "( (BottomLongitude - SurfaceLongitude) * (BottomLongitude - SurfaceLongitude) )" 

      #part2 = 0.6 *         ( BottomLongitude - SurfaceLongitude ) ^ 2 ))  
                                 
      #part2  = 0.6 * power ( ( BottomLongitude - SurfaceLongitude ),  2)
   
      #str_lat_length = "abs(5280.0 * 69.1 * sqrt " + c_delta_lat_squared + "  + 0.6 * " + c_delta_long_squared + " ) - 800.0 "
      #str_lat_length = "SQRT(10 * 10)"
      #lat_length = np.sqrt(10 * 10)

      #print()
      #print(lat_length)
      #print()
      #any_lat_length = part1 + part2 - 800.0
      if nDone in list_display:
         print("Updating", next_leaseid, "with", lat_length, nDone, "done", nToDo, "to do")
      
      cSQL = "UPDATE Lease SET LAT_LENGTH = " + str(lat_length) + " WHERE LeaseID = " + next_leaseid

      sqlite_execute(oSQLITE, cSQL) 


   df_lease = df_from_sqlite(any_state, "SELECT * FROM Lease")
   df_to_webbrowser("df_lease AFTER", df_lease)

   input("STOP")

   

# ALTER TABLE LeaseProduction ADD status VARCHAR
# CREATE INDEX IF NOT EXISTS Lease_ookups_pmid ON lookups(pmid)")
# ALTER TABLE Lease DROP SurfaceLongitudeIHS
# ALTER TABLE Lease DROP BottomLatitudeIHS
# ALTER TABLE Lease DROP BottomLongitudeIHS
# ALTER TABLE Lease DROP Analyzed

   
 
        








def xxxopen_sqlite_conn(database, db_sqlite):

   print("in open_geometadb_sqlite_conn")
   print("database = ", database)
   print("db_sqlite = ", db_sqlite)
  
   #db_sqlite = 'test.sqlite'

   if 1 == 1: #is_file("", db_sqlite):
      print(db_sqlite, "exists")
      CREATE_NEW_YN = "N"
   else:
      print(db_sqlite, "does not exist")
      input("wait")
      return
    
   oSQLITE = sqlite3.connect(db_sqlite)
   print("oSQLITE object is connected to", db_sqlite)

   oENGINE = create_engine(database)
   print("oENGINE object is connected to", database)

        
   # Inspecting data
   #insp = inspect(oENGINE)
   #list_tables = insp.get_table_names()   # WORKS
   #print("list_tables")
   #print(list_tables)
   
   #if "temp" in list_tables:
   #   cstr  = "\ntemp table exists, drop it "
   #   cstr += "\n<Y> Yes, Drop it "
   #   cstr += "\n<N> No, Keep it  "  
   #   DROP_TEMP_YN = input(cstr)
   #   if DROP_TEMP_YN == "Y":
   #      sql_within_database(oSQLITE, "DROP TABLE IF EXISTS temp")
     
   return oENGINE, oSQLITE


"""
def open_pubmed_sqlite_conn(database, db_sqlite):

   print("in open_pubmed_sqlite_conn")
   print("database = ", database)
   print("db_sqlite = ", db_sqlite)
  
   #db_sqlite = 'test.sqlite'

   if is_file("", db_sqlite):
      print(db_sqlite, "exists")
      CREATE_NEW_YN = "N"
 
   else:
      print(db_sqlite, "does not exist")
      CREATE_NEW_YN = "Y"
   
   if 1 == 2:         
      cstr  = "\nCreate New " + db_sqlite + " SQLite3 Database "
      cstr += "\n<Y> Yes (DELETE the existing db) "
      cstr += "\n<N> No "  
      CREATE_NEW_YN = input(cstr)
      if CREATE_NEW_YN == "Y":
         if is_file("", db_sqlite):
            print(db_sqlite, "exists")
            delete_file("", db_sqlite)
         else:
            print(db_sqlite, "does not exist")    
    
   oSQLITE = sqlite3.connect(db_sqlite)
   print("oSQLITE object is connected to", db_sqlite)

   oENGINE = create_engine(database)
   print("oENGINE object is connected to", database)

   if CREATE_NEW_YN == "Y":
      create_pubmed_articles_table(oSQLITE)
      print("created pubmed articles table")
      create_pubmed_citations_table(oSQLITE)
      print("created pubmed citations table")
      create_pubmed_lookups_table(oSQLITE)
      print("created pubmed lookups table")
      
   # Inspecting data
   insp = inspect(oENGINE)
   list_tables = insp.get_table_names()   # WORKS
   print("list_tables")
   print(list_tables)
   
   if "temp" in list_tables:
      cstr  = "\ntemp table exists, drop it "
      cstr += "\n<Y> Yes, Drop it "
      cstr += "\n<N> No, Keep it  "  
      DROP_TEMP_YN = input(cstr)
      if DROP_TEMP_YN == "Y":
         sql_within_database(oSQLITE, "DROP TABLE IF EXISTS temp")
   
   #input("wait")  
   return oENGINE, oSQLITE
"""

   


def create_pubmed_lookups_table(oSQLITE):  # add more fields

   print("in create_pubmed_lookups_table(oSQLITE)")
   #print("database = ", database)
   #print("db_sqlite = ", db_sqlite)        
   #conn=sqlite3.connect("books.db")
   cur = oSQLITE.cursor()

   if 1 == 2:   # TEMPORARY
      cur.execute("DROP TABLE IF EXISTS lookups")
      oSQLITE.commit()
      print("dropping lookups table if exists")
      
   if 1 == 2:
      cur.execute("CREATE TABLE IF NOT EXISTS articles (pmid text PRIMARY KEY, xml_file text, pmcid text, doi text, title text, year text, country text, journal text, abstract text)")
   else:
      #cur.execute("CREATE TABLE IF NOT EXISTS citations (pmid text PRIMARY KEY, citationid text)")
      #cur.execute("CREATE TABLE IF NOT EXISTS citations (pmid text, citationid text)")
      cur.execute("CREATE TABLE IF NOT EXISTS lookups (pmid text PRIMARY KEY, initial_author text, final_author text)")

   oSQLITE.commit()

   if 1 == 1:   
      cur.execute("CREATE INDEX IF NOT EXISTS lookups_pmid ON lookups(pmid)")
      oSQLITE.commit()

   return ""


def create_pubmed_citations_table(oSQLITE):  # add more fields

   print("in create_pubmed_citations_table(oSQLITE)")
   #print("database = ", database)
   #print("db_sqlite = ", db_sqlite)        
   #conn=sqlite3.connect("books.db")
   cur = oSQLITE.cursor()

   if 1 == 2:   # TEMPORARY
      cur.execute("DROP TABLE IF EXISTS citations")
      oSQLITE.commit()
      print("dropping citations table if exists")
      
   if 1 == 2:
      cur.execute("CREATE TABLE IF NOT EXISTS articles (pmid text PRIMARY KEY, xml_file text, pmcid text, doi text, title text, year text, country text, journal text, abstract text)")
   else:
      #cur.execute("CREATE TABLE IF NOT EXISTS citations (pmid text PRIMARY KEY, citationid text)")
      #cur.execute("CREATE TABLE IF NOT EXISTS citations (pmid text, citationid text)")
      cur.execute("CREATE TABLE IF NOT EXISTS citations (pmid text, citationid text, first_author text, last_author text, PRIMARY KEY (pmid, citationid) )")

   oSQLITE.commit()

   if 1 == 1:  
      cur.execute("CREATE INDEX IF NOT EXISTS citations_pmid_citationid ON citations(pmid, citationid)")
      oSQLITE.commit()

   return ""



def create_pubmed_articles_table(oSQLITE):  # add more fields

   print("in create_pubmed_articles_table(oSQLITE)")
   #print("database = ", database)
   #print("db_sqlite = ", db_sqlite)        
   #conn=sqlite3.connect("books.db")
   cur = oSQLITE.cursor()

   if 1 == 2:
      cur.execute("ALTER TABLE articles ADD xml_file text")
      oSQLITE.commit()
      input("SUCCESS: ALTER TABLE articles ADD xml_file text") 
      #cur.execute("ALTER TABLE articles ADD pmcid text")
      #cur.execute("ALTER TABLE articles ADD pmcid text")
      #cur.execute("ALTER TABLE articles ADD abstract text")

           
   if 1 == 2:   # TEMPORARY
      cur.execute("DROP TABLE IF EXISTS articles")
      oSQLITE.commit()
      print("dropping articles table if exists")   

   if 1 == 2:
      cur.execute("CREATE TABLE IF NOT EXISTS articles (pmid text PRIMARY KEY, xml_file text, pmcid text, doi text, title text, year text, country text, journal text, abstract text)")
   else:
      cur.execute("CREATE TABLE IF NOT EXISTS articles (pmid text PRIMARY KEY, pmcid text, title text, year text, journal text, xml_file text, doi text, abstract text)")

   oSQLITE.commit()
   cur.execute("CREATE INDEX IF NOT EXISTS articles_pmid ON articles(pmid)")
   oSQLITE.commit()

   return ""

def get_sqlite_database_info(oENGINE, oSQLITE):
   """
   Returns an array of tables given a DB.
   """
   #if db_sqlite is None:
   #  log("perform_basic: No DB passed in")
   #  return
   print("in get_sqlite_database_info(oENGINE, oSQLITE)")
   #print("sql = ", sql)
   #print("db_sqlite = ", db_sqlite)
   #print("drop_table = ", drop_table)    
   #engine = create_engine(database)   
   cstr  = "\nThis could take time.  Are you sure"
   cstr += "\n<Y> Yes See summary statistics of database tables"
   cstr += "\n<N> No "  
   MENU_YN = input(cstr)

   list_tables = []
   list_rows = []
   list_cols = []
   
   if MENU_YN == "Y":  


      #oSQLITE = sqlite3.connect(db_sqlite)
      c = oSQLITE.cursor()
      arr = c.execute("select name from sqlite_master where type='table'")
      for row in arr:
         #tbl = row[0].encode('utf8')
         one_table = row[0]
         sql = "SELECT * FROM " + one_table + " LIMIT 20"
         df = database_to_df(oENGINE, sql)
         list_column_names = df.columns.values.tolist()
         print()
         print("list_column_names for", one_table)
         print(list_column_names)
         print()
         nRows = len(df)
         nCols = len(list_column_names)

         print("nCols = ", nCols, " for", one_table)
    
         list_tables.append(one_table)
         list_rows.append(nRows)
         list_cols.append(nCols)

      df_statistics = pd.DataFrame()
      df_statistics["Table"] = list_tables
      df_statistics["Rows"] = list_rows
      df_statistics["Cols"] = list_cols
  
      print()
      print("df_statistics.head(20) for all tables")
      print(df_statistics.head(20))
      print()
  
      #conn.close()
      print("list_tables")
      print(list_tables)
      input("wait")

   return list_tables




if 1 == 2:
   cstr  = "\nDatabase To DataFrame test.sqlite"
   cstr += "\n<Y> Yes "
   cstr += "\n<N> No "  
   MENU_YN = input(cstr)
   
   if MENU_YN == "Y":   

      #database = 'sqlite:///millbrae_2019.sqlite'
      db_sqlite = 'test.sqlite'
      database = 'sqlite:///' + db_sqlite   
      #sql = """SELECT * FROM Lease"""
      #sql = """SELECT * FROM Lease LIMIT 20"""
      #sql = """SELECT LeaseID, LeaseName FROM Lease LIMIT 20"""
      sql = '''
            SELECT
            a.product_name AS [PRODUCT NAME],
            b.price AS [PRICE]
            FROM products a
            LEFT JOIN prices b ON a.product_id = b.product_id
            '''
   
      database_to_df(database, sql)
   
      input("wait")
   
 




def sql_within_database(oSQLITE, sql):

   print("in sql_within_database(oSQLITE, sql)")
   print("sql = ", sql)
    
   cur = oSQLITE.cursor()
    
   #insert_sql = "INSERT OR IGNORE INTO articles VALUES (?,?,?)"
   #insert_sql = "INSERT OR REPLACE INTO articles VALUES (?,?,?)"

   cur.execute(sql)
   oSQLITE.commit()
   return ""

 
def insert_into_article(oSQLITE, pmid, xml_file, pmcid): # add more fields ...
    #conn=sqlite3.connect("books.db")
    cur = oSQLITE.cursor()
    
    #insert_sql = "INSERT INTO articles VALUES (?,?,?)"
    #insert_sql = "INSERT OR IGNORE INTO articles VALUES (?,?,?)"
    insert_sql = "INSERT OR REPLACE INTO articles VALUES (?,?,?)"

    cur.execute(insert_sql, (pmid, xml_file, pmcid))
    oSQLITE.commit()
    #conn.close()
    #view()


   
"""
def delete_file(any_path, any_file):

   # os.path.exists(path_to_file)
   
   print("opening", db_sqlite)
   #database = 'sqlite:///' + sqlite_path      
   connection = sqlite3.connect(db_sqlite)
   print("connected to", db_sqlite)
   #print("total change = ", connection.total_changes)
   return connection
"""




def drop_sqlite_table_if_exists(database, db_sqlite, drop_table): 

   print("in drop_sqlite_table_if_exists()")
   print("database = ", database)
   print("db_sqlite = ", db_sqlite)
   print("drop_table = ", drop_table)
 
   conn = sqlite3.connect(db_sqlite) 
   c = conn.cursor()
   drop_sql = "DROP TABLE IF EXISTS " + drop_table
   #drop_sql = "DROP TABLE " + drop_table
  
   c.execute(drop_sql)          
                     
   conn.commit()

   list_tables = get_database_tables(database)   
   if drop_table in list_tables:
      print()
      print("FAILURE: ", drop_table, "still in", database)
      input("WARNING")
   else:
      print()
      print("SUCCESS: ", drop_table, "not in ", database)
   
   return ""




def get_database_tables(oENGINE):  # WORKS
 
   print("in get_database_tables(oENGINE)")
   #print("database = ", database)
   #print("db_sqlite = ", db_sqlite)
   #print("drop_table = ", drop_table)
   
   #engine = create_engine(database)
   # Inspecting data
   oINSPECT = inspect(oENGINE)
   list_tables = oINSPECT.get_table_names()   # WORKS
   print("list_tables")
   print(list_tables)
   print()
   #columns = insp.get_columns('Lease')

   #print("type(columns)")
   #print(type(columns))
   #input("wait")
   return list_tables


if 1 == 2:
   cstr  = "\nGet Database Tables from millbrae_2019.sqlite"
   cstr += "\n<Y> Yes "
   cstr += "\n<N> No "  
   MENU_YN = input(cstr)
   if MENU_YN == "Y":   
      database = 'sqlite:///millbrae_2019.sqlite'
      list_tables = get_database_tables(database)  
      input("wait")
   



"""
def get_sqlite_database_info(database, db_sqlite):
    #
    #By looking at the db path it parses
    #out the tables and the number of entries
    #in each table
    #
    if not os.path.exists(db_sqlite):
      return

    size = os.stat(db_sqlite).st_size

    conn = sqlite3.connect(db_sqlite)
    c = conn.cursor()

    self = []
    
    tbl_arr = get_tbl_arr(db_sqlite)
    for tbl in tbl_arr:
      obj = sql_db_tbl(tbl)
      c = conn.cursor()
      c.execute("select count(*) from {}".format(tbl))
      obj.num_entries = c.fetchone()[0]
      self.add_tbl(obj)
    conn.close()
"""

if 1 == 2:
   cstr  = "\nGet SQLite Table Info NEW NEW NEW "
   cstr += "\n<Y> Yes "
   cstr += "\n<N> No "  
   MENU_YN = input(cstr)
   
   if MENU_YN == "Y":   
      #database = 'sqlite:///millbrae_2019.sqlite'
      db_sqlite = 'test.sqlite'
      database = 'sqlite:///' + db_sqlite
      get_sqlite_database_info(database, db_sqlite)
     





def create_sqlite_database(database, db_sqlite):  # WORKS
   conn = sqlite3.connect(db_sqlite) 
   #c = conn.cursor()
   conn.commit()   
   #df = get_database_tables(database)
   return ""

if 1 == 2:
   cstr  = "\nCreate SQLite Database test_sqlite"
   cstr += "\n<Y> Yes "
   cstr += "\n<N> No "  
   MENU_YN = input(cstr)
   if MENU_YN == "Y": 
   
      db_sqlite = 'test.sqlite'
      database = 'sqlite:///' + db_sqlite
   
      create_sqlite_database(database, db_sqlite)  
      input("wait")
   

def create_sqlite_table(database, db_sqlite, sql):   # NOT YET

   print("in create_sqlite_table()")
   print("database = ", database)
   print("db_sqlite = ", db_sqlite)
   print("sql = ", sql)
 
   conn = sqlite3.connect(db_sqlite) 
   c = conn.cursor()

   c.execute(sql)          
                     
   conn.commit()
   return ""


# 'sqlite': """CREATE TABLE iris (
#                "SepalLength" REAL,
#                "SepalWidth" REAL,
#                "PetalLength" REAL,
#                "PetalWidth" REAL,
#                "Name" TEXT
#            )""",

if 1 == 2:
   cstr  = "\nCreate SQLite Tables products and prices in test.sqlite"
   cstr += "\n<Y> Yes "
   cstr += "\n<N> No "  
   MENU_YN = input(cstr)
   if MENU_YN == "Y": 

      db_sqlite = 'test.sqlite'
      database = 'sqlite:///' + db_sqlite   
      sql = '''
            CREATE TABLE IF NOT EXISTS products
            ([product_id] INTEGER PRIMARY KEY, [product_name] TEXT)
            '''
      create_sqlite_table(database, db_sqlite, sql)
          
      sql = '''
            CREATE TABLE IF NOT EXISTS prices
            ([product_id] INTEGER PRIMARY KEY, [price] INTEGER)
            '''
     
      create_sqlite_table(database, db_sqlite, sql)
      list_tables = get_database_tables(database)
      input("wait")
   

   


# 'sqlite': """INSERT INTO iris VALUES(?, ?, ?, ?, ?)""",
def insert_or_ignore_into_sqlite_database(oENGINE, oSQLITE, sql):  # WORKS
   oSQLITE = sqlite3.connect(db_sqlite) 
   c = oSQLITE.cursor()
   #conn.commit()
   c.execute(sql)
   oSQLITE.commit()     
   #df = get_database_tables(database)
   return ""

if 1 == 2:
   cstr  = "\nInsert or Ignore into SQLite Database products and prices in test.sqlite"
   cstr += "\n<Y> Yes "
   cstr += "\n<N> No "  
   MENU_YN = input(cstr)
   if MENU_YN == "Y": 
   
      db_sqlite = 'test.sqlite'
      database = 'sqlite:///' + db_sqlite
      sql = '''
            INSERT OR IGNORE INTO products (product_id, product_name)

                VALUES
                (1,'Computer'),
                (2,'Printer'),
                (3,'Tablet'),
                (4,'Desk'),
                (5,'Chair')
             '''   
      insert_or_ignore_into_sqlite_database(database, db_sqlite, sql)
      sql = '''INSERT OR IGNORE INTO prices (product_id, price)

                VALUES
                (1,800),
                (2,200),
                (3,300),
                (4,450),
                (5,150)
          '''
      insert_or_ignore_into_sqlite_database(database, db_sqlite, sql)

      sql = """SELECT * FROM products"""
      database_to_df(database, sql)

      sql = """SELECT * FROM prices"""
      database_to_df(database, sql)   

      input("wait")





# 'sqlite': """INSERT INTO iris VALUES(?, ?, ?, ?, ?)""",
def insert_or_replace_into_sqlite_database(oENGINE, oSQLITE, db_sqlite, sql):  # WORKS
   #conn = sqlite3.connect(db_sqlite) 
   c = oSQLITE.cursor()
   #conn.commit()
   c.execute(sql)
   oSQLITE.commit()     
   #df = get_database_tables(database)
   return ""

if 1 == 2:
   cstr  = "\nInsert or Replace into SQLite Database products and prices in test.sqlite"
   cstr += "\n<Y> Yes "
   cstr += "\n<N> No "  
   MENU_YN = input(cstr)
   if MENU_YN == "Y": 
   
      db_sqlite = 'test.sqlite'
      database = 'sqlite:///' + db_sqlite
      sql = '''
            INSERT OR REPLACE INTO products (product_id, product_name)

            VALUES
            (1,'Computer aa'),
            (2,'Printer bb'),
            (3,'Tablet c'),
            (4,'Desk d'),
            (5,'Chair e'),
            (6,'Phone f')
            '''   
      insert_or_replace_into_sqlite_database(database, db_sqlite, sql)
      sql = '''INSERT OR REPLACE INTO prices (product_id, price)

                VALUES
                (1,800),
                (2,200),
                (3,300),
                (4,450),
                (5,150),
                (6,450)
          '''
      insert_or_replace_into_sqlite_database(database, db_sqlite, sql)

      sql = """SELECT * FROM products"""
      database_to_df(database, sql)

      sql = """SELECT * FROM prices"""
      database_to_df(database, sql)   

      input("wait")



   


if 1 == 2:   
   cstr  = "\nDatabase to DataFrame for test.sqlite "
   cstr += "\n<Y> Yes "
   cstr += "\n<N> No "  
   MENU_YN = input(cstr)
   if MENU_YN == "Y": 

      if 1 == 2:
         db_sqlite = 'millbrae_2019.sqlite'
         database = 'sqlite:///' + 'millbrae_2019.sqlite'
         sql = """SELECT * FROM Lease"""
         database_to_df(database, sql)
      else:
         db_sqlite = 'test.sqlite'
         database = 'sqlite:///' + db_sqlite   
         sql = """SELECT * FROM prices"""
         database_to_df(database, sql)
   
      input("wait")



# engine = create_engine("sqlite:///:memory:")

def create_empty_sqlite_table(database, db_sqlite, new_table): 

   print()
   print("in create_empty_sqlite_table()")
   print("new_table = ", new_table)
   print()
   
   import sqlalchemy
   #from sqlalchemy.ext.automap import automap_base
   #from sqlalchemy.orm import Session
   from sqlalchemy import create_engine, func, inspect 
   #Create engine 
   engine = create_engine(database)
   cnx = engine.connect()
   list_tables = get_database_tables(database)   
   if new_table in list_tables:
      print(new_table, "in", database, "before to_sql()")
      drop_sqlite_table_if_exists(database, db_sqlite, new_table)
   else:
      print(new_table, "not in", database, "before to_sql()")

   cstr = "calling df.to_sql(" + new_table + ") to create an empty table"   
   print(cstr)      

   df = pd.DataFrame()
   df["temp1"] = 1
   df["temp2"] = 2
   df["temp3"] = 3
   df["temp4"] = 4
   df["temp5"] = 5
   
   df.to_sql(new_table, cnx, if_exists='replace', index = False)  # if_exists='append'

   list_tables = get_database_tables(database)   
   if new_table in list_tables:
      print("SUCCESS: ", new_table, "in", database, "after create_empty_sqlite_table()")   
   else:
      print("FAILURE: ", new_table, "not in", database, "after create_empty_sqlite_table()")
   print()   
   #df = pd.read_sql(sql, cnx)
   #print(df.head(10))
   #print(df.dtypes)
   #input("wait")
   return ""

#engine = create_engine('sqlite:///DisasterResponse.db')
#df.to_sql('DisasterResponse', engine, index=False,if_exists='replace')
#df.to_sql('products', conn, if_exists='replace', index = False)
def df_to_database_table(oENGINE, oSQLITE, df, new_table): 

   print("in df_to_database()")
   cnx = oENGINE.connect()
   list_tables = get_database_tables(oENGINE)   
   if new_table in list_tables:
      print(new_table, "in", database, "before to_sql()")
      drop_sqlite_table_if_exists(database, db_sqlite, new_table)
   else:
      print(new_table, "not in", database, "before to_sql()")

   cstr = "calling df.to_sql(" + new_table + ")"   
   print(cstr)      

   df.to_sql(new_table, cnx, if_exists='replace', index = False)  # if_exists='append'
   list_tables = get_database_tables(oENGINE)   
   if new_table in list_tables:
      print(new_table, "in", database, "after to_sql()")   
   else:
      print(new_table, "not in", database, "after to_sql()")     
   #df = pd.read_sql(sql, cnx)
   #print(df.head(10))
   #print(df.dtypes)
   #input("wait")
   return ""


if 1 == 2:
   cstr  = "\nDataFrame To Database Table using to_sql()  (join_table in test.sqlite) "
   cstr += "\n<Y> Yes "
   cstr += "\n<N> No "  
   MENU_YN = input(cstr)
   if MENU_YN == "Y":    # Pandas requires version '1.4.0' or newer of 'sqlalchemy' (version '1.3.8' currently installed).
      #database = 'sqlite:///millbrae_2019.sqlite'
      db_sqlite = 'test.sqlite'
      database = 'sqlite:///' + db_sqlite   
      #sql = """SELECT * FROM Lease"""
      #sql = """SELECT * FROM Lease LIMIT 20"""
      #sql = """SELECT LeaseID, LeaseName FROM Lease LIMIT 20"""
      sql = '''
            SELECT
            a.product_name AS [PRODUCT NAME],
            b.price AS [PRICE]
            FROM products a
            LEFT JOIN prices b ON a.product_id = b.product_id
            '''
  
      df = database_to_df(database, sql)
      df_to_database_table(database, db_sqlite, df, "join_table") 
      df = database_to_df(database, "SELECT * FROM join_table")
   
      input("wait")
   


#INSERT INTO Table3 (A,B,C,D,E) 
#SELECT t1.A, t1.B, t1.C, t2.D, t2.E FROM Table1 t1
#INNER JOIN Table2 t2 ON t2.A = t1.A

def sql_to_new_database_table(oENGINE, oSQLITE, sql, new_table): 

   print()
   print("in sql_to_new_database_table()")
   print("sql = ", sql)   
   print("new_table = ", new_table)   
   print()
         
   #engine = create_engine(database)
   cnx = oENGINE.connect()
   list_tables = get_database_tables(oENGINE)

   drop_sqlite_table_if_exists(oENGINE, oSQLITE, new_table) 
   #create_empty_sqlite_table(database, db_sqlite, new_table) 

   #if new_table in list_tables:
   #   print(new_table, "in", database, "before sqlite sql")
   #   drop_sqlite_table_if_exists(database, db_sqlite, new_table) 
   #else:
   #   print( new_table, "not in", database, "before sqlite sql so we will create an empty one")   
   #   create_empty_sqlite_table(database, db_sqlite, new_table) 

   #new_table_sql = 'CREATE TABLE IF NOT EXISTS ' + new_table
   #create_sqlite_table(database, db_sqlite, new_table_sql)
      
   list_tables = get_database_tables(oENGINE)
   print("list_tables")
   print(list_tables)
   print()
   #temp_sql = "SELECT * FROM " + new_table
   #df = database_to_df(database, temp_sql)
   #print("df.head(30) of empty table", new_table) 
   #print(df.head(30)) 
   #print()
   #conn = sqlite3.connect(db_sqlite) 
   c = oSQLITE.cursor()
   #conn.commit()
   c.execute(sql)  # sqlite3.OperationalError: no such table: join_table
   oSQLITE.commit()       

   #df.to_sql(new_table, cnx, if_exists='replace', index = False)
   list_tables = get_database_tables(oENGINE)   
   if new_table in list_tables:
      print(new_table, "in", database, "after sqlite sql")   
   else:
      print(new_table, "not in", database, "after sqlite sql")     
   #df = pd.read_sql(sql, cnx)
   #print(df.head(10))
   #print(df.dtypes)
   #input("wait")
   return ""


if 1 == 2:
   cstr  = "\nSQL to create new table in database using SQLite "
   cstr += "\n<Y> Yes "
   cstr += "\n<N> No "  
   MENU_YN = input(cstr)
   if MENU_YN == "Y": 

      #database = 'sqlite:///millbrae_2019.sqlite'
      db_sqlite = 'test.sqlite'
      database = 'sqlite:///' + db_sqlite
      new_table = "join_table"
      #sql = """SELECT * FROM Lease"""
      #sql = """SELECT * FROM Lease LIMIT 20"""
      #sql = """SELECT LeaseID, LeaseName FROM Lease LIMIT 20"""
      if 1 == 2:  # WORKS
         sql = '''CREATE TABLE join_table AS SELECT * FROM products'''
      elif 1 == 2:  # WORKS
         sql = '''CREATE TABLE join_table AS SELECT product_name FROM products'''
      elif 1 == 1: # WORKS
         sql = '''CREATE TABLE join_table AS SELECT a.product_name, b.price FROM products a LEFT JOIN prices b ON a.product_id = b.product_id'''


      elif 1 == 2:
         sql = '''
               CREATE TABLE join_table
               SELECT
               product_name
               FROM products 
               '''
      elif 1 == 1: # WORKS but added a space after SELECT
         sql = '''
               CREATE TABLE join_table SELECT 
               a.product_name,
               b.price
               FROM products a
               LEFT JOIN prices b ON a.product_id = b.product_id
               '''      
      else:
      
         sql = '''
               CREATE TABLE join_table
               SELECT
               a.product_name AS [PRODUCT NAME],
               b.price AS [PRICE]
               FROM products a
               LEFT JOIN prices b ON a.product_id = b.product_id
               '''
  
      #df = database_to_df(database, sql)
      #df_to_database(database, df, "join_table") 
      sql_to_new_database_table(database, db_sqlite, sql, new_table) 

      df = database_to_df(database, 'SELECT * FROM join_table')
      print(df.head(30))
      input("wait")
   



# input("STOP")


  








if 1 == 2:   # WORKS list tables in SQLITE

   # Making a connection between sqlite3
   # database and Python Program
   sqliteConnection = sqlite3.connect('c:/data/millbrae_2019.sqlite')
     
   # If sqlite3 makes a connection with python
   # program then it will print "Connected to SQLite"
   # Otherwise it will show errors
   print("Connected to SQLite")
 
   # Getting all tables from sqlite_master
   sql_query = """SELECT name FROM sqlite_master
   WHERE type='table';"""
 
   # Creating cursor object using connection object
   cursor = sqliteConnection.cursor()
     
   # executing our sql query
   cursor.execute(sql_query)
   print("List of tables\n")
     
   # printing all tables list
   print(cursor.fetchall())
 
   # [('Lease',), ('LeaseCalculated',), ('LeaseCases',), ('LeaseCurveSegments',), ('LeaseEconCurves',), ('LeaseEconExpenses',),
   #('LeaseEconInterests',), ('LeaseEconInvestments',), ('LeaseEconMisc',), ('LeaseEconPrices',), ('LeaseEconRiskFactors',),
   #('LeaseEconTaxes',), ('LeaseEconWellCounts',), ('LeaseEvents',), ('LeaseGraphLabels',), ('LeaseGraphMultiCases',),
   # ('LeaseGraphMultiple',), ('LeasePressure',), ('LeaseProduction',), ('LeaseSummaries',), ('LeaseUndo',), ('LeaseVolumetrics',),
   # ('NEW_PRODUCTION',), ('ProjectCounties',), ('ProjectDepreciation',), ('ProjectEscHeader',), ('ProjectEscSegments',),
   # ('ProjectGraphCases',), ('ProjectGridCases',), ('ProjectMap',), ('ProjectOutputTree',), ('ProjectReportBooks',),
   # ('ProjectScenarios',), ('ProjectSchedules',), ('ProjectSelected',), ('ProjectSettings',), ('ProjectState',),
   # ('ProjectTreeFilter',), ('ProjectVersion',), ('Well',), ('WellCalculated',), ('WellCases',), ('WellCurveSegments',),
   # ('WellEconCurves',), ('WellEconExpenses',), ('WellEconInterests',), ('WellEconInvestments',), ('WellEconMisc',),
   # ('WellEconPrices',), ('WellEconRiskFactors',), ('WellEconTaxes',), ('WellEvents',), ('WellGraphLabels',), ('WellGraphMultiple',),
   # ('WellPressure',), ('WellProduction',), ('WellSummaries',), ('WellTest',), ('WellUndo',), ('WellVolumetrics',)]

   
   input("wait")


if 1 == 2:
  
   import sqlite3
   import pandas as pd
   # Create your connection.
   cnx = sqlite3.connect('C:/DATA/millbrae_2019.sqlite')
   if 1 == 2:   
      dat = sqlite3.connect('c:/data/millbrae.sqlite')
      query = dat.execute("SELECT * From Well")
      cols = [column[0] for column in query.description]
      df = pd.DataFrame.from_records(data = query.fetchall(), columns = cols)
   else:
      df = pd.read_sql_query("SELECT * FROM Lease", cnx)
  
   print()
   print("nRows = ", len(df))
   print()  
   print(df.dtypes)
   print()
   print(df.head(20))
   
   input("wait")
         
   

    
if 1 == 2:
   cursor.execute("PRAGMA table_info('Well')").fetchall()
   #cursor.execute(sql_query)
   print("Pragma for one table\n")
     
   # printing all tables list
   print(cursor.fetchall())


if 1 == 2:


   filename_in = "c:/DATA/millbrae_2019.mdb" # 1os.path.abspath(sys.argv[-2])
   #filename_out = "c:/DATA/millbrae_2019.sqlite" # sys.argv[-1]

   cnxn = pyodbc.connect('Driver={{Microsoft Access Driver (*.mdb, *.accdb)}};Dbq={};'.format(filename_in))

   cursor = cnxn.cursor()  # WORKS TO HERE

   #conn = sqlite3.connect(filename_out)
   #c = conn.cursor()
  
   #driver_string = "Driver={MS Access Database}"
   #driver_string = "Driver=MS Access Database"

   #driver_string = "Driver={Microsoft Access Driver (*.mdb, *.accdb)}" 
   #driver_string="DRIVER={Microsoft Access Driver (*.mdb)}"
   #file_string = "DBQ="+"millbrae_2019..mdb"
   #connection_string = ";".join([driver_string, file_string])
   #cnxn = pyodbc.connect(connection_string)
   #cursor = cnxn.cursor()
   #df = pd.read_sql("SELECT * FROM Wells", con=cnxn, index_col = ["indexCol"])
   df = pd.read_sql("SELECT * FROM wells", con=cnxn)


   
   print(df)
   input("wait")


if 1 == 2:
  
   # Connect to the database
   con = sqlite3.connect('c:/data/aquarium.db') 

   # Run SQL          
   sql_query = pd.read_sql('SELECT * from fish', con)

   # Convert SQL to DataFrame
   df = pd.DataFrame(sql_query, columns = ['course_id', 'course_name', 'fee','duration','discount'])
   print(df)

   input("stop")




if 1 == 2: # WORKS FOR MDB ##########################################################
   """ db_table_names.py -- a simple demo for ADO database table listing."""
   import sys
   import adodbapi

   try:
      databasename = "c:/DATA/millbrae_2019.mdb"
   except IndexError:
     databasename = "test.mdb"

   provider = ["prv", "Microsoft.ACE.OLEDB.12.0", "Microsoft.Jet.OLEDB.4.0"]
   constr = "Provider=%(prv)s;Data Source=%(db)s"



   # create the connection
   con = adodbapi.connect(constr, db=databasename, macro_is64bit=provider)

   print("Table names in= %s" % databasename)

   for table in con.get_table_names():
      print(table)
      
   #df = pd.read_sql_query('SELECT * FROM Lease', con=con)
   df = pd.read_sql_table('Well', con=con)
 
   print("df.dtypes")
   print(df.dtypes)
  


   input("wait")






if 1 == 2:
   import pandas_access as mdb
   import pandas as pd
   df=pd.DataFrame()
   #df = mdb.read_table("test.mdb", "MA MEMBERSHIP COMBINED CAP REPORT 2018")
   df = mdb.read_table("millbrae_2019.mdb", "[Lease]")
   print(df)
   input("STOP")






if 1 == 2:
   import pandas_access as mdb

   # Listing the tables.
   #any_mdb = "c:/data/millbrae_2019.mdb"
   any_mdb = "millbrae_2019.mdb"

   for tbl in mdb.list_tables("millbrae_2019.mdb"):
      print(tbl)
   input("wait")
    
   # Read a small table.
   df = pandas_access.read_table(any_mdb, "Lease")
   print(df)
   input("wait")

if 1 == 2:
   # Read a huge table.
   accumulator = []
   for chunk in pandas_access.read_table("my.mdb", "MyTable", chunksize=10000):
      accumulator.append(f(chunk))


















# It's remarkably hard to find such a thing, but I've built a handy Python utility to do it
# using SQLAlchemy and pandas_access, which relies on mdbtools.

#Everything you need can be acquired with:

#pip3 install sqlalchemy pandas_access
#sudo apt install mdbtools
#The code is as follows:

if 1 == 2:
  
   import pandas_access as mdb
   from sqlalchemy import create_engine
   import sys
   import os

   db_out = "test.db"   # arg 0
   mdb_in = "c:/data/millbrae_2019.mdb" # argv 1

   #if len(sys.argv)!=3:
   #  print("{0} <MDB File> <Sqlite3 File>".format(sys.argv[0]))
   #  sys.exit(-1)

   #if os.path.isfile(sys.argv[2]):
   #  print("Refusing to modify existing database!")
   #  sys.exit(-1)

   engine = create_engine('sqlite:///{0}'.format( db_out ), echo=False)
   tlist  = [tbl for tbl in mdb.list_tables( mdb_in )]
   tables = {tbl:mdb.read_table( mdb_in, tbl) for tbl in tlist}

   for k in tables:
      tables[k].to_sql(k, con=engine)

   input("stop")




if 1 == 2:

   import pandas_access as mdb

   db_filename = 'c:/data/millbrae_2019.mdb'

   # Listing the tables.
   for tbl in mdb.list_tables(db_filename):
      print(tbl)
   input("wait")  

   # Read a small table.
   df = mdb.read_table(db_filename, "Lease")

   print(df.dtypes)

   input("wait")

   input("STOP")
      





if 1 == 2:  # WORKS

   import sqlite3

   #con = sqlite3.connect(database = r'file_name.db')
   con = sqlite3.connect(database = r'aquarium.db')     # WORKS
 
   cur = con.cursor()
   cur.execute('SELECT name from sqlite_master where type="table"')
   tabl =cur.fetchall()
   print(tabl)
   input("wait")


#For using ‘pyodbc’ you must have the microsoft office/access installed in your system,
# therefore it will work on Windows only. If the office version is latest, i.e. above Office 2011 or 13,
# then make sure that the .mdb file is not of the old versions, older than 2003.

#In case of older files (97 versions) of .mdb (microsoft access files), please convert the file to the
# new version using microsoft access 2003 or 2007. The version 2003 is not quite available these days,
# hence it would become quite a problem.


if 1 == 2:
   import sqlite3

   con = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};    DBQ=millbrae_2019.mdb')
    
   cur = con.cursor()
   for row in cur.tables():
      print(row.table_name)
   input("wait")










# -*- coding: utf-8 -*-
# module : mdb_to_sqlite.py
# author : Panos Mavrogiorgos (gmail - pmav99)
# license : BSD
 
# pylint: disable= C0301
 
"""
A simple script to convert an Access database to sqlite3 database using pyodbc.
 
It just copies the tables and their data not the relationships (primary keys,
foreign keys, etc).:
 
It hasn't been thoroughly tested. Probably won't work for all the data types.
But it should serve as a basis for more complex scripts.
"""
 

if 1 == 2:
  
   import sqlite3
   import pyodbc
 
   # The path to the database files. The sqlite database
   SQL_FILE = "path\to\sqlite\database.db"
   MDB_FILE = "path\to\access\database.mdb"
 
   # pyodbc's connection string is different for python x86 and x64. Use the
   # appropriate one. More info here: http://code.google.com/p/pyodbc/issues/detail?id=203
   # The string for x86
   MDB_STRING = "DRIVER={Microsoft Access Driver (*.mdb)};DBQ=" + MDB_FILE
   # The string for x64
   #MDB_STRING = "DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=" + MDB_FILE
 
 
def convert(mdb_string, sql_file):
    """
    Converts an Access database to a SQLite database.
    """
    # Make sqlite connections
    sqlite_connection = sqlite3.connect(sql_file)
    sqlite_cursor = sqlite_connection.cursor()
 
    # Make mdb connections
    mdb_connection = pyodbc.connect(mdb_string, autocommit=False)
    mdb_cursor = mdb_connection.cursor()
    tables = [row.table_name for row in mdb_cursor.tables()]
 
    for tables in tables:
        # Access databases, have several internal tables. They all start with the
        # "MSys" prefix. If you need them, just remove the if clause.
        if not table.startswith("MSys"):
            ## Create tables
            columns = [column for column in mdb_cursor.columns(table=table)]
            s = []
            for columns in columns:
                # Quoting table names with braces.
                s.append("%s %s(%s)" % ("[" + column.column_name + "]",
                                        column.type_name,
                                        column.column_size))
            creation_string = ("CREATE TABLE [%s] (\n" % table +
                               ",\n".join(s) +
                               "\n);")
            print(creation_string, "\n")
            sqlite_cursor.execute(creation_string)
 
            ## Insert values
            # select everything from the mdb-table
            rows = [row for row in mdb_cursor.execute("SELECT * FROM [%s];" % table)]
            # Check if the table has data. If it doesn't go to the next table, else
            # insert them to the sqlite database.
            try:
                length = len(rows[0])
            except IndexError:
                pass
            
            #otherwise:
            insertion_string = "insert into [%s] values ​​" % table
            insertion_string += "(" + ", ".join(["?" for i in range(length)]) + ")"
            print(insertion_string, "\n")
            sqlite_connection.executemany(insertion_string, rows)
 
    # close databases
    sqlite_connection.commit()
    sqlite_cursor.close()
    mdb_cursor.close()
 
if 1 == 2:   
   db_out = "test.db"   # arg 0
   mdb_in = "c:/data/millbrae_2019.mdb" # argv 1
   convert(mdb_in, db_out)

   input("STOP")










