
import streamlit as st
#import src.pages.home
#import src.pages.data
#import src.pages.dashboard
#import src.pages.contribute
#import src.pages.about
#import src.pages.plotly_chart1
#import src.pages.mapping

import main_home
import main_data
import main_dashboard
import main_contribute
import main_about
import main_plotly_chart1
import main_mapping
import main_sqlite3

PAGES = {
    "Home": main_home,
    "Data": main_data,
    "Dashboard": main_dashboard,
    "About": main_about,
    "Contribute": main_contribute,
    "Plotly_Chart1": main_plotly_chart1,
    "Mapping": main_mapping,
    "Sqlite3": main_sqlite3
    
 
}

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


    
