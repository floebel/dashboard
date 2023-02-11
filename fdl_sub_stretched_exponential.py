
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


                                                                            
def fit_stretched_exponential ( rate_data, time_data, monthly_or_yearly, ND_OR_LC, study_product, test_data ):

   #e_constant = 2.71828
   
  
   iloop = 1
   while (iloop <= 2):
      
      smooth_data = "YES"
      if monthly_or_yearly == "DAILY" and ND_OR_LC == "ND":
         #smooth_data = "NO"
         smooth_data = "YES"
 
      elif iloop >= 2:
         smooth_data = "NO"
  
      if smooth_data == "YES":

         display_plot = "YES"
         if iloop >= 2:
            display_plot = "NO"
   
         values = fig_smoothed_data (rate_data, time_data, ND_OR_LC, study_product, display_plot)
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
      
      
      if 1 == 1:   # DAY_OR_MONTH == "DAY":
         gekko_rate_data = rate_data
         gekko_time_data = time_data
         max_daily_rate = gekko_rate_data[0]
         cstr = "max daily rate = " + str(max_daily_rate)
         print(cstr)
         gekko_time_data = time_data
      elif DAY_OR_MONTH == "YEAR":
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
         #raw_input("Press ENTER to continue...")
      
         #print(gekko_rate_data)
         #raw_input("Press ENTER to continue...")

         # fix for MONTH .....




      # start GEKKO code here .........................

      # GEKKO model
      m = GEKKO()
   
      if test_data == "YES":  # STD_OR_SPECIAL == "SPECIAL":
         gekko_q_daily = m.FV(lb=max_daily_rate*1.0,ub=max_daily_rate*22.00)         # q_daily
      elif 1 == 1:
         gekko_q_daily = m.FV(lb=max_daily_rate*1.0,ub=max_daily_rate*1.4)           # q_daily
 
         #gekko_q_daily = m.FV(lb=max_daily_rate*0.00001,ub=max_daily_rate*100000)    # q_daily
         fdl = 1
      
      if 1 == 1:   # STD_OR_SPECIAL == "SPECIAL":
         #gekko_se_hyperbolic = m.FV(lb=0.01,ub=10000)
      
         #gekko_se_tau = m.FV(lb=1.0,ub=10000)
         gekko_se_tau = m.FV(lb=0.50,ub=50000)        # ??????????????????????

         gekko_se_n = m.FV(lb=0.001,ub=0.999)   # 0.43
         #gekko_se_n = m.FV(lb=0.0000001,ub=1.0)

      #gekko_d_daily = m.FV(lb=0.0,ub=0.2)   # d_daily
      #gekko_d_daily = m.FV(lb=-10000,ub=10000)   # d_daily
   
      #gekko_d_yearly = m.FV(lb=0.0,ub=99.999999)                            # d_yearly
   
      gekko_se_e = m.FV(lb=2.71828,ub=2.71828)                    # e value
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
      yp = m.Var()                      # y is yp    UNKNOWN

      #m.Equation( yp == y1 )
   
      #m.Equation( yp == gekko_q_daily / ( 1.0 + gekko_h_hyperbolic * gekko_d_daily * xm ) ** (1.0/gekko_h_hyperbolic) )
      #m.Equation( yp == gekko_q_daily * gekko_se_e ** (( - xm / gekko_d_daily) ** gekko_se_hyperbolic) )  # stretched exponential
      m.Equation( yp == gekko_q_daily * gekko_se_e ** ( - ( xm / (gekko_se_tau * 1.0) ) ** gekko_se_n ) )  # stretched exponential
      #                                               3    2      1                   1 2               3
      """
      stretched exponential distribution to be used as Fit function

      f(x)=h*exp(-(x/t)^b )
      h: Height at time zero
      t: Relaxation time of the standard exponential
      b: Stretching exponent
      """



      m.Obj(((yp-ym)/ym)**2)

      # Options
      gekko_q_daily.STATUS = 1
      gekko_se_tau.STATUS = 1

      gekko_se_n.STATUS = 1
      gekko_se_e.STATUS = 1              
 
      #d.STATUS = 1
      m.options.IMODE = 2
      m.options.SOLVER = 1

      # Solve
      m.solve()

      q_daily = gekko_q_daily.value[0]             # convert from gekko to variable
      se_tau = gekko_se_tau.value[0]
      se_n = gekko_se_n.value[0]
      se_e = gekko_se_e.value[0]             
      #d_yearly = gekko_d_yearly.value[0]
 
      c1 = "q_daily rate = " + str(q_daily)
      print (c1)
      c2 = "se_n exponent = " + str(se_n)
      print (c2)
      c3 = "se_tau time = " + str(se_tau)
      print (c3)
  
      cFormula = "Formula is : " + "\n" + "Stretched Exponential Equation"

        
      if 1 == 2:   # another gekko calculation .....

         # start GEKKO code here .........................

         # GEKKO model
         m = GEKKO()
       
         #gekko_se_tau = m.FV(lb=0.0,ub=1000.0)                # time factor
         #    gekko_se_tau = m.FV(lb=0.0,ub=1000.0)                # time factor
         gekko_result = m.FV(lb=0.0,ub=20000.0)          # d_yearly
      
        
         # use lists 
         #xm = m.Param(value=list_days_cumulative)     # GIVEN
         #x2 = m.Param(value=list_xm2)  # GIVEN
         #x3 = m.Param(value=list_xm3)  # GIVEN
         #ym = m.Param(value=list_daily_rate)   # GIVEN  z = ym
 
         #yp = m.Var()                     # y is yp    UNKNOWN

         #m.Equation( yp == gekko_q_daily / ( 1.0 + gekko_h_hyperbolic * gekko_d_daily * xm ) ** (1.0/gekko_h_hyperbolic) )  
         #m.Equation(y==a*(x1**b)*(x2**c)*(x3**d))
   
         #m.Equation( 775 == 2700 * 2.71828 ** ( - ( 450.0 / gekko_se_tau ) ** 0.43 ) )  # stretched exponential

         m.Equation( gekko_result == 2700 * 2.71828 ** ( - ( 450.0 / (12.1*30.42) ) ** 0.43 ) )  # stretched exponential
         # result = 907.
         #m.Obj(((yp-ym)/ym)**2)

         # Options
         #gekko_se_tau.STATUS = 1
         gekko_result.STATUS = 1
 
         #d.STATUS = 1
         m.options.IMODE = 2
         m.options.SOLVER = 1

         # Solve
         m.solve()

         #q_daily = gekko_q_daily.value[0]             # convert from gekko to variable
         #h_hyperbolic = gekko_h_hyperbolic.value[0]
         #se_tau = gekko_se_tau.value[0]
         result = gekko_result.value[0]
 
 
         # c1 = "q_daily = " + str(q_daily)
         # c2 = "h_hyperbolic = " + str(h_hyperbolic)
         c1 = "result = " + str(result)
         #c1 = "se_tau = " + str(se_tau)
         print(c1)
      
         cFormula = "Formula is : " + "\n" + "Stretched Exponential Equation"

         #print (c3)
         #print (c4)
         raw_input("Press ENTER to continue...")
 

  
   

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
         #raw_input("Press ENTER to continue...")
       
      if iloop == 1:   # ND_OR_LC == "WELLCODE":
         cLegend = cFormula + "\n" + c1 + "\n" + c2 + "\n" + c3 + "\n" + cR2 
      elif 1 == 1:   
         cLegend = cFormula + "\n" + c1 + "\n" + c2 + "\n" + c3 + "\n" + cR2 + "\n" + cPoints1 + "\n" + cPoints2 


      if iloop == 2:  # only show final plot

         plt.figure(1)
         plt.title("Best Fit Analysis of Stretched Exponential Curve Fitting")
 
         #plt.plot(ym,yp,'ro',label='Predicted')           # numpy array
         plt.scatter(ym,yp, color='red', s=1)

         plt.xlabel('Measured Outcome (YM)')
         plt.ylabel('Predicted Outcome (YP)')
   
         #plt.legend(loc='best')
         plt.legend([cLegend])

         #plt.text(25,90,r'$R^2$ =' + str(r_value**2))
         plt.grid(True)
         plt.show()
   
 
      if 1 == 2:   # monthly_or_yearly == "DAILY" and ND_OR_LC == "ND":
         iloop = iloop + 100    # only 1 loop !!!
      elif 1 == 1:
         iloop = iloop + 1
   
   return [q_daily, se_n, se_tau]     # return a list



                                                                            
def fit_stretched_exponential_two_phase ( rate_data, time_data, monthly_or_yearly, ND_OR_LC, study_product, test_data ):

   #e_constant = 2.71828
     
   iloop = 1
   while (iloop <= 2):
      
      smooth_data = "YES"
      if monthly_or_yearly == "DAILY" and ND_OR_LC == "ND":
         #smooth_data = "NO"
         smooth_data = "YES"
 
      elif iloop >= 2:
         smooth_data = "NO"
  
      if smooth_data == "YES":

         display_plot = "NO"
         #display_plot = "YES"
         if iloop >= 2:
            display_plot = "NO"
   
         values = fig_smoothed_data (rate_data, time_data, ND_OR_LC, study_product, display_plot)
         smoothed_rate_data = values[0]
         smoothed_time_data = values[1]
         
         data_points = len(smoothed_rate_data)
         
         how_many = data_points   # all data points
         #how_many = 9            # only the first 24 data points ...........................................
         
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
         cstr = "max daily rate = " + str(max_daily_rate)
         print(cstr)
         gekko_time_data = time_data
      elif DAY_OR_MONTH == "YEAR":
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
         #raw_input("Press ENTER to continue...")
      
         #print(gekko_rate_data)
         #raw_input("Press ENTER to continue...")

        

      # start GEKKO code here .........................

      # GEKKO model
      m = GEKKO()
   
      if 1 == 1:   # STD_OR_SPECIAL == "SPECIAL":
         fdl = 1
       
         if test_data == "YES":  
            gekko_q_daily1 = m.FV(lb=max_daily_rate*0.10,ub=max_daily_rate*22.00)         # q_daily
            gekko_q_daily2 = m.FV(lb=max_daily_rate*0.10,ub=max_daily_rate*22.00)         # q_daily
 
         elif 1 == 1:
            gekko_q_daily1 = m.FV(lb=max_daily_rate*0.10,ub=max_daily_rate*1.7)             # q_daily
            gekko_q_daily2 = m.FV(lb=max_daily_rate*0.10,ub=max_daily_rate*1.7)             # q_daily


      if 1 == 1:   # STD_OR_SPECIAL == "SPECIAL":
         #gekko_se_hyperbolic = m.FV(lb=0.01,ub=10000)
      
         #gekko_se_tau = m.FV(lb=1.0,ub=10000)
         gekko_se_tau1 = m.FV(lb=0.5,ub=50000)        # ??????????????????????
         gekko_se_tau2 = m.FV(lb=0.5,ub=50000)        # ??????????????????????

         gekko_se_n1 = m.FV(lb=0.001,ub=0.999)   # 0.43
         gekko_se_n2 = m.FV(lb=0.001,ub=0.999)   # 0.43
         #gekko_se_n = m.FV(lb=0.0000001,ub=1.0)

      #gekko_d_daily = m.FV(lb=0.0,ub=0.2)   # d_daily
      #gekko_d_daily = m.FV(lb=-10000,ub=10000)   # d_daily
   
      #gekko_d_yearly = m.FV(lb=0.0,ub=99.999999)                            # d_yearly
   
      gekko_se_e = m.FV(lb=2.71828,ub=2.71828)                    # e value
      
      gekko_max_daily_rate = m.FV(lb=max_daily_rate,ub=max_daily_rate)  

      
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
      yp = m.Var()                      # y is yp    UNKNOWN

      #m.Equation( yp == y1 )
   
      #m.Equation( yp == gekko_q_daily / ( 1.0 + gekko_h_hyperbolic * gekko_d_daily * xm ) ** (1.0/gekko_h_hyperbolic) )
      #m.Equation( yp == gekko_q_daily * gekko_se_e ** (( - xm / gekko_d_daily) ** gekko_se_hyperbolic) )  # stretched exponential
      m.Equation( yp1 == gekko_q_daily1 * gekko_se_e ** ( - ( xm / (gekko_se_tau1 * 1.0) ) ** gekko_se_n1 ) )  # stretched exponential
      m.Equation( yp2 == gekko_q_daily2 * gekko_se_e ** ( - ( xm / (gekko_se_tau2 * 1.0) ) ** gekko_se_n2 ) )  # stretched exponential
      m.Equation( yp == yp1 + yp2 )  

      #m.Equation( gekko_se_n1 == 0.10 )    # fracture flow >= matrix flow
      #m.Equation( gekko_q_daily1 / gekko_q_daily2 >= 2.0 )    # fracture flow >= matrix flow
      #m.Equation( gekko_se_n1 / gekko_se_n2 >= 1.5 )    # too low
      m.Equation( gekko_se_n1 / gekko_se_n2 >= 2.5 )   # between both hyperbolics
      m.Equation( gekko_q_daily1 + gekko_q_daily2 >= gekko_max_daily_rate )   

      #m.Equation( gekko_se_n1 / gekko_se_n2 >= 10.0 )    # fracture flow >= matrix flow

      """
      if 1 == 1:   # test_data == "YES":  
         #m.Equation( gekko_q_daily1 / gekko_q_daily2 >= 1.33 )      # fracture flow >= matrix flow
         m.Equation( gekko_se_n1 / gekko_se_n2 >= 2.0 )    # fracture flow >= matrix flow
         #m.Equation( gekko_d_daily1 / gekko_d_daily2 >= 1.50 )    # fracture flow >= matrix flow
         #m.Equation( gekko_h_hyperbolic2 <= 0.25 )  # BEST  # fracture flow >= matrix flow
               
      elif typecurve == "YES":   # ND type curve
         #m.Equation( gekko_h_hyperbolic1 / gekko_h_hyperbolic2 >= 1.33 )    # fracture flow >= matrix flow
         m.Equation( gekko_q_daily1 / gekko_q_daily2 >= 1.33 )      # fracture flow >= matrix flow
         m.Equation( gekko_se_n1 / gekko_se_n2 >= 2.0 )    # fracture flow >= matrix flow
         #m.Equation( gekko_d_daily1 / gekko_d_daily2 >= 1.50 )    # fracture flow >= matrix flow
         #m.Equation( gekko_h_hyperbolic2 <= 0.50 )  # FAIR # fracture flow >= matrix flow
         m.Equation( gekko_se_n1 <= 0.25 )  # BEST  # fracture flow >= matrix flow
         #m.Equation( gekko_h_hyperbolic2 <= 0.10 ) # too low   # fracture flow >= matrix flow
      """
      
      #                                               3    2      1                   1 2               3
      """
      stretched exponential distribution to be used as Fit function

      f(x)=h*exp(-(x/t)^b )
      h: Height at time zero
      t: Relaxation time of the standard exponential
      b: Stretching exponent
      """

      m.Obj(((yp-ym)/ym)**2)

      # Options
      gekko_q_daily1.STATUS = 1
      gekko_q_daily2.STATUS = 1

      gekko_se_tau1.STATUS = 1
      gekko_se_tau2.STATUS = 1

      gekko_se_n1.STATUS = 1
      gekko_se_n2.STATUS = 1
 
      gekko_se_e.STATUS = 1              
 
      #d.STATUS = 1
      m.options.IMODE = 2
      m.options.SOLVER = 1

      # Solve
      m.solve()

      q_daily1 = gekko_q_daily1.value[0]             # convert from gekko to variable
      q_daily2 = gekko_q_daily2.value[0]   
 
      se_tau1 = gekko_se_tau1.value[0]
      se_tau2 = gekko_se_tau2.value[0]
  
      se_n1 = gekko_se_n1.value[0]
      se_n2 = gekko_se_n2.value[0]
 
      se_e = gekko_se_e.value[0]
      
      #d_yearly = gekko_d_yearly.value[0]

      c1 = "q_daily1 fracture = " + str(q_daily1)
      print (c1)

      c2 = "q_daily2 matrix = " + str(q_daily2)
      print (c2)

      c3 = "se_n1 exponent fracture = " + str(se_n1)
      print (c3)

      c4 = "se_n2 exponent matrix = " + str(se_n2)
      print (c4)

      c5 = "se_tau1 time fracture = " + str(se_tau1)
      print (c5)

      c6 = "se_tau2 time matrix = " + str(se_tau2)
      print (c6)
      
      cFormula = "Formula is : " + "\n" + "Two Phase Stretched Exponential Equation"


        
      if 1 == 2:   # another gekko calculation .....

         # start GEKKO code here .........................

         # GEKKO model
         m = GEKKO()
       
         #gekko_se_tau = m.FV(lb=0.0,ub=1000.0)                # time factor
         #    gekko_se_tau = m.FV(lb=0.0,ub=1000.0)                # time factor
         gekko_result = m.FV(lb=0.0,ub=20000.0)          # d_yearly
      

        
         # use lists 
         #xm = m.Param(value=list_days_cumulative)     # GIVEN
         #x2 = m.Param(value=list_xm2)  # GIVEN
         #x3 = m.Param(value=list_xm3)  # GIVEN
         #ym = m.Param(value=list_daily_rate)   # GIVEN  z = ym
 
         #yp = m.Var()                     # y is yp    UNKNOWN

         #m.Equation( yp == gekko_q_daily / ( 1.0 + gekko_h_hyperbolic * gekko_d_daily * xm ) ** (1.0/gekko_h_hyperbolic) )  
         #m.Equation(y==a*(x1**b)*(x2**c)*(x3**d))
   
         #m.Equation( 775 == 2700 * 2.71828 ** ( - ( 450.0 / gekko_se_tau ) ** 0.43 ) )  # stretched exponential

         m.Equation( gekko_result == 2700 * 2.71828 ** ( - ( 450.0 / (12.1*30.42) ) ** 0.43 ) )  # stretched exponential
         # result = 907.
         #m.Obj(((yp-ym)/ym)**2)

         # Options
         #gekko_se_tau.STATUS = 1
         gekko_result.STATUS = 1
 
         #d.STATUS = 1
         m.options.IMODE = 2
         m.options.SOLVER = 1

         # Solve
         m.solve()

         #q_daily = gekko_q_daily.value[0]             # convert from gekko to variable
         #h_hyperbolic = gekko_h_hyperbolic.value[0]
         #se_tau = gekko_se_tau.value[0]
         result = gekko_result.value[0]
 
 
         # c1 = "q_daily = " + str(q_daily)
         # c2 = "h_hyperbolic = " + str(h_hyperbolic)
         c1 = "result = " + str(result)
         #c1 = "se_tau = " + str(se_tau)
         print(c1)
      
         cFormula = "Formula is : " + "\n" + "Stretched Exponential Equation"

         #print (c3)
         #print (c4)
         raw_input("Press ENTER to continue...")
 

  
   

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
         #raw_input("Press ENTER to continue...")
       
   
      #cLegend = cFormula + "\n" + c1 + "\n" + c2 + "\n" + c3 + "\n" + c4 + "\n" + c5 + "\n" + c6 + "\n" + cR2
      #cLegend = cFormula + "\n" + c1 + "\n" + c2 + "\n" + c3 + "\n" + cR2

      if iloop == 1:   # ND_OR_LC == "WELLCODE":
         cLegend = cFormula + "\n" + c1 + "\n" + c2 + "\n" + c3 + "\n" + c4 + "\n" + c5 + "\n" + c6 + "\n" + cR2
      elif 1 == 1:   
         cLegend = cFormula + "\n" + c1 + "\n" + c2 + "\n" + c3 + "\n" + c4 + "\n" + c5 + "\n" + c6 + "\n" + cR2 + "\n" + cPoints1 + "\n" + cPoints2

      if iloop == 2:  # only show final plot

         plt.figure(1)
         plt.title("Best Fit Analysis of Two Phase Stretched Exponential Curve Fitting")
 
         #plt.plot(ym,yp,'ro',label='Predicted')           # numpy array
         plt.scatter(ym,yp, color='red', s=1)

         plt.xlabel('Measured Outcome (YM)')
         plt.ylabel('Predicted Outcome (YP)')
   
         #plt.legend(loc='best')
         plt.legend([cLegend])

         #plt.text(25,90,r'$R^2$ =' + str(r_value**2))
         plt.grid(True)
         plt.show()
   
 
      if 1 == 2:   # monthly_or_yearly == "DAILY" and ND_OR_LC == "ND":
         iloop = iloop + 100    # only 1 loop !!!
      elif 1 == 1:
         iloop = iloop + 1
   
   #return [q_daily, se_n, se_tau]     # return a list
   #return [q_daily1, se_n1, se_tau1]     # return a list
   return [max_daily_rate, q_daily1, q_daily2, se_n1, se_n2, se_tau1, se_tau2]   # return a list












