

# one phase and two phase hyperbolic fitting
# uses gekko

from fdl_sub_superposition import *
from fdl_sub_listbox import *

import os
import math
from gekko import GEKKO
import numpy as np
import numpy.polynomial.polynomial as poly
from numpy import linspace, loadtxt, ones, convolve
#import seaborn as sns
from scipy.optimize import minimize
import scipy as sp
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style
#from matplotlib.ticker import MultipleLocator
#from matplotlib import pyplot
import random

#from Tkinter import *
from tkinter import *

import csv, pyodbc

"""
# Prints out the numbers 0,1,2,3,4
for x in range(5):
    print(x)

# Prints out 3,4,5
for x in range(3, 6):
    print(x)

# Prints out 3,5,7
for x in range(3, 8, 2):
    print(x)
"""




def fig_smoothed_data (rate_data, time_data, ND_OR_LC, study_product, display_plot, list_volume_cumulative):
   
   if 1 == 1:  # use unsmoothed data
      values = fig_superposition_rate (rate_data, time_data, ND_OR_LC, study_product, display_plot, list_volume_cumulative)
      super_rate_data = values[0]
         
   #include_weighting = "YES"
   include_weighting = "NO"


   if 1 == 2:   # does not work points ......

      nTests = 9    # only keep last 9 points ....
      
      keep_rate_data = []
      keep_time_data = []
      data_points = len(rate_data)
      for i in range(data_points):
         any_time = time_data[i]
         any_rate = rate_data[i]
         if i >= (data_points - nTests):   
            keep_rate_data.append(any_rate)
            keep_time_data.append(any_time)
      rate_data = keep_rate_data
      time_data = keep_rate_data


   
   if 1 == 1:

      temp0_rate_data = []
      temp0_time_data = []
      data_points = len(rate_data)
      for i in range(data_points):
         any_time = time_data[i]
         any_rate = rate_data[i]
         any_log_rate = math.log(any_rate, 10)  
         if any_time >= 0:                                  # eliminate negative time and convert rate to log(rate)
            if 1 == 1:  # include_weighting == "NO":        # weighting MUST occur at end of this function!!!!  
               temp0_rate_data.append(any_log_rate)
               temp0_time_data.append(any_time)
            elif include_weighting == "YES":
               for j in range(i+1):                         # add weighting factor - make recent production moe important
                  temp0_rate_data.append(any_log_rate)
                  temp0_time_data.append(any_time)
  
     
   if 1 == 1:
      
      temp1_rate_data = []
      temp1_time_data = []
      data_points = len(temp0_rate_data)
      for i in range(data_points):
         if i == 0:                   # first point
            temp1_rate_data.append(temp0_rate_data[i])
            temp1_time_data.append(temp0_time_data[i])
  
         elif i == data_points - 1:   # last point
            temp1_rate_data.append(temp0_rate_data[i])
            temp1_time_data.append(temp0_time_data[i])     
   
         elif i == 1: # second point
            any_rate_sum = temp0_rate_data[i-1] + temp0_rate_data[i]
            any_rate_ave = any_rate_sum/2 
            temp1_rate_data.append(any_rate_ave)
            
            any_time_sum = temp0_time_data[i-1] + temp0_time_data[i]
            any_time_ave = any_time_sum/2 
            temp1_time_data.append(any_time_ave) 
         elif i == data_points - 2:  # next to last point
            any_rate_sum = temp0_rate_data[i-1] + temp0_rate_data[i]
            any_rate_ave = any_rate_sum/2 
            temp1_rate_data.append(any_rate_ave)
            
            any_time_sum = temp0_time_data[i-1] + temp0_time_data[i]
            any_time_ave = any_time_sum/2 
            temp1_time_data.append(any_time_ave)
         elif 1 == 1:
            any_rate_sum = temp0_rate_data[i-1] + temp0_rate_data[i] + temp0_rate_data[i+1]
            any_rate_ave = any_rate_sum/3 
            temp1_rate_data.append(any_rate_ave)
            
            any_time_sum = temp0_time_data[i-1] + temp0_time_data[i] + temp0_time_data[i+1]
            any_time_ave = any_time_sum/3 
            temp1_time_data.append(any_time_ave)

     
   if 1 == 2:
      temp2_rate_data = []
      temp2_time_data = []
      data_points = len(temp1_rate_data)
      for i in range(data_points):
         if i == 0:   # first point
            temp2_rate_data.append(temp1_rate_data[i])
            temp2_time_data.append(temp1_time_data[i])
  
         elif i == data_points - 1:   # last point
            temp2_rate_data.append(temp1_rate_data[i])
            temp2_time_data.append(temp1_time_data[i])     
   
         elif i == 1: # second point
            any_rate_sum = temp1_rate_data[i-1] + temp1_rate_data[i]
            any_rate_ave = any_rate_sum/2 
            temp2_rate_data.append(any_rate_ave)
            
            any_time_sum = temp1_time_data[i-1] + temp1_time_data[i]
            any_time_ave = any_time_sum/2 
            temp2_time_data.append(any_time_ave) 
         elif i == data_points - 2:  # next to last point
            any_rate_sum = temp1_rate_data[i-1] + temp1_rate_data[i]
            any_rate_ave = any_rate_sum/2 
            temp2_rate_data.append(any_rate_ave)
            
            any_time_sum = temp1_time_data[i-1] + temp1_time_data[i]
            any_time_ave = any_time_sum/2 
            temp2_time_data.append(any_time_ave)
         elif 1 == 1:
            any_rate_sum = temp1_rate_data[i-1] + temp1_rate_data[i] + temp1_rate_data[i+1]
            any_rate_ave = any_rate_sum/3 
            temp2_rate_data.append(any_rate_ave)
            
            any_time_sum = temp1_time_data[i-1] + temp1_time_data[i] + temp1_time_data[i+1]
            any_time_ave = any_time_sum/3 
            temp2_time_data.append(any_time_ave)

      

   if 1 == 2:
      temp3_rate_data = []
      temp3_time_data = []
      data_points = len(temp2_rate_data)
      for i in range(data_points):
         if i == 0:   # first point
            temp3_rate_data.append(temp2_rate_data[i])
            temp3_time_data.append(temp2_time_data[i])
  
         elif i == data_points - 1:   # last point
            temp3_rate_data.append(temp2_rate_data[i])
            temp3_time_data.append(temp2_time_data[i])     
   
         elif i == 1: # second point
            any_rate_sum = temp2_rate_data[i-1] + temp2_rate_data[i]
            any_rate_ave = any_rate_sum/2 
            temp3_rate_data.append(any_rate_ave)
            
            any_time_sum = temp2_time_data[i-1] + temp2_time_data[i]
            any_time_ave = any_time_sum/2 
            temp3_time_data.append(any_time_ave) 
         elif i == data_points - 2:  # next to last point
            any_rate_sum = temp2_rate_data[i-1] + temp2_rate_data[i]
            any_rate_ave = any_rate_sum/2 
            temp3_rate_data.append(any_rate_ave)
            
            any_time_sum = temp2_time_data[i-1] + temp2_time_data[i]
            any_time_ave = any_time_sum/2 
            temp3_time_data.append(any_time_ave)
         elif 1 == 1:
            any_rate_sum = temp2_rate_data[i-1] + temp2_rate_data[i] + temp2_rate_data[i+1]
            any_rate_ave = any_rate_sum/3 
            temp3_rate_data.append(any_rate_ave)
            
            any_time_sum = temp2_time_data[i-1] + temp2_time_data[i] + temp2_time_data[i+1]
            any_time_ave = any_time_sum/3 
            temp3_time_data.append(any_time_ave)

     
   if 1 == 2:
      temp4_rate_data = []
      temp4_time_data = []
      data_points = len(temp3_rate_data)
      for i in range(data_points):
         if i == 0:   # first point
            temp4_rate_data.append(temp3_rate_data[i])
            temp4_time_data.append(temp3_time_data[i])
  
         elif i == data_points - 1:   # last point
            temp4_rate_data.append(temp3_rate_data[i])
            temp4_time_data.append(temp3_time_data[i])     
   
         elif i == 1: # second point
            any_rate_sum = temp3_rate_data[i-1] + temp3_rate_data[i]
            any_rate_ave = any_rate_sum/2 
            temp4_rate_data.append(any_rate_ave)
            
            any_time_sum = temp3_time_data[i-1] + temp3_time_data[i]
            any_time_ave = any_time_sum/2 
            temp4_time_data.append(any_time_ave) 
         elif i == data_points - 2:  # next to last point
            any_rate_sum = temp3_rate_data[i-1] + temp3_rate_data[i]
            any_rate_ave = any_rate_sum/2 
            temp4_rate_data.append(any_rate_ave)
            
            any_time_sum = temp3_time_data[i-1] + temp3_time_data[i]
            any_time_ave = any_time_sum/2 
            temp4_time_data.append(any_time_ave)
         elif 1 == 1:
            any_rate_sum = temp3_rate_data[i-1] + temp3_rate_data[i] + temp3_rate_data[i+1]
            any_rate_ave = any_rate_sum/3 
            temp4_rate_data.append(any_rate_ave)
            
            any_time_sum = temp3_time_data[i-1] + temp3_time_data[i] + temp3_time_data[i+1]
            any_time_ave = any_time_sum/3 
            temp4_time_data.append(any_time_ave)

    

   if 1 == 2:
      temp5_rate_data = []
      temp5_time_data = []
      data_points = len(temp4_rate_data)
      for i in range(data_points):
         if i == 0:   # first point
            temp5_rate_data.append(temp4_rate_data[i])
            temp5_time_data.append(temp4_time_data[i])
  
         elif i == data_points - 1:   # last point
            temp5_rate_data.append(temp4_rate_data[i])
            temp5_time_data.append(temp4_time_data[i])     
   
         elif i == 1: # second point
            any_rate_sum = temp4_rate_data[i-1] + temp4_rate_data[i]
            any_rate_ave = any_rate_sum/2 
            temp5_rate_data.append(any_rate_ave)
            
            any_time_sum = temp4_time_data[i-1] + temp4_time_data[i]
            any_time_ave = any_time_sum/2 
            temp5_time_data.append(any_time_ave) 
         elif i == data_points - 2:  # next to last point
            any_rate_sum = temp4_rate_data[i-1] + temp4_rate_data[i]
            any_rate_ave = any_rate_sum/2 
            temp5_rate_data.append(any_rate_ave)
            
            any_time_sum = temp4_time_data[i-1] + temp4_time_data[i]
            any_time_ave = any_time_sum/2 
            temp5_time_data.append(any_time_ave)
         elif 1 == 1:
            any_rate_sum = temp4_rate_data[i-1] + temp4_rate_data[i] + temp4_rate_data[i+1]
            any_rate_ave = any_rate_sum/3 
            temp5_rate_data.append(any_rate_ave)
            
            any_time_sum = temp4_time_data[i-1] + temp4_time_data[i] + temp4_time_data[i+1]
            any_time_ave = any_time_sum/3 
            temp5_time_data.append(any_time_ave)

     


   if 1 == 2:
      
      temp6_rate_data = []
      temp6_time_data = []
      data_points = len(temp5_rate_data)
      for i in range(data_points):
         if i == 0:   # first point
            temp6_rate_data.append(temp5_rate_data[i])
            temp6_time_data.append(temp5_time_data[i])
  
         elif i == data_points - 1:   # last point
            temp6_rate_data.append(temp5_rate_data[i])
            temp6_time_data.append(temp5_time_data[i])     
   
         elif i == 1: # second point
            any_rate_sum = temp5_rate_data[i-1] + temp5_rate_data[i]
            any_rate_ave = any_rate_sum/2 
            temp6_rate_data.append(any_rate_ave)
            
            any_time_sum = temp5_time_data[i-1] + temp5_time_data[i]
            any_time_ave = any_time_sum/2 
            temp6_time_data.append(any_time_ave) 
         elif i == data_points - 2:  # next to last point
            any_rate_sum = temp5_rate_data[i-1] + temp5_rate_data[i]
            any_rate_ave = any_rate_sum/2 
            temp6_rate_data.append(any_rate_ave)
            
            any_time_sum = temp5_time_data[i-1] + temp5_time_data[i]
            any_time_ave = any_time_sum/2 
            temp6_time_data.append(any_time_ave)
         elif 1 == 1:
            any_rate_sum = temp5_rate_data[i-1] + temp5_rate_data[i] + temp5_rate_data[i+1]
            any_rate_ave = any_rate_sum/3 
            temp6_rate_data.append(any_rate_ave)
            
            any_time_sum = temp5_time_data[i-1] + temp5_time_data[i] + temp5_time_data[i+1]
            any_time_ave = any_time_sum/3 
            temp6_time_data.append(any_time_ave)


   if 1 == 1:   # smooth only once
        
      final_rate_data = []
      final_time_data = []
      data_points = len(temp1_rate_data)
      for i in range(data_points):
         any_time = temp1_time_data[i]
         any_log_rate = temp1_rate_data[i]
         any_rate = 10.0 ** any_log_rate  
         if include_weighting == "NO":          # convert log(rate) back to rate with no weighting      
            final_rate_data.append(any_rate)
            final_time_data.append(any_time)
         elif include_weighting == "XXXYES":
            for j in range(i+1):                # add weighting factor - make recent production more important
               final_rate_data.append(any_rate)
               final_time_data.append(any_time)
         elif include_weighting == "XXXYES":        # not as heavily weighted as above ....
            if i == 0:
               k = 2
            elif i == 1:
               k = 3
            elif i == 2:
               k = 4       
            elif 1 == 1:
               k = int(((i+1) / 2) + 2)
               
            for j in range(k):           # add weighting factor - make recent production more important
               final_rate_data.append(any_rate)
               final_time_data.append(any_time)
         elif include_weighting == "XXXYES":        # not as heavily weighted as above ....
            if i == 0:
               k = 3
            elif i == 1:
               k = 3
            elif i == 2:
               k = 3       
            elif 1 == 1:
               k = int(((i+3) / 3) + 2)   # when i = 3 k = 4
               #k = int(((i+3) / 3) + 2)   # when i = 4 k = 4
               #k = int(((i+3) / 3) + 2)   # when i = 5 k = 4
               #k = int(((i+3) / 3) + 2)   # when i = 6 k = 5  
            for j in range(k):           # add weighting factor - make recent production more important
               final_rate_data.append(any_rate)
               final_time_data.append(any_time)
         elif include_weighting == "YES":        # not as heavily weighted as above ....
            if i == 0:
               k = 6
            elif i == 1:
               k = 5
            elif i == 2:
               k = 5       
            elif 1 == 1:
               k = int(((i+4) / 4) + 3)   # when i = 3 k = 4
               #k = int(((i+4) / 4) + 3)   # when i = 4 k = 4
               #k = int(((i+4) / 4) + 3)   # when i = 5 k = 4
               #k = int(((i+4) / 4) + 3)   # when i = 6 k = 5  
            for j in range(k):           # add weighting factor - make recent production more important
               final_rate_data.append(any_rate)
               final_time_data.append(any_time)
   elif 1 == 1:   # smooth 6 times
        
      final_rate_data = []
      final_time_data = []
      data_points = len(temp6_rate_data)
      for i in range(data_points):
         any_time = temp6_time_data[i]
         any_log_rate = temp6_rate_data[i]
         any_rate = 10.0 ** any_log_rate  
         if include_weighting == "NO":     # convert log(rate) back to rate with no weighting      
            final_rate_data.append(any_rate)
            final_time_data.append(any_time)
         elif include_weighting == "XXXXXYES":
            for j in range(i+1):           # add weighting factor - make recent production moe important
               final_rate_data.append(any_rate)
               final_time_data.append(any_time)
         elif include_weighting == "YES":        # not as heavily weighted as above ....
            if i == 0:
               k = 2
            elif i == 1:
               k = 3
            elif i == 2:
               k = 4       
            elif 1 == 1:
               k = int(((i+1) / 2) + 2)
               
            for j in range(k):           # add weighting factor - make recent production moe important
               final_rate_data.append(any_rate)
               final_time_data.append(any_time)
   
      #print("temp1_time_data")
      #print(temp1_time_data)
      #input("Press ENTER to continue...")

      #print("temp1_rate_data")
      #print(temp1_rate_data)
      #input("Press ENTER to continue...")


   if 1 == 2:   # use smoothed data
      values = fig_superposition_rate (final_rate_data, final_time_data, ND_OR_LC, study_product, display_plot, list_volume_cumulative)
      super_rate_data = values[0]


  
   if display_plot == "YES":

      if study_product == "OIL":       
         cY = "Log(Oil Rate) in BOPD"
      elif study_product == "GAS":       
         cY = "Log(Gas Rate) in MCFDD"
         
      D_M_Y = "D"
    
      if D_M_Y == "D":
         cTitle = "Measured vs Smoothed Rate versus Time in Days\n"
         cX = "Time in Days"
           
      if 1 == 2:
         
         plt.figure(1)
          
         cTitle += "Preparing Data For Hyperbolic Prediction (LOG FORM)"
         plt.title(cTitle)
                
         #plt.plot(x, x + 0, linestyle='solid')
         #plt.plot(x, x + 1, linestyle='dashed')
         #plt.plot(x, x + 2, linestyle='dashdot')
         #plt.plot(x, x + 3, linestyle='dotted');

         # For short, you can use the following codes:
         #plt.plot(x, x + 4, linestyle='-')  # solid
         #plt.plot(x, x + 5, linestyle='--') # dashed
         #plt.plot(x, x + 6, linestyle='-.') # dashdot
         #plt.plot(x, x + 7, linestyle=':')  # dotted;
       
         #plt.plot(x, x + 0, '-g')  # solid green
         #plt.plot(x, x + 1, '--c') # dashed cyan
         #plt.plot(x, x + 2, '-.k') # dashdot black
         #plt.plot(x, x + 3, ':r')  # dotted red;
       
         #the RGB (Red/Green/Blue) and CMYK (Cyan/Magenta/Yellow/blacK)  
         if D_M_Y == "D":
            plt.plot(temp0_time_data, temp0_rate_data, color='red', linestyle='solid', label='Measured')
            # was yellow
            plt.plot(temp1_time_data, temp1_rate_data, color='black', linestyle='dashed', label='Smoothed1')
            plt.plot(time_data, super_rate_data, color='green', linestyle='dotted', label='Superposition of Rate')
   
            #plt.plot(temp2_time_data, temp2_rate_data, color='green', linestyle='dashdot', label='Smoothed2')
            #plt.plot(temp3_time_data, temp3_rate_data, color='cyan', linestyle='dotted', label='Smoothed3')
            #plt.plot(temp4_time_data, temp4_rate_data, color='blue', linestyle='dotted', label='Smoothed4')
            #plt.plot(temp5_time_data, temp5_rate_data, color='magenta', linestyle='dashed', label='Smoothed5')
            #plt.plot(temp6_time_data, temp6_rate_data, color='black', linestyle='dashed', label='Smoothed6')
                 
         plt.legend(loc='upper right')
         plt.xlabel(cX)
         plt.ylabel(cY)
         #plt.yscale('log')    # works
         plt.grid(True)
         plt.show()




   if display_plot == "YES":

      """  now done in superposition code ....
      nLast = len(final_rate_data)    
      last_smoothed = final_rate_data[nLast-1]
      nLast = len(final_rate_data)    
      last_super = super_rate_data[nLast-1]
      n_rows = len(super_rate_data)
      for i in range(n_rows):
         super_rate_data[i] = super_rate_data[i] * last_smoothed / last_super
      """         
     
      if study_product == "OIL":       
         cY = "Log(Oil Rate) in BOPD"
      elif study_product == "GAS":       
         cY = "Log(Gas Rate) in MCFDD"
         
      D_M_Y = "D"
    
      if D_M_Y == "D":
         cTitle = "Measured vs Smoothed Rate versus Time in Days\n"
         cX = "Time in Days"
               
      plt.figure(1)
         
     
      cTitle += "Preparing Data For Regression Fitting (After Smoothing)"
      plt.title(cTitle)
     
           
      #plt.plot(x, x + 0, linestyle='solid')
      #plt.plot(x, x + 1, linestyle='dashed')
      #plt.plot(x, x + 2, linestyle='dashdot')
      #plt.plot(x, x + 3, linestyle='dotted');

      # For short, you can use the following codes:
      #plt.plot(x, x + 4, linestyle='-')  # solid
      #plt.plot(x, x + 5, linestyle='--') # dashed
      #plt.plot(x, x + 6, linestyle='-.') # dashdot
      #plt.plot(x, x + 7, linestyle=':')  # dotted;
       
      #plt.plot(x, x + 0, '-g')  # solid green
      #plt.plot(x, x + 1, '--c') # dashed cyan
      #plt.plot(x, x + 2, '-.k') # dashdot black
      #plt.plot(x, x + 3, ':r')  # dotted red;
       
      #the RGB (Red/Green/Blue) and CMYK (Cyan/Magenta/Yellow/blacK)  
      if D_M_Y == "D":
         plt.plot(time_data, rate_data, color='red', linestyle='solid', label='Measured Rate')
         #plt.plot(temp1_time_data, temp1_rate_data, color='yellow', linestyle='dashed', label='Smoothed1')
         #plt.plot(temp2_time_data, temp2_rate_data, color='green', linestyle='dashdot', label='Smoothed2')
         #plt.plot(temp3_time_data, temp3_rate_data, color='cyan', linestyle='dotted', label='Smoothed3')
         #plt.plot(temp4_time_data, temp4_rate_data, color='blue', linestyle='dotted', label='Smoothed4')
         #plt.plot(temp5_time_data, temp5_rate_data, color='magenta', linestyle='dashed', label='Smoothed5')
         plt.plot(final_time_data, final_rate_data, color='black', linestyle='dashed', label='Smoothed Rate')
         plt.plot(time_data, super_rate_data, color='green', linestyle='dotted', label='Superposition Rate')
         
      #plt.xlim(0, max(log_min_value, log_max_value)
      #plt.ylim(0, max(rate_data) * 1.35)
                   
      plt.legend(loc='upper right')
      plt.xlabel(cX)
      plt.ylabel(cY)
      plt.yscale('log')    # works
      plt.grid(True)
      plt.show()
 
   oList = Tk()
   returnValue = True
   list_items = ['SUPERPOSITION RATE - For Refracs or Erratic Production', \
                 'SMOOTHED RATE - For Normalized or Gradually Declining Production', \
                 'MEASURED RATE - To Use Actual Production Data']
   choice = ListBoxChoice(oList, "Select one", "Pick one", list_items).returnValue()
   choice = choice[:8]       # slicing - first 8 characters
   method = choice.rstrip()       # trim spaces on right

   #length = len(ND_OR_LC)
   #print ("length of ND_OR_LC = " + str(length))
       
   oList.destroy()
   cstr = "Method = " + method
     
   if method == "SUPERPOS":
      return [super_rate_data, time_data]   # return a list
   elif method == "SMOOTHED":
      return [final_rate_data, final_time_data]   # return a list
   elif method == "MEASURED":
      return [rate_data, time_data]      # return a list
   
   #    plt.plot(time_data, super_rate_data, color='green', linestyle='dotted', label='Superposition of Rate')
   #  plt.plot(final_time_data, final_rate_data, color='black', linestyle='dashed', label='Smoothed')
   #    plt.plot(time_data, rate_data, color='red', linestyle='solid', label='Measured Rate')
      
   #return [final_rate_data, final_time_data]   # return a list





def fig_remove_outlier_points (ym, yp, rate_data, time_data, ND_OR_LC, study_product):

   if 1 == 1:       # then remove outlier points 

      if 1 == 1:    # then remove outlier points
         
         temp_rate_data = rate_data
         temp_time_data = time_data
         ym_points = len(ym)
         yp_points = len(yp)
         data_points = len(temp_rate_data)
         cstr = "ym points = " + str(ym_points)
         cstr += "  yp points = " + str(yp_points)
         cstr += "  data points = " + str(data_points)
         print(cstr)
         #input("Press ENTER to continue...")
         list_percent_accuracy = [] 
         for i in range(data_points):
            any_percent_accuracy = 100.0 * (ym[i] - yp[i]) / ym[i]    
            list_percent_accuracy.append(any_percent_accuracy)
            if 1 == 2:
               cstr = "i = " + str(i)
               cstr += "  pct = " + str(list_percent_accuracy[i]) 
               cstr += "   ym = " + str(ym[i]) 
               cstr += "   yp = " + str(yp[i]) 
               #cstr += "   rate = " + str(temp_rate_data[i])
               #cstr += "   time = " + str(temp_time_data[i]) 
               print(cstr) 
         #input("Press ENTER to continue...")

         if ND_OR_LC == "DD":
            #any_low_pct_cutoff = -25.0   # shut ins            # change this !!!!!!!
            any_low_pct_cutoff = -30.0   # shut ins            # change this !!!!!!!
            #any_high_pct_cutoff = 45.0   # refracs             # change this !!!!!!!  
            any_high_pct_cutoff = 50.0   # refracs             # change this !!!!!!!  
         elif 1 == 1: 
            any_low_pct_cutoff = -10.0   # shut ins            # change this !!!!!!!
            any_high_pct_cutoff = 55.0   # refracs             # change this !!!!!!!
         elif 1 == 1:   
            any_low_pct_cutoff = -30.0                         # change this !!!!!!!
            any_high_pct_cutoff = 30.0                         # change this !!!!!!!
 
         rate_data = []
         time_data = []
         for i in range(data_points):
            any_pct_accuracy = 100.0 * (ym[i] - yp[i]) / ym[i]
            if i == 0:       # first point
               keep = "YES"
            elif i == 2:     # second point
               keep = "YES"
            elif i == 3:     # third point
               keep = "YES"    
            elif i == (data_points -1):  # last point 
               keep = "YES"
            elif i == (data_points -2):  # next to last point 
               keep = "YES"
            elif i == (data_points -3):  # third to last point 
               keep = "YES"     
            elif any_pct_accuracy >= any_low_pct_cutoff and any_pct_accuracy <= any_high_pct_cutoff:
               keep = "YES"
            elif 1 == 1:
               keep = "NO"
               
            if keep == "YES":   
               rate_data.append(temp_rate_data[i])   # keep valid data points
               time_data.append(temp_time_data[i])


   return [rate_data, time_data]   # return a list


def fig_get_subset_of_two_lists (list_x_data, list_y_data):
   
   subset = AlertBox("\nSelect data subset to include :\n<A>ll Data\n<1> First Half\n<2> Second Half")

   data_points = len(list_x_data)

   if subset == "A":   
      start = 0
      end = data_points
   elif subset == "1":
      start = 0
      end = int(2*data_points/4) 
   elif subset == "2":
      start = int(2*data_points/4)
      end = data_points   
                                                      
   keep_x_data = []
   keep_y_data = []   
   for i in range(start,end):
      any_keep_x_data = list_x_data[i]
      any_keep_y_data = list_y_data[i]
      keep_x_data.append(any_keep_x_data)
      keep_y_data.append(any_keep_y_data)
      
   return [keep_x_data, keep_y_data]   # return a list
  
 



 
                                                                             # DAILY MONTHLY or YEARLY   
def fit_hyperbolic ( rate_data, time_data, ND_OR_LC, study_year, study_product, monthly_or_yearly, STD_OR_SPECIAL, study_state, test_data, list_volume_cumulative ):

   values = fig_get_subset_of_two_lists (time_data, rate_data)
   time_data = values[0]
   rate_data = values[1]

   aa = 1

   if test_data == "YES":   
      typecurve = "NO"
   elif ND_OR_LC == "PT":    # ??????????????
      typecurve = "YES"
   elif ND_OR_LC == "ND":
      typecurve = "YES"    
   elif ND_OR_LC == "WELLCODE" and study_state == "ND":
      typecurve = "YES"
   elif ND_OR_LC == "WELLCODE" and study_state == "SD":
      typecurve = "YES"
   elif ND_OR_LC == "WELLCODE" and study_state == "MT":
      typecurve = "YES"
   elif 1 == 1:      
      typecurve = "NO"

   iloop = 1
   while (iloop <= 2):
      
      if test_data == "YES" and iloop == 1:
         minimum_h_string = AlertBox("Enter minimum hyperbolic value for One Phase (0.499-0.710-0.799) ")
         minimum_h = float(minimum_h_string)
         #minimum_h = 0.90
         #minimum_h = 0.65
         #minimum_h = 0.149
         #minimum_h = 0.399
         #minimum_h = 0.699
         #minimum_h = 0.799

      smooth_data = "YES"
      if monthly_or_yearly == "DAILY" and ND_OR_LC == "ND":
         #smooth_data = "NO"
         smooth_data = "YES"
 
      elif iloop >= 2:
         smooth_data = "NO"
  
      if smooth_data == "YES":

         display_plot = "YES"     
         #display_plot = "NO"     
         values = fig_smoothed_data (rate_data, time_data, ND_OR_LC, study_product, display_plot, list_volume_cumulative)
         smoothed_rate_data = values[0]
         smoothed_time_data = values[1]
         
         data_points = len(smoothed_rate_data)
         
         how_many = data_points   # all data points
         #how_many = 9            # only the first 24 data points .............................................................
         
         if how_many == data_points:
            rate_data = smoothed_rate_data
            time_data = smoothed_time_data
         elif 1 == 1:
            rate_data = []
            time_data = []
            for i in range(how_many):
               rate_data.append(smoothed_rate_data[i])
               time_data.append(smoothed_time_data[i])
      


      if monthly_or_yearly == "DAILY" or monthly_or_yearly == "MONTHLY" or monthly_or_yearly == "DRAWDOWN":
         gekko_rate_data = rate_data
         gekko_time_data = time_data
         max_daily_rate = gekko_rate_data[0]
         cstr = "fit_hyperbolic: max daily rate = " + str(max_daily_rate)
         print(cstr)
         gekko_time_data = time_data
      elif monthly_or_yearly == "YEAR":
         gekko_rate_data = []
         gekko_time_data = []
         data_points = len(rate_data)
         for i in range(data_points):
            if i == 0: 
               any_cum_days = i + (365.25/2.)             # 0 = 365/2    1 = 1 + 365/2
            elif 1 == 1:
               any_cum_days += 365.25
    
            gekko_time_data.append(any_cum_days)
            any_annual_volume = rate_data[i]
            any_daily_volume = any_annual_volume / 365.25
            gekko_rate_data.append(any_daily_volume)
            
         max_daily_rate = gekko_rate_data[0]                     # fix to use max function .....
         cstr = "max daily rate = " + str(max_daily_rate)
         print(cstr)

         #print("gekko_time_data")
         #print(gekko_time_data)
         #input("Press ENTER to continue...")
      
         #print("gekko_rate_data")
         #print(gekko_rate_data)
         #input("Press ENTER to continue...")

         # fix for MONTH .....




      # start GEKKO code here for both loops .........................

      # GEKKO model
      m = GEKKO()
     
      
      if test_data == "YES":
         #gekko_q_daily = m.FV(lb=777.0,ub=777.0)    # q_daily  if monthly_or_yearly == "DAILY":
         #gekko_q_daily = m.FV(lb=max_daily_rate*1.0,ub=max_daily_rate*5.0)   # in case first time is later ...  # q_daily
         gekko_q_daily = m.FV(lb=max_daily_rate*0.85,ub=max_daily_rate*5.0)   # in case first time is later ...  # q_daily
      elif typecurve == "YES":
         #gekko_q_daily = m.FV(lb=777.0,ub=777.0)    # q_daily  if monthly_or_yearly == "DAILY":
         gekko_q_daily = m.FV(lb=max_daily_rate*1.0,ub=max_daily_rate*1.40)    # q_daily

      elif monthly_or_yearly == "DAILY":
         gekko_q_daily = m.FV(lb=max_daily_rate*1.0,ub=max_daily_rate*1.40)    # q_daily
         
      elif STD_OR_SPECIAL == "SPECIAL":
         gekko_q_daily = m.FV(lb=max_daily_rate*1.0,ub=max_daily_rate*1.40)    # q_daily
      elif (ND_OR_LC == "ND" or ND_OR_LC == "WELLCODE") and study_product == "OIL":
         gekko_q_daily = m.FV(lb=max_daily_rate*1.0,ub=max_daily_rate*1.30)    # q_daily
      elif (ND_OR_LC == "ND" or ND_OR_LC == "WELLCODE") and study_product == "GAS":
         gekko_q_daily = m.FV(lb=max_daily_rate*1.0,ub=max_daily_rate*1.40)    # q_daily
      elif 1 == 1:
         gekko_q_daily = m.FV(lb=max_daily_rate*1.0,ub=max_daily_rate*1.20)    # q_daily


       
      if test_data == "YES":
         #gekko_h_hyperbolic = m.FV(lb=0.01,ub=1.00)
         #gekko_h_hyperbolic = m.FV(lb=0.01,ub=1.3) 
         gekko_h_hyperbolic = m.FV(lb=minimum_h,ub=1.3) 

      elif typecurve == "YES":
         #gekko_h_hyperbolic = m.FV(lb=0.99,ub=0.99)
         gekko_h_hyperbolic = m.FV(lb=1.080836,ub=1.080836)  # ND type curve

      elif monthly_or_yearly == "DAILY":
         gekko_h_hyperbolic = m.FV(lb=0.01,ub=2.1)

      elif STD_OR_SPECIAL == "SPECIAL":
         gekko_h_hyperbolic = m.FV(lb=0.01,ub=2.1)
      elif ND_OR_LC == "LC":
         #gekko_h_hyperbolic = m.FV(lb=2.1,ub=2.5)                            # h_hyperbolic   # long canyon
         #gekko_h_hyperbolic = m.FV(lb=1.3,ub=1.6)                            # h_hyperbolic   # long canyon
         #gekko_h_hyperbolic = m.FV(lb=1.2,ub=1.2)
         gekko_h_hyperbolic = m.FV(lb=1.1,ub=1.1)
         #gekko_h_hyperbolic = m.FV(lb=0.2,ub=2.1)                            # h_hyperbolic   # long canyon

      elif ND_OR_LC == "WELLCODE" and study_product == "OIL":
         gekko_h_hyperbolic = m.FV(lb=0.10,ub=1.99) # 0.90 to 1.99             # h_hyperbolic
      elif ND_OR_LC == "WELLCODE" and study_product == "GAS":
         gekko_h_hyperbolic = m.FV(lb=0.10,ub=1.99) # 0.90 to 1.99             # h_hyperbolic

      elif ND_OR_LC == "ND" and study_year == 2012 and study_product == "OIL":
         gekko_h_hyperbolic = m.FV(lb=0.40,ub=1.99) # 0.90 to 1.99             # h_hyperbolic

      elif ND_OR_LC == "ND" and study_year == 2013 and study_product == "OIL":
         gekko_h_hyperbolic = m.FV(lb=0.40,ub=1.01) # 0.90 to 1.99             # h_hyperbolic
      
      elif ND_OR_LC == "ND" and study_year == 2014 and study_product == "OIL":
         gekko_h_hyperbolic = m.FV(lb=0.40,ub=1.99)   # h_hyperbolic
      
      elif ND_OR_LC == "ND" and study_year == 2015 and study_product == "OIL":
         gekko_h_hyperbolic = m.FV(lb=0.40,ub=1.99) # 0.90 to 1.99             # h_hyperbolic
      
      elif ND_OR_LC == "ND" and study_year == 2016 and study_product == "OIL":
         gekko_h_hyperbolic = m.FV(lb=0.70,ub=1.99) # 0.90 to 1.99             # h_hyperbolic
      
      elif ND_OR_LC == "ND" and study_year == 2017 and study_product == "OIL":
         gekko_h_hyperbolic = m.FV(lb=0.80,ub=1.99) # 0.90 to 1.99             # h_hyperbolic
      
      elif ND_OR_LC == "ND" and study_year == 2012 and study_product == "GAS":
         gekko_h_hyperbolic = m.FV(lb=0.40,ub=1.99) # 0.90 to 1.99             # h_hyperbolic

      elif ND_OR_LC == "ND" and study_year == 2013 and study_product == "GAS":
         gekko_h_hyperbolic = m.FV(lb=0.40,ub=1.99) # 0.90 to 1.99             # h_hyperbolic
      
      elif ND_OR_LC == "ND" and study_year == 2014 and study_product == "GAS":
         gekko_h_hyperbolic = m.FV(lb=1.99,ub=1.99)   # h_hyperbolic
      
      elif ND_OR_LC == "ND" and study_year == 2015 and study_product == "GAS":
         gekko_h_hyperbolic = m.FV(lb=0.40,ub=1.99) # 0.90 to 1.99             # h_hyperbolic
      
      elif ND_OR_LC == "ND" and study_year == 2016 and study_product == "GAS":
         gekko_h_hyperbolic = m.FV(lb=1.99,ub=1.99) # 0.90 to 1.99             # h_hyperbolic
      
      elif ND_OR_LC == "ND" and study_year == 2017 and study_product == "GAS":
         gekko_h_hyperbolic = m.FV(lb=0.40,ub=1.99) # 0.90 to 1.99             # h_hyperbolic
      

      gekko_d_daily = m.FV(lb=0.0,ub=0.2)                                    # d_daily
      #gekko_d_yearly = m.FV(lb=0.0,ub=99.999999)                            # d_yearly
 
      #d = m.FV(lb=-100.0,ub=100.0)

      # hyperbolic fit this.........................................
      # ym = list_daily_rate       
      # xm = list_days_cumulative    

      # use lists 
      xm = m.Param(value=gekko_time_data)       # GIVEN cumulative days
      #x2 = m.Param(value=list_xm2)  # GIVEN
      #x3 = m.Param(value=list_xm3)  # GIVEN
      ym = m.Param(value=gekko_rate_data)          # GIVEN daily rate   z = ym
 
      yp = m.Var()                     # y is yp    UNKNOWN

      m.Equation( yp == gekko_q_daily / ( 1.0 + gekko_h_hyperbolic * gekko_d_daily * xm ) ** (1.0/gekko_h_hyperbolic) )  
      #m.Equation(y==a*(x1**b)*(x2**c)*(x3**d))
      #m.Equation( gekko_d_daily == 1 - (( 100.0 - gekko_d_yearly ) / 100.0) ** (1./365.0) )  

      # D_DAILY = 1 - (( 100.0 - D_YEARLY ) / 100.0) ^ (1/365.00)

      m.Obj(((yp-ym)/ym)**2)

      # Options
      gekko_q_daily.STATUS = 1
      gekko_h_hyperbolic.STATUS = 1
      gekko_d_daily.STATUS = 1
      #gekko_d_yearly.STATUS = 1
 
      #d.STATUS = 1
      m.options.IMODE = 2
      m.options.SOLVER = 1

      # Solve
      m.solve()

      q_daily = gekko_q_daily.value[0]             # convert from gekko to variable
      h_hyperbolic = gekko_h_hyperbolic.value[0]
      d_daily = gekko_d_daily.value[0]
      #d_yearly = gekko_d_yearly.value[0]
 
 
      c1 = "ONE PHASE q_daily = " + str(q_daily)
      print (c1)

      c2 = "ONE PHASE h_hyperbolic = " + str(h_hyperbolic)
      print (c2)

      c3 = "ONE PHASE d_daily = " + str(d_daily)
      print (c3)

      #c4 = "d_yearly = " + str(d_yearly)

      cFormula = "Formula is : " + "\n" + "Hyperbolic Equation"

      #print (c4)
      
      if iloop == 1: 

         #values = fig_d_yearly_nominal (d_daily)     # call GEKKO
         #d_yearly = 100.0 * values[0]   # as a percent
         d_yearly = 99.9999 # not needed yet

      elif iloop >= 2: 

         values = fig_d_yearly_nominal (d_daily)     # call GEKKO
         d_yearly = 100.0 * values[0]   # as a percent

      c4 = "ONE PHASE d_yearly (percent) = " + str(d_yearly)
      print (c4)
      #input("Press ENTER to continue ... " + " in loop " + str(iloop))



      # look at correlation fit ....
   
      #print('d: ', d.value[0])

      #cFormula = "Formula is : " + "\n" + \
      #           r"$A * WTI^B * HH^C * PROPANE^D$"

      from scipy import stats
      slope, intercept, r_value, p_value, \
             std_err = stats.linregress(ym, yp)   # GEKKO variables ... # numpy array

      r2 = r_value**2 
      cR2 = "R^2 correlation = " + str(r_value**2)
      print(cR2)

      old_data_points = len(rate_data)
      if iloop == 1:   # ND_OR_LC == "WELLCODE":
      
         values = fig_remove_outlier_points (ym, yp, rate_data, time_data, ND_OR_LC, study_product)
         new_smoothed_rate_data = values[0]
         new_smoothed_time_data = values[1]
            
         rate_data = new_smoothed_rate_data
         time_data = new_smoothed_time_data
  
         new_data_points = len(rate_data)
         cstr = "old data points = " + str(old_data_points)
         cstr += "   new data points = " + str(new_data_points) + " after removing outliers"
         print(cstr)
         cPoints1 = "Original points included = " + str(old_data_points)
         print(cPoints1)
         cPoints2 = "Points after removing outliers = " + str(new_data_points)
         print(cPoints2)
         #cPoints = "Points included after removing outliers = " + str(new_data_points)
         #print(cPoints) 
         #input("Press ENTER to continue...")

         
      cLegend = cFormula + "\n" + c1 + "\n" + c2 + "\n" + c3 + "\n" + c4 + "\n" + cR2 + "\n" + cPoints1 + "\n" + cPoints2
      
      if iloop == 2:  # only show final plot

         # plot solution
         plt.figure(1)
         #plt.plot([20,140],[20,140],'k-',label='Measured')
         plt.title("Best Fit Analysis of Hyperbolic Curve Fitting for loop " + str(iloop))
 
         #plt.plot(ym,yp,'ro',label='Predicted')           # numpy array
         plt.scatter(ym,yp, color='black', s=2)

         plt.xlabel('Measured Outcome (YM)')
         plt.ylabel('Predicted Outcome (YP)')
   
         #plt.legend(loc='best')
         plt.legend([cLegend])

         #plt.text(25,115,'q_daily =' + str(q_daily.value[0]))
         #plt.text(25,110,'h_hyperbolic =' + str(h_hyperbolic.value[0]))
         #plt.text(25,105,'d_daily =' + str(d_daily.value[0]))
         #plt.text(25,100,'d =' + str(d.value[0]))
         #plt.text(25,90,r'$R^2$ =' + str(r_value**2))
         #plt.text(80,40,cFormula)
         plt.grid(True)
         plt.show()
      
      if 1 == 2:   # monthly_or_yearly == "DAILY" and ND_OR_LC == "ND":
         iloop = iloop + 100    # only 1 loop !!!
      elif 1 == 1:
         iloop = iloop + 1
   

      
   if d_daily == 0.0:
      d_daily = 0.000001
   if d_yearly == 0.0:
      d_yearly = 0.000001
        
      
   return [q_daily, h_hyperbolic, d_daily, d_yearly]   # return a list
  

   

                                                                              
def fit_hyperbolic_two_phase ( rate_data, time_data, ND_OR_LC, study_product, monthly_or_yearly, study_state, test_data, list_volume_cumulative):

   values = fig_get_subset_of_two_lists (time_data, rate_data)
   time_data = values[0]
   rate_data = values[1]

   aa = 1
   
   if test_data == "YES": 
      typecurve = "NO"
   elif ND_OR_LC == "PT":   # ??????????????
      typecurve = "YES"
   elif ND_OR_LC == "ND":
      typecurve = "YES"   
   elif ND_OR_LC == "WELLCODE" and study_state == "ND":
      typecurve = "YES"
   elif ND_OR_LC == "WELLCODE" and study_state == "SD":
      typecurve = "YES"
   elif ND_OR_LC == "WELLCODE" and study_state == "MT":
      typecurve = "YES"
   elif 1 == 1:      
      typecurve = "NO"
  
   
   iloop = 1
   while (iloop <= 2):
   
      if test_data == "YES" and iloop == 1:
         minimum_h_string = AlertBox("Enter minimum hyperbolic value for FRAC in Two Phase (0.499-0.799-1.066)")
         minimum_h = float(minimum_h_string)
         #minimum_h = 0.90
         #minimum_h = 0.149
         #minimum_h = 0.399
         #minimum_h = 0.699
         #minimum_h = 0.799
         maximum_h = 1.50

      smooth_data = "YES"
      if monthly_or_yearly == "DAILY" and ND_OR_LC == "ND":
         #smooth_data = "NO"
         smooth_data = "YES"
  
      elif iloop >= 2:
         smooth_data = "NO"
  
      if smooth_data == "YES":
         
         display_plot = "NO"     
         values = fig_smoothed_data (rate_data, time_data, ND_OR_LC, study_product, display_plot, list_volume_cumulative)
         smoothed_rate_data = values[0]
         smoothed_time_data = values[1]
            
         rate_data = smoothed_rate_data
         time_data = smoothed_time_data
     
         data_points = len(smoothed_rate_data)
         
         how_many = data_points   # all data points
         #how_many = 12            # only the first 24 data points
         #how_many = 9            # only the first 24 data points
         
         if how_many == data_points:
            rate_data = smoothed_rate_data
            time_data = smoothed_time_data
         elif 1 == 1:
            rate_data = []
            time_data = []
            for i in range(how_many):
               rate_data.append(smoothed_rate_data[i])
               time_data.append(smoothed_time_data[i])
      
      if 1 == 1:   # DAY_OR_MONTH == "DAY":
         gekko_rate_data = rate_data
         gekko_time_data = time_data
         max_daily_rate = gekko_rate_data[0]
         cstr = "fit_hyperbolic_two_phase: max daily rate = " + str(max_daily_rate)
         print(cstr)
         gekko_time_data = time_data
      elif monthly_or_yearly == "YEAR":         # fix - pass DAY_OR_MONTH ???????????
         gekko_rate_data = []
         gekko_time_data = []
         data_points = len(rate_data)
         for i in range(data_points):
            if i == 0: 
               any_cum_days = i + (365.25/2.)     # 0 = 365/2    1 = 1 + 365/2
            elif 1 == 1:
               any_cum_days += 365.25
    
            gekko_time_data.append(any_cum_days)
            any_annual_volume = rate_data[i]
            any_daily_volume = any_annual_volume / 365.25
            gekko_rate_data.append(any_daily_volume)
            
         max_daily_rate = gekko_rate_data[0]           #   fix to use max function .....
         cstr = "max daily rate = " + str(max_daily_rate)
         print(cstr)

         #print(gekko_time_data)
         #input("Press ENTER to continue...")
      
         #print(gekko_rate_data)
         #input("Press ENTER to continue...")

         # fix for MONTH .....


      if iloop <= 2:

         # start GEKKO code here .........................

         # GEKKO model
         m = GEKKO()
   
      if test_data == "YES":  
         gekko_q_daily1 = m.FV(lb=max_daily_rate*0.05,ub=max_daily_rate*5.0)    # q_daily  in case first point is late in life
         gekko_q_daily2 = m.FV(lb=max_daily_rate*0.05,ub=max_daily_rate*5.0)    # q_daily
       
      elif 1 == 1:   # STD_OR_SPECIAL == "SPECIAL":
         gekko_q_daily1 = m.FV(lb=max_daily_rate*0.10,ub=max_daily_rate*1.40)    # q_daily
         gekko_q_daily2 = m.FV(lb=max_daily_rate*0.10,ub=max_daily_rate*1.40)    # q_daily
       
      if test_data == "YES":  
         #gekko_h_hyperbolic1 = m.FV(lb=1.01,ub=1.3)   # fracture hyperbolic
         gekko_h_hyperbolic1 = m.FV(lb=minimum_h,ub=maximum_h)   # fracture hyperbolic
      elif typecurve == "YES":   # ND type curve
         gekko_h_hyperbolic1 = m.FV(lb=1.272417,ub=1.272417)   # fracture hyperbolic
      elif 1 == 1:   # STD_OR_SPECIAL == "SPECIAL":
         gekko_h_hyperbolic1 = m.FV(lb=0.19,ub=1.99)   # fracture hyperbolic
         #gekko_h_hyperbolic1 = m.FV(lb=0.01,ub=3.1)   # fracture hyperbolic
 
      if test_data == "YES":
         gekko_h_hyperbolic2 = m.FV(lb=0.01,ub=1.29)   # limit hyperbolic for matrix ?????
         #gekko_h_hyperbolic2 = m.FV(lb=0.01,ub=1.98)   # limit hyperbolic for matrix ?????
 
      elif 1 == 1:
         gekko_h_hyperbolic2 = m.FV(lb=0.03,ub=1.98)   # limit hyperbolic for matrix ?????
      elif 1 == 1:
         gekko_h_hyperbolic2 = m.FV(lb=0.40,ub=1.5)   # could set lb to about 0.4 .................
         

      gekko_d_daily1 = m.FV(lb=0.0,ub=0.03102907)    # 99.9999 yearly
      gekko_d_daily2 = m.FV(lb=0.0,ub=0.03102907)     
      #gekko_d_daily1 = m.FV(lb=0.0,ub=0.01846906)    # 99.9 yearly
      #gekko_d_daily2 = m.FV(lb=0.0,ub=0.01846906)     
      #gekko_d_daily1 = m.FV(lb=0.0,ub=0.01065338)   # 98 yearly
      #gekko_d_daily2 = m.FV(lb=0.0,ub=0.01065338)
   
      gekko_base = m.FV(lb=max_daily_rate*0.0,ub=max_daily_rate*0.0) # set to zero   # base adjustment
      
      gekko_max_daily_rate = m.FV(lb=max_daily_rate,ub=max_daily_rate)  

      # d_daily
      #gekko_d_yearly = m.FV(lb=0.0,ub=99.999999)                            # d_yearly
 
      #d = m.FV(lb=-100.0,ub=100.0)

      # hyperbolic fit this.........................................
      # ym = list_daily_rate       
      # xm = list_days_cumulative    

      # use lists 
      xm = m.Param(value=gekko_time_data)       # GIVEN cumulative days
      #x2 = m.Param(value=list_xm2)  # GIVEN
      #x3 = m.Param(value=list_xm3)  # GIVEN
      ym = m.Param(value=gekko_rate_data)          # GIVEN daily rate   z = ym
 
      yp1 = m.Var()  # fracture                   # y is yp    UNKNOWN
      yp2 = m.Var()  # matrix                    # y is yp    UNKNOWN
      yp = m.Var()                     # y is yp    UNKNOWN

      m.Equation( yp1 == gekko_q_daily1 / ( 1.0 + gekko_h_hyperbolic1 * gekko_d_daily1 * xm ) ** (1.0/gekko_h_hyperbolic1) )
      m.Equation( yp2 == gekko_q_daily2 / ( 1.0 + gekko_h_hyperbolic2 * gekko_d_daily2 * xm ) ** (1.0/gekko_h_hyperbolic2) )
      #m.Equation( yp == gekko_base + yp1 + yp2 )
      m.Equation( yp == yp1 + yp2 )    # do not use base ...
      m.Equation( gekko_q_daily1 + gekko_d_daily2 >= gekko_max_daily_rate ) 

      if test_data == "YES":  
         #m.Equation( gekko_q_daily1 / gekko_q_daily2 >= 1.33 )      # fracture flow >= matrix flow
         #m.Equation( gekko_h_hyperbolic1 / gekko_h_hyperbolic2 >= 2.0 )    # fracture flow >= matrix flow
         m.Equation( gekko_h_hyperbolic1 / gekko_h_hyperbolic2 >= 1.33 )    # fracture flow >= matrix flow
         #m.Equation( gekko_d_daily1 / gekko_d_daily2 >= 1.50 )    # fracture flow >= matrix flow
      elif test_data == "xxxYES":  
         m.Equation( gekko_q_daily1 / gekko_q_daily2 >= 1.33 )      # fracture flow >= matrix flow
         m.Equation( gekko_h_hyperbolic1 / gekko_h_hyperbolic2 >= 2.0 )    # fracture flow >= matrix flow
         m.Equation( gekko_d_daily1 / gekko_d_daily2 >= 1.50 )    # fracture flow >= matrix flow
         #m.Equation( gekko_h_hyperbolic2 <= 0.25 )  # BEST  # fracture flow >= matrix flow
               
      elif typecurve == "YES":   # ND type curve
         #m.Equation( gekko_h_hyperbolic1 / gekko_h_hyperbolic2 >= 1.33 )    # fracture flow >= matrix flow
         m.Equation( gekko_q_daily1 / gekko_q_daily2 >= 1.33 )      # fracture flow >= matrix flow
         m.Equation( gekko_h_hyperbolic1 / gekko_h_hyperbolic2 >= 2.0 )    # fracture flow >= matrix flow
         m.Equation( gekko_d_daily1 / gekko_d_daily2 >= 1.50 )    # fracture flow >= matrix flow
         #m.Equation( gekko_h_hyperbolic2 <= 0.50 )  # FAIR # fracture flow >= matrix flow
         m.Equation( gekko_h_hyperbolic2 <= 0.25 )  # BEST  # fracture flow >= matrix flow
         #m.Equation( gekko_h_hyperbolic2 <= 0.10 ) # too low   # fracture flow >= matrix flow
      
      elif ND_OR_LC == "WELLCODE":
         m.Equation( gekko_h_hyperbolic1 > gekko_h_hyperbolic2 )    # fracture flow >= matrix flow
         m.Equation( gekko_q_daily1 / gekko_q_daily2 >= 1.33 )    # fracture flow >= matrix flow
      elif monthly_or_yearly == "DAILY" and ND_OR_LC == "ND":
         #m.Equation( gekko_h_hyperbolic1 / gekko_h_hyperbolic2 >= 1.33 )    # fracture flow >= matrix flow
         m.Equation( gekko_q_daily1 / gekko_q_daily2 >= 1.33 )      # fracture flow >= matrix flow
         m.Equation( gekko_h_hyperbolic1 / gekko_h_hyperbolic2 >= 2.0 )    # fracture flow >= matrix flow
         m.Equation( gekko_d_daily1 / gekko_d_daily2 >= 1.50 )    # fracture flow >= matrix flow
         #m.Equation( gekko_h_hyperbolic2 <= 0.50 )  # FAIR # fracture flow >= matrix flow
         m.Equation( gekko_h_hyperbolic2 <= 0.25 )  # BEST  # fracture flow >= matrix flow
         #m.Equation( gekko_h_hyperbolic2 <= 0.10 ) # too low   # fracture flow >= matrix flow
      elif 1 == 1:
         m.Equation( gekko_h_hyperbolic1 / gekko_h_hyperbolic2 >= 1.33 )    # fracture flow >= matrix flow

         
         #m.Equation( gekko_h_hyperbolic1 > gekko_h_hyperbolic2 )    # fracture flow >= matrix flow
 
         #m.Equation( gekko_q_daily1 / gekko_q_daily2 >= 1.5 )    # fracture flow >= matrix flow
         #m.Equation( gekko_h_hyperbolic1 >= gekko_h_hyperbolic2 )   # will this work ?????

      #m.Equation(y==a*(x1**b)*(x2**c)*(x3**d))
      #m.Equation( gekko_d_daily == 1 - (( 100.0 - gekko_d_yearly ) / 100.0) ** (1./365.0) )  

      # D_DAILY = 1 - (( 100.0 - D_YEARLY ) / 100.0) ^ (1/365.00)

      m.Obj(((yp-ym)/ym)**2)

      # Options
      gekko_base.STATUS = 1
      gekko_q_daily1.STATUS = 1
      gekko_q_daily2.STATUS = 1 
      gekko_h_hyperbolic1.STATUS = 1
      gekko_h_hyperbolic2.STATUS = 1
      gekko_d_daily1.STATUS = 1
      gekko_d_daily2.STATUS = 1

      #gekko_d_yearly.STATUS = 1
 
      #d.STATUS = 1
      m.options.IMODE = 2
      m.options.SOLVER = 1

      # Solve
      m.solve()

      q_daily1 = gekko_q_daily1.value[0]             # convert from gekko to variable
      q_daily2 = gekko_q_daily2.value[0]             # convert from gekko to variable
 
      h_hyperbolic1 = gekko_h_hyperbolic1.value[0]
      h_hyperbolic2 = gekko_h_hyperbolic2.value[0]
 
      d_daily1 = gekko_d_daily1.value[0]
      d_daily2 = gekko_d_daily2.value[0]
   
      base = gekko_base.value[0]
   
      #d_yearly = gekko_d_yearly.value[0]
 
 
      c1 = "q_daily1 fracture = " + str(q_daily1)
      print (c1)

      c2 = "q_daily2 matrix = " + str(q_daily2)
      print (c2)


      c3 = "h_hyperbolic fracture = " + str(h_hyperbolic1)
      print (c3)

      c4 = "h_hyperbolic matrix = " + str(h_hyperbolic2)
      print (c4)

      #print (c2)

      c5 = "d_daily fracture = " + str(d_daily1)
      print (c5)

      c6 = "d_daily matrix = " + str(d_daily2)
      print (c6)

      #print (c3)
      """ 
      c7 = "d_yearly fracture = " + str(d_yearly1)
      c8 = "d_yearly matrix = " + str(d_yearly2)
      """
      cFormula = "Formula is : " + "\n" + "Two Phase Hyperbolic Equation"

      #print (c3)
      #print (c4)
      #input("Press ENTER to continue...")



    
      if iloop == 1: 

         #values = fig_d_yearly_nominal (d_daily1)     # call GEKKO
         #d_yearly1 = 100.0 * values[0]   # as a percent
         d_yearly1 = 99.99   # not needed yet

         #values = fig_d_yearly_nominal (d_daily2)     # call GEKKO
         #d_yearly2 = 100.0 * values[0]   # as a percent
         d_yearly2 = 99.99   # not needed yet

      elif iloop >= 2: 

         values = fig_d_yearly_nominal (d_daily1)     # call GEKKO    # could modify to calc both at same time
         d_yearly1 = 100.0 * values[0]   # as a percent

         values = fig_d_yearly_nominal (d_daily2)     # call GEKKO
         d_yearly2 = 100.0 * values[0]   # as a percent


      c7 = "d_yearly fracture (percent) = " + str(d_yearly1)
      print (c7)
 
      c8 = "d_yearly matrix (percent) = " + str(d_yearly2)
      print (c8)
      #input("Press ENTER to continue...")

     

      #cFormula = "Formula is : " + "\n" + \
      #           r"$A * WTI^B * HH^C * PROPANE^D$"



      from scipy import stats
      slope, intercept, r_value, p_value, \
                 std_err = stats.linregress(ym, yp)   # GEKKO variables ... # numpy array

      r2 = r_value**2 
      cR2 = "R^2 correlation = " + str(r_value**2)
      print(cR2)


      old_data_points = len(rate_data)
      if iloop == 1:   # ND_OR_LC == "WELLCODE":
      
         values = fig_remove_outlier_points (ym, yp, rate_data, time_data, ND_OR_LC, study_product)
         new_smoothed_rate_data = values[0]
         new_smoothed_time_data = values[1]
            
         rate_data = new_smoothed_rate_data
         time_data = new_smoothed_time_data
  
         new_data_points = len(rate_data)
         cstr = "old data points = " + str(old_data_points)
         cstr += "   new data points = " + str(new_data_points) + " after removing outliers"
         print(cstr)
         cPoints1 = "Original points included = " + str(old_data_points)
         print(cPoints1)
         cPoints2 = "Points after removing outliers = " + str(new_data_points)
         print(cPoints2)
         #cPoints = "Points included after removing outliers = " + str(new_data_points)
         #print(cPoints)
         #input("Press ENTER to continue...")


      cLegend = cFormula + "\n" + c1 + "\n" + c2 + "\n" + c3 + "\n" + c4 + "\n"
      
      if iloop == 1:   # ND_OR_LC == "WELLCODE":
         cLegend += c5 + "\n" + c6 + "\n" + c7 + "\n" + c8 + "\n" + cR2 
      elif 1 == 1:   
          cLegend += c5 + "\n" + c6 + "\n" + c7 + "\n" + c8 + "\n" + cR2 + "\n" + cPoints1 + "\n" + cPoints2

      #cLegend = "NOT YET"
          
      if iloop == 2:  # only show final plot  

         # plot solution
         plt.figure(1)
         #plt.plot([20,140],[20,140],'k-',label='Measured')
         plt.title("Best Fit Analysis of TWO PHASE Hyperbolic Curve Fitting for loop = " + str(iloop))
 
         #plt.plot(ym,yp,'ro',label='Predicted')           # numpy array
         plt.scatter(ym,yp, color='black', s=2)

         plt.xlabel('Measured Outcome (YM)')
         plt.ylabel('Predicted Outcome (YP)')
   
         #plt.legend(loc='best')
         plt.legend([cLegend])

         #plt.text(25,115,'q_daily =' + str(q_daily.value[0]))
         #plt.text(25,110,'h_hyperbolic =' + str(h_hyperbolic.value[0]))
         #plt.text(25,105,'d_daily =' + str(d_daily.value[0]))
         #plt.text(25,100,'d =' + str(d.value[0]))
         #plt.text(25,90,r'$R^2$ =' + str(r_value**2))
         #plt.text(80,40,cFormula)
         plt.grid(True)
         plt.show()
 
      if 1 == 2:   # monthly_or_yearly == "DAILY" and ND_OR_LC == "ND":
         iloop = iloop + 100    # only 1 loop !!!
      elif 1 == 1:
         iloop = iloop + 1
   
      
   if d_daily1 == 0.0:
      d_daily1 = 0.000001
   if d_daily2 == 0.0:
      d_daily2 = 0.000001
   if d_yearly1 == 0.0:
      d_yearly1 = 0.000001
   if d_yearly2 == 0.0:
      d_yearly2 = 0.000001      
  
   #return [q_daily, h_hyperbolic, d_daily, d_yearly]   # return a list
   return [max_daily_rate, q_daily1, q_daily2, h_hyperbolic1, h_hyperbolic2, d_daily1, d_daily2, d_yearly1, d_yearly2, base]   # return a list



                                                                            
def fit_hyperbolic_one_phase ( rate_data, time_data):

   aa = 1
   

   # smooth ........
   
   
   if 1 == 1:   # DAY_OR_MONTH == "DAY":
      gekko_rate_data = rate_data
      gekko_time_data = time_data
      max_daily_rate = gekko_rate_data[0]
      cstr = "max daily rate = " + str(max_daily_rate)
      print(cstr)
      gekko_time_data = time_data
   elif monthly_or_yearly == "YEAR":
      gekko_rate_data = []
      gekko_time_data = []
      data_points = len(rate_data)
      for i in range(data_points):
         if i == 0: 
            any_cum_days = i + (365.25/2.)     # 0 = 365/2    1 = 1 + 365/2
         elif 1 == 1:
             any_cum_days += 365.25
    
         gekko_time_data.append(any_cum_days)
         any_annual_volume = rate_data[i]
         any_daily_volume = any_annual_volume / 365.25
         gekko_rate_data.append(any_daily_volume)       
      max_daily_rate = gekko_rate_data[0]           #   fix to use max function .....
      cstr = "max daily rate = " + str(max_daily_rate)
      print(cstr)

      print(gekko_time_data)
      input("Press ENTER to continue...")
      
      print(gekko_rate_data)
      input("Press ENTER to continue...")

      # fix for MONTH .....




   # start GEKKO code here .........................

   # GEKKO model
   m = GEKKO()
   
   if 1 == 1:   # STD_OR_SPECIAL == "SPECIAL":
       gekko_q_daily = m.FV(lb=max_daily_rate*0.60,ub=max_daily_rate*1.40)    # q_daily
       
   if 1 == 1:   # STD_OR_SPECIAL == "SPECIAL":
      gekko_h_hyperbolic = m.FV(lb=0.01,ub=2.1)
     
   gekko_d_daily = m.FV(lb=0.0,ub=0.2)                                    # d_daily
   #gekko_d_yearly = m.FV(lb=0.0,ub=99.999999)                            # d_yearly
 
   #d = m.FV(lb=-100.0,ub=100.0)

   # hyperbolic fit this.........................................
   # ym = list_daily_rate       
   # xm = list_days_cumulative    

   # use lists 
   xm = m.Param(value=gekko_time_data)       # GIVEN cumulative days
   #x2 = m.Param(value=list_xm2)  # GIVEN
   #x3 = m.Param(value=list_xm3)  # GIVEN
   ym = m.Param(value=gekko_rate_data)          # GIVEN daily rate   z = ym
 
   #y1 = m.Var()                     # y is yp    UNKNOWN
   yp = m.Var()                     # y is yp    UNKNOWN

   #m.Equation( yp == y1 )
   
   m.Equation( yp == gekko_q_daily / ( 1.0 + gekko_h_hyperbolic * gekko_d_daily * xm ) ** (1.0/gekko_h_hyperbolic) )

   #m.Equation(y==a*(x1**b)*(x2**c)*(x3**d))
   #m.Equation( gekko_d_daily == 1 - (( 100.0 - gekko_d_yearly ) / 100.0) ** (1./365.0) )  

   # D_DAILY = 1 - (( 100.0 - D_YEARLY ) / 100.0) ^ (1/365.00)

   m.Obj(((yp-ym)/ym)**2)

   # Options
   gekko_q_daily.STATUS = 1
   gekko_h_hyperbolic.STATUS = 1
   gekko_d_daily.STATUS = 1
   #gekko_d_yearly.STATUS = 1
 
   #d.STATUS = 1
   m.options.IMODE = 2
   m.options.SOLVER = 1

   # Solve
   m.solve()

   q_daily = gekko_q_daily.value[0]             # convert from gekko to variable
   h_hyperbolic = gekko_h_hyperbolic.value[0]
   d_daily = gekko_d_daily.value[0]
   #d_yearly = gekko_d_yearly.value[0]
 
 
   c1 = "q_daily = " + str(q_daily)
   #print (c1)

   c2 = "h_hyperbolic = " + str(h_hyperbolic)
   #print (c2)

   c3 = "d_daily = " + str(d_daily)
   #print (c3)

   #c4 = "d_yearly = " + str(d_yearly)

   cFormula = "Formula is : " + "\n" + "Hyperbolic Equation"

   #print (c3)
   #print (c4)
   #input("Press ENTER to continue...")
 
   # now calculate d_yearly from d_daily

   values = fig_d_yearly_nominal (d_daily)     # call GEKKO
   d_yearly = 100.0 * values[0]   # as a percent

   c4 = "d_yearly (percent) = " + str(d_yearly)
   

   
   #print('d: ', d.value[0])

   #cFormula = "Formula is : " + "\n" + \
   #           r"$A * WTI^B * HH^C * PROPANE^D$"

   from scipy import stats
   slope, intercept, r_value, p_value, \
          std_err = stats.linregress(ym, yp)   # GEKKO variables ... # numpy array

   r2 = r_value**2 
   cR2 = "R^2 correlation = " + str(r_value**2)
   print(cR2)
   
   cLegend = cFormula + "\n" + c1 + "\n" + c2 + "\n" + c3 + "\n" + c4 + "\n" + cR2
   
   # plot solution
   plt.figure(1)
   #plt.plot([20,140],[20,140],'k-',label='Measured')
   plt.title("Best Fit Analysis of ONE PHASE Hyperbolic Curve Fitting")
 
   #plt.plot(ym,yp,'ro',label='Predicted')           # numpy array
   plt.scatter(ym,yp, color='red', s=1)

   plt.xlabel('Measured Outcome (YM)')
   plt.ylabel('Predicted Outcome (YP)')
   
   #plt.legend(loc='best')
   plt.legend([cLegend])

   #plt.text(25,115,'q_daily =' + str(q_daily.value[0]))
   #plt.text(25,110,'h_hyperbolic =' + str(h_hyperbolic.value[0]))
   #plt.text(25,105,'d_daily =' + str(d_daily.value[0]))
   #plt.text(25,100,'d =' + str(d.value[0]))
   #plt.text(25,90,r'$R^2$ =' + str(r_value**2))
   #plt.text(80,40,cFormula)
   plt.grid(True)
   plt.show()
  
   return [q_daily, h_hyperbolic, d_daily, d_yearly]   # return a list





"""



! two phase hyperbolic
!   yp[1:ROWS] = BASE + ( Q_DAILY1 / ( 1.0 + H_HYPERBOLIC1 * D_DAILY1 * xm[1:ROWS] ) ^ (1.0/H_HYPERBOLIC1) ) + ( Q_DAILY2 / ( 1.0 + H_HYPERBOLIC2 * D_DAILY2 * xm[1:ROWS] ) ^ (1.0/H_HYPERBOLIC2) )

   yp[1:ROWS] = BASE + FRACTURE[1:ROWS] + MATRIX[1:ROWS]
   FRACTURE[1:ROWS] = ( Q_DAILY1 / ( 1.0 + H_HYPERBOLIC1 * D_DAILY1 * xm[1:ROWS] ) ^ (1.0/H_HYPERBOLIC1) )
   MATRIX[1:ROWS]   = ( Q_DAILY2 / ( 1.0 + H_HYPERBOLIC2 * D_DAILY2 * xm[1:ROWS] ) ^ (1.0/H_HYPERBOLIC2) )

   minimize   ( (ym[1:ROWS] - yp[1:ROWS]) / ym[1:ROWS] ) ^2
!   minimize    WF_VOL[1:ROWS] * ( (ym[1:ROWS] - yp[1:ROWS]) / ym[1:ROWS] ) ^2
!   minimize    ( 0.50 * ( WF_TIME[1:ROWS] + WF_VOL[1:ROWS] ) ) * ( (ym[1:ROWS] - yp[1:ROWS]) / ym[1:ROWS] ) ^2
!   minimize    WF_AVE[1:ROWS] * ( (ym[1:ROWS] - yp[1:ROWS]) / ym[1:ROWS] ) ^2

  INLINE, CSV_2D_TO_1D, C:\WEL_ADS\HYPERBOLIC.CSV, YM, XM_MO, ROWS, 2

 ! INLINE, WF_DECREASING, WF, ROWS

!  INLINE, CSV_2D_TO_1D, C:\WEL_ADS\DECREASING_W.CSV, WEIGHT_FACTOR, ROWS, 1

  End Equations

  End Model

"""


def fig_hyperbolic_cumulative_volume (q_daily, h_hyperbolic, d_daily, time_days):

   any_exp = (1 - h_hyperbolic) / h_hyperbolic
   any_left = q_daily / (d_daily * ( 1 - h_hyperbolic))
   any_right_inner = 1 + (h_hyperbolic * d_daily * time_days)
   any_right_term = any_right_inner ** any_exp

   any_cum_volume = any_left * (1 - 1/any_right_term)                  

   return any_cum_volume


def fig_twophase_cumulative_volume (q_daily1, h_hyperbolic1, d_daily1, q_daily2, h_hyperbolic2, d_daily2, time_days):

   any_exp1 = (1 - h_hyperbolic1) / h_hyperbolic1
   any_left1 = q_daily1 / (d_daily1 * ( 1 - h_hyperbolic1))
   any_right_inner1 = 1 + (h_hyperbolic1 * d_daily1 * time_days)
   any_right_term1 = any_right_inner1 ** any_exp1

   any_cum_volume1 = any_left1 * (1 - 1/any_right_term1)

   any_exp2 = (1 - h_hyperbolic2) / h_hyperbolic2
   any_left2 = q_daily2 / (d_daily2 * ( 1 - h_hyperbolic2))
   any_right_inner2 = 1 + (h_hyperbolic2 * d_daily2 * time_days)
   any_right_term2 = any_right_inner2 ** any_exp2

   any_cum_volume2 = any_left2 * (1 - 1/any_right_term2)                  


   return any_cum_volume1 + any_cum_volume2


def fig_hyperbolic_economic_days (q_daily, h_hyperbolic, d_daily, any_economic_rate):

  day_counter = 0
  is_economic = "YES"
  any_economic_days = 0
  while is_economic == "YES":
          
     day_counter = day_counter + 1
     any_current_rate = fig_hyperbolic_q_at_time_t (q_daily, h_hyperbolic, d_daily, day_counter)  # rate per day at time t (days)
     if any_current_rate < any_economic_rate:
        is_economic = "NO"
        any_economic_days = day_counter
           
  return any_economic_days


def fig_twophase_economic_days (q_daily1, h_hyperbolic1, d_daily1, q_daily2, h_hyperbolic2, d_daily2, any_economic_rate): 

  day_counter = 0
  is_economic = "YES"
  any_economic_days = 0
  while is_economic == "YES":
          
     day_counter = day_counter + 1
     any_current_rate = fig_twophase_q_at_time_t (q_daily1, h_hyperbolic1, d_daily1, q_daily2, h_hyperbolic2, d_daily2, day_counter)
     if any_current_rate < any_economic_rate:
        is_economic = "NO"
        any_economic_days = day_counter
           
  return any_economic_days





def fig_hyperbolic_q_at_time_t (q_daily, h_hyperbolic, d_daily, time_days):  # rate per day at time t (days)

   #any_exp = (1 - h_hyperbolic) / h_hyperbolic
   #any_left = q_daily / (d_daily * ( 1 - h_hyperbolic))
   #any_right_inner = 1 + (h_hyperbolic * d_daily * time_days)
   #any_right_term = any_right_inner ** any_exp

   #any_cum_volume = any_left * (1 - 1/any_right_term)                  
   any_inner = 1 + (h_hyperbolic * d_daily * time_days)
   any_exp = -1/h_hyperbolic
   any_q_at_time_t = q_daily * (any_inner) ** any_exp

   return any_q_at_time_t

def fig_twophase_q_at_time_t (q_daily1, h_hyperbolic1, d_daily1, q_daily2, h_hyperbolic2, d_daily2, time_days):  # rate per day at time t (days)

   #any_exp = (1 - h_hyperbolic) / h_hyperbolic
   #any_left = q_daily / (d_daily * ( 1 - h_hyperbolic))
   #any_right_inner = 1 + (h_hyperbolic * d_daily * time_days)
   #any_right_term = any_right_inner ** any_exp

   #any_cum_volume = any_left * (1 - 1/any_right_term)

   
   any_inner1 = 1 + (h_hyperbolic1 * d_daily1 * time_days)
   any_exp1 = -1/h_hyperbolic1
   any_q1_at_time_t = q_daily1 * (any_inner1) ** any_exp1

   any_inner2 = 1 + (h_hyperbolic2 * d_daily2 * time_days)
   any_exp2 = -1/h_hyperbolic2
   any_q2_at_time_t = q_daily2 * (any_inner2) ** any_exp2

   return any_q1_at_time_t + any_q2_at_time_t


def fig_hyperbolic_d_yearly_at_time_t (q_daily, h_hyperbolic, d_daily, time_days):    # effective decline rate
 
   # find derivative ...
   
   any_q_at_time_t1 = fig_hyperbolic_q_at_time_t (q_daily, h_hyperbolic, d_daily, time_days - 15.21)
   any_q_at_time_t2 = fig_hyperbolic_q_at_time_t (q_daily, h_hyperbolic, d_daily, time_days + 15.21)
   
   any_decline_for_1_month = (any_q_at_time_t1 - any_q_at_time_t2) / any_q_at_time_t1
   #// 0.10 
   #// 1 + 0.10
   #// 1.10^12 - 1
   any_value = ((1.0 + any_decline_for_1_month) ** 12.0) - 1.0
   return any_value


def fig_twophase_d_yearly_at_time_t (q_daily1, h_hyperbolic1, d_daily1, q_daily2, h_hyperbolic2, d_daily2, time_days):    # effective decline rate
   
   any_q_at_time_t1 = fig_twophase_q_at_time_t (q_daily1, h_hyperbolic1, d_daily1, q_daily2, h_hyperbolic2, d_daily2, time_days - 15.21)
   any_q_at_time_t2 = fig_twophase_q_at_time_t (q_daily1, h_hyperbolic1, d_daily1, q_daily2, h_hyperbolic2, d_daily2, time_days + 15.21)
   
   any_decline_for_1_month = (any_q_at_time_t1 - any_q_at_time_t2) / any_q_at_time_t1
   #// 0.10 
   #// 1 + 0.10
   #// 1.10^12 - 1
   any_value = ((1.0 + any_decline_for_1_month) ** 12.0) - 1.0
   
   return any_value





def fig_hyperbolic_d_daily_at_time_t (q_daily, h_hyperbolic, d_daily, time_days):    # effective decline rate
  
   # find derivative ...
   
   any_q_at_time_t1 = fig_hyperbolic_q_at_time_t (q_daily, h_hyperbolic, d_daily, time_days - 0.5)
   any_q_at_time_t2 = fig_hyperbolic_q_at_time_t (q_daily, h_hyperbolic, d_daily, time_days + 0.5)
   
   any_decline_for_1_day = (any_q_at_time_t1 - any_q_at_time_t2) / any_q_at_time_t1
   #// 0.10 
   #// 1 + 0.10
   #// 1.10^12 - 1
   #any_value = ((1.0 + any_decline_for_1_month) ** 12.0) - 1.0

   #any_value = any_decline_for_1_day 
   
   return any_decline_for_1_day


def fig_twophase_d_daily_at_time_t (q_daily1, h_hyperbolic1, d_daily1, q_daily2, h_hyperbolic2, d_daily2, time_days):    # effective decline rate
  
   # find derivative ...
   
   any_q_at_time_t1 = fig_twophase_q_at_time_t (q_daily1, h_hyperbolic1, d_daily1, q_daily2, h_hyperbolic2, d_daily2, time_days - 0.5)
   any_q_at_time_t2 = fig_twophase_q_at_time_t (q_daily1, h_hyperbolic1, d_daily1, q_daily2, h_hyperbolic2, d_daily2, time_days + 0.5)
   
   any_decline_for_1_day = (any_q_at_time_t1 - any_q_at_time_t2) / any_q_at_time_t1
   #// 0.10 
   #// 1 + 0.10
   #// 1.10^12 - 1
   #any_value = ((1.0 + any_decline_for_1_month) ** 12.0) - 1.0

   #any_value = any_decline_for_1_day 
   
   return any_decline_for_1_day



def moving_average (values, window):
    weights = np.repeat(1.0, window)/window
    sma = np.convolve(values, weights, 'same')
    return sma

  

def fig_d_yearly_nominal (d_daily):
   
   if 1 == 1:
      
      if 1 == 1:
         
         nominal_yearly = 1 - ( 1 - d_daily) ** 365.25
         d_yearly_nominal = 1.00 * nominal_yearly
         #cstr = "nominal yearly = " + str(d_yearly_nominal)
         #print(cstr)     
         #input("Press ENTER to continue...")
            
      elif 1 == 1:
         
         # now calculate d_yearly from d_daily
   
         # start GEKKO code here to calculate d_yearly ........................

         # GEKKO model
         m = GEKKO()
       
         gekko_d_daily = m.FV(lb=d_daily,ub=d_daily)                            # d_daily
         gekko_d_yearly_nominal = m.FV(lb=0.0000001,ub=0.9999999)               # d_yearly
         gekko_d_yearly_adjusted = m.FV(lb=0.00000001,ub=0.999999)              # d_yearly
         #d = m.FV(lb=-100.0,ub=100.0)

         # hyperbolic fit this.........................................
         # ym = list_daily_rate       
         # xm = list_days_cumulative    

         # use lists 
         #xm = m.Param(value=list_days_cumulative)     # GIVEN
         #x2 = m.Param(value=list_xm2)  # GIVEN
         #x3 = m.Param(value=list_xm3)  # GIVEN
         #ym = m.Param(value=list_daily_rate)   # GIVEN  z = ym
 
         #yp = m.Var()                     # y is yp    UNKNOWN

         #m.Equation( yp == gekko_q_daily / ( 1.0 + gekko_h_hyperbolic * gekko_d_daily * xm ) ** (1.0/gekko_h_hyperbolic) )  
         #m.Equation(y==a*(x1**b)*(x2**c)*(x3**d))
         m.Equation( gekko_d_yearly_adjusted == (1.0 - gekko_d_yearly_nominal ) ** (1./365.25) )  
         m.Equation( gekko_d_daily == 1 - gekko_d_yearly_adjusted )  
         #m.Equation( gekko_d_daily == 1 - (( 100.0 - gekko_d_yearly ) / 100.0) ** (1./365.25) )  

         # D_DAILY = 1 - (( 100.0 - D_YEARLY ) / 100.0) ^ (1/365.00)

         #m.Obj(((yp-ym)/ym)**2)

         # Options
         #gekko_q_daily.STATUS = 1
         #gekko_h_hyperbolic.STATUS = 1
         gekko_d_daily.STATUS = 1
         gekko_d_yearly_adjusted.STATUS = 1
         gekko_d_yearly_nominal.STATUS = 1

         #d.STATUS = 1
         m.options.IMODE = 2
         m.options.SOLVER = 1

         # Solve
         m.solve()

         #q_daily = gekko_q_daily.value[0]             # convert from gekko to variable
         #h_hyperbolic = gekko_h_hyperbolic.value[0]
         d_daily = gekko_d_daily.value[0]
         d_yearly_adjusted = gekko_d_yearly_adjusted.value[0]
         d_yearly_nominal = gekko_d_yearly_nominal.value[0]
         
         d_yearly = d_yearly_nominal * 100.0     # as a percent

         temp1 = "d_daily = " + str(d_daily)
         temp2 = "d_yearly_nominal = " + str(d_yearly_nominal)
         temp3 = "d_yearly_adjusted = " + str(d_yearly_adjusted)
         print (temp1)
         print (temp2)
         print (temp3)
         
         #c1 = "q_daily = " + str(q_daily)
         #c2 = "h_hyperbolic = " + str(h_hyperbolic)
         #c3 = "d_daily = " + str(d_daily) + " as decimal"
         #c4 = "d_yearly = " + str(d_yearly) + " as percent"
         #c5 = "d_yearly_adjusted = " + str(d_yearly_adjusted)
         #cFormula = "Formula is : " + "\n" + "Hyperbolic Equation"

         #print (c3)
         #print (c4)
         #print (c5)

         #input("Press ENTER to continue...")
 

   return [d_yearly_nominal]   # return a list




 






