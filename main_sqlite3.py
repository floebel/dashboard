

from fdl_sub_html_small import *


from sqlite3_functions import *

import streamlit as st
import sqlite3
import pandas as pd
import numpy as np
import seaborn as sns
import probscale
import matplotlib.pyplot as plt
import plotly.express as px  # pip install plotly-express

def handle_change():
   if st.session_state.state_picked:
      st.session_state.type = st.session_state.state_picked



def main():
   #st.title("Sqlite3 Test")
   #st.info(
   #    """
   #    This app is maintained by Fulton Loebel
   #    """
   #)

   any_state = "OK"
   state_picked = "OK"
   st.session_state['any_state'] = ""  # initialize          

   if len(st.session_state.any_state) == 0:
      any_title = "Select either KS (Kansas) or OK (Oklahoma) to analyze oil and gas statistics"
   else:  
      any_title = "Oil and Gas Statistics in State Of " + any_state
   #st.title(any_title)
   st.subheader(any_title)

   any_title = "Top 12 Counties for any selected state"  
   st.subheader(any_title)
   
   #any_title = "Summary Data of Lease Count By County in State of " + any_state
   #st.subheader(any_title)


   list_states = ["KS", "OK"]
   
   state_picked = st.radio("Select another state to analyze", list_states,
                           on_change=handle_change, key='state_picked')
   if state_picked:

      any_state = state_picked
      cstr = "You currently have " + state_picked + " selected (click above to change states)"
      st.write(cstr)
      
      st.session_state['any_state'] = state_picked                       
  
   #if len(st.session_state.any_state) >= 1:
   if st.session_state['any_state'] in list_states:
   
      cSQL  = "SELECT count(COUNTY) AS 'WELL COUNT', "
      cSQL += "COUNTY AS 'County', STATE AS 'State' "
      cSQL += "FROM Lease "
      cSQL += "WHERE LAT_LENGTH > 1000 AND First_Year >= 2005 "
      cSQL += "GROUP BY COUNTY ORDER BY count(COUNTY) DESC LIMIT 12" # LIMIT 20 ASC
      # LIMIT 10
   
      #with st.spinner("Loading  ..."):
      df_county_summary = df_from_sqlite(any_state, cSQL)

      #df_county_summary = database_to_df(oENGINE, cSQL)
      #df_county_summary = df_county_summary.head(20)  

      if 1 == 2:
         st.dataframe(df_county_summary)

      if 1 == 2:
         # plot the data
         fig_scatter = px.scatter(df_county_summary, x='WELL COUNT', y='County', 
                 title="MY TITLE", 
                 color="State", hover_data=["County", "State"])
         fig_scatter.update_layout(yaxis={'visible': True, 'showticklabels': True})
         fig_scatter.update_layout(xaxis={'visible': True, 'showticklabels': True})
         fig_scatter.update_traces(marker=dict(size=5, opacity=0.7, line=dict(width=1,color='DarkSlateGrey')),selector=dict(mode='markers'))
         st.plotly_chart(fig_scatter, use_container_width=True)


      # --- PLOT PIE CHART
      any_title = "Pie Chart of Top 12 Counties in " + any_state + " Measuring Horizontal Well Count"
      fig_pie_chart = px.pie(df_county_summary,
                         title=any_title,
                         values='WELL COUNT',
                         names='County')

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

      if 1 == 2: 
         fig_county_summary = px.bar(
            df_county_summary,
            x="WELL COUNT",
            #y=sales_by_product_line.index,
            y="County",
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
   




      if 1 == 2:
         #ave_sepal_length = df["Sepal_Length"].mean()
         #dist_county = pd.DataFrame(df_county["Sepal_Length"].value_counts())
         st.subheader("Wells By County Distribution Plot")
         #st.bar_chart(df_county_summary["LEASE COUNT"])
         st.bar_chart(data = df_county_summary, x="LEASE COUNT", y="County")


         st.subheader("Summary Plot of Lease Count By County")
         fig = plt.figure(figsize=(10, 4))
         sns.countplot(data = df_county_summary, y='County')
         st.pyplot(fig)


      if 1 == 2:
         df_lease = df_from_sqlite("KS", "SELECT * FROM Lease")
         df_to_webbrowser("df_lease", df_lease)
         st.dataframe(df_prod)
         list_lease = list(df_lease.columns)
         st.write(list_lease)

      if 1 == 2:
         df_prod = df_from_sqlite("KS", "SELECT * FROM LeaseProduction")
         df_to_webbrowser("df_prod", df_prod)
         st.dataframe(df_prod)
         list_prod = list(df_prod.columns)
         st.write(list_prod)

      #sql = "UPDATE citations SET first_author = ( SELECT initial_author FROM lookups WHERE lookups.pmid = citations.pmid )"    

      #cur.execute("DROP TABLE IF EXISTS citations")

      #sql_within_database(oSQLITE, sql)


      if 1 == 2:
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
     
 
         cSQL = "SELECT DISTINCT series_id, gpl FROM gsm WHERE gpl LIKE 'GPL1%' AND series_id IS NOT NULL ORDER BY gpl" #  LIMIT 500"
 
         #elif one_table == "INDEX":

         #Another way to get all indexes from a database is to query from the sqlite_master table:
         sql = "SELECT type, name, tbl_name, sql FROM sqlite_master WHERE type= 'index'"
         #print("df.head(100) of INDEXES")
         #print(df.head(100))
         #input("wait")

      if 1 == 2:  # WORKS ONE FIELD AT A TIME 
         sql = "UPDATE citations SET first_author = ( SELECT initial_author FROM lookups WHERE lookups.pmid = citations.pmid )"    
         #sql_within_database(oSQLITE, sql)

         sql = "UPDATE citations SET last_author = ( SELECT final_author FROM lookups WHERE lookups.pmid = citations.pmid )"    
         #sql_within_database(oSQLITE, sql)


      if 1 == 2:
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
         #df_all["first_author"] = ""
         #df_all["last_author"] = ""

         start_time = start_timer()
         df_all.to_sql("temp", cnx, if_exists='replace', index = False)  # if_exists='append' 'replace'   
         end_timer(start_time)

         oSQLITE.close()
         #oENGINE.close()
         print()
         print("closed connections to oSQLITE and oENGINE")
         print()


     
   
          
