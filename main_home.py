import streamlit as st
from PIL import Image

import matplotlib.pyplot as plt
import matplotlib.image as mpimg
# Read the image file
#img = mpimg.imread('image.png')

# Display the image
#plt.imshow(img)
#plt.show()
# Read the image file
#img = mpimg.imread('image.png')

# Display the image
#plt.imshow(img)
#plt.show()

def main():

    st.title("Home")
    #st.info(
    #     """
    #     This app is maintained by Fulton Loebel.
    #     """
    
    #image = Image.open("assets/monalisa-4893660_640.jpg")
    #image = Image.open("rocket.jpg")
    image = mpimg.imread('oil_well.png') 
 
    st.image(image)
    #st.title("COVID-19 Dashboard")
    st.write("""
    This is a prototype of a Streamlit web-application for the oil and gas industry.
    An SQLITE3 database contains the data which is queried into Pandas dataframes.
    This application generates multi-page dashboards. Each web page is a separate python
    application.  Pages contain interactive features that are controlled through
    Streamlit session_state variables. It has drill down capability.
    It has mapping capability.
    """)
    st.markdown("## Highlighted Features")
    st.markdown(("* Utilizes the latest Python 3 code\n"
                "* Whereas tools like Spotfire utilize Iron Python version 2.7\n"
                "* Includes connectivity to many databases, SQL, CSV or Excel files\n"
                "* Can easily incorporate regression or classification analysis\n"
                "* Can perform supervised or unsupervised learning tasks\n"
                "* Can utilize Scikit machine learning or Tensorflow Deep Learning algorithms\n"
                "* Can include explainable AI such as Shapley Values or Integrated Gradients\n"
                "* Can be deployed to Streamlit, Heroku or other platforms"))

     
    #            "* Includes mapping features\n"
    #            "* Performs hyperbolic curve fitting on well prodution data\n"
    #            "* Performs hyperbolic curve fitting on well prodution data\n"
    #            "* Generates Probit Plots\n"
            
    #st.markdown("## Vaccines")
    #st.markdown("Track [here](https://www.raps.org/news-and-articles/news-articles/2020/3/covid-19-vaccine-tracker)")
    #st.markdown("## Resources")
    #st.markdown(("* [World Health Organization](https://www.who.int/maternal_child_adolescent/links/covid19-resources-and-support-for-mncah-and-ageing/en/)\n"
    #             "* [Center for Disease Control](https://www.cdc.gov/coronavirus/2019-ncov/index.html)\n"
    #             "* [National Institute of Health](https://www.nih.gov/coronavirus)"))

