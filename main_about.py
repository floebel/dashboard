import streamlit as st
import time


def change_photo_state():
    st.session_state["photo"] = "done"
    
  
     


def main():

    if "photo" not in st.session_state:
       st.session_state["photo"] = "not done"    
    st.title("About")

    col1, col2, col3 = st.columns([1,2,1])

    col1.markdown("### Welcome to my app")
    col1.markdown("## Here is some info")

    uploaded_photo = col2.file_uploader("Upload a photo", on_change=change_photo_state)

    camera_photo = col2.camera_input("Take a photo", on_change=change_photo_state)
   
    if st.session_state["photo"] == "done":    

       progress_bar = col2.progress(0)
       for pct_completed in range(100):
          time.sleep(0.01)    
          progress_bar.progress(pct_completed+1)

       col2.success("Photo uploaded successfully")

       col3.metric(label="Temperature", value="60 deg C", delta="3 deg C")

       with st.expander("Click to read more"):
          st.write("Here are more details about this topic")
          if uploaded_photo is not None:
             st.image(uploaded_photo)
          elif camera_photo is not None:
             st.image(camera_photo)
    
    
    
    st.info(
        """
        This app is maintained by Fulton Loebel.
        """
)
