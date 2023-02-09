
import streamlit as st
import pandas as pd
#from sklearn.ensembl import RandomForestRegressor, RandomForestClassifier
#from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score



@st.cache
def load_data_once():
   csv_path = ""
   csv_name = "clean_iris.csv"
   csv_path_name = csv_path + csv_name
   df = pd.read_csv(csv_path_name, header=0)
   #st.write(df.head(10))   
   return df


def main():
   st.title("Contribute")
   st.info("Feel free to contribute to this open source project")

   header = st.container()
   dataset = st.container()
   features = st.container()
   training = st.container()
   metrics = st.container()
   
   
   with header:
      st.title("Header section")
      st.text("Text line")
    
   with dataset:
      #st.title("Dataset section")
      st.text("Dataset Section")
      df = load_data_once()
          
      st.write(df.head(10))

      #ave_sepal_length = df["Sepal_Length"].mean()
      dist_sepal_length = pd.DataFrame(df["Sepal_Length"].value_counts())
      st.subheader("Sepal Length Distribution Plot")

      if 1 == 2:  
         st.bar_chart(dist_sepal_length)
  
      list_sepal_length = df["Sepal_Length"].values.tolist()
      min_value = min(list_sepal_length)
      max_value = max(list_sepal_length)
      st.write(str(min_value))
      st.write(str(max_value))
          
 

   with features:
      #st.title("Features section")
      st.text("Features section")

      st.markdown("* **first feature** ")
      st.markdown("* **second feature** ")
      st.markdown("* **third feature was created** ")
          
  

   with training:
      #st.title("Training section")
      st.text("Training section")

      st.write("Min value", str(min_value))
      st.write("Max value", str(max_value))

      select_col, display_col = st.columns(2)

      
      
      
      value_selected = select_col.slider("What is the Sepal Length to use?", min_value=min_value, max_value=max_value, value=min_value, step=0.1)
      st.write("Current value selected from slider", str(value_selected))
       
      value_estimators = select_col.selectbox("How many estimators?", options=[50,100,150], index=0)  
      st.write("Current value of estimators is", str(value_estimators))

      list_cols = list(df.columns)
      select_col.text("The columns are")
      select_col.write(df.columns)

      default_value = ""
      target_outcome = select_col.text_input("Enter target outcome", default_value) 
      st.write("Target Outcome is", target_outcome)

     
                   
      
 
 
   with metrics:
      
      select_col, display_col = st.columns(2)
      
      #st.title("Metrics section")
      st.text("Metrics section")
      value_results = 98.5
      display_col.subheader("results are")
      display_col.write(value_results)
      #display_col.write("display col test2")





      

