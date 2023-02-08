
print("starting fdl_sub_html_small.py")


import pandas as pd
import numpy as np
import webbrowser
import os
import shutil
from shutil import copyfile

import datetime

import re
import time
import csv
import os
import sys
#import math
import numpy as np
#import seaborn as sns
# sns.set(style="ticks", color_codes=True)
# plt.style.use('seaborn')
#cmap = 'tab10'
#sns.set_style("white")

#sns.set_style('whitegrid')
# Save a palette to a variable:
#palette = sns.color_palette("bright")

#sns.color_palette("bright")

#current_palette = sns.color_palette()
#sns.palplot(current_palette)
#sns.set_palette("bright")
#sns.color_palette(palette = None, n_colors = None, desat = None)

import os

# from glob import glob        # FIX see IMAGE MAIN ..
import glob

dpi_image = 300 # 200  # 300


from itertools import islice


import random

if sys.version_info[0] >= 3:
    unicode = str


def substr(any_string, start, length):   # ONE BASED ...
   
   any_substr = any_string[start-1:start+length-1]
   #input(any_substr)
   return any_substr



def Replace(any_before, any_find, any_replace):  # VB6  # also in fdl_sub_utilities.py
   
   any_after = any_before.replace(any_find, any_replace, 999)
   return any_after


def fig_very_unique_string():
    
   #print("entered fig_unique_string() in fdl_sub_display.py") 

   unique_string = str(datetime.datetime.now().date()) + '_' + str(datetime.datetime.now().time()).replace(':', '_')
   unique_string = Replace(unique_string, "-", "_")
   unique_string = Replace(unique_string, ".", "_")
   nLength = len(unique_string)
   #unique_string = substr(unique_string, 6, nLength - 5)    # 11_10_09_23_26_903301
   unique_string = substr(unique_string, 12, nLength - 11)  #       09_21_23_333714
   #unique_string = substr(unique_string, 12, nLength - 18)   #       09_27_37        HH_MM_SS

   #os.environ["HH_MM_SS"] = unique_string
   #print("set os.environ['HH_MM_SS'] to " + unique_string) 
   #print(unique_string + " leaving fig_unique_string() in fdl_sub_display.py") 

   return unique_string




def df_to_html(file_title, df):

   if 1 == 2:  
      print("file_title = ", file_title)

     
   html_header = "<results-display>"
   html_header += "<br />"     # line break
   html_header += "<hr />"      # horizontal rule
   html_header += "<br 1>"      # line break
   if len(file_title) <= 120:
      html_header += "<h3 align='center'>" + file_title + "</h3>"
   else:
      html_header += "<h3 align='left'>" + file_title + "</h3>"
       
   #html_header += "<br />"     # line break
   #html_header += "<hr />"     # horizontal rule
   html_header += "<br />"     # line break
   html_header += "<hr />"     # horizontal rule
   html_header += "<br />"     # line break
   html_header += "</results-display>"

   try:
      nRows = len(df)
   except:
      html_from_df = "No rows in table"
      html_from_df = '<strong><span style="color:black">' + html_from_df + '</span></strong>'  
      return html_from_df

   if len(df) == 0:
      html_from_df = "No rows in table"
      html_from_df = '<strong><span style="color:black">' + html_from_df + '</span></strong>'
   else:
      my_index = False
      # Add some bootstrap styling to <table>
      # return df.to_html(classes="table table-striped")
      # OUTPUT AN HTML FILE
      #with open('myhtml.html', 'w') as f:
      pd.set_option('colheader_justify', 'center')   # FOR TABLE <th>

      html_string = '''
      <html>
        <head><title>HTML Pandas Dataframe with CSS</title></head>
        <link rel="stylesheet" type="text/css" href="df_style.css"/>
        <body>
          {table}
        </body>
      </html>.
      '''

   #list_df_cols = df.columns.tolist()

   nRows = len(df)

   #print(nRows, "nRows for webbrowser")

   print()
   
   list_cols = list(df.columns)   
   nCols = len(list_cols)

   #print(nCols, "nCols for webbrowser")

   #np_cols = df.columns.values
   #list_cols = np_cols.tolist()
   rows_cols_title = ""
   if 1 == 1:
      RANDOM_SHUFFLE_Y_N = "N"   # FIX TEMPORARY
   elif nRows <= 100:
      RANDOM_SHUFFLE_Y_N = "N"
   elif "df_github" in file_path:
      RANDOM_SHUFFLE_Y_N = "N"
   elif "df_url" in file_path:
      RANDOM_SHUFFLE_Y_N = "N"
   elif "df_txt" in file_path:
      RANDOM_SHUFFLE_Y_N = "N"
   elif "df_csv" in file_path:
      RANDOM_SHUFFLE_Y_N = "N"
   elif "Regex" in file_path:
      RANDOM_SHUFFLE_Y_N = "N"        
   else:
      RANDOM_SHUFFLE_Y_N = "Y"   
      rows_cols_title += "Rows are randomly shuffled "
   rows_cols_title += "There are " + str(len(df)) + " rows " 
   rows_cols_title += "There are " + str(len(list_cols)) + " columns "
        
   #print()
   #print("there are", nCols, "nCols")
   #print("there are", nRows, "nRows")
   #print()      
   #cstr  = "\nFilter on just the first 200 columns "
   #cstr += "\n<Y> Yes "
   #cstr += "\n<N> No  "
   #PICK_YN = input(cstr)

   #print("nRows", nRows)
   #print("nCols", nCols)
   
   if nCols <= 5 and nRows <= 50000:
      fdl = 1
      #print("lets display all columns")
      #df = df.iloc[:,0:400]
      #rows_cols_title += "Only displaying first 400 columns "
      #print("Only displaying first 400 columns in webbrowser")    
   elif nCols <= 30 and nRows <= 5000:
      fdl = 1
      #print("lets display all columns")
      #df = df.iloc[:,0:10000]
      #rows_cols_title += "Only displaying first 400 columns "
      #print("Only displaying first 400 columns in webbrowser")   
    
   elif "xxxxxTransposed" in file_title:
      fdl = 1
   elif "xxxxxImportant" in file_title:
      fdl = 1     
   elif nCols > 400:
      df = df.iloc[:,0:400]
      rows_cols_title += "Only displaying first 400 columns "
      #print("Only displaying first 400 columns in webbrowser")
      #print(df.dtypes)
   else:
      rows_cols_title += "Displaying all " + str(nCols) + " columns "  
      #print("All", nCols, "columns will be displayed in webbrowser")    
      
   #print()
   if RANDOM_SHUFFLE_Y_N == "Y":
      #   print()
      #   print("before random shuffle dimension of data dimensions : {}".format(df.shape)) 
      #   #shuffle_fraction_string = input("Enter fraction of data to keep : <0.25> for FANNIE_MAE *** " )
      #   shuffle_fraction_string = input("Enter fraction of data to keep, i.e. <0.25>, <0.50>, <1> " )
      # 
      shuffle_fraction = 1.0
      df = df.sample(frac=shuffle_fraction)  # random shuffle and keep part of the data
      nRows = len(df)

   if nCols <= 5 and nRows <= 30000:
      fdl = 1
      #print("lets display it all")
   elif nCols <= 30 and nRows <= 10000:
      fdl = 1
      #print("lets display first 10000 rows")
      #df = df.head(10000)
      #rows_cols_title += "Only displaying first 10000 rows "
      #print("Only displaying first 10000 rows in webbrowser")
        
   #elif "Transposed" in file_title:
   #   fdl = 1
   #elif "Important" in file_title:
   #   fdl = 1         
   elif nRows > 500:
      df = df.head(500)
      rows_cols_title += "Only displaying first 500 rows "
      #print("Only displaying first 500 rows in webbrowser")
   #cstr  = "\n<Y> Yes ... Random Shuffle And Filter On Fraction Of Data "
   #cstr += "\n<N> No .... No Random Shuffling and Keep All Of  The Data "   
   #RANDOM_SHUFFLE_Y_N = input(cstr)
  
      #   print(len(df), "df rows after random shufflng")
      #   print()
      #
      #   nRows = len(df)
      #  
      #   list_col_names = list(df.columns.values)   
      #   nCols = len(list_col_names)
   
      #   # FIX list_categorical_columns is meaningless now since they are now encoded
      #   print("there are", nCols, "nCols")
      #   print("there are", nRows, "nRows")

  

   if len(df) == 0:
      rows_cols_title = ""
   else:   
      fdl = 1

   html_rows_cols = "<h4 align='left'>" + rows_cols_title + "</h4>"

   if len(df) == 0:
      html_from_df = ""
   else:

      list_df_cols = list(df.columns.values)

      next_col = "Topic and Accomplishments"
      if next_col in list_df_cols:
         df[next_col] = df.apply(lambda row: Fig_Bold(row, next_col), axis=1)

      next_col = "Accomplishments"
      if next_col in list_df_cols:
         df[next_col] = df.apply(lambda row: Fig_Bold(row, next_col), axis=1)

      next_col = "Goals"
      if next_col in list_df_cols:
         df[next_col] = df.apply(lambda row: Fig_Bold(row, next_col), axis=1)
                                                           
      next_col = "data_row_count"
      if next_col in list_df_cols:
         df[next_col] = df.apply(lambda row: Fig_Yellow_Background(row, next_col), axis=1)
               
      next_col = "VALUE"
      if next_col in list_df_cols:
         df[next_col] = df.apply(lambda row: Fig_Bold(row, next_col), axis=1)
            
      next_col = "ID"  # FIX NOT WORKING
      if next_col in list_df_cols:
         df[next_col] = df.apply(lambda row: Fig_Orange_Background(row, next_col), axis=1)
      next_col = "ID_REF"
      if next_col in list_df_cols:
         df[next_col] = df.apply(lambda row: Fig_Orange_Background(row, next_col), axis=1)

      
      next_col = "ENTREZ_GENE_ID"
      if next_col in list_df_cols:
         df[next_col] = df.apply(lambda row: Fig_Green_Background(row, next_col), axis=1)
      next_col = "Gene Symbol"
      if next_col in list_df_cols:
         df[next_col] = df.apply(lambda row: Fig_Green_Background(row, next_col), axis=1)
                                 
      next_col = "geo_accession"
      if next_col in list_df_cols:
         df[next_col] = df.apply(lambda row: Fig_Red_Background(row, next_col), axis=1)
             
      next_col = "series_id"
      if next_col in list_df_cols:
         df[next_col] = df.apply(lambda row: Fig_Red_Background(row, next_col), axis=1)
                  
      next_col = "platform_id"
      if next_col in list_df_cols:
         df[next_col] = df.apply(lambda row: Fig_Red_Background(row, next_col), axis=1)

      next_col = "pubmed_id"
      if next_col in list_df_cols:
         df[next_col] = df.apply(lambda row: Fig_Red_Background(row, next_col), axis=1)
                                      
      next_col = "title"
      if next_col in list_df_cols:
         df[next_col] = df.apply(lambda row: Fig_Blue_Background(row, next_col), axis=1)

      if 1 == 2:
         print(file_title)
         print()
      
      if 1 == 2: # input("Display with GREENS Heatmap <Y> or <N> ") == "Y":
         html_from_df = css_include()

         #df = df.style.background_gradient(cmap='Greens', axis=1)
         list_cols = list(df.columns)
         first_col = list_cols[0]
         df= df.set_index(first_col)  # remove index 
         #KeyError: '`Styler.apply` and `.applymap` are not compatible with non-unique index or columns.'

         #df.drop("Key", inplace=True)
         html_from_df += df.style.background_gradient(cmap='Greens',axis=1).to_html()   
                         
      elif "Goals" in list_df_cols:
         #list_cols = list(df.columns)
         #first_col = list_cols[0]
         #df= df.set_index(first_col)  # remove index 
          
         html_from_df = css_include()
         html_from_df += df.to_html(col_space="200px", index=False,\
                                    justify="left", show_dimensions=False, \
                                    bold_rows=True, border=True,\
                                    render_links=True, escape=False)   

            
      elif 1 == 1:
         html_from_df = css_include()

         #pd.set_option('display.float_format', lambda x: '%.9f' % x)
         #pd.set_option('display.float_format', lambda x: '%.5f' % x)     
        
         html_from_df += df.to_html(index=True, justify="left", show_dimensions=False, \
                                    bold_rows=True, border=True, render_links=True, escape=False)   
              
      elif 1 ==  1:
         html_from_df = css_include()

         html_from_df += df.to_html(index=True, justify="center", show_dimensions=False, \
                                    bold_rows=True, border=True, render_links=True, escape=False)   
      elif 1 ==  2:
         html_from_df = html_string.format(table=df.to_html(classes='mystyle'))
      else:
         #notebook=False, border=None, table_id=None, render_links=False, encoding=None)  
         html_from_df = df.to_html(classes="table table-striped", index=my_index, \
                                   justify="center", show_dimensions=False, \
                                   bold_rows=True, border=True, render_links=True, escape=False)   
   
   html_phone = '<meta name="format-detection" content="telephone=no">'
      
   
   html_combined = html_rows_cols + html_phone + html_header + html_from_df 

   return html_combined
  




def df_to_webbrowser(any_title, df_maybe):

   import pandas
   import numpy
   #print("title", title)

   #if "TRANSPOSE_SPLIT" in title:
   #   input("WAIT TRANSPOSE_SPLIT in df_to_webbrowser")

   #print(type(df_maybe))
   #<class 'pandas.core.frame.DataFrame'>
  
   if isinstance(df_maybe, list):
      df = pd.DataFrame()
      df["List"] = df_maybe
      title = "LIST<BR>" + any_title
      
   elif isinstance(df_maybe, dict):
      df = pd.DataFrame([df_maybe])
      title = "DICTIONARY<BR>" + any_title
 
   elif isinstance(df_maybe, np.ndarray):
      df = pd.DataFrame(df_maybe)
      str_shape = str(df_maybe.shape)
      title  = "NUMPY ARRAY<BR>" + str_shape
      title += "<BR>" + any_title
  
   elif isinstance(df_maybe, pandas.core.series.Series):
      df = pd.DataFrame()
      list_series = df_maybe.tolist()
      df["Series"] = list_series
      title = "PANDAS SERIES<BR>" + any_title    

   else:
      df = df_maybe.copy()
      title = "DATA FRAME<BR>" + any_title
        

   if any_title == "xxxx df_txt":  
      print("df.dtypes")
      print(df.dtypes)
      #input("wait line 693 df_to_webbrowser BEFORE df_to_html")  # OK here


      
   
   html = df_to_html(title, df)  # see fdl_sub_html_custom.py

   unique_string = fig_very_unique_string()

   html_file = "c:/temp_html/" + unique_string + ".HTML" 
   #html_file = unique_string + ".HTML"
   #html_file = title + ".HTML"

   if 1 == 2:
      print("html_file", html_file)
    
   text_to_txt_file(html, "", html_file)   # FDL convert html string to html txt file
   if 1 == 2:
      print("created ", html_file)

   #input("wait line 308 in fdl_sub_html.py")
   
   #filename = 'file:///'+os.getcwd()+'/' + html_file    # FDL need a generic folder and filename 
   filename = html_file
   webbrowser.open_new_tab(filename)    

   if 1 == 2:
      input("wait in df_to_webbrowser() in fdl_sub_html.py")
   
  


def Fig_Colorize_Text(any_color, any_text):
   #any_outcome_value = row[outcome_name]
   #any_rank_value = row[rank_name]
   #html_replace = "<h1 style='color: red; text-align: center'>CI</h1>"
   #any_pre = '<span style="font-weight:bold;text-align: center">'   # DID NOT CENTER


   if any_color == "BLUE":
      #any_pre = '<span style="background-color:lightgreen;font-weight:bold">'
      #any_pre = '<span style="font-weight:bold">'
      any_pre = '<span style="color:blue">'
      #any_pre = '<span style="color:green">'
  
      #any_pre = '<font color="green"> Welcome to freeCodeCamp. </font> 
      any_post = '</span>'
   elif any_color == "RED":
      #any_pre = '<span style="background-color:lightgreen;font-weight:bold">'
      #any_pre = '<span style="font-weight:bold">'
      any_pre = '<span style="color:red">'
      #any_pre = '<span style="color:green">'
  
      #any_pre = '<font color="green"> Welcome to freeCodeCamp. </font> 
      any_post = '</span>'    
   #elif any_outcome_value >= 330:
   #   any_pre = '<span style="background-color:lightgreen;font-weight:bold">'
   #   any_post = '</span>'
   #elif any_outcome_value >= 165:
   #   any_pre = '<span style="background-color:yellow;font-weight:bold">'
   #   any_post = '</span>'
   #elif any_outcome_value >= 0:
   #   any_pre = '<span style="background-color:pink;font-weight:bold">'
   #   any_post = '</span>'
          
   any_replace = any_pre + any_text + any_post 
   if 1 == 2:
      any_outcome_string = Replace(str(any_outcome_value), str(any_outcome_value), any_replace)
   return any_replace   # any_outcome_string


#df[next_col] = df.apply(lambda row: Fig_Blue_Background(row, next_col), axis=1)
def Fig_Blue_Background(row, one_column):
   any_one_column = row[one_column]
   #any_rank_value = row[rank_name]
   any_pre = '<span style="background-color:lightblue;font-weight:bold">'
   any_post = '</span>'
             
   any_replace = any_pre + str(any_one_column) + any_post 
   any_output_string = Replace(str(any_one_column), str(any_one_column), any_replace)
   return any_output_string

#df[next_col] = df.apply(lambda row: Fig_Blue_Background(row, next_col), axis=1)
def Fig_Red_Background(row, one_column):
   any_one_column = row[one_column]
   #any_rank_value = row[rank_name]
   any_pre = '<span style="background-color:pink;font-weight:bold">'
   any_post = '</span>'
             
   any_replace = any_pre + str(any_one_column) + any_post 
   any_output_string = Replace(str(any_one_column), str(any_one_column), any_replace)
   return any_output_string

#df[next_col] = df.apply(lambda row: Fig_Blue_Background(row, next_col), axis=1)
def Fig_Green_Background(row, one_column):
   any_one_column = row[one_column]
   #any_rank_value = row[rank_name]
   any_pre = '<span style="background-color:lightgreen;font-weight:bold">'
   any_post = '</span>'
             
   any_replace = any_pre + str(any_one_column) + any_post 
   any_output_string = Replace(str(any_one_column), str(any_one_column), any_replace)
   return any_output_string

#df[next_col] = df.apply(lambda row: Fig_Blue_Background(row, next_col), axis=1)
def Fig_Yellow_Background(row, one_column):
   any_one_column = row[one_column]
   #any_rank_value = row[rank_name]
   any_pre = '<span style="background-color:yellow;font-weight:bold">'
   any_post = '</span>'
             
   any_replace = any_pre + str(any_one_column) + any_post 
   any_output_string = Replace(str(any_one_column), str(any_one_column), any_replace)
   return any_output_string

#df[next_col] = df.apply(lambda row: Fig_Blue_Background(row, next_col), axis=1)
def Fig_Orange_Background(row, one_column):
   any_one_column = row[one_column]
   #any_rank_value = row[rank_name]
   any_pre = '<span style="background-color:lightorange;font-weight:bold">'
   any_post = '</span>'
             
   any_replace = any_pre + str(any_one_column) + any_post 
   any_output_string = Replace(str(any_one_column), str(any_one_column), any_replace)
   return any_output_string
  
def Fig_Outcome_Color(row, outcome_name):
   any_outcome_value = row[outcome_name]
   #any_rank_value = row[rank_name]
   if any_outcome_value >= 330:
      any_pre = '<span style="background-color:lightgreen;font-weight:bold">'
      any_post = '</span>'
   elif any_outcome_value >= 165:
      any_pre = '<span style="background-color:yellow;font-weight:bold">'
      any_post = '</span>'
   elif any_outcome_value >= 0:
      any_pre = '<span style="background-color:pink;font-weight:bold">'
      any_post = '</span>'
          
   any_replace = any_pre + str(round(any_outcome_value,1)) + any_post 
   any_outcome_string = Replace(str(any_outcome_value), str(any_outcome_value), any_replace)
   return any_outcome_string

def Fig_Bold(row, bold_name):
   any_bold_string = row[bold_name]
   any_bold_string = str(any_bold_string)

   #html_replace = "<h1 style='color: red; text-align: center'>CI</h1>"
   #any_pre = '<span style="font-weight:bold;text-align: center">'   # DID NOT CENTER
   any_pre = '<span style="font-weight:bold">'
   any_post = '</span>'
        
   any_replace = any_pre + any_bold_string + any_post 
   any_result_string = Replace(any_bold_string, any_bold_string, any_replace)
   return any_result_string







# used by fdl_sub_process_statistic1.py and fdl_sub_process_statistic2.py
def Fig_Pattern_Color(row, pattern_name):  

   any_pattern_name = row[pattern_name]
   if len(any_pattern_name) == 0:
      return any_pattern_name
     
   if pattern_name == "zzzzzzURL_Pattern":
      any_pre = '<a>'
      any_post = '</a>'   
      #any_pre = '<span style="background-color:yellow;font-weight:bold">'
      #any_post = '</span>'
   elif pattern_name == "PAIRS_Pattern":
      any_replace = '<strong><span style="color:blue;text-align:left;">' + any_pattern_name + '</span></strong>'

   elif pattern_name == "FIND_Pattern":
      any_replace = '<strong><span style="color:purple;text-align:left;">' + any_pattern_name + '</span></strong>'

   elif pattern_name == "BIOID_Pattern":
      any_replace = '<strong><span style="color:brown;text-align:left;">' + any_pattern_name + '</span></strong>'

   elif pattern_name == "URL_Pattern":
      any_replace = '<strong><span style="color:blue;text-align:left;">' + any_pattern_name + '</span></strong>'
   elif pattern_name == "EMAIL_Pattern":
      any_replace = '<strong><span style="color:green;text-align:left;">' + any_pattern_name + '</span></strong>'
  
   else:
      #any_pre = '<font color="red">' + one_item + '</font>'
      #any_replace = '<strong><span style="color:red;text-align:left;">' + any_pattern_name + '</span></strong>'
      any_replace = '<strong><span style="color:blue;text-align:left;">' + any_pattern_name + '</span></strong>'
      #any_replace = '<strong>' + any_pattern_name + '</strong>'
 
      #any_pre = '<span style="background-color:yellow;font-weight:bold">'
      #any_post = '</span>'    
   #anydef Replace(any_before, any_find, any_replace):  # VB6
    
   #any_after = any_before.replace(any_find, any_replace, 999999)
   #any_after = any_after.replace(
   #return any_after

   any_return = Replace(any_pattern_name, any_pattern_name, any_replace)
   any_return = Replace(any_return, "\n", " ")  # remove CRLFs
 
   return any_return

  

   
def text_to_txt_file(text, any_file_path, any_file_name):   # FDL ########
          
   full_txt_path = any_file_path + any_file_name    
   #file = open(full_txt_path, "a", encoding="utf-8")   # FDL
   file = open(full_txt_path, "w", encoding="utf-8")   # FDL
 
   file.write(text)                   # FDL
   file.close()                       # FDL    



def css_include():

   html  = '<pdf-display>'
   html += '<style type="text/css">'
   html += '@media print{'
   html += ' .no-print{'
   html += '  display: none;'
   html += ' }'
   html += ' .bgcol{'
   html += '  background-color: #999;'
   html += ' }'
   html += ' body{'
   html += ' padding-top: 1px;'
   html += ' background: transparent;'
   html += ' }'
   html += '}'
   html += '</style>'
   html += "</pdf-display>"
 
   """
   html  = ""
   html += 'html {'
   html += 'background-color: #333;'
   html += 'margin: 0px;'
   html += 'padding: 0px;'
   html += '}'
   html += 'body {'
   html += 'font-size:12px;'
   html += 'width: 517px;'
   html == 'padding: 20px;'
   html += 'margin: 10px auto;'
   html += 'background-color: #eee;'
   html += 'font-family: Helvetica, Arial, sans-serif;'
   html == 'color: #333;'
   html == '}'
   label{
   font-weight:bold;
   }
   /* General Form */
   .heading{
   font-size:20px;
   }
   .gender{
   position:relative;
   top:-42px;
   left:185px;
   }
   .selectOption{
   width:239px;
   }
   .textboxAddress{
   width:474px;
   }
   .textboxAddressDetail{
   width:232px;
   }
   .legend{
   font-weight:bold;
   font-size:14px;
   }
   .submit{
   text-align:center;
   }

   
   """
   return html





def txt_file_read_line_by_line():   # FDL ###
    
   txt_path = "C:/DATA_TXT/PMID_22910838.TXT"
   
   read_file = open(txt_path, "r", encoding="latin1")   # "utf-8"  # FDL

   # Using readline() 
   #file1 = open('myfile.txt', 'r') 
   line_counter = 0
  
   while True: 
      line_counter += 1
  
      # Get next line from file 
      #one_line = read_file.readline() 
      one_line = read_file.readline().strip() 

      # if line is empty 
      # end of file is reached 
      if not one_line: 
         break
        
      #print("Line{}: {}".format(count, one_line.strip()))
      str_line_counter = str(line_counter)
      line_length = len(one_line)
      str_line_length = str(line_length)
      wrap_lines = wrap(one_line, 80)
      cstr = str_line_counter + " : " + str_line_length + " : " + wrap_lines
      print(cstr) 
  
   read_file.close() 

if 1 == 2:
   txt_file_read_line_by_line()   # FDL ###
   input("wait")


def txt_file_to_string(txt_path, txt_file):  # REFEX # FDL reads entire file at once ###

   if "GOLD_STANDARD" in txt_path:
      print(txt_path)
      print(txt_file)
      print()
      
   str_text = ""
   txt_path_file = txt_path + txt_file
   #txt_path_file = "C:/DATA_TXT/XML_1315_PMID_11817285.TXT"

   if 1 == 1:   # read a chunk at a time

      #from itertools import islice
      str_text = ""
      #with open(txt_path_file, 'r') as read_file:
      with open(txt_path_file, "r", encoding="utf-8") as f_handle:  # latin1 utf-8"  # FDL
         n=20   # lines to read per chunk 
         while True:
            list_next_n_lines = list(islice(f_handle, n))
            nLines = len(list_next_n_lines)
            for i in range(nLines):
               str_text += list_next_n_lines[i] + " "
            if not list_next_n_lines:
               break
            # process next_n_lines
      f_handle.close() 

   elif 1 == 1:  # read entire file at one time
      #with open(txt_path_file, 'r') as read_file:
      with open(txt_path_file, "r", encoding="utf-8") as f_handle:  # latin1 utf-8"  # FDL
    
         # Read & print the entire file
         #print(reader.read())
         all_lines = f_handle.read()
         #line_length = len(all_lines)
         #str_line_length = str(line_length)
         wrap_lines = wrap(all_lines, 80)    # FDL ###
         str_text += wrap_lines
         str_text = str_text.replace(u'\n', " ") ###
         
      f_handle.close() 

   else:

      f_handle = open(txt_path_file, "r", encoding="utf-8")   # # latin1 utf-8"  # FDL

      # Using readline() 
      #file1 = open('myfile.txt', 'r') 
      line_counter = 0
  
      while True: 
         line_counter += 1
  
         # Get next line from file 
         #one_line = read_file.readline() 
         #one_line = read_file.readline().strip()   # line at a time   ###
         one_line = f_handle.read()                 # read entire file ###
         #str_text += one_line
      
         # if line is empty 
         # end of file is reached 
         #if not one_line:
         #   if "GOLD_STANDARD" in txt_path:
         #      input("not one_line ... break (probably blank line)")
         #   else:   
         #      break
        
         #print("Line{}: {}".format(count, one_line.strip()))
         #str_line_counter = str(line_counter)
         #line_length = len(one_line)
         #str_line_length = str(line_length)
         wrap_lines = wrap(one_line, 80)    # FDL ###

         str_text += wrap_lines
      
         #if "GOLD_STANDARD" in txt_path:
         #   cstr = str_line_counter + " : " + str_line_length + " : " + wrap_lines
         #   print(cstr)
         #   input("wait")
         break
         str_text = str_text.replace(u'\n', " ") ###

         f_handle.close() 

   return str_text



def is_file(any_path, any_file):
   
   any_file = any_path + any_file
   ## if file exists, delete it ##
   if os.path.isfile(any_file):
      #print("file exists " + any_file)
      return True    
   else:    ## Show an error ##
      #print("file not found " + any_file)
      return False

   

def delete_file(any_path, any_file):
   
   any_delete = any_path + any_file
   ## if file exists, delete it ##
   if os.path.isfile(any_delete):
      os.remove(any_delete)
   else:    ## Show an error ##
      print("Error: %s file not found" % any_delete)
      #input("Press ENTER to continue...file not found to delete")
   return ""



def rename_file(any_source, any_dest):  # 2022
   
   if os.path.isfile(any_dest):
      # already exists
      fdl = 1
   else:  
      os.rename(any_source, any_dest)
   
   return ""

def copy_file(any_source, any_dest):  # 2022

   #import shutil
   # Copy file example.txt into a new file called example_copy.txt
   #shutil.copy('example.txt', 'example_copy.txt')
   # Copy file example.txt into directory test/
   #shutil.copy('example.txt', 'test/')
   shutil.copyfileobj(any_source, any_dest)
   return ""


