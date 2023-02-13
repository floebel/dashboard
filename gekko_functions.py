

import streamlit as st

# one phase and two phase hyperbolic fitting
# uses gekko

#from fdl_sub_superposition import *
#from fdl_sub_listbox import *

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
import matplotlib
from matplotlib.ticker import FormatStrFormatter

#from matplotlib.ticker import MultipleLocator
#from matplotlib import pyplot
#import random

#from Tkinter import *
#from tkinter import *

#import csv, pyodbc

import math


def arps_hyperbolic_rate(qi, di, b, t):
    return qi / ((1.0 + b * di * t) ** (1.0 / b))


def arps_hyperbolic_cumulative(qi, q, di, b, t):
    return ((qi ** b) / (di * (1.0 - b))) ** (qi ** (1.0 - b) - q ** (1.0 - b))


def arps_exponential_rate(qi, di, b):
    return qi * math.e(-di)


def arps_exponential_cumulative(qi, q, di, b, t):
    return qi / di * (1 - math.e ** (-di * t))


def rate_at_time_t(
    nominal_monthly_decline,
    initial_rate,
    prior_interval_rate,
    b_factor,
    b_factor_adj,
    Dmin_monthly,
    standard_time,
    ):
    if (
        nominal_monthly_decline * (prior_interval_rate / initial_rate) ** b_factor
        >= Dmin_monthly
        ):
        return initial_rate * (
            (1.0 + b_factor_adj * nominal_monthly_decline * standard_time)
            ** (-1.0 / b_factor_adj)
        )
    else:
        return prior_interval_rate * math.e ** (-Dmin_monthly)


def cumulative_at_time_t(
    nominal_monthly_decline,
    initial_rate,
    prior_interval_rate,
    b_factor,
    b_factor_adj,
    Dmin_monthly,
    standard_time,
    prior_standard_time,
    prior_cum_production,
):
    if (
        nominal_monthly_decline * (prior_interval_rate / initial_rate) ** b_factor
        >= Dmin_monthly
    ):
        return (initial_rate / (nominal_monthly_decline * (b_factor_adj - 1.0))) * (
            (
                (1 + b_factor_adj * nominal_monthly_decline * standard_time)
                ** (1 - (1 / b_factor_adj))
            )
            - 1.0
        )
    else:
        return (prior_interval_rate / Dmin_monthly) * (
            1 - (math.e ** (-Dmin_monthly * (standard_time - prior_standard_time)))
        ) + prior_cum_production


def nominal_decline_annual(
    nominal_annual_decline, prior_interval_rate, initial_rate, b_factor, Dmin_annual
    ):

    if (
        nominal_annual_decline * (prior_interval_rate / initial_rate) ** b_factor
        >= Dmin_annual
    ):
        return nominal_annual_decline * (prior_interval_rate / initial_rate) ** b_factor
    else:
        return nominal_annual_decline


def effective_decline_annual(nominal_annual_decline):
    return 1 - math.e ** (-nominal_annual_decline)



def fig_superposition_rate():
   return ""


def fig_max_point(list_rate):

   nMaxPoint = 0
   nMaxVolume = 0
   nPoints = len(list_rate)
   for i in range(nPoints):
      if i == 0:
         nMaxPoint = 0
         nMaxVolume = list_rate[i]
      else:
         next_volume = list_rate[i]
         if next_volume > nMaxVolume:
            nMaxPoint = i
            nMaxVolume = next_volume
   return nMaxPoint            
            

                                                                          
def fit_hyperbolic_one_phase ( OIL_OR_GAS, raw_rate_data, raw_time_data):

   aa = 1
 
   # smooth ........

   nMaxPoint = fig_max_point(raw_rate_data)
   
   time_data = []
   rate_data = []
   nPoints = len(raw_rate_data)
   #nSplit = nPoints + 1 # int(nPoints * 0.90)
   
   for i in range(nPoints):
      if i < nMaxPoint:  # only analyze points on or after nMaxPoint
         fdl = 1
      else:   
         next_time = raw_time_data[i]
         next_rate = raw_rate_data[i]
         if i == 0:
            if raw_rate_data[1] > raw_rate_data[0]:
               next_rate = raw_rate_data[1]
         #if next_rate == 0.0 and raw_rate_data[i-1] > 0.0:
         #   next_rate = raw_rate_data[i-1] * 0.10
         #else:
         #   next_rate = 0.10
         if next_rate > 0.0:   
            time_data.append(next_time)
            rate_data.append(next_rate)


   #max_daily_rate = gekko_rate_data[0]
   gekko_max_daily_rate = raw_rate_data[nMaxPoint]

   #if raw_rate_data[1] > raw_rate_data[0]:
   #   raw_max_daily_rate = raw_rate_data[1]    

   cstr = "max daily rate = " + str(gekko_max_daily_rate) + " at point " + str(nMaxPoint)
   print(cstr)   
   st.write(cstr)

   
   if 1 == 1:   # DAY_OR_MONTH == "DAY":
      gekko_rate_data = rate_data
      gekko_time_data = time_data

      #max_daily_rate = gekko_rate_data[0]
      #gekko_max_daily_rate = gekko_rate_data[0]

      #if gekko_rate_data[1] > gekko_rate_data[0]:
      #   gekko_max_daily_rate = gekko_rate_data[1]    

      #cstr = "one phase gekko max daily rate = " + str(gekko_max_daily_rate)
      #print(cstr)
      #st.write(cstr)


        
      
   elif monthly_or_yearly == "xxxYEAR":
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
      cstr = "one phase max daily rate = " + str(max_daily_rate)
      print(cstr)

      print(gekko_time_data)
      #input("Press ENTER to continue...")
      
      print(gekko_rate_data)
      #input("Press ENTER to continue...")

      # fix for MONTH .....




   # start GEKKO code here .........................

   # GEKKO model
   m = GEKKO()
   
   if 1 == 1:   # STD_OR_SPECIAL == "SPECIAL":
       #gekko_q_daily = m.FV(lb=max_daily_rate*0.60,ub=max_daily_rate*1.40)    # q_daily
       #gekko_q_daily = m.FV(lb=gekko_max_daily_rate*0.40,ub=gekko_max_daily_rate*5.00)    # q_daily
       gekko_q_daily = m.FV(lb=gekko_max_daily_rate*0.950,ub=gekko_max_daily_rate*1.05)    # q_daily


   if 1 == 1:
      gekko_h_hyperbolic = m.FV(lb=1.49,ub=1.51)
     
   elif OIL_OR_GAS == "OIL":   # STD_OR_SPECIAL == "SPECIAL":
      #gekko_h_hyperbolic = m.FV(lb=0.01,ub=2.1)
      #gekko_h_hyperbolic = m.FV(lb=0.50,ub=4.5)
      #gekko_h_hyperbolic = m.FV(lb=0.001,ub=3.0)
      gekko_h_hyperbolic = m.FV(lb=0.05,ub=2.5)
   elif OIL_OR_GAS == "GAS":   # STD_OR_SPECIAL == "SPECIAL":
      #gekko_h_hyperbolic = m.FV(lb=0.01,ub=2.1)
      #gekko_h_hyperbolic = m.FV(lb=0.50,ub=4.5)
      #gekko_h_hyperbolic = m.FV(lb=0.001,ub=3.0)
      gekko_h_hyperbolic = m.FV(lb=0.05,ub=2.5)
  

      
  
  
   
   #gekko_d_daily = m.FV(lb=0.0,ub=0.5)                                    # d_daily
   gekko_d_daily = m.FV(lb=0.0,ub=99.9999)                                # d_daily
     
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

   if 1 == 1:
      m.Obj(((yp-ym)/ym)**2)
   else:   
      m.Obj(((yp-ym)/ym)**1)

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

   cstr = "d_daily from gekko = " + str(d_daily)
   st.write(cstr)


   #def arps_hyperbolic_rate(qi, di, b, t):
   # return qi / ((1.0 + b * di * t) ** (1.0 / b))
   rate_at_60_days = 30.4375 * arps_hyperbolic_rate(q_daily, d_daily, h_hyperbolic, 60)
   cstr = "rate at 60 days = " + str(rate_at_60_days)
   st.write(cstr) 
 
   rate_at_120_days = 30.4375 * arps_hyperbolic_rate(q_daily, d_daily, h_hyperbolic, 120)
   cstr = "rate at 120 days = " + str(rate_at_120_days)
   st.write(cstr) 
  
   rate_at_180_days = 30.4375 * arps_hyperbolic_rate(q_daily, d_daily, h_hyperbolic, 180)
   cstr = "rate at 180 days = " + str(rate_at_180_days)  
   st.write(cstr) 

   rate_at_360_days = 30.4375 * arps_hyperbolic_rate(q_daily, d_daily, h_hyperbolic, 360)
   cstr = "rate at 360 days = " + str(rate_at_360_days)  
   st.write(cstr)

   rate_at_720_days = 30.4375 * arps_hyperbolic_rate(q_daily, d_daily, h_hyperbolic, 720)
   cstr = "rate at 720 days = " + str(rate_at_720_days)  
   st.write(cstr)    

   if 1 == 2:
      gekko_d_yearly_nominal = d_daily # ???
      gekko_d_yearly_adjusted = (1.0 - gekko_d_yearly_nominal ) ** (1./365.25)   
      gekko_d_daily = 1 - gekko_d_yearly_adjusted   
      cstr = "gekko_d_yearly_nominal = " + str(gekko_d_yearly_nominal)
      st.write(cstr)
      cstr = "gekko_d_yearly_adjusted = " + str(gekko_d_yearly_adjusted)
      st.write(cstr)
      cstr = "gekko_d_daily = " + str(gekko_d_daily)
      st.write(cstr)
      

   if 1 == 2:  
      d_yearly_percent = d_daily  # * 100.0
      d_daily_from_d_yearly = 1.0 - ((100.0 - d_yearly_percent)/100.0) ** (1.0/365.25)
      d_daily_from_d_yearly = round(d_daily_from_d_yearly,6)
      cstr = "d_daily from d_yearly = " + str(d_daily_from_d_yearly)
      st.write(cstr)

      d_daily = d_daily_from_d_yearly # FIX ######## 

   if 1 == 2:  # calculate EUR at various times ...

      list_predict_days = []
      list_predict_years = []
      list_predict_years_plus_one = []
      list_actual_rate = []
      list_predict_rate = []
      list_predict_cumul = []
   
      #def fit_hyperbolic_one_phase ( OIL_OR_GAS, raw_rate_data, raw_time_data):
      #nMonths = 360 # months
      nMonths = 12 # months
  
      for i in range(nMonths):
         next_month = i + 1
         next_year = next_month * 0.083333333    
         next_day = next_year * 365.25
       
         list_predict_days.append(next_day)
         list_predict_years.append(next_year)
         list_predict_years_plus_one.append(next_year + 1)
          
         #list_actual_rate.append(next_rate)   # BOPD or MCFD

         #any_predict_rate = fig_hyperbolic_q_at_time_t (q_daily, h_hyperbolic, d_daily, next_day)  # rate per day at time t (days)
         any_predict_rate = fig_hyperbolic_q_at_time_t (q_daily, h_hyperbolic, d_daily, next_year)  # rate per day at time t (days)
         cstr = "rate at year " + str(next_year) + " is " + str(any_predict_rate)
         st.write(cstr)
         #any_q_at_time_t2 = fig_hyperbolic_q_at_time_t (q_daily, h_hyperbolic, d_daily, time_days + 0.5)

         #any_predict_rate = q_daily / ( 1.0 + h_hyperbolic * d_daily * next_days ) ** (1.0 / h_hyperbolic)      

         list_predict_rate.append(any_predict_rate)   # prediction of rate from time 0 only including test data

         # estimate cumulative volume from hyperbolic fit
         #any_cumul = fig_hyperbolic_cumulative_volume (q_daily, h_hyperbolic, d_daily, next_day)
         any_cumul = fig_hyperbolic_cumulative_volume (q_daily, h_hyperbolic, d_daily_from_d_yearly, next_day)
         cstr = "cumul at year " + str(next_year) + " is " + str(any_cumul)
         st.write(cstr)
  
         list_predict_cumul.append(any_cumul)   # prediction of CUM VOLUME from time 0 only including test data

         print()
         
         print("list_predict_years")
         print(list_predict_years)
         print()

         print("list_predict_days")
         print(list_predict_days)
         print()

         print("list_predict_rate")
         print(list_predict_rate)
         print()

         #print("list_actual_rate")
         #print(list_actual_rate)
         #print()
           
  
  




   if 1 == 1:

      list_predict_days = []
      list_predict_years = []
      #list_predict_years_plus_one = []
      list_actual_rate = []
      list_predict_rate = []
      list_predict_cumul = []
   
      #def fit_hyperbolic_one_phase ( OIL_OR_GAS, raw_rate_data, raw_time_data):
      nPoints = len(raw_rate_data)
      nPointsMultiple = nPoints * 3
      for i in range(nPointsMultiple):
         next_days = 30.4375 * (i + 1)  
         #next_years = (i + 1) * 0.083333333 #raw_time_data[i]
         #next_days = next_years * 365.25
         #next_rate = raw_rate_data[i]

         list_predict_days.append(next_days)
         #list_predict_years.append(next_years)
         #list_predict_years_plus_one.append(next_years + 1)
          
         #list_actual_rate.append(next_rate)   # BOPD or MCFD

         any_predict_rate = 30.4375 * arps_hyperbolic_rate(q_daily, d_daily, h_hyperbolic, next_days)

         #any_predict_rate = 1000.0 * fig_hyperbolic_q_at_time_t (q_daily, h_hyperbolic, d_daily, next_days)  # rate per day at time t (days)
         #any_predict_rate = fig_hyperbolic_q_at_time_t (q_daily, h_hyperbolic, d_daily, next_years)  # rate per day at time t (days)

         #any_q_at_time_t2 = fig_hyperbolic_q_at_time_t (q_daily, h_hyperbolic, d_daily, time_days + 0.5)

         #any_predict_rate = q_daily / ( 1.0 + h_hyperbolic * d_daily * next_days ) ** (1.0 / h_hyperbolic)      
         list_predict_rate.append(any_predict_rate)   # prediction of rate from time 0 only including test data


         # estimate cumulative volume from hyperbolic fit
         any_cumul_1 = fig_hyperbolic_cumulative_volume (q_daily, h_hyperbolic, d_daily, next_days - 15.21875)
         any_cumul_2 = fig_hyperbolic_cumulative_volume (q_daily, h_hyperbolic, d_daily, next_days + 15.21875)

         #any_predict_rate = (any_cumul_2 - any_cumul_1) / 30.4375
         
         if 1 == 2:
            list_predict_rate.append(any_predict_rate)   # prediction of rate from time 0 only including test data

         any_cumul   = fig_hyperbolic_cumulative_volume (q_daily, h_hyperbolic, d_daily, next_days)

         #any_cumul = fig_hyperbolic_cumulative_volume (q_daily, h_hyperbolic, d_daily, next_years)
  
         list_predict_cumul.append(any_cumul)   # prediction of CUM VOLUME from time 0 only including test data

         print()
         
         print("list_predict_years")
         print(list_predict_years)
         print()

         print("list_predict_days")
         print(list_predict_days)
         print()

         print("list_predict_rate")
         print(list_predict_rate)
         print()

         print("list_predict_cumul")
         print(list_predict_cumul)
         print()
           
  
  

         # compare to rate vs cumul data ...



  

         

   if 1 == 2:

         #list_hours_forecast = []
         #  list_x_forecast = []
         list_y_forecast = []       # hyperbolic rate forecast

         forecast_rows = int(1 * 12 * 30.32)    # forecast for 1 years by day
         #forecast_rows = int(40 * 12)           # forecast for 40 years by month
         #forecast_rows = int(40 * 12 / 4)       # forecast for 40 years by quarter
         for i in range(forecast_rows):
            any_forecast_days = int(i * 30.42 * 365.25)       # daily
            #any_forecast_days = int(i * 30.42)       # monthly
            #any_forecast_days = int(i * (365.25/4))   # quarterly 
            #any_x_forecast = any_forecast_days
            list_days_forecast.append(any_forecast_days)   # days from time 0 out to 40 years

            any_y_forecast = q_daily / ( 1.0 + h_hyperbolic * d_daily * any_forecast_days ) ** (1.0/h_hyperbolic)      
            list_y_forecast.append(any_y_forecast)   # forecast of Y from time 0 out to 40 years

            # estimate cumulative volume from hyperbolic fit
            any_cum_volume = fig_hyperbolic_cumulative_volume (q_daily, h_hyperbolic, d_daily, any_forecast_days)
            list_hyperbolic_cum_vol_forecast.append(any_cum_volume)   # prediction of CUM VOLUME from time 0 only including forecast data





 

   if OIL_OR_GAS == "OIL":
      st.write("OIL Analysis of Normalized Production Data")
   elif OIL_OR_GAS == "GAS":
      st.write("GAS Analysis of Normalized Production Data")    
      
   c1 = "q_daily = " + str(q_daily)
   st.write(c1)
   #print (c1)

   c2 = "h_hyperbolic = " + str(h_hyperbolic)
   st.write(c2)

   c3 = "d_daily = " + str(d_daily)
   st.write(c3)

   #c4 = "d_yearly = " + str(d_yearly)

   cFormula = "Formula is : " + "\n" + "Hyperbolic Equation"

   #print (c3)
   #print (c4)
   #input("Press ENTER to continue...")
 
   # now calculate d_yearly from d_daily

   if 1 == 2:  
      #d_yearly_percent = d_daily * 100.0
   
      d_daily_from_d_yearly = 1.0 - ((100.0 - d_yearly_percent)/100.0) ** (1.0/365.25)
      d_daily_from_d_yearly = round(d_daily_from_d_yearly,6)
      cstr = "d_daily from d_yearly = " + str(d_daily_from_d_yearly)
      st.write(cstr)

   if 1 == 2:
      values = fig_d_yearly_nominal(d_daily)     # call GEKKO
      d_yearly = 100.0 * values[0]   # as a percent

      c4 = "d_yearly (percent) = " + str(d_yearly)
      print (c4)
  
   d_yearly = 0.0  # FIX ###########################################
   
   #print('d: ', d.value[0])

   #cFormula = "Formula is : " + "\n" + \
   #           r"$A * WTI^B * HH^C * PROPANE^D$"

   from scipy import stats
   slope, intercept, r_value, p_value, \
          std_err = stats.linregress(ym, yp)   # GEKKO variables ... # numpy array

   r2 = r_value**2 
   cR2 = "R^2 correlation = " + str(r_value**2)
   
   st.write(cR2)
   
   #cLegend = cFormula + "\n" + c1 + "\n" + c2 + "\n" + c3 + "\n" + c4 + "\n" + cR2
   cLegend = cFormula + "\n" + c1 + "\n" + c2 + "\n" + c3 + "\n" + cR2

   if 1 == 2: # graph of how well it fits
      
      st.set_option('deprecation.showPyplotGlobalUse', False) 
  
      # plot solution
      plt.figure(1)
      #plt.plot([20,140],[20,140],'k-',label='Measured')
      plt.title("Best Fit Analysis of ONE PHASE Hyperbolic Curve Fitting")
 
      #plt.plot(ym,yp,'ro',label='Predicted')           # numpy array
      plt.scatter(ym, yp, color='red', s=1)

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
      #plt.show()
      st.pyplot() 


   if 1 == 1:

      st.set_option('deprecation.showPyplotGlobalUse', False) 
      fig, ax = plt.subplots(figsize=(10,7))
      # fig, ax = plt.subplots() 
      #ax.set_figure(figsize=(10,7))
      #ax.step(series_time, series_rate, color='blue')
      #ax.step(np_cum_days_std, series_rate, color='blue', label="Normalized Production Data")      

      if OIL_OR_GAS == "OIL":
         #ax.step(xm, ym, color='green', label="Normalized Oil Rate BOPD")
         ax.step(raw_time_data, raw_rate_data, color='green', label="Normalized Oil Rate BOPD")
    
      elif OIL_OR_GAS == "GAS":
         #ax.step(xm, ym, color='red', label="Normalized Gas Rate MCFD")
         ax.step(raw_time_data, raw_rate_data, color='red', label="Normalized Gas Rate MCFD")
 
      #list_predict_days = []
      #list_predict_years = []
      #list_actual_rate = []
      #list_predict_rate = []
      #list_predict_cumul = []

      if 1 == 1:
         #ax.plot(list_predict_years, list_predict_rate, color='blue', linestyle = 'dashed', label = "Predicted Rate From Hyperbolic Eqn")
         ax.plot(list_predict_days, list_predict_rate, color='blue', linestyle = 'dashed', label = "Predicted Rate From Hyperbolic Eqn")
    

      if 1 == 2:
         ax.plot(xm, yp, color='blue', linestyle = 'dashed', label = "Predicted Rate From Hyperbolic Eqn")

      #plt.plot(students, marks, color = 'green',
      #linestyle = 'solid', marker = 'o',
      #markerfacecolor = 'red', markersize = 12)
      
      #ax.plot(xm, yp, color='red', label="Hyperbolic Curve Fit Weighted More Recent")
          
      #ax.plot(tfit_std, qfit_std, color='orange', label="Hyperbolic Curve Fit Not Weighted")

      any_title = 'Normalized ' + OIL_OR_GAS + ' Production Rate vs Time Plot'
      ax.set_title(any_title, size=16, weight='bold' ,pad=15)
   
      ax.set_xlabel('Normalized Producing Years', size=12, weight='bold')

      if OIL_OR_GAS == "OIL":   
         ax.set_ylabel('Oil Rate BOPD Normalized to 4500 Foot Lateral', size=12, weight='bold')
      elif OIL_OR_GAS == "GAS":   
         ax.set_ylabel('Gas Rate MCFD Normalized to 4500 Foot Lateral', size=12, weight='bold')    
      
      #ax.set_yscale('log')
      #plt.semilogy()
      #ax.set_xlim(min(series_time), max(series_time))
      #ax.set_ylim(ymin=0)
      #ax.set_ylabel('Cost'))
      #ax.set_xlim(0.0, max(np_cum_days_std) * 1.50)
      #ax.set_xlim(0.0, max(np_cum_days_std))
  
      #ax.set_ylim(ymin=0)


      ax.set_yscale('log')

      plt.grid(visible=True, which='major', color='gray', linestyle='-')
      plt.grid(visible=True, which='minor', color='gray', linestyle='--')

      # Create the second legend and add the artist manually.
      #from matplotlib.legend import Legend
      #leg = Legend(ax, lines[2:], ['line C', 'line D'], loc='lower right', frameon=True)
      #leg = Legend(ax, ['line C', 'line D'], loc='lower right', frameon=True)
      #ax.add_artist(leg)
      
      # Create the second legend and add the first manually.
      #leg2 = ax.legend(['',''], ['line C', 'line D'], loc='lower right', frameon=True)
      #ax.add_artist(leg2)
      #any_cum_volume = fig_hyperbolic_cumulative_volume (q_daily, h_hyperbolic, d_daily, any_forecast_days)

      any_cumul_01 = fig_hyperbolic_cumulative_volume (q_daily, h_hyperbolic, d_daily, 1.0 * 365.25)
      any_cumul_05 = fig_hyperbolic_cumulative_volume (q_daily, h_hyperbolic, d_daily, 5.0 * 365.25)
      any_cumul_10 = fig_hyperbolic_cumulative_volume (q_daily, h_hyperbolic, d_daily, 10.0 * 365.25)
      any_cumul_20 = fig_hyperbolic_cumulative_volume (q_daily, h_hyperbolic, d_daily, 20.0 * 365.25)
      any_cumul_30 = fig_hyperbolic_cumulative_volume (q_daily, h_hyperbolic, d_daily, 30.0 * 365.25)
      text_cumul  = "EUR  1 Year = " + str(round(any_cumul_01,0))
      text_cumul += "\nEUR  5 Year = " + str(round(any_cumul_05,0))
      text_cumul += "\nEUR 10 Year = " + str(round(any_cumul_10,0))
      text_cumul += "\nEUR 20 Year = " + str(round(any_cumul_20,0))
      text_cumul += "\nEUR 30 Year = " + str(round(any_cumul_30,0))


      from matplotlib.offsetbox import AnchoredText
      # anchored_text = AnchoredText(text_cumul, loc=4, prop={'weight': 'bold', 'fontsize': 12, 'color': 'black'},
      anchored_text = AnchoredText(text_cumul, loc=4, prop={'fontsize': 12, 'color': 'black'},
                                    **{'frameon': True})
      ax.add_artist(anchored_text)


      print("max_daily_rate = ", gekko_max_daily_rate)



      if 1 == 2:
         
         ax.set_yticks([0.1, 0.3, 1, 3, 10, 30, 100, 300, 1000, 3000, 10000])
         ax.get_yaxis().set_major_formatter(matplotlib.ticker.ScalarFormatter())
         ax.yaxis.set_major_formatter(FormatStrFormatter('%.2f'))
         #ax.get_yaxis().set_major_formatter(FormatStrFormatter('%.2f')) 
         ax.set_ylim(0.1, 10000)
         

      elif gekko_max_daily_rate >= 5000:
         ax.set_yticks([0.1, 0.3, 1, 3, 10, 30, 50, 100, 300, 1000, 3000, 10000])
         ax.get_yaxis().set_major_formatter(matplotlib.ticker.ScalarFormatter())
         ax.get_yaxis().set_major_formatter(FormatStrFormatter('%.1f')) 
         ax.set_ylim(0.1, 10000)
         
      elif gekko_max_daily_rate >= 2000:
         ax.set_yticks([0.03, 0.10, 0.3, 1, 3, 10, 30, 100, 300, 1000, 3000, 10000])
         ax.get_yaxis().set_major_formatter(matplotlib.ticker.ScalarFormatter())
         ax.get_yaxis().set_major_formatter(FormatStrFormatter('%.2f')) 
         ax.set_ylim(0.03, 10000)

      elif gekko_max_daily_rate >= 1000:
         ax.set_yticks([0.01, 0.03, 0.1, .3, 1, 3, 10, 30, 100, 300, 1000, 3000])
         ax.get_yaxis().set_major_formatter(matplotlib.ticker.ScalarFormatter())
         ax.get_yaxis.set_major_formatter(FormatStrFormatter('%.2f')) 
         ax.set_ylim(0.01, 3000)

      elif gekko_max_daily_rate >= 500:
         ax.set_yticks([0.01, 0.03, .1, .3, 1, 3, 10, 30, 100, 300, 1000, 3000])
         ax.get_yaxis().set_major_formatter(matplotlib.ticker.ScalarFormatter())
         ax.get_yaxis().set_major_formatter(FormatStrFormatter('%.2f')) 
         ax.set_ylim(0.01, 3000)

      elif gekko_max_daily_rate >= 200:
         ax.set_yticks([0.003, 0.01, .03, 0.10, 0.30, 1, 3, 10, 30, 100, 300, 1000])
         ax.get_yaxis().set_major_formatter(matplotlib.ticker.ScalarFormatter())
         ax.get_yaxis().set_major_formatter(FormatStrFormatter('%.3f')) 
         ax.set_ylim(0.003, 1000)        
            
      elif gekko_max_daily_rate >= 100:
         ax.set_yticks([0.001, 0.003, 0.01, 0.03, 0.10, 0.30, 1, 3, 10, 30, 100, 300])
         ax.get_yaxis().set_major_formatter(matplotlib.ticker.ScalarFormatter())
         ax.get_yaxis().set_major_formatter(FormatStrFormatter('%.3f')) 
         ax.set_ylim(0.001, 300)

      elif gekko_max_daily_rate >= 50:
         ax.set_yticks([0.001, 0.003, 0.01, 0.03, 0.10, 0.30, 1, 3, 10, 30, 100, 300])
         ax.get_yaxis().set_major_formatter(matplotlib.ticker.ScalarFormatter())
         ax.get_yaxis().set_major_formatter(FormatStrFormatter('%.3f')) 
         ax.set_ylim(0.001, 300)

      elif gekko_max_daily_rate >= 20:
         ax.set_yticks([0.001, 0.003, 0.01, 0.03, 0.10, 0.30, 1, 3, 10, 30, 100])
         ax.get_yaxis().set_major_formatter(matplotlib.ticker.ScalarFormatter())
         ax.get_yaxis().set_major_formatter(FormatStrFormatter('%.3f')) 
         ax.set_ylim(0.001, 100)        
                  
               
      elif 1 == 1:
         fdl = 1   
      elif OIL_OR_GAS == "OIL":
         #ax.plot([10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120], [1,2,3,4,5,6,7,8,9,10,11,12])
         ax.set_yticks([10,20,30,40,50,60,70,80,90,100,110,120 ])
         ax.get_yaxis().set_major_formatter(matplotlib.ticker.ScalarFormatter())
         ax.set_ylim(10,120)
         
      elif OIL_OR_GAS == "GAS":
         #ax.plot([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12], [1,2,3,4,5,6,7,8,9,10,11,12])
         ax.set_yticks([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12 ])
         ax.get_yaxis().set_major_formatter(matplotlib.ticker.ScalarFormatter())
         ax.set_ylim(1, 12)    



      #plt.xticks(x, weight = 'bold')
      plt.xticks(weight = 'bold')
      plt.yticks(weight = 'bold')

      #elif 1 == 1:
      #plt.figure(1)

      #plt.xticks(np.arange(2005.0, 2033+1, 2.0))
   
      #if OIL_OR_GAS == "OIL":
      #   ax_set_yticks(np.arange(0, 120, 10))
      #elif OIL_OR_GAS == "GAS":
      #   ax.set_yticks(np.arange(0, 12, 1))
      
      #plt.yscale('log')    # works
    

      # Plot data and hyperbolic curve
      #plt.figure(figsize=(10,7))

      #plt.title('Decline Curve Analysis', size=20, pad=15)
      #plt.xlabel('Days')
      #plt.ylabel('Rate (SCF/d)')

      plt.legend()
      #plt.grid()
      #plt.show()
     
      plt.grid(True)
      plt.tight_layout() 
      #plt.show()
      st.pyplot()


   if 1 == 1:

      #def func_cum_hyp(self, t, qi, di, b):
      #return (qi/((1-b)*di))*(1-(1+b*di*t)**(1-(1/b)))      
      
      actual_volume = 0.0
      nPoints = len(raw_rate_data)
      for i in range(nPoints):
         next_daily_rate = raw_rate_data[i]
         actual_volume = actual_volume + (next_daily_rate * 30.4375)

      if OIL_OR_GAS == "GAS":     
         cstr = "actual cumulative volume in MCF = " + str(actual_volume)
      elif OIL_OR_GAS == "OIL":     
         cstr = "actual cumulative volume in BBL = " + str(actual_volume)    
      
      st.write(cstr)      

      nPoints = len(raw_time_data)
      max_years = raw_time_data[nPoints-1]
      cstr = "max_years = " + str(max_years)
      st.write(cstr)
      
      #max_years = time_data[nPoints-1]
      time_in_days = max_years * 365.25

      estimated_cumul_000 = fig_hyperbolic_cumulative_volume (q_daily, h_hyperbolic, d_daily, time_in_days)
      estimated_cumul = estimated_cumul_000 * 1000.

      if OIL_OR_GAS == "GAS":     
         cstr = "estimated cumulative volume from curve fit in MCF = " + str(estimated_cumul)
      elif OIL_OR_GAS == "OIL":     
         cstr = "estimated cumulative volume from curve fit in BBL = " + str(estimated_cumul)
      st.write(cstr)
   
      time_30_years_in_days = 30.0 * 365.25
      estimated_eur_000 = fig_hyperbolic_cumulative_volume (q_daily, h_hyperbolic, d_daily, time_30_years_in_days)

      estimated_remaining_000 = estimated_eur_000 - estimated_cumul_000
      estimated_remaining = (estimated_eur_000 - estimated_cumul_000) * 1000.0
   

      if OIL_OR_GAS == "GAS":     
         cstr = "estimated remaining volume from curve fit in MCF = " + str(estimated_remaining)
      elif OIL_OR_GAS == "OIL":     
         cstr = "estimated cumulative volume from curve fit in BBL = " + str(estimated_remaining)
      st.write(cstr)

      actual_plus_forecast = actual_volume + estimated_remaining
      if OIL_OR_GAS == "GAS":     
         cstr = "estimated EUR (sum of actual production plus forecast of remaining in MCF) = " + str(actual_plus_forecast)
      elif OIL_OR_GAS == "OIL":     
         cstr = "estimated EUR (sum of actual production plus forecast of remaining in BBL) = " + str(actual_plus_forecast)
      st.write(cstr) 
   
        
   return [q_daily, h_hyperbolic, d_daily, d_yearly]   # return a list




#def fit_hyperbolic_two_phase ( rate_data, time_data, ND_OR_LC, study_product, monthly_or_yearly, study_state, test_data, list_volume_cumulative):
                        
def fit_hyperbolic_two_phase ( OIL_OR_GAS, raw_rate_data, raw_time_data):

   test_data = "NO"
   ND_OR_LC = "LC"
   monthly_or_yearly = "xxxxYEARLY"
   typecurve = "NO"
   study_product = OIL_OR_GAS

   if 1 == 1:   # DAY_OR_MONTH == "DAY":
      nStart = 5                             # SKIP early data points .....
      nEnd = len(raw_rate_data)
      temp_time_data = raw_time_data[nStart:nEnd]     # option 1
      temp_rate_data = raw_rate_data[nStart:nEnd]     # option 1
      #temp_time_data = raw_time_data[nStart:]         # option 2
      max_daily_rate = raw_rate_data[0]
      if raw_rate_data[1] > max_daily_rate:
         max_daily_rate = raw_rate_data[1]   
      cstr = "two phase max daily rate = " + str(max_daily_rate)
      raw_max_daily_rate = max_daily_rate
      print(cstr)
      st.write(cstr)

   
   time_data = []
   rate_data = []
   nPoints = len(raw_rate_data)
   nSplit = -1 # int(nPoints * 0.3333)
   
   for i in range(nPoints):
      if i <= nSplit:  # only analyze points after nSplit
         fdl = 1
      else:   
         next_time = raw_time_data[i]
         next_rate = raw_rate_data[i]
         if i == 0:
            if raw_rate_data[1] > raw_rate_data[0]:
               next_rate = raw_rate_data[1]
         #if next_rate == 0.0 and raw_rate_data[i-1] > 0.0:
         #   next_rate = raw_rate_data[i-1] * 0.10
         #else:
         #   next_rate = 0.10
         if next_rate > 0.0:   
            time_data.append(next_time)
            rate_data.append(next_rate)


   #max_daily_rate = gekko_rate_data[0]
   #raw_max_daily_rate = raw_rate_data[0]

   #if raw_rate_data[1] > raw_rate_data[0]:
   #   raw_max_daily_rate = raw_rate_data[1]    

   #cstr = "two phase raw max daily rate = " + str(raw_max_daily_rate)
   #print(cstr)
   #st.write(cstr)



   if 1 == 2:
      values = fig_get_subset_of_two_lists (time_data, rate_data)
      time_data = values[0]
      rate_data = values[1]

   aa = 1

   """
   if 1 == 1:
      typecurve = "NO"
   elif test_data == "YES": 
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
   """   
  
   
   iloop = 1
   while (iloop <= 2):
   
      if 1 == 2:  # test_data == "YES" and iloop == 1:
         minimum_h_string = AlertBox("Enter minimum hyperbolic value for FRAC in Two Phase (0.499-0.799-1.066)")
         minimum_h = float(minimum_h_string)
         #minimum_h = 0.90
         #minimum_h = 0.149
         #minimum_h = 0.399
         #minimum_h = 0.699
         #minimum_h = 0.799
         maximum_h = 1.50

      #smooth_data = "YES"
      smooth_data = "NO"
 
      if 1 == 1: # monthly_or_yearly == "DAILY" and ND_OR_LC == "ND":
         smooth_data = "NO"
         #smooth_data = "YES"
  
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
         #max_daily_rate = gekko_rate_data[0]
         #if gekko_rate_data[1] > max_daily_rate:
         #   max_daily_rate = gekko_rate_data[1]   
         #cstr = "fit_hyperbolic_two_phase: max daily rate = " + str(max_daily_rate)
         #print(cstr)
         #st.write(cstr)
         #gekko_time_data = time_data
      elif 1 == 2: # monthly_or_yearly == "YEAR":   # fix - pass DAY_OR_MONTH ???????????
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
       
      if test_data == "xxxYES":  
         #gekko_h_hyperbolic1 = m.FV(lb=1.01,ub=1.3)   # fracture hyperbolic
         gekko_h_hyperbolic1 = m.FV(lb=minimum_h,ub=maximum_h)   # fracture hyperbolic
      elif typecurve == "xxxYES":   # ND type curve
         gekko_h_hyperbolic1 = m.FV(lb=1.272417,ub=1.272417)   # fracture hyperbolic
      elif 1 == 1:   # STD_OR_SPECIAL == "SPECIAL":
         gekko_h_hyperbolic1 = m.FV(lb=0.01,ub=4.1)   # fracture hyperbolic
         #gekko_h_hyperbolic1 = m.FV(lb=0.01,ub=3.1)   # fracture hyperbolic
 
      if test_data == "xxxYES":
         gekko_h_hyperbolic2 = m.FV(lb=0.01,ub=1.29)   # limit hyperbolic for matrix ?????
         #gekko_h_hyperbolic2 = m.FV(lb=0.01,ub=1.98)   # limit hyperbolic for matrix ?????
 
      elif 1 == 2:
         gekko_h_hyperbolic2 = m.FV(lb=0.03,ub=1.98)   # limit hyperbolic for matrix ?????
      elif 1 == 1:
         gekko_h_hyperbolic2 = m.FV(lb=0.01,ub=10.0)   # could set lb to about 0.4 .................
         

      gekko_d_daily1 = m.FV(lb=0.0,ub=0.333)    # 99.9999 yearly
      gekko_d_daily2 = m.FV(lb=0.0,ub=0.333)     
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

      if 1 == 2:
         m.Equation( gekko_q_daily1 + gekko_d_daily2 >= gekko_max_daily_rate ) 

      if 1 == 1:
         fdl = 1   
      elif test_data == "YES":  
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
 
 
      c1 = "two phase q_daily1 fracture = " + str(q_daily1)
      print (c1)
      st.write(c1)
      
      c2 = "two phases q_daily2 matrix = " + str(q_daily2)
      print (c2)
      st.write(c2)

      c3 = "two phase h_hyperbolic fracture = " + str(h_hyperbolic1)
      print (c3)
      st.write(c3)

      c4 = "two phase h_hyperbolic matrix = " + str(h_hyperbolic2)
      print (c4)
      st.write(c4)

      #print (c2)

      c5 = "two phase d_daily fracture = " + str(d_daily1)
      print (c5)
      st.write(c5)

      c6 = "two phase d_daily matrix = " + str(d_daily2)
      print (c6)
      st.write(c6)

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


      c7 = "two phase d_yearly fracture (percent) = " + str(d_yearly1)
      print (c7)
      st.write(c7)
 
      c8 = "two phase d_yearly matrix (percent) = " + str(d_yearly2)
      print (c8)
      st.write(c8)
      
      #input("Press ENTER to continue...")

     

      #cFormula = "Formula is : " + "\n" + \
      #           r"$A * WTI^B * HH^C * PROPANE^D$"



      from scipy import stats
      slope, intercept, r_value, p_value, \
                 std_err = stats.linregress(ym, yp)   # GEKKO variables ... # numpy array

      r2 = r_value**2 
      cR2 = "two phase R^2 correlation = " + str(r_value**2)
      print(cR2)
      st.write(r2)

      old_data_points = len(rate_data)
      if iloop == 1:   # ND_OR_LC == "WELLCODE":

         if 1 == 2:
            values = fig_remove_outlier_points (ym, yp, rate_data, time_data, ND_OR_LC, study_product)
            new_smoothed_rate_data = values[0]
            new_smoothed_time_data = values[1]
            
            rate_data = new_smoothed_rate_data
            time_data = new_smoothed_time_data


  
         new_data_points = len(rate_data)
         cstr = "two phase old data points = " + str(old_data_points)
         cstr += "   new data points = " + str(new_data_points) + " after removing outliers"
         print(cstr)
         st.write(cstr)
         cPoints1 = "two phase Original points included = " + str(old_data_points)
         print(cPoints1)
         st.write(cstr)
         cPoints2 = "two phase Points after removing outliers = " + str(new_data_points)
         print(cPoints2)
         st.write(cstr)
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
         plt.scatter(ym, yp, color='black', s=2)

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
         #plt.show()
         st.pyplot()

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



   if 1 == 1:

      st.set_option('deprecation.showPyplotGlobalUse', False) 
      fig, ax = plt.subplots(figsize=(10,7))
      # fig, ax = plt.subplots() 
      #ax.set_figure(figsize=(10,7))
      #ax.step(series_time, series_rate, color='blue')
      #ax.step(np_cum_days_std, series_rate, color='blue', label="Normalized Production Data")      

      if OIL_OR_GAS == "OIL":
         #ax.step(xm, ym, color='green', label="Normalized Oil Rate BOPD")
         #ax.step(raw_time_data, raw_rate_data, color='green', label="Normalized Oil Rate BOPD")
         ax.step(time_data, rate_data, color='green', label="Normalized Oil Rate BOPD")
 
    
      elif OIL_OR_GAS == "GAS":
         #ax.step(xm, ym, color='red', label="Normalized Gas Rate MCFD")
         #ax.step(raw_time_data, raw_rate_data, color='red', label="Normalized Gas Rate MCFD")
         ax.step(time_data, rate_data, color='red', label="Normalized Gas Rate MCFD")

         

      ax.plot(xm, yp, color='blue', linestyle = 'dashed', label = "Predicted Rate From Two Phase Hyperbolic Eqn")

      #plt.plot(students, marks, color = 'green',
      #linestyle = 'solid', marker = 'o',
      #markerfacecolor = 'red', markersize = 12)
      
      #ax.plot(xm, yp, color='red', label="Hyperbolic Curve Fit Weighted More Recent")
          
      #ax.plot(tfit_std, qfit_std, color='orange', label="Hyperbolic Curve Fit Not Weighted")

      any_title = 'Two Phase Normalized ' + OIL_OR_GAS + ' Production Rate vs Time Plot'
      ax.set_title(any_title, size=16, weight='bold' ,pad=15)
   
      ax.set_xlabel('Normalized Producing Years', size=12, weight='bold')

      if OIL_OR_GAS == "OIL":   
         ax.set_ylabel('Oil Rate BOPD Normalized to 4500 Foot Lateral', size=12, weight='bold')
      elif OIL_OR_GAS == "GAS":   
         ax.set_ylabel('Gas Rate MCFD Normalized to 4500 Foot Lateral', size=12, weight='bold')    
      
      #ax.set_yscale('log')
      #plt.semilogy()
      #ax.set_xlim(min(series_time), max(series_time))
      #ax.set_ylim(ymin=0)
      #ax.set_ylabel('Cost'))
      #ax.set_xlim(0.0, max(np_cum_days_std) * 1.50)
      #ax.set_xlim(0.0, max(np_cum_days_std))
  
      #ax.set_ylim(ymin=0)


      ax.set_yscale('log')

      #ax2 = ax1.twinx()    # TWIN

      print("max_daily_rate = ", raw_max_daily_rate)



      if 1 == 2:
         
         ax.set_yticks([0.1, 0.3, 1, 3, 10, 30, 100, 300, 1000, 3000, 10000])
         ax.get_yaxis().set_major_formatter(matplotlib.ticker.ScalarFormatter())
         ax.yaxis.set_major_formatter(FormatStrFormatter('%.2f'))
         #ax.get_yaxis().set_major_formatter(FormatStrFormatter('%.2f')) 
         ax.set_ylim(0.1, 10000)
         

      elif raw_max_daily_rate >= 5000:
         ax.set_yticks([0.1, 0.3, 1, 3, 10, 30, 50, 100, 300, 1000, 3000, 10000])
         ax.get_yaxis().set_major_formatter(matplotlib.ticker.ScalarFormatter())
         ax.get_yaxis().set_major_formatter(FormatStrFormatter('%.1f')) 
         ax.set_ylim(0.1, 10000)
         
      elif raw_max_daily_rate >= 2000:
         ax.set_yticks([0.03, 0.10, 0.3, 1, 3, 10, 30, 100, 300, 1000, 3000, 10000])
         ax.get_yaxis().set_major_formatter(matplotlib.ticker.ScalarFormatter())
         ax.get_yaxis().set_major_formatter(FormatStrFormatter('%.2f')) 
         ax.set_ylim(0.03, 10000)

      elif raw_max_daily_rate >= 1000:
         ax.set_yticks([0.01, 0.03, 0.1, .3, 1, 3, 10, 30, 100, 300, 1000, 3000])
         ax.get_yaxis().set_major_formatter(matplotlib.ticker.ScalarFormatter())
         ax.get_yaxis.set_major_formatter(FormatStrFormatter('%.2f')) 
         ax.set_ylim(0.01, 3000)

      elif raw_max_daily_rate >= 500:
         ax.set_yticks([0.01, 0.03, .1, .3, 1, 3, 10, 30, 100, 300, 1000, 3000])
         ax.get_yaxis().set_major_formatter(matplotlib.ticker.ScalarFormatter())
         ax.get_yaxis().set_major_formatter(FormatStrFormatter('%.2f')) 
         ax.set_ylim(0.01, 3000)

      elif raw_max_daily_rate >= 200:
         ax.set_yticks([0.003, 0.01, .03, 0.10, 0.30, 1, 3, 10, 30, 100, 300, 1000])
         ax.get_yaxis().set_major_formatter(matplotlib.ticker.ScalarFormatter())
         ax.get_yaxis().set_major_formatter(FormatStrFormatter('%.3f')) 
         ax.set_ylim(0.003, 1000)        
            
      elif raw_max_daily_rate >= 100:
         ax.set_yticks([0.001, 0.003, 0.01, 0.03, 0.10, 0.30, 1, 3, 10, 30, 100, 300])
         ax.get_yaxis().set_major_formatter(matplotlib.ticker.ScalarFormatter())
         ax.get_yaxis().set_major_formatter(FormatStrFormatter('%.3f')) 
         ax.set_ylim(0.001, 300)

      elif raw_max_daily_rate >= 50:
         ax.set_yticks([0.001, 0.003, 0.01, 0.03, 0.10, 0.30, 1, 3, 10, 30, 100, 300])
         ax.get_yaxis().set_major_formatter(matplotlib.ticker.ScalarFormatter())
         ax.get_yaxis().set_major_formatter(FormatStrFormatter('%.3f')) 
         ax.set_ylim(0.001, 300)

      elif raw_max_daily_rate >= 20:
         ax.set_yticks([0.001, 0.003, 0.01, 0.03, 0.10, 0.30, 1, 3, 10, 30, 100])
         ax.get_yaxis().set_major_formatter(matplotlib.ticker.ScalarFormatter())
         ax.get_yaxis().set_major_formatter(FormatStrFormatter('%.3f')) 
         ax.set_ylim(0.001, 100)        
                  
               
      elif 1 == 1:
         fdl = 1   
      elif OIL_OR_GAS == "OIL":
         #ax.plot([10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120], [1,2,3,4,5,6,7,8,9,10,11,12])
         ax.set_yticks([10,20,30,40,50,60,70,80,90,100,110,120 ])
         ax.get_yaxis().set_major_formatter(matplotlib.ticker.ScalarFormatter())
         ax.set_ylim(10,120)
         
      elif OIL_OR_GAS == "GAS":
         #ax.plot([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12], [1,2,3,4,5,6,7,8,9,10,11,12])
         ax.set_yticks([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12 ])
         ax.get_yaxis().set_major_formatter(matplotlib.ticker.ScalarFormatter())
         ax.set_ylim(1, 12)    



      #plt.xticks(x, weight = 'bold')
      plt.xticks(weight = 'bold')
      plt.yticks(weight = 'bold')

      #elif 1 == 1:
      #plt.figure(1)

      #plt.xticks(np.arange(2005.0, 2033+1, 2.0))
   
      #if OIL_OR_GAS == "OIL":
      #   ax_set_yticks(np.arange(0, 120, 10))
      #elif OIL_OR_GAS == "GAS":
      #   ax.set_yticks(np.arange(0, 12, 1))
      
      #plt.yscale('log')    # works
      


  

      # Plot data and hyperbolic curve
      #plt.figure(figsize=(10,7))

      #plt.title('Decline Curve Analysis', size=20, pad=15)
      #plt.xlabel('Days')
      #plt.ylabel('Rate (SCF/d)')

      plt.legend()
      #plt.grid()
      #plt.show()
     
      plt.grid(True)
      plt.tight_layout() 
      #plt.show()
      st.pyplot()


   if 1 == 2:
      
      actual_volume = 0.0
      nPoints = len(raw_rate_data)
      for i in range(nPoints):
         next_daily_rate = raw_rate_data[i]
         actual_volume = actual_volume + (next_daily_rate * 30.4375)

      if OIL_OR_GAS == "GAS":     
         cstr = "actual cumulative volume in MCF = " + str(actual_volume)
      elif OIL_OR_GAS == "OIL":     
         cstr = "actual cumulative volume in BBL = " + str(actual_volume)    
      
      st.write(cstr)      

      nPoints = len(raw_time_data)
      max_years = raw_time_data[nPoints-1]
      cstr = "max_years = " + str(max_years)
      st.write(cstr)
      
      #max_years = time_data[nPoints-1]
      time_in_days = max_years * 365.25
   
      # def fig_twophase_cumulative_volume (q_daily1, h_hyperbolic1, d_daily1, q_daily2, h_hyperbolic2, d_daily2, time_days):

      estimated_cumul_000 = fig_hyperbolic_cumulative_volume (q_daily, h_hyperbolic, d_daily, time_in_days)
      estimated_cumul = estimated_cumul_000 * 1000.

      if OIL_OR_GAS == "GAS":     
         cstr = "estimated cumulative volume from curve fit in MCF = " + str(estimated_cumul)
      elif OIL_OR_GAS == "OIL":     
         cstr = "estimated cumulative volume from curve fit in BBL = " + str(estimated_cumul)
      st.write(cstr)
   
      time_30_years_in_days = 30.0 * 365.25
      estimated_eur_000 = fig_hyperbolic_cumulative_volume (q_daily, h_hyperbolic, d_daily, time_30_years_in_days)

      estimated_remaining_000 = estimated_eur_000 - estimated_cumul_000
      estimated_remaining = (estimated_eur_000 - estimated_cumul_000) * 1000.0
   
      if OIL_OR_GAS == "GAS":     
         cstr = "estimated remaining volume from curve fit in MCF = " + str(estimated_remaining)
      elif OIL_OR_GAS == "OIL":     
         cstr = "estimated cumulative volume from curve fit in BBL = " + str(estimated_remaining)
      st.write(cstr)

      actual_plus_forecast = actual_volume + estimated_remaining
      if OIL_OR_GAS == "GAS":     
         cstr = "estimated EUR (sum of actual production plus forecast of remaining in MCF) = " + str(actual_plus_forecast)
      elif OIL_OR_GAS == "OIL":     
         cstr = "estimated EUR (sum of actual production plus forecast of remaining in BBL) = " + str(actual_plus_forecast)
      st.write(cstr) 
   



  
   #return [q_daily, h_hyperbolic, d_daily, d_yearly]   # return a list
   return [max_daily_rate, q_daily1, q_daily2, h_hyperbolic1, h_hyperbolic2, d_daily1, d_daily2, d_yearly1, d_yearly2, base]   # return a list
















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

      #now done in superposition code ....
      #nLast = len(final_rate_data)    
      #last_smoothed = final_rate_data[nLast-1]
      #nLast = len(final_rate_data)    
      #last_super = super_rate_data[nLast-1]
      #n_rows = len(super_rate_data)
      #for i in range(n_rows):
      #   super_rate_data[i] = super_rate_data[i] * last_smoothed / last_super
              
     
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

   """
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
   """
     
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

def AlertBox(cstr):
   return input(cstr)



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





def fig_hyperbolic_d_daily_at_time_t (q_daily, h_hyperbolic, d_daily, time_days):  # effective decline rate
  
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




 






