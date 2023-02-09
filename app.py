
import streamlit as st

import main_home
#import main_covid_data
#import main_dashboard
import main_contribute
import main_about
import main_plotly_chart1
#import main_mapping
import main_sqlite3
import main_geojson
import main_probit
import main_lat_long



PAGES = {
    "Home": main_home,
    "About": main_about,
    "Contribute": main_contribute,
    "Plotly_Chart1": main_plotly_chart1,
    "Sqlite3": main_sqlite3,
    "Probit": main_probit,
    "GeoJson": main_geojson,
    "Lat Long Maps": main_lat_long
    }

#    "Dashboard": main_dashboard,
#    "Covid Data": main_covid_data,
#    "Mapping": main_mapping,


def main():
    st.sidebar.title("Menu")
    choice = st.sidebar.radio("Navigate", list(PAGES.keys()))
    PAGES[choice].main()
    st.sidebar.title("About")
    st.sidebar.info(
        """
        This app is maintained by Fulton Loebel
        """
    )
    st.sidebar.title("Contribute")
    st.sidebar.info("Feel free to contribute to this open source project.")
    
if __name__ == "__main__":
    main()


    
