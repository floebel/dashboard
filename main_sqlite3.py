

from fdl_sub_html_small import *


from sqlite3_functions import *

import streamlit as st
import sqlite3
import pandas as pd
import seaborn as sns
import probscale
from scipy.stats import norm
import matplotlib.pyplot as plt
import plotly.express as px  # pip install plotly-express



def main():
   st.title("Sqlite3 Test")
   #st.info(
   #    """
   #    This app is maintained by Fulton Loebel
   #    """
   #)
   
   # oENGINE, oSQLITE = open_sqlite_conn(database, db_sqlite)

   db_sqlite = 'hz_kansas.sqlite'
   #db_sqlite = 'hz_oklahoma.sqlite'
  
   database = 'sqlite:///' + db_sqlite   
   oENGINE, oSQLITE = open_sqlite_conn(database, db_sqlite)
   list_tables = get_database_tables(oENGINE)
   st.write(list_tables)

  
   st.subheader("Summary Data of Lease Count By County")
   cSQL  = "SELECT count(COUNTY) AS 'LEASE COUNT', COUNTY, STATE FROM Lease "
   cSQL += "GROUP BY COUNTY ORDER BY count(COUNTY) DESC" # LIMIT 20 ASC
   # LIMIT 10
   
   #with st.spinner("Loading  ..."):
   
   df_county_summary = database_to_df(oENGINE, cSQL)
   #df_county_summary = df_county_summary.head(20)  
   st.dataframe(df_county_summary)

   # plot the data
   fig_scatter = px.scatter(df_county_summary, x='LEASE COUNT', y='COUNTY', 
           title="MY TITLE", 
           color="STATE", hover_data=["COUNTY", "STATE"])
   fig_scatter.update_layout(yaxis={'visible': True, 'showticklabels': True})
   fig_scatter.update_layout(xaxis={'visible': True, 'showticklabels': True})
   fig_scatter.update_traces(marker=dict(size=5, opacity=0.7, line=dict(width=1,color='DarkSlateGrey')),selector=dict(mode='markers'))
   st.plotly_chart(fig_scatter, use_container_width=True)




   # --- PLOT PIE CHART
   fig_pie_chart = px.pie(df_county_summary,
                      title='Pie Chart of Wells Per County',
                      values='LEASE COUNT',
                      names='COUNTY')

   #st.plotly_chart(fig_pie_chart)
   st.plotly_chart(fig_pie_chart, use_container_width=True)

   #if 1 == 1:   # aggregate sales by product lines, starting point for bar chart 

   # SALES BY PRODUCT LINE [BAR CHART]
   # 'Product line' is the .index
   # 'Total' is a column
   #sales_by_product_line = (
   #   df_selection.groupby(by=["Product line"]).sum()[["Total"]].sort_values(by="Total")
   #)

   # create bar chart
   # orientation = 'h' for horizontal bar chart
   fig_county_summary = px.bar(
      df_county_summary,
      x="LEASE COUNT",
      #y=sales_by_product_line.index,
      y="COUNTY",
      orientation="h",
      title="<b>Well Counts By County</b>",
      color_discrete_sequence=["#0083B8"] * len(df_county_summary),
      template="plotly_white",
   )


   # remove background color
   # remove gridlines
   fig_county_summary.update_layout(
      plot_bgcolor="rgba(0,0,0,0)",
      xaxis=(dict(showgrid=False))
   )
   
   st.plotly_chart(fig_county_summary)
   




   
   #ave_sepal_length = df["Sepal_Length"].mean()
   #dist_county = pd.DataFrame(df_county["Sepal_Length"].value_counts())
   st.subheader("Wells By County Distribution Plot")
   #st.bar_chart(df_county_summary["LEASE COUNT"])
   st.bar_chart(data = df_county_summary, x="LEASE COUNT", y="COUNTY")



   st.subheader("Summary Plot of Lease Count By County")
   fig = plt.figure(figsize=(10, 4))
   sns.countplot(data = df_county_summary, y='COUNTY')
   st.pyplot(fig)


   if 1 == 2:
      df_lease = database_to_df(oENGINE, "SELECT * FROM Lease")
      df_to_webbrowser("df_lease", df_lease)
      st.dataframe(df_prod)
      list_lease = list(df_lease.columns)
      st.write(list_lease)

   if 1 == 2:
      df_prod = database_to_df(oENGINE, "SELECT * FROM LeaseProduction")
      df_to_webbrowser("df_prod", df_prod)
      st.dataframe(df_prod)
      list_prod = list(df_prod.columns)
      st.write(list_prod)

   #sql = "UPDATE citations SET first_author = ( SELECT initial_author FROM lookups WHERE lookups.pmid = citations.pmid )"    

   #cur.execute("DROP TABLE IF EXISTS citations")

   #sql_within_database(oSQLITE, sql)


   if 1 == 2:
      df = database_to_df(oENGINE, "SELECT * FROM articles")
      get_sqlite_table_info(oENGINE, oSQLITE)

      cSQL  = "SELECT gsm, series_id, gpl, description, title, source_name_ch1 "
      cSQL += "FROM gsm "
      cSQL += "WHERE organism_ch1 = 'Homo sapiens' "
      cSQL += "AND description NOT LIKE '%https%' "
      cSQL += "AND description NOT LIKE 'Gene expression%' "
      cSQL += "AND description NOT LIKE 'Gene_expression%' "
      cSQL += "AND description NOT LIKE 'The collected%' "

      cSQL += "AND title NOT LIKE 'PLACENTA%' "
 
      cSQL += "AND type = 'RNA' " 
      cSQL += "AND gpl LIKE 'GPL1%' AND series_id IS NOT NULL " 
      cSQL += "AND description IS NOT NULL AND title IS NOT NULL "
      cSQL += "AND source_name_ch1 IS NOT NULL "  
      cSQL += "ORDER BY series_id, gsm LIMIT 100000 "
     
 
      df = database_to_df(oENGINE, cSQL)

      cSQL = "SELECT DISTINCT series_id, gpl FROM gsm WHERE gpl LIKE 'GPL1%' AND series_id IS NOT NULL ORDER BY gpl" #  LIMIT 500"
 
      df = database_to_df(oENGINE, cSQL)
      create_pubmed_articles_table(oSQLITE)
      create_pubmed_citations_table(oSQLITE)

      #elif one_table == "INDEX":

      #Another way to get all indexes from a database is to query from the sqlite_master table:
      sql = "SELECT type, name, tbl_name, sql FROM sqlite_master WHERE type= 'index'"
      df = database_to_df(oENGINE, sql)
      #print("df.head(100) of INDEXES")
      #print(df.head(100))
      #input("wait")

   if 1 == 2:  # WORKS ONE FIELD AT A TIME 
      sql = "UPDATE citations SET first_author = ( SELECT initial_author FROM lookups WHERE lookups.pmid = citations.pmid )"    
      sql_within_database(oSQLITE, sql)

      sql = "UPDATE citations SET last_author = ( SELECT final_author FROM lookups WHERE lookups.pmid = citations.pmid )"    
      sql_within_database(oSQLITE, sql)


   if 1 == 2:
      df = database_to_df(oENGINE, "SELECT * FROM citations WHERE first_author IS NOT NULL and last_author IS NOT NULL ORDER BY pmid, citationid")
      print("df.head(100) of citations sorted by pmid, citationid ")
      print(df.head(100))
      input("wait")
      #elif one_table == "TEMP":
                         
      #sql = "INSERT OR IGNORE INTO articles SELECT pmid, pmcid, title, year, journal, xml_file, doi, abstract FROM temp" 
      sql = "INSERT OR REPLACE INTO articles SELECT pmid, pmcid, title, year, journal, xml_file, doi, abstract FROM temp" 

      print("insert or replace records from temp table to articles table")
      start_time = start_timer()
      sql_within_database(oSQLITE, sql)
      end_timer(start_time)
 
      #elif one_table == "articles":

      print("rows = ", len(df_all), "before dropping duplicates")
      start_time = start_timer()
      df_all = df_all.drop_duplicates(subset=['pmid'], keep="first")
      end_timer(start_time)
   
      print("rows = ", len(df_all), "after dropping duplicates")
   

   if 1 == 2:
      cnx = oENGINE.connect()

      print("appending", len(df_all),"records to temp table")

      #df_all["first_author"] = ""
      #df_all["last_author"] = ""

      start_time = start_timer()
      df_all.to_sql("temp", cnx, if_exists='replace', index = False)  # if_exists='append' 'replace'   
      end_timer(start_time)

      get_sqlite_database_info(oENGINE, oSQLITE)
      end_timer(start_time)


      oSQLITE.close()
      #oENGINE.close()
      print()
      print("closed connections to oSQLITE and oENGINE")
      print()


     
   if 1 == 2:

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

          
   #from flask import Flask
   #from flask_sqlite3 import SQLite3

   #app = Flask(__name__)
   #app.config['SQLITE3_DATABASE_URI'] = 'sqlite:///test.db'
   #db = SQLite3(app)



   
