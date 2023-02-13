

from fdl_sub_html_small import *

from sqlite3_functions import *

import streamlit as st
import sqlite3
import pandas as pd
import numpy as np
#import seaborn as sns
import plotly.express as px
#import probscale
#from scipy.stats import norm
import matplotlib.pyplot as plt

import leafmap.foliumap as leafmap
#import leafmap.kepler as leafmap
#import folium


def fig_area(string_list):
   from geojson_utils import area
   #box_str = string_list  # '{"type": "Polygon","coordinates": [[ [0, 0], [10, 0], [10, 10], [0, 10] ]]}'
   box_str = '{"type": "Polygon","coordinates": ' + string_list + '}' 
   box = json.loads(box_str)
   #self.assertEqual(area(box), 100)
   area = area(box)
   area = abs(area)   # because negative lat/long values..   
   #cstr = "area = " + str(area) 
   #print(cstr)
   return area



def fig_centroid(string_list):
   from geojson_utils import centroid
   #box_str = '{"type": "Polygon","coordinates": [[ [0, 0], [10, 0], [10, 10], [0, 10] ]]}'
   box_str = '{"type": "Polygon","coordinates": ' + string_list + '}'  
   box = json.loads(box_str)
   dict_centroid = centroid(box)
   #print(dict_centroid)

   list_centroid = list(dict_centroid.values())
   #print(list_centroid)
   if list_centroid[0] == "Point":
      list_lat_long = list_centroid[1]
   elif list_centroid[1] == "Point":
      list_lat_long = list_centroid[0]
   #print(list_lat_long)
   return list_lat_long   # return a list





# Step 1: Create a mapping between the ID of a shape to a color
dict_id2color = { '10002': 'green',
   '10003': 'green',
   '10009': 'yellow',
   '10011': 'red',
   '10012': 'yellow',
   '10013': 'green',
   '10014': 'red',
   '11211': 'red',
   '11222': 'yellow'}

def state_style_function(feature):
   return {
   'fillcolor': 'black',  # fill color     
   'color': 'black',      # line color
   'weight': 4,          # line width
   'opacity': 0.2,       # line opacity
   'fillOpacity': 0.01   # fill color opacity
   }

def county_style_function(feature):
   return {
   'fillcolor': 'purple',  # fill color     
   'color': 'purple',      # line color
   'weight': 3,          # line width
   'opacity': 0.30,       # line opacity
   'fillOpacity': 0.01   # fill color opacity
   }

def township_style_function(feature):
   return {
   'fillcolor': 'black',  # fill color     
   'color': 'black',      # line color
   'weight': 1.5,          # line width
   'opacity': 0.4,       # line opacity
   'fillOpacity': 0.01   # fill color opacity
   }

def section_style_function(feature):
   return {
   'fillcolor': 'red',  # fill color     
   'color': 'red',      # line color
   'weight': 0.50,          # line width
   'opacity': 0.5,       # line opacity
   'fillOpacity': 0.01   # fill color opacity
   }

def pipeline_style_function(feature):
   return {
   'fillcolor': 'green', # fill color     
   'color': 'green',     # line color
   'weight': 2,          # line width
   'opacity': 0.5,       # line opacity
   'fillOpacity': 0.01   # fill color opacity
   }

def shale_style_function(feature):
   return {
   'fillcolor': 'gray', # fill color     
   'color': 'gray',     # line color
   'weight': 3,          # line width
   'opacity': 0.5,       # line opacity
   'fillOpacity': 0.20   # fill color opacity
   }


# ======= highlight_function ============
def state_highlight_function(feature):
   return {
   'fillColor': 'black',  # fill color
   'color': 'black',      # line color
   'weight': 3,           # line width
   'dashArray': '0, 0', 
   'opacity': 0.7,        # line opacity
   'fillOpacity': 0.11   # fill color opacity
   }

# ======= highlight_function ============
def county_highlight_function(feature):
   return {
   'fillColor': 'purple',  # fill color
   'color': 'purple',      # line color
   'weight': 3,           # line width
   'dashArray': '0, 0', 
   'opacity': 0.7,        # line opacity
   'fillOpacity': 0.11   # fill color opacity
   }

# ======= highlight_function ============
def township_highlight_function(feature):
   return {
   'fillColor': 'black',  # fill color
   'color': 'black',      # line color
   'weight': 1.5,           # line width
   'dashArray': '0, 0', 
   'opacity': 0.7,        # line opacity
   'fillOpacity': 0.04   # fill color opacity
   }

# ======= highlight_function ============
def section_highlight_function(feature):
   return {
   'fillColor': 'red',  # fill color
   'color': 'red',      # line color
   'weight': 1,           # line width
   'dashArray': '0, 0', 
   'opacity': 0.7,        # line opacity
   'fillOpacity': 0.04   # fill color opacity
   }

# ======= highlight_function ============
def my_highlight_function(feature):
   return {
   'fillColor': dict_id2color[feature['id']],
   'color': 'white',
   'weight': 3,
   'dashArray': '0, 0',
   'opacity': 1.,
   'fillOpacity': 1.  
   }



# elif substr(choice,1,9) == "CGR_TRAIN":
def substr(any_string, start, length):   # ONE BASED ...
   
   any_substr = any_string[start-1:start+length-1]
   #Alert(any_substr)
   return any_substr



def circle_dist(lat1, lng1, lat2, lng2):
    """
    Distance on a circle (in km)

    Parameters
    ----------
    lat1, lng1, lat2, lng2: float or array of float

    Returns
    -------
    distance:
      distance from ``(lat1, lng1)`` to ``(lat2, lng2)`` in kilometers.
    """
    phi1 = np.deg2rad(90 - lat1)
    phi2 = np.deg2rad(90 - lat2)

    theta1 = np.deg2rad(lng1)
    theta2 = np.deg2rad(lng2)

    cos = (np.sin(phi1) * np.sin(phi2) * np.cos(theta1 - theta2) +
           np.cos(phi1) * np.cos(phi2))
    arc = np.arccos(cos)
    return arc * 6373  # Earth radius in km


     
# ['red', 'blue', 'green', 'purple', 'orange', 'darkred',
#             'lightred', 'beige', 'darkblue', 'darkgreen', 'cadetblue', 
#             'darkpurple', 'white', 'pink', 'lightblue', 'lightgreen',
#             'gray', 'black', 'lightgray']




def fig_color(value):
    if value >= 8000:
        return 'orange'
    elif 6000 <= value <= 8000:
        return 'red'
    elif 4000 <= value <= 6000:
        return 'purple'
    elif 2000 <= value <= 4000:
        return 'blue'      
    else:
        return 'green'
      

def main():

   import folium
   from folium import FeatureGroup, LayerControl, Map, Marker
   from folium.plugins import MarkerCluster
   import json
   import area
   import math

   
   #import pandas as pd
   #import streamlit as st
   from streamlit_folium import st_folium
      
   st.title("Mapping Lateral Lengths")
   #st.info(
   #    """
   #    This app is maintained by Fulton Loebel
   #    """
   #)

   cSQL  = "SELECT LeaseID, LeaseName, SurfaceLatitude AS 'SurfLat', SurfaceLongitude AS 'SurfLong', "
   cSQL += "BottomLatitude AS 'BotLat', BottomLongitude AS 'BotLong', OPERATOR AS 'Operator', "
   cSQL += "LAT_LENGTH AS 'Lateral_Length', "
   cSQL += "Reservoir, COUNTY AS 'County', STATE AS 'State' "
   cSQL += "FROM Lease "
   cSQL += "WHERE LAT_LENGTH > 1000.0 "
 
   # LIMIT 10
   any_state = "OK"
   df_map = df_from_sqlite(any_state, cSQL)
   #df_map.insert(2, 'Lateral_Length', df_map.apply(lambda row: fig_lat_length(row), axis=1))  
   #df_map = df_map.query('Lateral_Length > 1000.0')  

   st.subheader("Latitude Longitude Mapping Analysis")
   if 1 == 1:
      st.dataframe(df_map)
      
   
   center_lat  = df_map.SurfLat.mean()
   center_long = df_map.SurfLong.mean()
   
   INIT_COORDINATES = ( df_map.SurfLat.mean(), df_map.SurfLong.mean() )



   if 1 == 1:    # works
      my_map = folium.Map(location=INIT_COORDINATES, tiles = "Stamen Terrain", zoom_start = 8)
      geo_json = folium.GeoJson("us_counties_5m.geojson",
                 style_function= county_style_function)
      my_map.add_child(geo_json) 
   elif 1 == 2: #   elif county_code == "US":
      my_map = folium.Map(location=INIT_COORDINATES, tiles = "Stamen Terrain", zoom_start = 10)
      geo_json = folium.GeoJson("us_counties_5m.geojson", 
                 style_function= county_style_function,
                 highlight_function=county_highlight_function)
      # Note that this is the same as geojson.add_to(map)
      my_map.add_child(geo_json, name='county layer')  
   elif 1 == 1: # FULTECH_OR_TOP == "TOP":
      my_map = folium.Map(location=INIT_COORDINATES, tiles = "Stamen Terrain", zoom_start = 10)
      geo_json4 = folium.GeoJson("KANSAS_TOWNSHIPS.geojson", style_function= township_style_function, highlight_function=township_highlight_function)
      #geo_json4 = folium.GeoJson("KANSAS_TOWNSHIPS.geojson", style_function= township_style_function) 
      my_map.add_child(geo_json4, name='township layer')   # Note that this is the same as geojson.add_to(map)
         
  

   elif 1 == 1:
      
      #INIT_COORDINATES = (36.99015, -97.03633)

      my_map = folium.Map(location=INIT_COORDINATES, tiles = "Stamen Terrain", zoom_start = 10)
      geo_json = open("kansas_counties.geojson", "r", encoding="utf-8-sig")
      my_map.add_child(folium.GeoJson(data=geo_json.read()))
      my_map.add_child(folium.LayerControl()) 

      #my_map.to_streamlit(height=700)
      #events = st_folium(my_map)  # WORKS 
      #st.write(events)
 
  
   elif 1 == 2:
      np_lat  = df_lat_long[df_lat_long["State"] == "KS"].SurfLat.values  #[0]
      np_long = df_lat_long[df_lat_long["State"] == "KS"].SurfLong.values #[0]

      #m = folium.Map(location=[np_lat, np_long])
      my_map = leafmap.Map(center = [center_lat, center_long], tiles="stamentoner", zoom=2)
      #m = leafmap.Map(center = [50,110], zoom=4)

      #my_map.to_streamlit(height=700)


   elif 1 == 1:
  

      #df_folium = df_lat_long.copy()
      #trees_df = trees_df.head(n=100)

      lat_avg = df_map["SurfLat"].mean()
      lon_avg = df_map["SurfLong"].mean()
      value = df_map["Lateral_Length"]
      my_map = folium.Map(location=[lat_avg, lon_avg], zoom_start=12)

      #fg = folium.FeatureGroup(name="My Map")    


   if 1 == 1:

      my_legend_html = '''
<style>
.legend {
  background-color: white;
  padding: 10px;
  border: 2px solid gray;
  border-radius: 5px;
  font-size: 12px;
}
.legend i {
  display: inline-block;
  width: 20px;
  height: 20px;
  margin-right: 10px;
}
.bold {
  font-weight: bold;
}
.title {
  font-size: 16px;
  font-weight: bold;
  margin-bottom: 10px;
}
</style>
<div class="legend">

  <div class="title">Legend for Horizontal Well Lateral Length Map</div>
  <span class="bold"><i style="background-color: orange"></i>Lateral Length >= 8000 feet</span>
  <br>
  <span class="bold"><i style="background-color: red"></i>6000 <= Lateral Length <= 8000 feet</span>
  <br>
  <span class="bold"><i style="background-color: purple"></i>4000 <= Lateral Length <= 6000 feet</span>
  <br>
  <span class="bold"><i style="background-color: blue"></i>2000 <= Lateral Length <= 4000 feet</span>
  <br>
  <span class="bold"><i style="background-color: green"></i>Lateral Length <= 2000 feet</span>
  <br>
 </div>
'''



      # Add the legend to the app
      st.write(my_legend_html, unsafe_allow_html=True)
      st.write('<br><br>', unsafe_allow_html=True)



   elif 1 == 1:  # add legend to map

      my_legend_html = """
      <div style=
      "position: fixed;background-color: rgba(255, 255, 255, 0.5); border-radius: 5px;
      bottom: 50px; left: 10px; width: 200px; height: 280px; border:2px solid grey; z-index:9999; font-size:14px;
      ">
      <p style="text-align:center;"> <b> Cleveland Legend </b> </p>
      <p style="margin-left:5px"> <i class="fa fa-square fa-1x" style="margin-right:5px;color:green;"></i> Oil Cumulative </p>
      <p style="margin-left:5px"> <i class="fa fa-square fa-1x" style="margin-right:5px;color:red;"></i> Gas Cumulative </p>
      <p style="margin-left:5px"> <i class="fa fa-square fa-1x" style="margin-right:5px; color:blue;"></i> Oil and Gas Cumulative </p>
      <p style="margin-left:5px"> <i class="fa fa-square fa-1x" style="margin-right:5px; color:purple;"></i> Cleveland Net Pay </p>
      <p style="margin-left:5px"> <i class="fa fa-square fa-1x" style="margin-right:5px; color:black;"></i> TIF Without Net Pay </p>
      <p style="margin-left:5px"> <i class="fa fa-square fa-1x" style="margin-right:5px; color:brown;"></i> LAS (2000-2019) </p>
      <p style="margin-left:5px"> <i class="fa fa-square fa-1x" style="margin-right:5px; color:orange;"></i> LAS (1980=1999) </p>
      <p style="margin-left:5px"> <i class="fa fa-square fa-1x" style="margin-right:5px; color:yellow;"></i> LAS (Pre 1980) </p>
      </div>
      """
      st.write(my_legend_html, unsafe_allow_html=True)
 
   elif 1 == 2:
      
      my_legend_html = '''
        <div style="position: fixed; 
        bottom: 50px; left: 50px; width: 100px; height: 90px; 
        border:2px solid grey; z-index:9999; font-size:14px;
        ">&nbsp; Cool Legend <br>
            &nbsp; East &nbsp; <i class="fa fa-map-marker fa-2x"
                 style="color:green"></i><br>
            &nbsp; West &nbsp; <i class="fa fa-map-marker fa-2x"
                 style="color:red"></i>
        </div>
        '''
      my_legend_layer = folium.Element(my_legend_html)
      # Add the legend to the map
      #my_map.get_root().html.add_child(folium.Element(my_legend_layer))
      #my_map.get_root().html.add_child(folium.Element(my_legend_layer))
      #                ).add_to(my_map)

     
 
   if 1 == 1: # now add markers to my_map
      
      for index, row in df_map.iterrows():
         lat = row["SurfLat"]
         long = row["SurfLong"]
         value = row["Lateral_Length"]
         color = fig_color(value)
         folium.CircleMarker(
                       location = [lat, long],\
                       radius = 0.5,
                       color = color,
                       fill = True,
                       fill_color = color,
                       fill_opacity=0.99,  
                       #popup=str(value)+" meters",\
                       #icon=folium.Icon(color=color_producer(value))  
                       ).add_to(my_map)






      #looks for objects added to map, only one child and folium will treat this together
      #m.add_child(folium.LayerControl()) 
      folium.LayerControl().add_to(my_map)
      events = st_folium(my_map)
      #st.write(events)





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

   

   elif 1 == 2: # WORKS
      st.title("Heatmap") 
      filepath = "https://raw.githubusercontent.com/giswqs/leafmap/master/examples/data/us_cities.csv"
      my_map = leafmap.Map(tiles="stamentoner")
      my_map.add_heatmap(
          filepath,
          latitude="latitude",
          longitude="longitude",
          value="pop_max",
          name="Heat map",
          radius=20,
          )
      my_map.to_streamlit(height=700)





   elif 1 == 2:
      #center_lat = state_wise_census.mean().Latitude
      #center_long = state_wise_census.mean().Longitude
      my_map = leafmap.Map(center = [center_lat, center_long], zoom=4)
      in_geojson = "KANSAS_COUNTIES.geojson"
      #in_geojson = 'https://raw.githubusercontent.com/giswqs/leafmap/master/examples/data/us_states.json'
      
      #in_geojson = "USstates.geojson"
      #in_geojson = 'https://raw.githubusercontent.com/giswqs/leafmap/master/examples/data/cable_geo.geojson'
      my_map.add_geojson(in_geojson, layer_name = "Kansas Counties")
      my_map.to_streamlit(height=700)
   

   if 1 == 2:
      import geopandas as gpd
      gdf = gpd.read_file("https://raw.githubusercontent.com/giswqs/leafmap/master/examples/data/world_cities.geojson")
      my_map = leafmap.Map(center=[20, 0], zoom=1)
      my_map.add_gdf(gdf, "World cities")


   if 1 == 2:
      #df_map = df_lat_long.copy()
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

      fig_map = px.scatter(df_map, x="SurfLat", y="SurfLong", color="County")
      st.plotly_chart(fig_map)
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



   
