
import streamlit as st

import main_home
#import main_covid_data
#import main_dashboard
#import main_contribute
#import main_about
#import main_plotly_chart1
#import main_mapping
import main_sqlite3
#import main_geojson
import main_probit
import main_lat_long
#import main_hyperbolic
import main_curve_fit


PAGES = {
    "Home": main_home,
    "Oil and Gas Statistics": main_sqlite3,
    "Hyperbolic Curve Fit": main_curve_fit,
    "Probit Analysis": main_probit,
    "Mapping Analysis": main_lat_long
    }

#    "Sqlite3": main_sqlite3,
#    "Plotly_Chart1": main_plotly_chart1,
#    "Contribute": main_contribute,
#   "About": main_about,
#    "Dashboard": main_dashboard,
#    "Covid Data": main_covid_data,
#    "Mapping": main_mapping,
#    "Hyperbolic Curve Fit": main_hyperbolic,
#    "GeoJson": main_geojson,


def main():
    #st.sidebar.title("Menu")
    st.sidebar.subheader("Menu")
    choice = st.sidebar.radio("Navigate", list(PAGES.keys()))
    PAGES[choice].main()
    st.sidebar.subheader("About")
    st.sidebar.info(
        """
        This app is maintained by Fulton Loebel
        """
    )
    st.sidebar.subheader("Contact Information")
    st.sidebar.info("Email fulton.loebel@gmail.com for further info.")
    
if __name__ == "__main__":
    main()


    
