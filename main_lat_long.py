

from fdl_sub_html_small import *

from sqlite3_functions import *

import streamlit as st
import sqlite3
import pandas as pd
#import seaborn as sns
import plotly.express as px
#import probscale
#from scipy.stats import norm
import matplotlib.pyplot as plt

import leafmap.foliumap as leafmap
#import leafmap.kepler as leafmap
#import folium


def main():
   st.title("Lat Long Plots etc")
   #st.info(
   #    """
   #    This app is maintained by Fulton Loebel
   #    """
   #)
   if 1 == 2:

      import geopandas as gpd
      df = gpd.read_file('KANSAS_COUNTIES.geojson')
      #df_to_webbrowser("df", df)
      #input("WAIT")
      #df['lon'] = df.geometry.x  # extract longitude from geometry
      #df['lat'] = df.geometry.y  # extract latitude from geometry
      #df = df[['lon','lat']]     # only keep longitude and latitude
      #st.write(df.head())        # show on table for testing only
      st.map(df)                  # show on map

   
   # oENGINE, oSQLITE = open_sqlite_conn(database, db_sqlite)

   #db_sqlite = 'hz_kansas.sqlite'
   #db_sqlite = 'hz_oklahoma.sqlite'
  
   #database = 'sqlite:///' + db_sqlite   
   #oENGINE, oSQLITE = open_sqlite_conn(database, db_sqlite)
   #list_tables = get_database_tables(oENGINE)
   #if 1 == 2:
   #   st.write(list_tables)

   if 1 == 2:
      st.subheader("Lateral Length Analysis")

   cSQL  = "SELECT LeaseID, LeaseName, SurfaceLatitude AS 'SurfLat', SurfaceLongitude AS 'SurfLong', "
   cSQL += "BottomLatitude AS 'BotLat', BottomLongitude AS 'BotLong', OPERATOR AS 'Operator', "
   cSQL += "Reservoir, COUNTY AS 'County', STATE AS 'State' "
   cSQL += "FROM Lease"
 
   # LIMIT 10 
   df_lat_long = df_from_sqlite("KS", cSQL)
   df_lat_long.insert(2, 'Lateral_Length', df_lat_long.apply(lambda row: fig_lat_length(row), axis=1))  
   df_lat_long = df_lat_long.query('Lateral_Length > 1000.0')  

   

   st.subheader("Latitude Longitude Analysis")
   if 1 == 1:
      st.dataframe(df_lat_long)


   center_lat  = df_lat_long.SurfLat.mean()
   center_long = df_lat_long.SurfLong.mean()

   if 1 == 2:
      np_lat  = df_lat_long[df_lat_long["State"] == "KS"].SurfLat.values  #[0]
      np_long = df_lat_long[df_lat_long["State"] == "KS"].SurfLong.values #[0]

      #m = folium.Map(location=[np_lat, np_long])
      m = leafmap.Map(center = [center_lat, center_long], tiles="stamentoner", zoom=2)
      #m = leafmap.Map(center = [50,110], zoom=4)

      m.to_streamlit(height=700)


   if 1 == 1:
      

      import folium
      #import pandas as pd
      #import streamlit as st
      from streamlit_folium import st_folium

      st.title("Using Folium Library")

      df_folium = df_lat_long.copy()
      #trees_df = trees_df.head(n=100)

      lat_avg = df_folium["SurfLat"].mean()
      lon_avg = df_folium["SurfLong"].mean()
      m = folium.Map(location=[lat_avg, lon_avg], zoom_start=12)

      for index, row in df_folium.iterrows():
         folium.Marker(
             [row["SurfLat"], row["SurfLong"]],
         ).add_to(m)

      events = st_folium(m)
      #st.write(events)





   if 1 == 2: # WORKS
      st.title("Heatmap") 
      filepath = "https://raw.githubusercontent.com/giswqs/leafmap/master/examples/data/us_cities.csv"
      m = leafmap.Map(tiles="stamentoner")
      m.add_heatmap(
          filepath,
          latitude="latitude",
          longitude="longitude",
          value="pop_max",
          name="Heat map",
          radius=20,
          )
      m.to_streamlit(height=700)





   if 1 == 1:
      #center_lat = state_wise_census.mean().Latitude
      #center_long = state_wise_census.mean().Longitude
      m = leafmap.Map(center = [center_lat, center_long], zoom=4)
      in_geojson = "KANSAS_COUNTIES.geojson"
      #in_geojson = 'https://raw.githubusercontent.com/giswqs/leafmap/master/examples/data/us_states.json'
      
      #in_geojson = "USstates.geojson"
      #in_geojson = 'https://raw.githubusercontent.com/giswqs/leafmap/master/examples/data/cable_geo.geojson'
      m.add_geojson(in_geojson, layer_name = "Kansas Counties")
      m.to_streamlit(height=700)
   

   if 1 == 2:
      import geopandas as gpd
      gdf = gpd.read_file("https://raw.githubusercontent.com/giswqs/leafmap/master/examples/data/world_cities.geojson")
      m = leafmap.Map(center=[20, 0], zoom=1)
      m.add_gdf(gdf, "World cities")


   if 1 == 2:
      df_map = df_lat_long.copy()
      #df_to_webbrowser("df_map", df_map)
      list_include = ["SurfLat", "SurfLong"]
      df_map = df_map[list_include]
      pd_rename(df_map, "SurfLat", "lat")
      pd_rename(df_map, "SurfLong", "lon")
      #df = df[['lon','lat']]     # only keep longitude and latitude
      #st.write(df.head())        # show on table for testing only
      st.map(df_map)                  # show on map



   if 1 == 2:
      #np_lat_long_all = df_lat_long["Lateral_Length"].values
      st.subheader("Lat Long Analysis By County")

      fig_lat_long = px.scatter(df_lat_long, x="SurfLat", y="SurfLong", color="County")
      st.plotly_chart(fig_lat_long)
      #selected_point = plotly_events(fig, click_event=True)
      #if len(selected_point) == 0:
      #   st.stop()



   #df_morrow = df_lat_long.copy()
   #df_morrow = df_morrow.query('Reservoir == "MORROW"')  
   #list_morrow_include = ["Reservoir", "Lateral_Length"]
   #df_morrow = df_lat_long[list_morrow_include]
 
   #np_lat_long_morrow = df_morrow["Lateral_Length"].values

   #list_morrow_include = ["Reservoir", "Lateral_Length"]
   #df_morrow = df_lat_long[list_morrow_include]
   #np_lat_long_morrow = df_morrow["Lateral_Length"].values  
 
  

   if 1 == 2:
      
      # Set up the figure using matplotlib.pyplot
      fig, ax = plt.subplots(figsize=(12,6))

      # Plot and configure the first sample
      probscale.probplot(np_lat_long_all,
                   probax='y',
                   bestfit=True,
                   datascale='log',
                   label='Lateral Length All Kansas', # for the legend
                   ax=ax,
                   color='red'
                   )

      # Plot and configure the second sample
      probscale.probplot(np_lat_long_morrow,
                   probax='y',
                   bestfit=True,
                   datascale='log',
                   label='Lateral Length Morrow Reservoir',
                   ax=ax,
                   color='blue'
                   )

      # Select the ticks to label
      ax.set_yticks([1, 2, 5, 10, 20, 30, 40, 50, 60, 70, 80, 90, 95, 98, 99])

      # Reverse the tick labels for the convention where P10 is the 90th percentile
      ax.set_yticklabels(100 - ax.get_yticks())

      # Add and annotate the P10, P50, and P90 lines
      ax.axhline(90, color='k', linewidth=.5)
      ax.axhline(50, color='k', linewidth=.5)
      ax.axhline(10, color='k', linewidth=.5)

      ax.annotate('P10', xy=(.9, .78), xycoords='axes fraction', fontsize=16)
      ax.annotate('P50', xy=(.9, .51), xycoords='axes fraction', fontsize=16)
      ax.annotate('P90', xy=(.9, .23), xycoords='axes fraction', fontsize=16)

      # Add the title, axis labels, and the legend
      ax.set_title('Probit Plot', fontsize=16)
      ax.set_ylabel('Exceedance Probability')
      ax.set_xlabel('Data Values')
      ax.legend()

      sns.despine()
      st.pyplot(fig)

      

   if 1 == 2:
      # Generate 20 random numbers from the normal distribution
      data = norm.rvs(size=20)
      st.subheader("Probit Plot")
      fig = plt.figure(figsize=(10, 4))
      plt.title("Probit Plot", fontsize = 12)
      #fig.ylabel('y label')
      #fig.xlabel('x label')
   
      probscale.probplot(data, probax='y')
      sns.despine()
      st.pyplot(fig)
   
   if 1 == 2:
      st.subheader("Summary Data of Lease Count By County")
      cSQL  = "SELECT count(COUNTY) AS 'LEASE COUNT', COUNTY, STATE FROM Lease "
      cSQL += "GROUP BY COUNTY ORDER BY count(COUNTY) DESC"
      # LIMIT 10 
      df_county_summary = database_to_df(oENGINE, cSQL)
      st.dataframe(df_county_summary)


      st.subheader("Summary Plot of Lease Count By County")
      fig = plt.figure(figsize=(10, 4))
      sns.countplot(data = df_county_summary, y='COUNTY')
      st.pyplot(fig)



   #sql = "UPDATE citations SET first_author = ( SELECT initial_author FROM lookups WHERE lookups.pmid = citations.pmid )"    

   #cur.execute("DROP TABLE IF EXISTS citations")

   #sql_within_database(oSQLITE, sql)


          
   #from flask import Flask
   #from flask_sqlite3 import SQLite3

   #app = Flask(__name__)
   #app.config['SQLITE3_DATABASE_URI'] = 'sqlite:///test.db'
   #db = SQLite3(app)



   
