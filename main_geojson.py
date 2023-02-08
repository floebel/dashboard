
import streamlit as st
from PIL import Image
import plotly.express as px
import json
from urllib.request import urlopen
import pandas as pd

def main():

    st.title("Geojson Dashboard")
    #st.info(
    #     """
    #     This app is maintained by Fulton Loebel.
    #     """
    
    #image = Image.open("assets/monalisa-4893660_640.jpg")
    #image = Image.open("rocket.jpg")
 
    #st.image(image)
    #st.title("COVID-19 Dashboard")
    st.write("""
    This is a geojson example
    """)

# Load the GeoJSON data
@st.cache
def load_data(file_path):
    with open(file_path, "r") as file:
        return json.load(file)

# Display the data in a Streamlit app
def main():
    
   st.title("GeoJSON Example")

   if 1 == 1:
       
      df_url = 'https://raw.githubusercontent.com/plotly/datasets/master/fips-unemp-16.csv'
  
      df = pd.read_csv(df_url,
                       dtype={"fips": str})

      st.dataframe(df)

      #url = 'https://raw.githubusercontent.com/plotly/datasets/master/geojson-counties-fips.json'
   
      #with urlopen(url) as response:
      #   counties = json.load(response)

      # Load the county boundary coordinates
      map_url = 'https://raw.githubusercontent.com/plotly/datasets/master/geojson-counties-fips.json'

      with urlopen(map_url) as response:
         counties = json.load(response)

      # Build the choropleth
      fig = px.choropleth(df, 
         geojson=counties, 
         locations='fips', 
         color='unemp',
         color_continuous_scale="Viridis",
         range_color=(0, 12),
         scope="usa",
         labels={'unemp':'unemployment rate'}
      )
      fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})

      # Improve the legend
      fig.update_layout(coloraxis_colorbar=dict(
         thicknessmode="pixels", thickness=10,
         lenmode="pixels", len=150,
         yanchor="top", y=0.8,
         ticks="outside", ticksuffix=" %",
         dtick=5
      ))

      #fig.show()
      st.plotly_chart(fig)   

      
   if 1 == 2:
      fig = px.choropleth(perCountry, geojson=counties, locations='FIPS', 
                       color='Cases',
                       color_continuous_scale=px.colors.sequential.OrRd,
                       color_continuous_midpoint=2,
                       range_color=(1, 20),
                       scope="usa",
                       labels={'Cases':'Confirmed'}, 
                       hover_name = 'Province_State'
                       )
      fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
      #fig.show()
      st.plotly_chart(fig)


   
   if 1 == 2:
      fig = px.choropleth(locations=["CA","TX","NY"],\
                          locationmode="USA-states",\
                          color=[1,2,3], scope="usa")
 
      #fig.show()
      st.plotly_chart(fig)

   if 1 == 2:
      # Get the file path from the user
      #file_path = st.file_uploader("Upload a GeoJSON file", type="json")
      file_path = "USstates.geojson" 
 
      # Load the data from the file
      if file_path is not None:
         data = load_data(file_path)
         st.write("GeoJSON data:")
         #st.write(data)

         # Create a map with Plotly Express
         fig2 = px.choropleth(geojson=data, color="property1",
                              title="Map of GeoJSON data")
         #st.write(fig2)
         st.plotly_chart(fig2)
   

