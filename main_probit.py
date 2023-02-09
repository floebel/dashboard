


from fdl_sub_html_small import *

from sqlite3_functions import *

import streamlit as st
import sqlite3
import pandas as pd
import numpy as np
import seaborn as sns
import probscale
#from scipy.stats import norm
import matplotlib.pyplot as plt



def main():
   st.title("Probit Plots")
   #st.info(
   #    """
   #    This app is maintained by Fulton Loebel
   #    """
   #)


   

   # 	 //		   	cSelect += " (SELECT COUNT(*) FROM LeaseProduction P WHERE P.LeaseID = L.LeaseID) AS [PROD_PTS], "       // not working ............
   #cSelect += " (SELECT COUNT(*) FROM LeaseProduction P WHERE P.LeaseID = L.LeaseID AND ( P.Oil > 0 OR P.Gas > 0 ) ) AS [PROD_PTS], "   # not working ............
   #    cSelect += "L.FirstProdDate AS [FIRST_DATE], (L.LastProdDate) AS [LAST_DATE], "



   if 1 == 2:
      st.subheader("Lateral Length Analysis")

   cSQL  = "SELECT API, LeaseID, LeaseName, SurfaceLatitude AS 'SurfLat', SurfaceLongitude AS 'SurfLong', "
   cSQL += "BottomLatitude AS 'BotLat', BottomLongitude AS 'BotLong', OPERATOR AS 'Operator', "
   cSQL += "Reservoir "
   cSQL += "FROM Lease"
 
   # LIMIT 10 
   df_lat_long = df_from_sqlite("OK", cSQL)
   df_lat_long.insert(2, 'Lateral_Length', df_lat_long.apply(lambda row: fig_lat_length(row), axis=1))  
   df_lat_long = df_lat_long.query('Lateral_Length > 1000.0')  

   np_lat_long_all = df_lat_long["Lateral_Length"].values

   
   df_morrow = df_lat_long.copy()
   df_morrow = df_morrow.query('Reservoir == "WOODFORD"')  # WOODFORD
   #list_morrow_include = ["Reservoir", "Lateral_Length"]
   #df_morrow = df_lat_long[list_morrow_include]
 
   np_lat_long_morrow = df_morrow["Lateral_Length"].values

   #list_morrow_include = ["Reservoir", "Lateral_Length"]
   #df_morrow = df_lat_long[list_morrow_include]
   #np_lat_long_morrow = df_morrow["Lateral_Length"].values  
 
   st.subheader("Lateral Length Table")
  


   if 1 == 1:
      
      # Set up the figure using matplotlib.pyplot
      fig, ax = plt.subplots(figsize=(12,6))

      # Plot and configure the first sample
      probscale.probplot(np_lat_long_all,
                   probax='y',
                   bestfit=True,
                   datascale='log',
                   label='Lateral Length All Oklahoma', # for the legend
                   ax=ax,
                   color='red'
                   )

      # Plot and configure the second sample
      probscale.probplot(np_lat_long_morrow,
                   probax='y',
                   bestfit=True,
                   datascale='log',
                   label='Lateral Length Woodford Reservoir',
                   ax=ax,
                   color='blue'
                   )

      # Select the ticks to label

      if 1 == 2: 
         ax.set_yticks([1, 2, 5, 10, 20, 30, 40, 50, 60, 70, 80, 90, 95, 98, 99])
      else:
         ax.set_yticks([0.10, 0.20, 0.5, 1, 2, 5, 10, 20, 30, 40, 50, 60, 70, 80, 90, 95, 98, 99])
 

      # Reverse the tick labels for the convention where P10 is the 90th percentile
      ax.set_yticklabels(100 - ax.get_yticks())

      ax.set_xticks([1000, 1500, 2000, 2500, 3000, 4000, 5000, 6000, 7000, 8000, 10000])
      ax.set_xticklabels(ax.get_xticks())


      if 1 == 1:
         # Add and annotate the P10, P50, and P90 lines
         ax.axhline(90, color='k', linewidth=.5)
         ax.axhline(50, color='k', linewidth=.5)
         ax.axhline(10, color='k', linewidth=.5)

         ax.annotate('P10', xy=(.9, .78), xycoords='axes fraction', fontsize=16)
         ax.annotate('P50', xy=(.9, .51), xycoords='axes fraction', fontsize=16)
         ax.annotate('P90', xy=(.9, .23), xycoords='axes fraction', fontsize=16)

      # Add the title, axis labels, and the legend
      ax.set_title('Probit Plot', fontsize=16, fontweight='bold')
      ax.set_ylabel('Exceedance Probability', fontsize=12, fontweight='bold')
      ax.set_xlabel('Lateral Length of Horizontal Wells', fontsize=12, fontweight='bold')


      ax.xaxis.grid(True, which='major')
      ax.yaxis.grid(False, which='major')
      
      ax.legend()

      #sns.despine()
      st.pyplot(fig)

      

   #if 1 == 2:
   #   # Generate 20 random numbers from the normal distribution
   #   data = norm.rvs(size=20)
   #   st.subheader("Probit Plot")
   #   fig = plt.figure(figsize=(10, 4))
   #   plt.title("Probit Plot", fontsize = 12)
   #   #fig.ylabel('y label')
   #   #fig.xlabel('x label')
   
   #   probscale.probplot(data, probax='y')
   #   sns.despine()
   #   st.pyplot(fig)
   
   if 1 == 2:
      st.subheader("Summary Data of Lease Count By County")
      cSQL  = "SELECT count(COUNTY) AS 'LEASE COUNT', COUNTY, STATE FROM Lease "
      cSQL += "GROUP BY COUNTY ORDER BY count(COUNTY) DESC"
      # LIMIT 10
      df_county_summary = df_from_sqlite("KS", cSQL)
      st.dataframe(df_county_summary)


      st.subheader("Summary Plot of Lease Count By County")
      fig = plt.figure(figsize=(10, 4))
      sns.countplot(data = df_county_summary, y='COUNTY')
      st.pyplot(fig)


   if 1 == 2:
      df_lease = df_from_sqlite("KS","SELECT * FROM Lease")
      df_to_webbrowser("df_lease", df_lease)
      st.dataframe(df_prod)
      list_lease = list(df_lease.columns)
      st.write(list_lease)

   if 1 == 2:
      df_prod = df_from_sqlite("KS","SELECT * FROM LeaseProduction")
      df_to_webbrowser("df_prod", df_prod)
      st.dataframe(df_prod)
      list_prod = list(df_prod.columns)
      st.write(list_prod)

          
   #from flask import Flask
   #from flask_sqlite3 import SQLite3

   #app = Flask(__name__)
   #app.config['SQLITE3_DATABASE_URI'] = 'sqlite:///test.db'
   #db = SQLite3(app)



   
