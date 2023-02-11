
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



def fig_superposition_rate (rate_data, time_data, ND_OR_LC, study_product, display_plot, list_volume_cumulative):
   
   how_many_string = AlertBox("How many points to include for last average rate: 1, 2, 3, 4, 5, 6 or 7")
   how_many = float(how_many_string)
   
   any_points = len(rate_data)
   any_max_rate = max(rate_data)

   more = "YES"
   #any_factor = 0
   counter = 0
   
   old_super_exponent = 0.50
   any_super_exponent = 0.50   # 1.50
   
   while counter <= 18 and more == "YES":   # vary this ..........
          
      counter = counter + 1
      
      e_constant = 2.71828182845904523536028
      
      super_rate_data = []
      
      #print("")
      print("")
      print("superposition calculations")
      

      if 1 == 2:
         rate_data = [ 478.5,  478.5,  478.5,   319.0,  159.5,  159.5,  159.5]  # Qn
         time_data = [0.333,  0.666,   1.00,    2.0,    2.333,  2.666,  3.0]
      elif 1 == 2:
         rate_data = [ 200.0,  150.0,  100.0,   80.0]      # Qn
         time_data = [0.10, 0.13, 0.16, 0.20]


      if 1 == 1:
         fudge_factor = 1.0
      elif 1 == 1:   
         fudge_factor = 0.50 * 0.75 * 0.84 * 0.825 * 1.10 * 0.957 * 0.956
    
      LOG_OR_LN = "LOG"
      #LOG_OR_LN = "LN"   # DO NOT USE LN......

      #TIME_OR_RATE = "TIME"
      TIME_OR_RATE = "RATE"

      RADIAL_OR_LINEAR = "LOOP"
      #RADIAL_OR_LINEAR = "RADIAL"
      #RADIAL_OR_LINEAR = "0.80"  # too flat
      #RADIAL_OR_LINEAR = "1.00"   # too flat
      #RADIAL_OR_LINEAR = "1.1"   # too flat
      #RADIAL_OR_LINEAR = "1.42"     # too flat
      #RADIAL_OR_LINEAR = "1.45"     # too flat

      #RADIAL_OR_LINEAR = "1.48"     # too flat

      #RADIAL_OR_LINEAR = "1.50"     # too flat
      #RADIAL_OR_LINEAR = "1.56"   # maybe here .....
      #RADIAL_OR_LINEAR = "1.60"   # maybe here .....

      #RADIAL_OR_LINEAR = "1.63"   # good fit ......... maybe too steep   AKRON 5
      #RADIAL_OR_LINEAR = "1.75"  # too steep  
  
      #RADIAL_OR_LINEAR = "LINEAR"  # 2.0  # too steep
      #RADIAL_OR_LINEAR = "BILINEAR"


      data_points = len(rate_data)
      
      #cstr = "data_points = " + str(data_points) 
      #print(cstr)
            
      for i in range(data_points):
               
         if 1 == 1:  # i == 3:
            
            adjust_factor = (i+1.0) / data_points 

            #mid_point = int(data_points/2)
            #if i = mid_point:
            #   fudge_factor = 1.0 
            #elif i < mid_point:
            #   fudge_factor = mid_point - i
            #elif i > mid_point:
            #   fudge_factor = i - mid_point

            #cstr = "fudge_factor = " + str(   

            if 1 == 2:
               adjust_factor2 = 0.25 * 1.05 * 1.15 * 1.15 * 1.1
               any_super_exponent_adjusted = any_super_exponent + (adjust_factor * adjust_factor2)
               cstr = "for i = " + str(i) + "  super exp = " + str(any_super_exponent) + "  adjusted = " + str(any_super_exponent_adjusted)
               print(cstr)
            elif 1 == 1:   
               any_super_exponent_adjusted = any_super_exponent  

           
            list_delta_q = []
            list_delta_t = []
            list_log_delta_t = []
            list_t = []
            sum_of_delta_t = 0
            
            any_time = time_data[i]

            if TIME_OR_RATE == "TIME": 
               #divisor = rate_data[3]    # divisor for superposition of time
               divisor = rate_data[i]     # divisor for superposition of time
            elif TIME_OR_RATE == "RATE": 
               #any_time = time_data[3]
               any_time = time_data[i]
               if LOG_OR_LN == "LOG":
                  if RADIAL_OR_LINEAR == "LOOP":
                     #divisor = any_time ** (1.0/any_super_exponent)            # divisor for superposition of rate
                     divisor = any_time ** (1.0/any_super_exponent_adjusted)    # divisor for superposition of rate
                  elif RADIAL_OR_LINEAR == "RADIAL":
                     divisor = math.log(any_time,10)     # divisor for superposition of rate
                  elif RADIAL_OR_LINEAR == "0.80":
                     divisor = any_time ** (1.0/0.80)    # divisor for superposition of rate
                  elif RADIAL_OR_LINEAR == "1.00":
                     divisor = any_time ** (1.0/1.00)    # divisor for superposition of rate             
                  elif RADIAL_OR_LINEAR == "1.1":
                     divisor = any_time ** (1.0/1.1)    # divisor for superposition of rate
                  elif RADIAL_OR_LINEAR == "1.42":
                     divisor = any_time ** (1.0/1.42)   # divisor for superposition of rate
                  elif RADIAL_OR_LINEAR == "1.45":
                     divisor = any_time ** (1.0/1.45)   # divisor for superposition of rate    
                  elif RADIAL_OR_LINEAR == "1.48":
                     divisor = any_time ** (1.0/1.48)   # divisor for superposition of rate        
                  elif RADIAL_OR_LINEAR == "1.50":
                     divisor = any_time ** (1.0/1.50)   # divisor for superposition of rate
                  elif RADIAL_OR_LINEAR == "1.56":
                     divisor = any_time ** (1.0/1.56)   # divisor for superposition of rate
                  elif RADIAL_OR_LINEAR == "1.60":
                     divisor = any_time ** (1.0/1.60)   # divisor for superposition of rate       
                  elif RADIAL_OR_LINEAR == "1.63":
                     divisor = any_time ** (1.0/1.63)   # divisor for superposition of rate
                  elif RADIAL_OR_LINEAR == "1.75":
                     divisor = any_time ** (1.0/1.75)   # divisor for superposition of rate           
                  elif RADIAL_OR_LINEAR == "LINEAR":
                     divisor = any_time ** 0.50         # 1/2.0 divisor for superposition of rate
                  elif RADIAL_OR_LINEAR == "BILINEAR":
                     divisor = any_time ** 0.25         # divisor for superposition of rate
               elif LOG_OR_LN == "LN":   # DO NOT USE ...
                  divisor = math.log(any_time)        # divisor for superposition of rate
                  #divisor = any_time                 # divisor for superposition of rate
                  
            cstr = TIME_OR_RATE + "   for i = " + str(i) + "   divisor = " + str(divisor) 
            #print(cstr)

            #for i in range(data_points):
            #for j in range(i):
            #for j in range(i):
            for j in range(0, i+1):
               #print("")
               #print("")
               cstr = "for i = " + str(i) + "  and j = " + str(j) + "  starting calculations"
               #print(cstr)

               #delta_q1 = (rate_data[0] - 0.0) / rate_data[3]             # 200 - 0 where 0 is q0
               #delta_q1 = (rate_data[0] - 0.0) / 1.0                      # 200 - 0 where 0 is q0
               if j == 0:
                  any_delta_q = (rate_data[0] - 0.0) / divisor                    # 200 - 0 where 0 is q0
               elif 1 == 1:
                  #delta_q2 = (rate_data[1] - rate_data[0]) / 1.0  # 150 - 200
                  #delta_q3 = (rate_data[2] - rate_data[1]) / 1.0  # 100 - 150
                  #delta_q4 = (rate_data[3] - rate_data[2]) / 1.0  # 80 - 100
                  any_delta_q = (rate_data[j] - rate_data[j-1]) / divisor          # 200 - 0
               
               list_delta_q.append(any_delta_q)

               cstr = "for i = " + str(i) + "  and j = " + str(j) + "  any_delta_q = " + str(any_delta_q)
               #print(cstr)
                     
               if j == 0:
                  #delta_t1 = time_data[3] - 0             # 0.20 - 0 where 0 is t0

                  any_delta_t = time_data[i] - 0             # 0.20 - 0 where 0 is t0
                  
               elif 1 == 1:

                  #delta_t2 = any_time - time_data[0]  # 0.20 - 0.10
                  #delta_t3 = any_time - time_data[1]  # 0.20 - 0.13
                  #delta_t4 = any_time - time_data[2]  # 0.20 - 0.16
                  any_delta_t = time_data[i] - time_data[j-1]
                             
               
               list_delta_t.append(any_delta_t)
                  
               cstr = "for i = " + str(i) + "  and j = " + str(j) + "  delta_t = " + str(any_delta_t)
               #print(cstr)
               
               if RADIAL_OR_LINEAR == "LOOP":
                  #any_log_delta_t = any_delta_t ** (1.0/any_super_exponent)             # square root 
                  any_log_delta_t = any_delta_t ** (1.0/any_super_exponent_adjusted)     # square root 
               elif RADIAL_OR_LINEAR == "RADIAL":
                  any_log_delta_t = math.log(any_delta_t,10)   # log
               elif RADIAL_OR_LINEAR == "0.80":
                   any_log_delta_t = any_delta_t ** (1.0/0.80)     # square root
               elif RADIAL_OR_LINEAR == "1.00":
                   any_log_delta_t = any_delta_t ** (1.0/1.00)     # square root               
               elif RADIAL_OR_LINEAR == "1.1":
                   any_log_delta_t = any_delta_t ** (1.0/1.10)     # square root             
               elif RADIAL_OR_LINEAR == "1.42":
                   any_log_delta_t = any_delta_t ** (1.0/1.42)     # square root
               elif RADIAL_OR_LINEAR == "1.45":
                   any_log_delta_t = any_delta_t ** (1.0/1.45)     # square root     
               elif RADIAL_OR_LINEAR == "1.48":
                   any_log_delta_t = any_delta_t ** (1.0/1.48)     # square root    
               elif RADIAL_OR_LINEAR == "1.50":
                   any_log_delta_t = any_delta_t ** (1.0/1.50)     # square root
               elif RADIAL_OR_LINEAR == "1.56":
                   any_log_delta_t = any_delta_t ** (1.0/1.56)     # square root
               elif RADIAL_OR_LINEAR == "1.60":
                   any_log_delta_t = any_delta_t ** (1.0/1.60)     # square root          
               elif RADIAL_OR_LINEAR == "1.63":
                   any_log_delta_t = any_delta_t ** (1.0/1.63)     # square root    
               elif RADIAL_OR_LINEAR == "1.75":
                   any_log_delta_t = any_delta_t ** (1.0/1.75)     # square root           
               elif RADIAL_OR_LINEAR == "LINEAR":
                   any_log_delta_t = any_delta_t ** 0.50       # (1/2) square root
               elif RADIAL_OR_LINEAR == "BILINEAR":
                   any_log_delta_t = any_delta_t ** 0.25       # (1/4) bilinear 4th root
                            
               cstr = "for i = " + str(i) + "  and j = " + str(j) + "  log_delta_t = " + str(any_log_delta_t)
               #print(cstr)

               list_log_delta_t.append(any_log_delta_t)
                    
               #log_delta_t2 = delta_t2  # math.log(delta_t2, 10)
               #log_delta_t3 = delta_t3  # math.log(delta_t3, 10)
               #log_delta_t4 = delta_t4  # math.log(delta_t4, 10)

               #print("list_delta_q")
               #print(list_delta_q)
               
               #print("list_delta_t")
               #print(list_delta_t)
               
               #print("list_log_delta_t")
               #print(list_log_delta_t)

               any_t = list_delta_q[j] * list_log_delta_t[j] / 1.0   # divisor   # j or j-1 ????
               list_t.append(any_t)
  
               #t1 = delta_q1 * log_delta_t1 / divisor
               cstr = "for i = " + str(i) + "  and j = " + str(j) + "  t = " + str(any_t)
               #print(cstr)
      
               #t2 = delta_q2 * log_delta_t2 / divisor
               #cstr = "t2 = " + str(t2)
               #print(cstr)
      
               #t3 = delta_q3 * log_delta_t3 / divisor
               #cstr = "t3 = " + str(t3)
               #print(cstr)
      
               #t4 = delta_q4 * log_delta_t4 / divisor
               #cstr = "t4 = " + str(t4)
               #print(cstr)
                           
               sum_of_delta_t += any_t

               #sum_of_delta_t = t1 + t2 + t3 + t4
               #cstr = "sum of delta_t = " + str(sum_of_delta_t)
               #print(cstr)
               
            #print("list_t")
            #print(list_t)

            #print("")
            #print("")
  
            cstr = "for i = " + str(i) + "   sum_of_delta_t = " + str(sum_of_delta_t)
            #print(cstr)
            
            if LOG_OR_LN == "LOG":
               if RADIAL_OR_LINEAR == "LOOP":   # too flat
                  #super_t = sum_of_delta_t ** any_super_exponent
                  super_t = sum_of_delta_t ** any_super_exponent_adjusted
               elif RADIAL_OR_LINEAR == "RADIAL":
                  super_t = 10.0 ** sum_of_delta_t
               elif RADIAL_OR_LINEAR == "0.80":   # too flat
                  super_t = sum_of_delta_t ** 0.80
               elif RADIAL_OR_LINEAR == "1.00":
                  super_t = sum_of_delta_t ** 1.00             
               elif RADIAL_OR_LINEAR == "1.1":
                  super_t = sum_of_delta_t ** 1.10
               elif RADIAL_OR_LINEAR == "1.42":
                  super_t = sum_of_delta_t ** 1.42    
               elif RADIAL_OR_LINEAR == "1.45":
                  super_t = sum_of_delta_t ** 1.45
               elif RADIAL_OR_LINEAR == "1.48":
                  super_t = sum_of_delta_t ** 1.48   
               elif RADIAL_OR_LINEAR == "1.50":
                  super_t = sum_of_delta_t ** 1.50
               elif RADIAL_OR_LINEAR == "1.56":
                  super_t = sum_of_delta_t ** 1.56
               elif RADIAL_OR_LINEAR == "1.60":
                  super_t = sum_of_delta_t ** 1.60       
               elif RADIAL_OR_LINEAR == "1.63":
                  super_t = sum_of_delta_t ** 1.63   
               elif RADIAL_OR_LINEAR == "1.75":
                  super_t = sum_of_delta_t ** 1.75         
               elif RADIAL_OR_LINEAR == "LINEAR":
                  super_t = sum_of_delta_t ** 2.0
               elif RADIAL_OR_LINEAR == "BILINEAR":
                  super_t = sum_of_delta_t ** 4.0

            elif LOG_OR_LN == "LN":     # DO NOT USE THIS ........
               super_t = e_constant ** sum_of_delta_t

            super_t = super_t * fudge_factor
               
            cstr = "SUPER OF " + TIME_OR_RATE + " for i = " + str(i) + " = " + str(super_t)
            #print(cstr)
            
            #print("")
            #print("")
  
            super_rate_data.append(super_t)
          

      nLast = len(rate_data)    
      nLast = len(super_rate_data)    

      if how_many == 1:
         last_measured_average = rate_data[nLast-1]
         last_super_average = super_rate_data[nLast-1] 
      elif how_many == 2:
         last_measured_average = rate_data[nLast-1] + rate_data[nLast-2]
         last_super_average = super_rate_data[nLast-1] + super_rate_data[nLast-2] 
      elif how_many == 3:
         last_measured_average = rate_data[nLast-1] + rate_data[nLast-2] + rate_data[nLast-3]
         last_super_average = super_rate_data[nLast-1] + super_rate_data[nLast-2] + super_rate_data[nLast-3]
      elif how_many == 4:
         last_measured_average = rate_data[nLast-1] + rate_data[nLast-2] + rate_data[nLast-3] + rate_data[nLast-4]
         last_super_average = super_rate_data[nLast-1] + super_rate_data[nLast-2] + super_rate_data[nLast-3] + super_rate_data[nLast-4]
      elif how_many == 5:
         last_measured_average = rate_data[nLast-1] + rate_data[nLast-2] + rate_data[nLast-3] + rate_data[nLast-4] + rate_data[nLast-5]
         last_super_average = super_rate_data[nLast-1] + super_rate_data[nLast-2] + super_rate_data[nLast-3] + super_rate_data[nLast-4] + super_rate_data[nLast-5]
      elif how_many == 6:
         last_measured_average = rate_data[nLast-1] + rate_data[nLast-2] + rate_data[nLast-3] + rate_data[nLast-4] + rate_data[nLast-5] + rate_data[nLast-6]
         last_super_average = super_rate_data[nLast-1] + super_rate_data[nLast-2] + super_rate_data[nLast-3] + super_rate_data[nLast-4] + super_rate_data[nLast-5] + super_rate_data[nLast-6]
      elif how_many == 7:
         last_measured_average = rate_data[nLast-1] + rate_data[nLast-2] + rate_data[nLast-3] + rate_data[nLast-4] + rate_data[nLast-5] + rate_data[nLast-6] + rate_data[nLast-7]
         last_super_average = super_rate_data[nLast-1] + super_rate_data[nLast-2] + super_rate_data[nLast-3] + super_rate_data[nLast-4] + super_rate_data[nLast-5] + super_rate_data[nLast-6] + super_rate_data[nLast-7]

      n_rows = len(super_rate_data)
      for i in range(n_rows):
         super_rate_data[i] = super_rate_data[i] * last_measured_average / last_super_average 
        
      """
      for i in range(data_points):
         cstr = "i = " + str(i) + " time = " + str(time_data[i]) + " rate = " + str(rate_data[i]) + " super-rate = " + str(super_rate_data[i]) 
         print(cstr)       
      """
      
      list_super_cumulative = []

      any_super_cumulative = 0 
      n_rows = len(super_rate_data)    

      for i in range(n_rows):
         if i == 0:
            any_delta_days = time_data[0]
         elif 1  == 1:
            any_delta_days = time_data[i] - time_data[i-1]
         any_delta_volume = super_rate_data[i] * any_delta_days
         any_super_cumulative += any_delta_volume

      nLast = len(list_volume_cumulative)    
      any_cumulative_volume = list_volume_cumulative[nLast-1]
             
      cstr = "measured cumulative volume from max rate = " + str(any_cumulative_volume)
      #print(cstr)
      
      cstr = "estimated superposition cumulative volume = " + str(any_super_cumulative)
      #print(cstr)

      if any_super_cumulative >= any_cumulative_volume:
         any_factor = any_super_cumulative / any_cumulative_volume
         cComment = "super exponent " + str(any_super_exponent) + " too high by factor of " + str(any_factor) # + " so exponent of " + RADIAL_OR_LINEAR + " is too high"
         print(cComment)
         #any_factor = (any_factor + (any_factor/2.0)) / 2.0              # gradual change ...
         #any_factor = (any_factor + (any_factor/2.0)) / 2.0              # gradual change ...
         any_super_exponent = any_super_exponent / any_factor
         cComment1 = "next attempt for super exponent = " + str(any_super_exponent) # + " too high by factor of " + str(any_factor) # + " so exponent of " + RADIAL_OR_LINEAR + " is too high"
         #print(cComment1)
      elif any_super_cumulative <= any_cumulative_volume:
         any_factor = any_super_cumulative / any_cumulative_volume
         cComment = "super exponent " + str(any_super_exponent) + " too low by factor of " + str(any_factor) # + " so exponent of " + RADIAL_OR_LINEAR + " is too low"
         print(cComment)
         #any_factor = (any_factor + (any_factor/2.0)) / 2.0              # gradual change ...
         #any_factor = (any_factor + (any_factor/2.0)) / 2.0              # gradual change ...
         any_super_exponent = any_super_exponent / any_factor
         cComment1 = "next attempt for super exponent = " + str(any_super_exponent) # + " too high by factor of " + str(any_factor) # + " so exponent of " + RADIAL_OR_LINEAR + " is too high"
         #print(cComment1)

      any_super_exponent = (any_super_exponent + old_super_exponent) / 2   # gradual change ...
      #any_super_exponent = (any_super_exponent + any_super_exponent + old_super_exponent) / 3   # gradual change ...
      cComment2 = "gradual change for super exponent = " + str(any_super_exponent) # + " too high by factor of " + str(any_factor) # + " so exponent of " + RADIAL_OR_LINEAR + " is too high"
      #print(cComment2) 
      old_super_exponent = any_super_exponent

      if abs(any_factor) >= 0.99 and abs(any_factor) <= 1.01:   # vary convergence ...
         more = "NO"
         
 
      #print("")
      #print("") 
      #raw_input("Press ENTER to continue...")


   any_max_rate = max(rate_data)
   any_max_super_rate = max(super_rate_data)
   print("")

   if any_max_super_rate >= any_max_rate:
      any_factor = any_max_super_rate / any_max_rate
      cComment = "max super rate " + str(any_max_super_rate) + " too high by factor of " + str(any_factor)
      print(cComment)
         
   elif any_max_super_rate <= any_max_rate:
      any_factor = any_max_super_rate / any_max_rate
      cComment = "max super rate " + str(any_max_super_rate) + " too low by factor of " + str(any_factor) 
      print(cComment)
          

   print("")
   print("") 
   raw_input("Press ENTER to continue...")  
   print("") 

   if display_plot == "YES":

      if study_product == "OIL":       
         #cY = "Log(Oil Rate) in BOPD"
         cY = "Oil Rate in BOPD"

      elif study_product == "GAS":       
         #cY = "Log(Gas Rate) in MCFDD"
         cY = "Gas Rate in MCFD"

      D_M_Y = "D"
    
      if D_M_Y == "D":
         cTitle = "Measured Rate and Superposition Rate versus Time in Days\n"
         cNext = "Measured Cumulative Volume = " + str(any_cumulative_volume)
         cTitle += cNext + "\n"
         cNext = "Estimated Superposition Cumulative Volume = " + str(any_super_cumulative)
         cTitle += cNext + "\n"
         #cTitle += cComment + "\n"
         
         cX = "Time in Days"
           
      if 1 == 1:
         
         plt.figure(1)
          
         #cTitle += "Preparing Data For Hyperbolic Prediction (LOG FORM)"
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
            # was yellow
            plt.plot(time_data, super_rate_data, color='black', linestyle='dashed', label='Superposition Rate')
            #plt.plot(temp2_time_data, temp2_rate_data, color='green', linestyle='dashdot', label='Smoothed2')
            #plt.plot(temp3_time_data, temp3_rate_data, color='cyan', linestyle='dotted', label='Smoothed3')
            #plt.plot(temp4_time_data, temp4_rate_data, color='blue', linestyle='dotted', label='Smoothed4')
            #plt.plot(temp5_time_data, temp5_rate_data, color='magenta', linestyle='dashed', label='Smoothed5')
            #plt.plot(temp6_time_data, temp6_rate_data, color='black', linestyle='dashed', label='Smoothed6')

            #plt.xlim(0, max(log_min_value, log_max_value)
            #plt.ylim(0, max(rate_data) * 1.35)
               
         plt.legend(loc='upper right')
         plt.xlabel(cX)
         plt.ylabel(cY)
         if 1 == 1:
            plt.yscale('log')    # works
         plt.grid(True)
         plt.show()

         #plt.yscale('log')    # works
         #plt.show()

   if display_plot == "xxxYES":
     
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
         plt.plot(time_data, rate_data, color='red', linestyle='solid', label='Measured')
         #plt.plot(temp1_time_data, temp1_rate_data, color='yellow', linestyle='dashed', label='Smoothed1')
         #plt.plot(temp2_time_data, temp2_rate_data, color='green', linestyle='dashdot', label='Smoothed2')
         #plt.plot(temp3_time_data, temp3_rate_data, color='cyan', linestyle='dotted', label='Smoothed3')
         #plt.plot(temp4_time_data, temp4_rate_data, color='blue', linestyle='dotted', label='Smoothed4')
         #plt.plot(temp5_time_data, temp5_rate_data, color='magenta', linestyle='dashed', label='Smoothed5')
         plt.plot(final_time_data, final_rate_data, color='black', linestyle='dashed', label='Smoothed')
                 
      plt.legend(loc='upper right')
      plt.xlabel(cX)
      plt.ylabel(cY)
      plt.yscale('log')    # works
      plt.grid(True)
      plt.show()
      
   return [super_rate_data]   # return a list





def fig_superposition_time (rate_data, time_data, ND_OR_LC, study_product, display_plot, list_volume_cumulative):



   if 1 == 1:
      
      print("")
      print("")
      # assume previous point is 0,0 ...
      rate_data = [ 200.0,  150.0,  100.0,   80.0]  # Qn
      time_data = [0.10, 0.13, 0.16, 0.20]
      data_points = len(rate_data)
      
      delta_q1 = (rate_data[0] - 0.0) / rate_data[3]             # 200 - 0 where 0 is q0
      cstr = "delta_q1 = " + str(delta_q1)
      print(cstr)
      
      delta_q2 = (rate_data[1] - rate_data[0]) / rate_data[3]  # 150 - 200
      delta_q3 = (rate_data[2] - rate_data[1]) / rate_data[3]  # 100 - 150
      delta_q4 = (rate_data[3] - rate_data[2]) / rate_data[3]  # 80 - 100
      
      delta_t1 = time_data[3] - 0             # 0.20 - 0 where 0 is t0
      cstr = "delta_t1 = " + str(delta_t1)
      print(cstr)
       
      delta_t2 = time_data[3] - time_data[0]  # 0.20 - 0.10
      delta_t3 = time_data[3] - time_data[1]  # 0.20 - 0.13
      delta_t4 = time_data[3] - time_data[2]  # 0.20 - 0.16
      
      log_delta_t1 = math.log(delta_t1,10)
      cstr = "log_delta_t1 = " + str(log_delta_t1)
      print(cstr)
      
      log_delta_t2 = math.log(delta_t2, 10)
      log_delta_t3 = math.log(delta_t3, 10)
      log_delta_t4 = math.log(delta_t4, 10)

      t1 = delta_q1 * log_delta_t1
      cstr = "t1 = " + str(t1)
      print(cstr)
      
      t2 = delta_q2 * log_delta_t2
      cstr = "t2 = " + str(t2)
      print(cstr)
      
      t3 = delta_q3 * log_delta_t3
      cstr = "t3 = " + str(t3)
      print(cstr)
      
      t4 = delta_q4 * log_delta_t4
      cstr = "t4 = " + str(t4)
      print(cstr)
      
      sum_of_delta_t = t1 + t2 + t3 + t4
      cstr = "super of delta_t = " + str(sum_of_delta_t)
      print(cstr)
      
      super_t = 10.0 ** sum_of_delta_t
      cstr = "super t = " + str(super_t)
      print(cstr)
      
      #qn1 = rate_data[0]           # flow rate during first flow period
      #cstr = "qn1 = " + str(qn1)
      #print(cstr)
      #recip_rate1 = 1.0 / rate_data[0]
      #cstr = "recip_rate1 = " + str(recip_rate1)
      #print(cstr)
   
      #t_start1 = 0
      #t_end1 = time_data[0]
 
      #sum_term1 = t_end1 - t_start1
      #cstr = "sum_term1 = " + str(sum_term1) 
      #print(cstr)  
      #log_sum_term1 = math.log(sum_term1, 10)   # base 10
      #ln_sum_term1 = math.log(sum_term1)          # base e
      #cstr = "log_sum_term1 = " + str(log_sum_term1) 
      #print(cstr)  
      #result1 = recip_rate1 * delta_q1 * log_sum_term1
      #cstr = "super rate result1 = " + str(result1)
      #print(cstr)
      #result2 = 10 ** result1
      #cstr = "super rate result2 = " + str(result2)
      #print(cstr)
     
      print("")
      print("") 
      raw_input("Press ENTER to continue...")

   elif 1 == 2:
      
      print("")
      print("")
      # assume previous point is 0,0 ...
      rate_data = [ 200,  150,  100,   80]  # Qn
      time_data = [0.10, 0.13, 0.16, 0.20]
      data_points = len(rate_data)
      delta_q1 = rate_data[0] - 0  # where 0 is q0
      cstr = "delta_q1 = " + str(delta_q1)
      print(cstr)
      qn1 = rate_data[0]           # flow rate during first flow period
      cstr = "qn1 = " + str(qn1)
      print(cstr)
      recip_rate1 = 1.0 / rate_data[0]
      cstr = "recip_rate1 = " + str(recip_rate1)
      print(cstr)
   
      t_start1 = 0
      t_end1 = time_data[0]
 
      sum_term1 = t_end1 - t_start1
      cstr = "sum_term1 = " + str(sum_term1) 
      print(cstr)  
      log_sum_term1 = math.log(sum_term1, 10)   # base 10
      #ln_sum_term1 = math.log(sum_term1)          # base e
      cstr = "log_sum_term1 = " + str(log_sum_term1) 
      print(cstr)  
      result1 = recip_rate1 * delta_q1 * log_sum_term1
      cstr = "super rate result1 = " + str(result1)
      print(cstr)
      result2 = 10 ** result1
      cstr = "super rate result2 = " + str(result2)
      print(cstr)
     
      print("")
      print("") 
      raw_input("Press ENTER to continue...")





   #for i in range(data_points):
   #   any_calc 

   """
   !C
   !C CALCULATE SUPERPOSITION OF TIME (SUM)
   !C NOTE THAT SUPERPOSITION OF TIME IS NOT AFFECTED BY TURBULENCE
   !C
          data_points = len(rate_data)
          DO 189 II = 1,POINTS
          for i in range(data_points):
 
          DO 165 JJ = 1,II
            IF (JJ .EQ. 1) THEN
            SUM(JJ)=1.0*XXRATE(JJ)*LOG10(HRS(II))/(1.0*XXRATE(II))
            ELSEIF (JJ .GE. 2) THEN
            SUM(JJ) = (XXRATE(JJ) - XXRATE(JJ-1)) * LOG10( HRS(II) - HRS(JJ-1) ) / (1.0 * XXRATE(II))
            ENDIF
            TSUMJ(II) = TSUMJ(II) + SUM(JJ)
    165   CONTINUE
    189   CONTINUE

          DO 200 II=1,POINTS
       SUPER(II) = 10.**TSUMJ(II)
   !C      IF (SUPER(II) .GE. 999999.) SUPER(II) = 999999.
          IF (SUPER(II) .GE.  99999.) SUPER(II) =  99999.
    200   CONTINUE
   !C
   !C CALCULATE AVERAGE TIME BETWEEN HRS AND SUPER
          DO 248 II=1,POINTS
          HRSMID(II) = (HRS(II) + SUPER(II)) / 2.
         LOGMID(II) = LOG10(HRSMID(II))
    248   CONTINUE
   !C
   """


   """
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
      #raw_input("Press ENTER to continue...")

      #print("temp1_rate_data")
      #print(temp1_rate_data)
      #raw_input("Press ENTER to continue...")
         
     

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
         plt.plot(time_data, rate_data, color='red', linestyle='solid', label='Measured')
         #plt.plot(temp1_time_data, temp1_rate_data, color='yellow', linestyle='dashed', label='Smoothed1')
         #plt.plot(temp2_time_data, temp2_rate_data, color='green', linestyle='dashdot', label='Smoothed2')
         #plt.plot(temp3_time_data, temp3_rate_data, color='cyan', linestyle='dotted', label='Smoothed3')
         #plt.plot(temp4_time_data, temp4_rate_data, color='blue', linestyle='dotted', label='Smoothed4')
         #plt.plot(temp5_time_data, temp5_rate_data, color='magenta', linestyle='dashed', label='Smoothed5')
         plt.plot(final_time_data, final_rate_data, color='black', linestyle='dashed', label='Smoothed')
                 
      plt.legend(loc='upper right')
      plt.xlabel(cX)
      plt.ylabel(cY)
      plt.yscale('log')    # works
      plt.grid(True)
      plt.show()


      
   return [final_rate_data, final_time_data]   # return a list
   """









