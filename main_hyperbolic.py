

#from fdl_sub_hyperbolic import *   # A06
from gekko_functions import *   # A06

from fdl_sub_html_small import *



from sqlite3_functions import *
from dca_functions import *

import streamlit as st
import sqlite3
import pandas as pd
import seaborn as sns
import numpy as np
import probscale
import matplotlib.pyplot as plt
import matplotlib
import plotly.express as px  # pip install plotly-express



import scipy
#import scipy.stats as st  # CANT USE st 
from datetime import datetime



import os
import math
#from gekko import GEKKO
import numpy.polynomial.polynomial as poly
from numpy import linspace, loadtxt, ones, convolve
#import seaborn as sns
from scipy.optimize import minimize
import scipy as sp
from pandas.api.types import is_string_dtype
from pandas.api.types import is_numeric_dtype

from pylab import figure, show, legend, ylabel, xlabel




def oil_comparison_graph() : # ND_OR_LC, study_year, study_product):
    
   hhc_measured = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

   hhc_forecast = [41803, 28483, 21589, 17290, 14290, 12137, 10538, 9278, 8262, 7424, 6742, 6154, 5647, 5209, 4818]
   pin_forecast = [48270, 36000, 29500, 25070, 21940, 19560, 17550, 15910, 14640, 13540, 12600, 11770, 11070, 10440, 9900]
   hyp_forecast = [40929, 29468, 23373, 19428, 16620, 14504, 12847, 11513, 10416, 9499, 8721, 8054, 7476, 6970, 6525]
         
   forecast_year = [2018, 2019, 2020, 2021, 2022, 2023, 2024, 2025, 2026, 2027, 2028, 2029, 2030, 2031, 2032]                

   if 1 == 1: 
      STD_OR_SPECIAL = "SPECIAL"
      DAY_OR_MONTH = "YEAR"
      study_state = "??"
      #values = fit_hyperbolic ( hyp_forecast, forecast_year, ND_OR_LC, study_year, study_product, DAY_OR_MONTH, STD_OR_SPECIAL, study_state)    # call GEKKO
      #values = fit_hyperbolic_one_phase ( hyp_forecast, forecast_year)    # call GEKKO

      values = fit_hyperbolic_one_phase ( pin_forecast, forecast_year)  # FDL HYPERBOLIC   # call GEKKO

      print()
      print("values from fit_hyperbolic_one_phase")
      print(values)
      print()
  
      q_daily = values[0]
      h_hyperbolic = values[1]
      d_daily = values[2]
      d_yearly = values[3]
      cstr = "from oil_comparison_graph returned from GEKKO ONE PHASE ... q_daily = " + str(q_daily) + " h_hyperbolic = " + str(h_hyperbolic) + " d_yearly = " + str(d_yearly) + " d_daily = " + str(d_daily)
      print(cstr)
      input("Press ENTER to continue...")

       
   if 1 == 2:
      study_state = "??"
      #values = fit_hyperbolic_two_phase ( pin_forecast, forecast_year, ND_OR_LC, study_product, monthly_or_yearly, study_state ) # FDL HYPERBOLIC  # call GEKKO

   
      print()
      print("values from fit_hyperbolic_two_phase")
      print(values)
      print()
  
      q_daily0 = values[0]  # max daily rate
      q_daily1 = values[1]
      q_daily2 = values[2]  
      h_hyperbolic1 = values[3]
      h_hyperbolic2 = values[4]
      d_daily1 = values[5]
      d_daily2 = values[6]
      d_yearly1 = values[7]
      d_yearly2 = values[8]
      base = values[8]
      cstr = "from oil_comparison_graph returned from GEKKO TWO PHASE... max daily rate = " + str(q_daily)
      print(cstr)
      cstr = "q_daily1 fracture = " + str(q_daily1) + " h_hyperbolic1 = " + str(h_hyperbolic1) + " d_yearly1 = " + str(d_yearly1) + " d_daily1 = " + str(d_daily1)
      print(cstr)
      cstr = "q_daily2 matrix = " + str(q_daily2) + " h_hyperbolic2 = " + str(h_hyperbolic2) + " d_yearly2 = " + str(d_yearly2) + " d_daily2 = " + str(d_daily2)
      print(cstr)
      cstr = "returned from GEKKO TWO PHASE ... two phase base = " + str(base) 
      print(cstr)
      raw_input("Press ENTER to continue...")

   



  
   plt.figure(1)
   cTitle = "Comparison of North Dakota Net Production Forecasts\n"
   cTitle += "For Oil Production\n"
   cTitle += "From HHC and Pinnacle\n"
   #cTitle += "Using Both Linear Rate/Cumul Method and Hyperbolic Forecast Method"
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

   # fix below - not same sizes ..........
         
  
                

   #plt.plot(actual_year, actual_production, color='red', linestyle='solid', label='Measured')
         
   plt.plot(forecast_year, hhc_forecast, color='black', linestyle='dashed', label='Reserve Report by HHC')
   plt.plot(forecast_year, pin_forecast, color='green', linestyle='dotted', label='Reserve Report by Pinnacle')
   #plt.plot(forecast_year, hyp_forecast, color='blue', linestyle='dashdot', label='Hyperbolic Fit Summing Each Reserve Year Added')

   #list_linear_cum_vol_forecast.append(cum_vol_forecast)
   #list_linear_rate_predict.append(daily_rate)
   plt.legend(loc='upper right')

   #  plt.legend([cLegend])

      
         
   cX = "Forecast Year"
   cY = "Forecasted Net Production Volume"
   plt.xlabel(cX)
   plt.ylabel(cY)
   
   plt.yscale('log')    # works
   
   plt.grid(True)
   plt.show()



if 1 == 2:
   oil_comparison_graph()







def historical_vs_forecast_comparison_graph_only_price(OIL_OR_GAS):

   #OIL_OR_GAS = "OIL"
   #OIL_OR_GAS = "GAS"
   
   #actual_yearM = [2017.0417, 2017.125, 2017.2083, 2017.2916, 2017.3749, 2017.4583, 2017.5415, 2017.6248, 2017.7081, 2017.7914, 2017.8747]
   #actual_oil_volumeM = [6261, 6769, 8213, 7091, 7122, 6254, 5775, 5121, 4446, 4173, 4045 ]
   #actual_gas_volumeM = [21766, 20049, 21683, 20753, 21061, 20457, 21209, 21268, 20627, 21278, 20356 ] 
   actual_oil_volume = [21515/12, 23279/12, 22322/12, 23476/12, 24948/12, 25093/12, 24345/12, 26021/12, 26810/12, 26915/12, 25563/12, 22956/12, 22417/12]
   actual_gas_volume = [36205/12, 37577/12, 35470/12, 33094/12, 33624/12, 34795/12, 31025/12, 30977/12, 32873/12, 25482/12, 33079/12, 26362/12, 20029/12]
   actual_year = [2005.5, 2006.5, 2007.5, 2008.5, 2009.5, 2010.5, 2011.5, 2012.5, 2013.5, 2014.5, 2015.5, 2016.5, 2017.5]
   
   actual_gas_price = [8.86,   6.74,  6.98,  8.86,  3.95,  4.39,  4.00,  2.75,  3.73,  4.37,  2.61,  2.49, 2.96]
   actual_gas10_price = [8.86*10,   6.74*10,  6.98*10,  8.86*10,  3.95*10,  4.39*10,  4.00*10,  2.75*10,  3.73*10,  4.37*10,  2.61*10,  2.49*10, 2.96*10]
 
   actual_oil_price = [56.44, 66.05, 72.29, 99.59, 61.69, 79.40, 95.05, 94.14, 97.93, 93.13, 48.75, 43.23, 50.91]                

   #hhc_forecast = [41803, 28483, 21589, 17290, 14290, 12137, 10538, 9278, 8262, 7424, 6742, 6154, 5647, 5209, 4818]
   #pin_forecast = [48270, 36000, 29500, 25070, 21940, 19560, 17550, 15910, 14640, 13540, 12600, 11770, 11070, 10440, 9900]
   #hyp_forecast = [40929, 29468, 23373, 19428, 16620, 14504, 12847, 11513, 10416, 9499, 8721, 8054, 7476, 6970, 6525]
         
   hhc_oil_forecast = [20912/12, 18745/12, 16901/12, 15339/12, 13997/12, 12830/12, 11805/12, 10900/12, 10092/12, 9371/12, 8725/12, 8140/12, 7612/12, 7134/12, 6699/12]
   hhc_gas_forecast = [21619/12, 18788/12, 16567/12, 14758/12, 13246/12, 11931/12, 10823/12, 9879/12, 9022/12, 8291/12, 7635/12, 7054/12, 6537/12, 6065/12, 5652/12]   
   #pin_oil_forecast = [48270/12, 36000/12, 29500/12, 25070/12, 21940/12, 19560/12, 17550/12, 15910/12, 14640/12, 13540/12, 12600/12, 11770/12, 11070/12, 10440/12, 9900/12]
   #pin_gas_forecast = [250020/12, 234010/12, 220530/12, 207340/12, 195950/12, 185490/12, 176270/12, 166740/12, 158270/12, 150300/12, 143150/12, 135620/12, 128880/12, 122490/12, 116750/12]

   forecast_year = [2018.5, 2019.5, 2020.5, 2021.5, 2022.5, 2023.5, 2024.5, 2025.5, 2026.5, 2027.5, 2028.5, 2029.5, 2030.5, 2031.5, 2032.5]                

   hhc_oil_forecastM = [1789, 1773, 1757, 1742, 1727, 1712, 1698, 1684, 1670, 1656, 1648, 1635, 1622, 1609, 1597]
   hhc_gas_forecastM = [1874, 1852, 1830, 1809, 1788, 1768, 1749, 1731, 1712, 1695, 1677, 1660, 1644, 1628, 1612]
   forecast_yearM = [2018.0417, 2018.125, 2018.2083, 2018.2916, 2018.3749, 2018.4582, 2018.5415, 2018.6248, 2018.7081, 2018.7914, 2018.8747, 2018.9580, 2019.0417, 2019.125, 2019.2083]                


   if 1 == 1:

      ONE_OR_TWO = "ONE"
      #ONE_OR_TWO = "TWO"
      #ONE_OR_TWO = "DOUBLE"

      
      #if ONE_OR_TWO == "DOUBLE":
      #   fig = plt.figure()
      #   f, axes = plt.subplots(2, 1)
      #   axes[0].plot(
      #   ay1 = fig.add_subplot(111)
      #   ax1 = fig.add_subplot(111)
      #   ax2 = ax1.twinx()
      if ONE_OR_TWO == "xxxONE":
         fig = plt.figure()   
         ay1 = fig.add_subplot(111)
         ax1 = fig.add_subplot(111)
         ax2 = ax1.twinx() 
      elif ONE_OR_TWO == "ONE":                # WORKS 
         fig, ay1 = plt.subplots()
      elif ONE_OR_TWO == "TWO":
         plt.figure()    #TWO
         ax1 = fig.add_subplot(111)
      
      #fig = plt.figure()
      
      #ax1 = fig.add_subplot(111)   # TWIN
      
      #ax2 = fig.add_subplot(111, sharex=ax1, frameon=False)
      #ay1 = plt.subplots()
      #fig, ax1 = plt.subplots()

      ay1.set_yscale('log')

      #ax2 = ax1.twinx()    # TWIN
             
      if OIL_OR_GAS == "OIL":
         ay1.plot([10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120], [1,2,3,4,5,6,7,8,9,10,11,12])
         ay1.set_yticks([10,20,30,40,50,60,70,80,90,100,110,120 ])
         ay1.get_yaxis().set_major_formatter(matplotlib.ticker.ScalarFormatter())
         plt.ylim(10,120)
         
      elif OIL_OR_GAS == "GAS":
         ay1.plot([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12], [1,2,3,4,5,6,7,8,9,10,11,12])
         ay1.set_yticks([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12 ])
         ay1.get_yaxis().set_major_formatter(matplotlib.ticker.ScalarFormatter())
         plt.ylim(1, 12)    

 
   elif 1 == 1:
      plt.figure(1)

      plt.xticks(np.arange(2005.0, 2033+1, 2.0))
   
      if OIL_OR_GAS == "OIL":
         plt.yticks(np.arange(0, 120, 10))
      elif OIL_OR_GAS == "GAS":
         plt.yticks(np.arange(0, 12, 1))
      
      plt.yscale('log')    # works
      
   plt.xlim(2005, 2034)    
   plt.xticks(np.arange(2005.0, 2033+1, 2.0))
   
   if OIL_OR_GAS == "OIL":
      #cTitle = "\nHistory of WTI Oil Price ($/BBL)"
      cTitle = "WTI Oil Price ($/BBL)\nAnd Adjusted Henry Hub Price ($/MMBTU * 10)\nVersus Production Year"
  
   elif OIL_OR_GAS == "GAS":
      cTitle = "\nHistory of Henry Hub Gas Price ($/MMBTU)"
      
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

   # fix below - not same sizes ..........
         
  
                

   #plt.plot(actual_year, actual_production, color='red', linestyle='solid', label='Measured')
   

   if OIL_OR_GAS == "OIL":
      plt.plot(actual_year, actual_oil_price, color='green', linestyle='solid', label='WTI Oil Price ($/BBL)')
      plt.plot(actual_year, actual_gas10_price, color='red', linestyle='solid', label='Adjusted Henry Hub Price ($/MMBTU * 10)')
   ##plt.plot(actual_yearM, actual_oil_volumeM, color='black', linestyle='dashed', label='Actual Monthly Net Oil BBL')

      #ax1.plot(forecast_year, hhc_oil_forecast, color='green', linestyle='solid', label='TBC Forecast Average Monthly Net Oil BBL')
      #ax1.plot(forecast_yearM, hhc_oil_forecastM, color='green', linestyle='dashed', label='TBC Forecast Monthly Net Oil BBL')
      #plt.plot(forecast_year, pin_oil_forecast, color='blue', linestyle='dotted', label='Pinnacle Forecast Average Monthly Net Oil BBL')

      #ax1.plot(actual_year, actual_oil_price, 'b-')
      #ax12.set_ylabel('WTI Oil Price ($/BBL)', color='b')

   elif OIL_OR_GAS == "GAS":
      plt.plot(actual_year, actual_gas_price, color='black', linestyle='solid', label='Henry Hub Gas Price ($/MMBTU)')
      #plt.plot(actual_yearM, actual_gas_volumeM, color='black', linestyle='dashed', label='Actual Monthly Net Gas MCF')

      #ax1.plot(forecast_year, hhc_gas_forecast, color='green', linestyle='solid', label='TBC Forecast Average Monthly Net Gas MCF')
      #ax1.plot(forecast_yearM, hhc_gas_forecastM, color='green', linestyle='dashed', label='TBC Forecast Monthly Net Gas MCF')
  
      #ax2.plot(actual_year, actual_gas_price, 'b-')
      #ax2.set_ylabel('Henry Hub Gas Price ($/MMBTU)', color='b')
     
      #plt.plot(forecast_year, pin_gas_forecast, color='blue', linestyle='dotted', label='Pinnacle Forecast Average Monthly Net Gas MCF')

   #ax2.set_ylabel('PRICE', color='r')
   #ax2.tick_params('y', colors='r')
    
   #plt.plot(forecast_year, pin_forecast, color='green', linestyle='dotted', label='Reserve Report by Pinnacle')
       
   #plt.plot(forecast_year, hhc_forecast, color='black', linestyle='dashed', label='Reserve Report by HHC')
   #plt.plot(forecast_year, pin_forecast, color='green', linestyle='dotted', label='Reserve Report by Pinnacle')
   #plt.plot(forecast_year, hyp_forecast, color='blue', linestyle='dashdot', label='xxxxx')

   #list_linear_cum_vol_forecast.append(cum_vol_forecast)
   #list_linear_rate_predict.append(daily_rate)
   plt.legend(loc='upper right')

   #  plt.legend([cLegend])

      
   #cX = "Production Year or Forecast Year"
      
   cX = "Production Year"
   if OIL_OR_GAS == "OIL":
      #cY = "Average WTI Oil Price ($/BBL)"
      cY = "WTI Oil Price or Adjusted Henry Hub Gas Price"
 
   elif OIL_OR_GAS == "GAS":
      cY = "Average Henry Hub Gas Price ($/MMBTU)"
      
   plt.xlabel(cX)
   plt.ylabel(cY)
     
   plt.grid(True)
   
   #fig.tight_layout()
   
   plt.show()

if 1 == 2:
   
   historical_vs_forecast_comparison_graph_only_price("OIL")
   historical_vs_forecast_comparison_graph_only_price("GAS")




def cash_flow_forecast(any_option):

             

   #hhc_forecast = [41803, 28483, 21589, 17290, 14290, 12137, 10538, 9278, 8262, 7424, 6742, 6154, 5647, 5209, 4818]
   #pin_forecast = [48270, 36000, 29500, 25070, 21940, 19560, 17550, 15910, 14640, 13540, 12600, 11770, 11070, 10440, 9900]
   #hyp_forecast = [40929, 29468, 23373, 19428, 16620, 14504, 12847, 11513, 10416, 9499, 8721, 8054, 7476, 6970, 6525]
         
   base_forecast_0 = [1243, 1164, 1097, 1041, 993, 951, 913, 856, 804, 757, 714, 675, 640, 607, 577]
   base_forecast_10 = [1182, 1006, 862, 744, 645, 561, 490, 417, 366, 305, 262, 225, 194, 167, 144]
   
   flat_forecast_0 = [1353, 1338, 1328, 1322, 1321, 1291, 1236, 1156, 1084, 1020, 962, 910, 862, 819, 778]
   flat_forecast_10 = [1286, 1156, 1043, 944, 857, 762, 663, 563, 480, 411, 353, 303, 261, 225, 194]
   
   pin_forecast_0 = [1237, 1156, 1097, 1044, 1003, 968, 939, 885, 837, 794, 756, 718, 685, 654, 627]
   pin_forecast_10 = [1177, 2175-1177, 3037-2175, 3783-3037, 4435-3783, 5006-4435, 5510-5006, 5941-5510, 6312-5941, 6632-6312, 6909-6632, 7149-6909, 7356-7149, 7536-7356, 7693-7536]
   
 
   #pin_oil_forecast = [48270/12, 36000/12, 29500/12, 25070/12, 21940/12, 19560/12, 17550/12, 15910/12, 14640/12, 13540/12, 12600/12, 11770/12, 11070/12, 10440/12, 9900/12]
   #pin_gas_forecast = [250020/12, 234010/12, 220530/12, 207340/12, 195950/12, 185490/12, 176270/12, 166740/12, 158270/12, 150300/12, 143150/12, 135620/12, 128880/12, 122490/12, 116750/12]

   forecast_year = [2018.5, 2019.5, 2020.5, 2021.5, 2022.5, 2023.5, 2024.5, 2025.5, 2026.5, 2027.5, 2028.5, 2029.5, 2030.5, 2031.5, 2032.5]                

   #hhc_oil_forecastM = [1789, 1773, 1757, 1742, 1727, 1712, 1698, 1684, 1670, 1656, 1648, 1635, 1622, 1609, 1597]
   #hhc_gas_forecastM = [1874, 1852, 1830, 1809, 1788, 1768, 1749, 1731, 1712, 1695, 1677, 1660, 1644, 1628, 1612]
   #forecast_yearM = [2018.0417, 2018.125, 2018.2083, 2018.2916, 2018.3749, 2018.4582, 2018.5415, 2018.6248, 2018.7081, 2018.7914, 2018.8747, 2018.9580, 2019.0417, 2019.125, 2019.2083]                


  
   if 1 == 1:
      #plt.figure(1)

      #fig1, ax1 = plt.subplots()
      #ax2 = ax1.twinx()
   
      fig1, ay1 = plt.subplots()
  
      ay1.set_yscale('log')    
 
      if 1 == 1:
         ay1.plot([125,250,375,500,625,750,875,1000,1125,1250,1375,1500], [1,2,3,4,5,6,7,8,9,10,11,12])
         ay1.set_yticks([125,250,375,500,625,750,875,1000,1125,1250,1375,1500 ])
         ay1.get_yaxis().set_major_formatter(matplotlib.ticker.ScalarFormatter())
         plt.ylim(125,1500)
         
      
 
   elif 1 == 1:
      plt.figure(1)

      plt.xticks(np.arange(2018.0, 2033+1, 1.0))
   
      if OIL_OR_GAS == "OIL":
         plt.yticks(np.arange(0, 12000, 1000))
      elif OIL_OR_GAS == "GAS":
         plt.yticks(np.arange(0, 100000, 5000))
      
      plt.yscale('log')    # works
      
   plt.xlim(2018, 2034)    
   plt.xticks(np.arange(2018.0, 2033+1, 1.0))
   
   cTitle = "\nUndiscounted and Discounted Cash Flow Comparison\n"
   cTitle += "Of Expected and Optimistic Cases\n"
   cTitle += "For THE BUFFALO COMPANY (TBC)\n"
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

   # fix below - not same sizes ..........
         
  
                

   #plt.plot(actual_year, actual_production, color='red', linestyle='solid', label='Measured')
   

   if 1 == 1:
      #plt.plot(actual_year, actual_oil_volume, color='black', linestyle='solid', label='Actual Average Monthly Net Oil BBL')
      #plt.plot(actual_yearM, actual_oil_volumeM, color='black', linestyle='dashed', label='Actual Monthly Net Oil BBL')

      plt.plot(forecast_year, base_forecast_0, color='green', linestyle='solid', label='Internal TBC Base Forecast Undiscounted Cash Flow (M$)')
      plt.plot(forecast_year, base_forecast_10, color='blue', linestyle='solid', label='Internal TBC Base Forecast Discounted (10%) Cash Flow (M$)')
      plt.plot(forecast_year, flat_forecast_0, color='green', linestyle='dashed', label='Internal TBC Optimistic Forecast Undiscounted Cash Flow (M$)')
      plt.plot(forecast_year, flat_forecast_10, color='blue', linestyle='dashed', label='Internal TBC Optimistic Forecast Discounted (10%) Cash Flow (M$)')

      plt.plot(forecast_year, pin_forecast_0, color='green', linestyle='dotted', label='Pinnacle TBC Base Forecast Undiscounted Cash Flow (M$)')
      plt.plot(forecast_year, pin_forecast_10, color='blue', linestyle='dotted', label='Pinnacle TBC Base Forecast Discounted (10%) Cash Flow (M$)')

      #plt.plot(forecast_yearM, hhc_oil_forecastM, color='green', linestyle='dashed', label='TBC Forecast Monthly Net Oil BBL')
      #plt.plot(forecast_year, pin_oil_forecast, color='blue', linestyle='dotted', label='Pinnacle Forecast Average Monthly Net Oil BBL')
      #plt.plot(forecast_year, hhc_oil_forecast_flat, color='blue', linestyle='dotted', label='TBC Optimistic Forecast Average Monthly Net Oil BBL')

      #ax2.plot(actual_year, actual_oil_price, 'r.')

   elif OIL_OR_GAS == "GAS":
      plt.plot(actual_year, actual_gas_volume, color='black', linestyle='solid', label='Actual Average Monthly Net Gas MCF')
      #plt.plot(actual_yearM, actual_gas_volumeM, color='black', linestyle='dashed', label='Actual Monthly Net Gas MCF')

      plt.plot(forecast_year, hhc_gas_forecast, color='green', linestyle='solid', label='TBC Forecast Average Monthly Net Gas MCF')
      plt.plot(forecast_yearM, hhc_gas_forecastM, color='green', linestyle='dashed', label='TBC Forecast Monthly Net Gas MCF')
      plt.plot(forecast_year, hhc_gas_forecast_flat, color='blue', linestyle='dotted', label='TBC Optimistic Forecast Average Monthly Net Gas MCF')

      #ax2.plot(actual_year, actual_gas_price, 'r.')
          
      #plt.plot(forecast_year, pin_gas_forecast, color='blue', linestyle='dotted', label='Pinnacle Forecast Average Monthly Net Gas MCF')

   #ax2.set_ylabel('PRICE', color='r')
   #ax2.tick_params('y', colors='r')
    
   #plt.plot(forecast_year, pin_forecast, color='green', linestyle='dotted', label='Reserve Report by Pinnacle')
       
   #plt.plot(forecast_year, hhc_forecast, color='black', linestyle='dashed', label='Reserve Report by HHC')
   #plt.plot(forecast_year, pin_forecast, color='green', linestyle='dotted', label='Reserve Report by Pinnacle')
   #plt.plot(forecast_year, hyp_forecast, color='blue', linestyle='dashdot', label='xxxxxxxxxx')

   #list_linear_cum_vol_forecast.append(cum_vol_forecast)
   #list_linear_rate_predict.append(daily_rate)
   plt.legend(loc='lower left')

   #  plt.legend([cLegend])

      
         
   cX = "Forecast Year"
   cY = "Annual Net Cash Flow (M$)"
         
   plt.xlabel(cX)
   plt.ylabel(cY)
     
   plt.grid(True)
   
   #fig1.tight_layout()
   
   plt.show()

if 1 == 2:
   
   cash_flow_forecast("UNDISCOUNTED")
   #cash_flow_forecast("10_PERCENT")





def query_rate_time_data():
   
   any_state = "KS"  # select state

  
   #// api operator firstproddate lastproddate state county prodzone location
   #     cStateLike := space(2)
   #      cCounty1_Like := space(24)
   #	       cCounty2_Like := space(24)
   #	       cCounty3_Like := space(24)
   #	       cOperatorLike := space(40)
   #	  //     cProdZoneLike := "RED FORK" + space(60)
   #	       cFieldEquals := space(40)
   #	       cProd1ZoneEquals := space(60)
   #	       cProd1ZoneLike := space(60)
   #	       cProd2ZoneLike := space(60)
   #	       cProd3ZoneLike := space(60)
   #	       cUser7Like := space(60)            // User7
   #				 IF Initials = "FDL"
   #	          cUser2Like := space(60)         // User2
   #				 ELSE
   #	          cUser2Like := space(60)         // User2
   #				 ENDIF
   nLatitude = 39.19050
   nLongitude = abs(-95.21802)
   nMaxMiles = 50.0
   #	//       cDistrictLike := "SEMINOLE          "
   #	       cDistrictLike := "                  "
   #
   #
   #    cAlertBox = "ENTER AN API NUMBER TO LOOK UP LATITUDE AND LONGITUDE ?"
   #    nLookup = AlertBox(cAlertBox, {"YES", "NO"})
   #			 IF nLookup = 1                                   // see a_ddfile.prg
   #	      	DO Fig_latitude_from_API WITH any_mdb_in, any_api, any_latitude, any_longitude, any_prodzone, any_leasename, any_operator, any_state, any_county        // priority - return field name ...
   #	     	  nLatitude := any_latitude
   #	        nLongitude := ABS(any_longitude)
   #	        cProd1ZoneLike := padr(any_prodzone + space(60),60)      // any_reservoir + space(60)
   #	        cStateLike := any_state
   #	        cCounty1_Like := any_county
   #	        cOperatorLike := any_operator
   #				  nMaxMiles := 5.0
   #			 ELSE
   #	     	  nLatitude := 0.0
   #	        nLongitude := 0.0
   #			  	nMaxMiles := 0.0
   #		   ENDIF
   #
   #		  	 cls
   #     set cursor on
   #
   #			    nMinYear := 0.0
   #					nMaxYear := 0.0
   #
   #			    nMinMCFD := 0.0
   #					nMaxMCFD := 0.0
   #			    nMinBOPD := 0.0
   #					nMaxBOPD := 0.0
   #			    nMinBOEPD := 0.0
   #					nMaxBOEPD := 0.0
   #			    nMinLatLength := 0.0
   #					nMaxLatLength := 0.0
   #
   #	 //			 IF Initials = "FDL"
   #
   #          @ 00, 02 SAY "1ST SALES MIN YEAR "
   #         @ 00, 21 GET nMinYear PICTURE '9999'
   #         @ 00, 30 SAY "1ST SALES MAX YEAR "
   #         @ 00, 49 GET nMaxYear PICTURE '9999'
   #
   #         @ 01, 02 SAY "GAS MIN MCFD "
   #         @ 01, 15 GET nMinMCFD PICTURE '999999'
   #         @ 01, 25 SAY "GAS MAX MCFD "
   #         @ 01, 38 GET nMaxMCFD PICTURE '999999'
   #         @ 01, 47 SAY "LEAVE AS ZEROES TO IGNORE THESE "
   #//       @ 04, 50 SAY "LEAVE AS ZERO TO IGNORE THIS (BEST AVERAGE RATE FOR ONE MONTH)"
   #
   #         @ 02, 02 SAY "OIL MIN BOPD "
   #         @ 02, 15 GET nMinBOPD PICTURE '999999'
   #         @ 02, 25 SAY "OIL MAX BOPD "
   #         @ 02, 38 GET nMaxBOPD PICTURE '999999'
   #         @ 02, 47 SAY "LEAVE AS ZEROES TO IGNORE THESE "
   #
   #         @ 03, 02 SAY "BOE MIN BOEPD "
   #         @ 03, 15 GET nMinBOEPD PICTURE '999999'
   #         @ 03, 25 SAY "BOE MAX BOEPD "
   #         @ 03, 38 GET nMaxBOEPD PICTURE '999999'
   #         @ 03, 47 SAY "LEAVE AS ZEROES TO IGNORE THESE "
   #
   #         @ 04, 02 SAY "MIN LAT LENGTH "
   #         @ 04, 18 GET nMinLatLength PICTURE '99999'
   #         @ 04, 24 SAY "MAX LAT LENGTH "
   #         @ 04, 40 GET nMaxLatLength PICTURE '99999'
   #         @ 04, 47 SAY "LEAVE AS ZEROES TO IGNORE THESE "
   #
   #	 	     @ 06, 02 SAY "FIELDNAME EQUALS "
   #      @ 06, 19 GET cFieldEquals PICTURE '@!'
   #
   #	 	     @ 08, 02 SAY "PROD ZONE EQUALS "
   #      @ 08, 19 GET cProd1ZoneEquals PICTURE '@S60@!'  
   #
   #       @ 10, 02 SAY "PROD ZONE LIKE "
   #      @ 10, 18 GET cProd1ZoneLike PICTURE '@S60@!'
   #      @ 11, 02 SAY "OR ZONE LIKE "
   #      @ 11, 18 GET cProd2ZoneLike PICTURE '@S60@!'
   #      @ 12, 02 SAY "OR ZONE LIKE "
   #      @ 12, 18 GET cProd3ZoneLike PICTURE '@S60@!'
   #
   #      @ 14, 02 SAY "LATITUDE "
   #      @ 14, 13 GET nLatitude  PICTURE '9999.999999'
   #      @ 14, 27 SAY "LONGITUDE (ABS) "
   #      @ 14, 44 GET nLongitude PICTURE '9999.999999'
   #      @ 14, 58 SAY "MAX MILES "    //          Enter 0 to exclude distance filter
   #      @ 14, 70 GET nMaxMiles PICTURE '999.99'
   #
   #      @ 16, 02 SAY "USER2 LIKE "                     // P_TREAT DATA
   #      @ 16, 18 GET cUser2Like PICTURE '@S60@!'
   #      @ 17, 02 SAY "USER7 LIKE "
   #      @ 17, 18 GET cUser7Like PICTURE '@S60@!'
   #      @ 18, 02 SAY "STATE LIKE "
   #      @ 18, 18 GET cStateLike PICTURE '@!'
   #      @ 20, 02 SAY "COUNTY LIKE "
   #      @ 20, 18 GET cCounty1_Like PICTURE '@!'
   #      @ 21, 02 SAY "OR COUNTY LIKE "
   #      @ 21, 18 GET cCounty2_Like PICTURE '@!'
   #      @ 22, 02 SAY "OR COUNTY LIKE "
   #      @ 22, 18 GET cCounty3_Like PICTURE '@!'
   #      @ 24, 02 SAY "OPERATOR LIKE "
   #      @ 24, 18 GET cOperatorLike PICTURE '@!'

   #//      @ 17, 02 SAY "DISTRICT LIKE                          NORTH TEXAS  ARK-LA-TX   WEATHERFORD"
   #//      @ 17, 18 GET cDistrictLike PICTURE '@!'

   #      READ
   #      set cursor off
   #
   #	cFieldEquals := alltrim(cFieldEquals) 
   #	cProd1ZoneEquals := alltrim(cProd1ZoneEquals)
   #	cProd1ZoneLike := alltrim(cProd1ZoneLike)
   #	cProd2ZoneLike := alltrim(cProd2ZoneLike)
   #	cProd3ZoneLike := alltrim(cProd3ZoneLike)
   #	er2Like := alltrim(cUser2Like)              // User2
   #	 cUser7Like := alltrim(cUser7Like)              // User7         // edna
   #	 cStateLike := alltrim(cStateLike)              // State
   #	 cCounty1_Like := alltrim(cCounty1_Like)            // County
   #	 cCounty2_Like := alltrim(cCounty2_Like)            // County
   #	 cCounty3_Like := alltrim(cCounty3_Like)            // County
   #	 cOperatorLike := alltrim(cOperatorLike)        // Operator
   #	 cDistrictLike := alltrim(cDistrictLike)        // District
   #
   #	 nLongitude := abs(nLongitude)


   #	cSelect := "SELECT PROD.BOE_CUMUL_MONTHS AS [CUMUL_MO], "

   #cSelect = "round(1000/1000,3) AS 'WELLCOUNT', "
   cSelect = ""
   #	        cSelect += "PROD.BOE_NORMYEAR AS [NORM_YR], PROD.BOE_NORMMONTH AS [NORM_MO], "
   #	        cSelect += "MID(L.State,1,2) AS [STATE], L.County AS [COUNTY], L.Operator AS [OPERATOR], "
   #	 //       	cSelect += "L.Location as [LOCATION], "
   #	 //  	cSelect += "L.ProdZone AS [PROD_ZONE], "
   #	        cSelect += "YEAR(L.FirstProdDate) AS [FIRST_YEAR], "
   # 	 //		   	cSelect += " (SELECT COUNT(*) FROM LeaseProduction P WHERE P.LeaseID = L.LeaseID) AS [PROD_PTS], "       // not working ............
   #cSelect += " (SELECT COUNT(*) FROM LeaseProduction P WHERE P.LeaseID = L.LeaseID AND ( P.Oil > 0 OR P.Gas > 0 ) ) AS [PROD_PTS], "   # not working ............
   #    cSelect += "L.FirstProdDate AS [FIRST_DATE], (L.LastProdDate) AS [LAST_DATE], "
   #	        cSelect += "L.LeaseName AS [LEASENAME], MID(L.LeaseNumber,1,12) AS [LEASENO], "
   #	         	cWhere += "	AND L.County IN ('Woods','Alfalfa','Grant','Major','Garfield','Blaine','Kingfisher','Logan','Canadian') "
   #  	         	cWhere += "	AND L.County IN ('Kay','Osage','Noble','Pawnee','Payne') "
   #	         	cWhere += "	AND L.County IN ('Woods','Alfalfa','Grant','Major','Garfield','Blaine','Kingfisher','Logan','Canadian','Kay','Osage','Noble','Pawnee','Payne') "
   cSelect += "PROD.Gas/30.42 AS 'MCFD', "
   cSelect += "PROD.Oil/30.42 AS 'BOPD', "
   #cSelect += "PROD.BOE/30.42 AS 'BOEPD', "

   if 1 == 2:
      cSelect += " ABS(5280.0 * 69.1* SQR (( L.BottomLatitude - L.SurfaceLatitude ) ^ 2  + 0.6 * ( L.BottomLongitude - L.SurfaceLongitude ) ^ 2 )) - 800.0 AS 'LAT_LENGTH', "

   if 1 == 2:
      cSelect += " 4500.0 * ( PROD.Gas/30.42 ) / ( 5280.0 * 69.1* SQR (( L.BottomLatitude - L.SurfaceLatitude ) ^ 2  + 0.6 * ( L.BottomLongitudeIHS - L.SurfaceLongitudeIHS ) ^ 2 ) - 800.0 ) AS 'MCFD_4500', "
      cSelect += " 4500.0 * ( PROD.Oil/30.42 ) / ( 5280.0 * 69.1* SQR (( L.BottomLatitude - L.SurfaceLatitude ) ^ 2  + 0.6 * ( L.BottomLongitude - L.SurfaceLongitude ) ^ 2 ) - 800.0 ) AS 'BOPD_4500', "
      cSelect += " 4500.0 * ( (PROD.Oil + (PROD.Gas/6.0) )  / 30.42 ) / ( 5280.0 * 69.1* SQR (( L.BottomLatitude - L.SurfaceLatitude ) ^ 2  + 0.6 * ( L.BottomLongitude - L.SurfaceLongitude ) ^ 2 ) - 800.0 ) AS 'BOEPD_4500', "

   #cSelect += " 4000.0 * ( PROD.Gas/30.42 ) / ( 5280.0 * 69.1* SQR (( L.BottomLatitude - L.SurfaceLatitude ) ^ 2  + 0.6 * ( L.BottomLongitude - L.SurfaceLongitude ) ^ 2 ) - 800.0 ) AS 'MCFD_4000', "
   #cSelect += " 4000.0 * ( PROD.Oil/30.42 ) / ( 5280.0 * 69.1* SQR (( L.BottomLatitude - L.SurfaceLatitude ) ^ 2  + 0.6 * ( L.BottomLongitude - L.SurfaceLongitude ) ^ 2 ) - 800.0 ) AS 'BOPD_4000', "
   #cSelect += " 4000.0 * ( (PROD.Oil + (PROD.Gas/6.0) ) / 30.42 ) / ( 5280.0 * 69.1* SQR (( L.BottomLatitude - L.SurfaceLatitude ) ^ 2  + 0.6 * ( L.BottomLongitude - L.SurfaceLongitude ) ^ 2 ) - 800.0 ) AS 'BOEPD_4000', "

   #cSelect += " 3800.0 * ( PROD.Gas/30.42 ) / ( 5280.0 * 69.1* SQR (( L.BottomLatitude - L.SurfaceLatitude ) ^ 2  + 0.6 * ( L.BottomLongitude - L.SurfaceLongitude ) ^ 2 ) - 800.0 ) AS 'MCFD_3800', "
   #cSelect += " 3800.0 * ( PROD.Oil/30.42 ) / ( 5280.0 * 69.1* SQR (( L.BottomLatitude - L.SurfaceLatitude ) ^ 2  + 0.6 * ( L.BottomLongitude - L.SurfaceLongitude ) ^ 2 ) - 800.0 ) AS 'BOPD_3800', "
   #cSelect += " 3800.0 * ( (PROD.Oil + (PROD.Gas/6.0) ) / 30.42 ) / ( 5280.0 * 69.1* SQR (( L.BottomLatitude - L.SurfaceLatitude ) ^ 2  + 0.6 * ( L.BottomLongitude - L.SurfaceLongitude ) ^ 2 ) - 800.0 ) AS 'BOEPD_3800', "

   #cSelect += " 3000.0 * ( PROD.Gas/30.42 ) / ( 5280.0 * 69.1* SQR (( L.BottomLatitude - L.SurfaceLatitude ) ^ 2  + 0.6 * ( L.BottomLongitude - L.SurfaceLongitude ) ^ 2 ) - 800.0 ) AS 'MCFD_3000', "
   #cSelect += " 3000.0 * ( PROD.Oil/30.42 ) / ( 5280.0 * 69.1* SQR (( L.BottomLatitude - L.SurfaceLatitude ) ^ 2  + 0.6 * ( L.BottomLongitude - L.SurfaceLongitude ) ^ 2 ) - 800.0 ) AS 'BOPD_3000', "
   #cSelect += " 3000.0 * ( (PROD.Oil + (PROD.Gas/6.0) ) / 30.42 ) / ( 5280.0 * 69.1* SQR (( L.BottomLatitude - L.SurfaceLatitude ) ^ 2  + 0.6 * ( L.BottomLongitude - L.SurfaceLongitude ) ^ 2 ) - 800.0 ) AS 'BOEPD_3000', "

   #cSelect += " 2700.0 * ( PROD.Gas/30.42 ) / ( 5280.0 * 69.1* SQR (( L.BottomLatitude - L.SurfaceLatitude ) ^ 2  + 0.6 * ( L.BottomLongitude - L.SurfaceLongitude ) ^ 2 ) - 800.0 ) AS 'MCFD_2700', "
   #cSelect += " 2700.0 * ( PROD.Oil/30.42 ) / ( 5280.0 * 69.1* SQR (( L.BottomLatitude - L.SurfaceLatitude ) ^ 2  + 0.6 * ( L.BottomLongitude - L.SurfaceLongitude ) ^ 2 ) - 800.0 ) AS 'BOPD_2700', "
   #cSelect += " 2700.0 * ( (PROD.Oil + (PROD.Gas/6.0) ) / 30.42 ) / ( 5280.0 * 69.1* SQR (( L.BottomLatitude - L.SurfaceLatitude ) ^ 2  + 0.6 * ( L.BottomLongitude - L.SurfaceLongitude ) ^ 2 ) - 800.0 ) AS 'BOEPD_2700', "

   if 1 == 2:
      cSelect += " (SELECT round(MAX(P.Gas/30.42),0) FROM LeaseProduction P WHERE P.LeaseID = L.LeaseID) AS 'MAX_MCFD', "
      cSelect += " (SELECT round(MAX(P.Oil/30.42),0) FROM LeaseProduction P WHERE P.LeaseID = L.LeaseID) AS 'MAX_BOPD', "
      cSelect += " (SELECT round(MAX(  ( P.Oil + (P.Gas/6.0) )  /30.42),0) FROM LeaseProduction P WHERE P.LeaseID = L.LeaseID) AS 'MAX_BOEPD', "

   if 1 == 2:
      cSelect += "L.API "
   else:
       cSelect += "PROD.LeaseID "
     

   if 1 == 2:
      cFrom = " FROM Lease L LEFT OUTER JOIN LeaseProduction PROD ON L.LeaseID = PROD.LeaseID "
   else:
      cFrom = " FROM LeaseProduction PROD "

   cWhere = ""
   if 1 == 2: # nMaxMiles > 0.0:
      cWhere = " WHERE 69.1* SQR (( " + alltrim(str(nLatitude)) + " - L.SurfaceLatitude ) ^ 2  + 0.6 * ( " + alltrim((str(nLongitude))) + " + L.SurfaceLongitude ) ^ 2 ) <= " + alltrim(str(nMaxMiles)) + " "
   else:
      #cWhere = " WHERE L.LeaseID IS NOT NULL "
      cWhere = " WHERE PROD.LeaseID IS NOT NULL "
 
      #cWhere = " WHERE L.API = L.API "
  
   #	  //    	cWhere := "	WHERE L.PRODZONE LIKE '%MISSISSIPPI%' "
   #	  //    	cWhere += "	AND L.USER6 = 'HORIZONTAL' "
   #	  //    	cWhere += "	AND YEAR(L.FIRSTPRODDATE) >= 2009 "
   #	      	cWhere += "	AND PROD.BOE_NORMYEAR >= 1970 "
   #	      	cWhere += "	AND PROD.BOE > 0 "
   #	  //    	cWhere += "	AND L.MAX_BOEPD >= 200 "
   #
   #				  IF Initials = "FDL" .or. Initials = "MAK" .or. Initials = "CHA" .or. Initials = "KLJ" .or. Initials = "EDP" .or. Initials = "JIM" .or. Initials = "MCS"
   #				 	   cAlertBox = "Filter on Groups of North Oklahoma Miss Play Counties ?"
   #          nNOMP := AlertBox(cAlertBox, {"N/A","WEST - 4000 FT","EAST - 3000 FT","Both WEST and EAST" } )
   #			       IF nNOMP = 2
   #  	         	cWhere += "	AND L.County IN ('Woods','Alfalfa','Grant','Major','Garfield','Blaine','Kingfisher','Logan','Canadian') "
   #			       ELSEIF nNOMP = 3
   #  	         	cWhere += "	AND L.County IN ('Kay','Osage','Noble','Pawnee','Payne') "
   #			       ELSEIF nNOMP = 4
   #  	         	cWhere += "	AND L.County IN ('Woods','Alfalfa','Grant','Major','Garfield','Blaine','Kingfisher','Logan','Canadian','Kay','Osage','Noble','Pawnee','Payne') "
   #			      ENDIF
   #				 ENDIF
   #
   #
   #      cAlertBox = "SELECT LEASE TYPE TO INCLUDE"
   #      nDirection := AlertBox(cAlertBox, {"  ALL  ","  GAS well  ", "  OIL well  ","  GAS or OIL well  ","  INJECTION  " } )
   #	 	   	 DO CASE
   #	 	   	  CASE nDirection = 1
   # //	    	cWhere += "	AND P.Year IN(2000,2001,2002,2003,2004,2005,2006,2007,2008,2009) "
   #	 	   	  CASE nDirection = 2
   #  	    	cWhere += "	AND L.LeaseType IN ('Gas') "
   #	 	   	  CASE nDirection = 3
   #  	    	cWhere += "	AND L.LeaseType IN ('Oil') "
   #	 	   	  CASE nDirection = 4
   #  	    	cWhere += "	AND L.LeaseType IN ('Gas','Oil') "
   #	 	   	  CASE nDirection = 5
   #  	    	cWhere += "	AND L.LeaseType IN ('Injection') "
   #	 	     END CASE
   #
   #
   #      cAlertBox = "SELECT DIRECTION TO INCLUDE"
   #      nDirection := AlertBox(cAlertBox, {"ALL","VERTICAL", "HORIZONTAL (required for lateral length options)" } )
   #	 	   	 DO CASE
   #	 	   	  CASE nDirection = 1
   #	 	   	  CASE nDirection = 2                              // vertical
   #		     		cWhere += " AND L.BottomLatitudeIHS < 1 "
   #	 	   	  CASE nDirection = 3                              // horizontal
   #		     		cWhere += " AND L.BottomLatitudeIHS > 1 "
   #	 	     END CASE

   #     cAlertBox = "MINIMUM TIME OF PRODUCTION DATA"
   #     nTimeChoice := AlertBox(cAlertBox, {"NO-MIN","2-MO","3-MO","6-MO","9-MO","1-YR","2-YR","3-YR","4-YR","5-YR","6-YR","7-YR","8-YR","9-YR","10-YR" } )      // priority
   #				DO CASE
   #					CASE nTimeChoice = 1
   #						 nProdPoints := 0
   #		  		CASE nTimeChoice = 2
   #						 nProdPoints := 2
   # 
   #					OTHERWISE
   #						 nProdPoints := 0
   #			 END CASE
   #
   #				IF nProdPoints > 0
   # 	    cWhere += " AND (SELECT COUNT(*) FROM LeaseProduction PROD WHERE PROD.LeaseID = L.LeaseID) >= " + str(nProdPoints) + " "
   #				ENDIF
   #
   #
   #			 IF nMinYear > 0.0 .and. nMaxYear > 0.0
   # 	      	cWhere += "	AND YEAR(L.FirstProdDate) BETWEEN " + str(nMinYear) + " AND " + str(nMaxYear) + " "
   #			 ENDIF
   #
   #
   #			 IF nMinMCFD > 0.0 .and. nMaxMCFD > 0.0
   # 	 	 cWhere += " AND (SELECT MAX(PROD.Gas/30.42) FROM LeaseProduction PROD WHERE PROD.LeaseID = L.LeaseID) BETWEEN " + str(nMinMCFD) + " AND " + str(nMaxMCFD) + " "
   #			 ENDIF
   #
   #			 IF nMinBOPD > 0.0 .and. nMaxBOPD > 0.0
   # 	 	 cWhere += " AND (SELECT MAX(PROD.Oil/30.42) FROM LeaseProduction PROD WHERE PROD.LeaseID = L.LeaseID) BETWEEN " + str(nMinBOPD) + " AND " + str(nMaxBOPD) + " "
   #			 ENDIF
   #
   #
   #		   IF nMinBOEPD > 0.0 .and. nMaxBOEPD > 0.0
   # 	 	 cWhere += " AND (SELECT MAX(((PROD.Oil + PROD.Gas/6.0)/30.42)) FROM LeaseProduction PROD WHERE PROD.LeaseID = L.LeaseID) BETWEEN " + str(nMinBOEPD) + " AND " + str(nMaxBOEPD) + " "
   #	     ENDIF
   #
   #			 IF Initials = "FDL"
   #					cString := "Min Lat Length = " + alltrim(str(nMinLatLength))
   #					Alert(cString)
   #					cString := "Max Lat Length = " + alltrim(str(nMaxLatLength))
   #					Alert(cString)
   #			 ENDIF
   #
   #	  	 IF nMinLatLength > 500.0 .and. nMaxLatLength > 500.0
   #   	 	 cWhere += " AND L.User13 BETWEEN " + str(nMinLatLength) + " AND " + str(nMaxLatLength) + " "          // special - fix this ...........
   #		 ELSE
   #		 ENDIF
   #
   #
   #	  	  IF !EMPTY(cDistrictLike)
   #			    	cWhere += "	AND L.User1 LIKE '%" + cDistrictLike + "%' "              // User1
   #	    	ENDIF
   #
   #				IF !empty(cFieldEquals)
   #			     	cWhere += "	AND L.Field = '" + cFieldEquals + "' "
   #				ENDIF
   #
   #				IF !empty(cProd1ZoneEquals)
   #			     	cWhere += "	AND L.ProdZone = '" + cProd1ZoneEquals + "' "
   #				ENDIF
   #
   #
   #				IF !empty(cProd1ZoneLike) .and. empty(cProd2ZoneLike) .and. empty(cProd3zonelike)
   #			     	cWhere += "	AND L.ProdZone LIKE '%" + cProd1ZoneLike + "%' "
   #
   #				ELSEIF !empty(cProd1zonelike) .and. !empty(cProd2zonelike) .and. empty(cProd3zonelike)
   #			    	cWhere += "	AND ( L.ProdZone LIKE '%" + cProd1ZoneLike + "%' or L.ProdZone LIKE '%" + cProd2ZoneLike + "%') "
   #
   #				ELSEIF !empty(cProd1zonelike) .and. !empty(cProd2zonelike) .and. !empty(cProd3zonelike)
   #			     	cWhere += "	AND ( L.ProdZone LIKE '%" + cProd1ZoneLike + "%' or L.ProdZone LIKE '%" + cProd2ZoneLike + "%' or L.ProdZone LIKE '%" + cProd3ZoneLike + "%' ) "
   #		  	 ENDIF
   #
   #
   #		  IF !EMPTY(cUser2Like)
   #			    	cWhere += "	AND L.User2 LIKE '%" + cUser2Like + "%' "              // User2
   #	  	ENDIF
   #
   #
   #		  IF !EMPTY(cUser7Like)
   #			    	cWhere += "	AND L.User7 LIKE '%" + cUser7Like + "%' "              // User7         // edna
   #	  	ENDIF
   #
   #
   #		  IF !EMPTY(cStateLike)
   #			    	cWhere += "	AND L.State LIKE '%" + cStateLike + "%' "              // State
   #	  	ENDIF
   #
   #
   #				IF !empty(cCounty1_like) .and. empty(cCounty2_like) .and. empty(cCounty3_like)
   #			     	cWhere += "	AND L.County LIKE '%" + cCounty1_like + "%' "
   #
   #				ELSEIF !empty(cCounty1_like) .and. !empty(cCounty2_like) .and. empty(cCounty3_like)
   #			    	cWhere += "	AND ( L.County LIKE '%" + cCounty1_like + "%' or L.County LIKE '%" + cCounty2_like + "%') "
   #
   #				ELSEIF !empty(cCounty1_like) .and. !empty(cCounty2_like) .and. !empty(cCounty3_like)
   #			     	cWhere += "	AND ( L.County LIKE '%" + cCounty1_like + "%' or L.County LIKE '%" + cCounty2_like + "%' or L.County LIKE '%" + cCounty3_like + "%' ) "
   #		  	 ENDIF
   #
   #
   #
   #		  IF !EMPTY(cOperatorLike)
   #			    	cWhere += "	AND L.Operator LIKE '%" + cOperatorLike + "%' "            // Operator
   #	  	ENDIF


   #         cAlertBox = "EXCLUDE INACTIVE LEASES ?"
   #       nInactive := AlertBox(cAlertBox, {"YES", "NO" } )
   #		   	 DO CASE
   #		   	  CASE nInactive = 1
   #	          	EXCLUDE_INACTIVE = "YES"
   #		   	  OTHERWISE
   # 	          	EXCLUDE_INACTIVE = "NO"
   #		     END CASE
   #
   #	      IF EXCLUDE_INACTIVE = "YES"                                               // priority - enhance this
   #			     	cWhere += "	AND L.LeaseStatus NOT LIKE '%" + "INACTIVE" + "%' "       // priority - enhance this ...
   #				ENDIF



   #         cAlertBox = "EXCLUDE LEASES WITH MULTIPLE WELLS ?"
   #      nMulti := AlertBox(cAlertBox, {"YES", "NO" } )
   #		   	 DO CASE
   #		   	  CASE nMulti = 1
   #	          	EXCLUDE_MULTI = "YES"
   #		   	  OTHERWISE
   #	          	EXCLUDE_MULTI = "NO"
   #		     END CASE




   # 	      IF EXCLUDE_MULTI = "YES"                                               // priority - enhance this
   #			     	cWhere += "	AND L.LeaseNumber NOT LIKE '%" + "MULTI" + "%' "       // priority - enhance this ...
   #				ENDIF


   # 	      IF EXCLUDE_MULTI = "YES"                                               // priority - enhance this
   #	   //       cWhere += " AND  (SELECT COUNT(*) FROM Well W WHERE W.LeaseID = L.LeaseID) <= 1 "
   #	          cWhere += " AND ( SELECT COUNT(*) FROM Well WHERE Well.LeaseID = L.LeaseID <= 1 ) "
   #				ENDIF




   #     //   	cOrderBy := " ORDER BY L.API, PROD.BOE_NORMYEAR, PROD.NORMMONTH"
   #     	cOrderBy := " ORDER BY L.API, PROD.BOE_CUMUL_MONTHS "

   if 1 == 2:
      cOrderBy = " ORDER BY L.API, PROD.Year, PROD.Month"
   else:   
      #cOrderBy = " ORDER BY PROD.LeaseID, PROD.Year, PROD.Month"
      cOrderBy = ""
      

   cSQL = cSelect + cFrom + cWhere + cOrderBy

   cSelect = ""
   cFrom = ""
   cWhere = ""
   cOrderBy = ""

   if 1 == 2: # WOEKS
      cSelect = "SELECT LeaseID, Year, Month, Oil, Gas From LeaseProduction"
   elif 1 == 2:   # WORKS 
      cSQL = "SELECT P.LeaseID, P.Year, P.Month, P.Oil, P.Gas From LeaseProduction P"
   elif 1 == 2:  # WORKS   
      cSelect  = "SELECT L.API, P.LeaseID, P.Year, P.Month, P.Oil, P.Gas "
      #cSelect += " abs(5280.0 * 69.1* sqrt (( L.BottomLatitude - L.SurfaceLatitude ) ^ 2  + 0.6 * ( L.BottomLongitude - L.SurfaceLongitude ) ^ 2 )) - 800.0 AS 'LAT_LENGTH', "
      #power(x,y)
      #cSelect += " abs(5280.0 * 69.1* sqrt (( L.BottomLatitude - L.SurfaceLatitude ) ^ 2  + 0.6 * ( L.BottomLongitude - L.SurfaceLongitude ) ^ 2 )) - 800.0 AS 'LAT_LENGTH', "
      #cWhere = " WHERE 69.1* SQR (( " + alltrim(str(nLatitude)) + " - L.SurfaceLatitude ) ^ 2  + 0.6 * ( " + alltrim((str(nLongitude))) + " + L.SurfaceLongitude ) ^ 2 ) <= " + alltrim(str(nMaxMiles)) + " "

      #cWhere = " WHERE 69.1* sqrt (( " + alltrim(str(nLatitude)) + " - L.SurfaceLatitude ) ^ 2  + 0.6 * ( " + alltrim((str(nLongitude))) + " + L.SurfaceLongitude ) ^ 2 ) <= " + alltrim(str(nMaxMiles)) + " "

      cFrom    = " FROM Lease L LEFT OUTER JOIN LeaseProduction P ON L.LeaseID = P.LeaseID "
      cOrderBy = " ORDER BY L.API, P.Year, P.Month"
   
   elif 1 == 2:    
      cSQL  = "SELECT L.API, P.LeaseID, P.Year, P.Month, P.Oil, P.Gas "

      cSQL += "P.Gas/30.42 AS 'MCFD', "
      cSQL += "P.Oil/30.42 AS 'BOPD', "
      #cSelect += "PROD.BOE/30.42 AS 'BOEPD', "

      
   elif 1 == 1:

      cSelect  = "SELECT P.Year, P.Month, P.Oil, P.Gas "
      cFrom    = "FROM Lease L LEFT OUTER JOIN LeaseProduction P ON L.LeaseID = P.LeaseID "
      cWhere   = "WHERE L.BottomLatitude > 1 AND P.Oil > 0 AND P.Year >= 2005 "
      cOrderBy = "GROUP BY P.Year, P.Month "
   

   if 1 == 2:
      cSelect += " ABS(5280.0 * 69.1* SQR (( L.BottomLatitude - L.SurfaceLatitude ) ^ 2  + 0.6 * ( L.BottomLongitude - L.SurfaceLongitude ) ^ 2 )) - 800.0 AS 'LAT_LENGTH', "
 
   if 1 == 2:
      cSelect += " 4500.0 * ( PROD.Gas/30.42 ) / ( 5280.0 * 69.1* SQR (( L.BottomLatitude - L.SurfaceLatitude ) ^ 2  + 0.6 * ( L.BottomLongitudeIHS - L.SurfaceLongitudeIHS ) ^ 2 ) - 800.0 ) AS 'MCFD_4500', "
      cSelect += " 4500.0 * ( PROD.Oil/30.42 ) / ( 5280.0 * 69.1* SQR (( L.BottomLatitude - L.SurfaceLatitude ) ^ 2  + 0.6 * ( L.BottomLongitude - L.SurfaceLongitude ) ^ 2 ) - 800.0 ) AS 'BOPD_4500', "
      cSelect += " 4500.0 * ( (PROD.Oil + (PROD.Gas/6.0) )  / 30.42 ) / ( 5280.0 * 69.1* SQR (( L.BottomLatitude - L.SurfaceLatitude ) ^ 2  + 0.6 * ( L.BottomLongitude - L.SurfaceLongitude ) ^ 2 ) - 800.0 ) AS 'BOEPD_4500', "



      
      cSQL += " FROM Lease L LEFT OUTER JOIN LeaseProduction P ON L.LeaseID = P.LeaseID "
      cWhere = " WHERE 69.1* SQR (( " + alltrim(str(nLatitude)) + " - L.SurfaceLatitude ) ^ 2  + 0.6 * ( " + alltrim((str(nLongitude))) + " + L.SurfaceLongitude ) ^ 2 ) <= " + alltrim(str(nMaxMiles)) + " "
      cWhere += " AND L.BottomLatitude > 1 "
      cSQL += " ORDER BY L.API, P.Year, P.Month"
 
   cSQL = cSelect + cFrom + cWhere + cOrderBy


   df = df_from_sqlite("OK", cSQL)
   return df


def fig_df_lease():

   cSelect  = "SELECT L.API, L.COUNTY, L.LeaseID, L.LeaseName, "

   #cSelect += " (SELECT COUNT(*) FROM LeaseProduction P WHERE P.LeaseID = L.LeaseID) AS 'PROD_PTS', "   

   #cSelect += " (SELECT COUNT(*) FROM LeaseProduction P WHERE P.LeaseID = L.LeaseID AND ( P.Oil > 0 OR P.Gas > 0 ) ) AS [PROD_PTS], "   # not working ............
   #    cSelect += "L.FirstProdDate AS [FIRST_DATE], (L.LastProdDate) AS [LAST_DATE], "
   #	        cSelect += "L.LeaseName AS [LEASENAME], MID(L.LeaseNumber,1,12) AS [LEASENO], "
   #   	cWhere += "	AND L.County IN ('Woods','Alfalfa','Grant','Major','Garfield','Blaine','Kingfisher','Logan','Canadian') "
   #   	cWhere += "	AND L.County IN ('Kay','Osage','Noble','Pawnee','Payne') "
   #  	cWhere += "	AND L.County IN (
   
   cSelect += "L.SurfaceLatitude AS 'SurfLat', L.SurfaceLongitude AS 'SurfLong', "
   cSelect += "L.BottomLatitude AS 'BotLat', L.BottomLongitude AS 'BotLong', "
   cSelect += "L.OPERATOR AS 'Operator', "
   cSelect += "L.Reservoir "
   cFrom   = " FROM Lease L "
   #cFrom   = " FROM Lease L LEFT OUTER JOIN LeaseProduction P ON L.LeaseID = P.LeaseID "
   cWhere  = " WHERE L.BottomLatitude > 1 "
   cWhere += " AND L.COUNTY = 'OKLAHOMA' "
 
   cOrderBy = " ORDER BY L.API "
 
   cSQL = cSelect + cFrom + cWhere + cOrderBy
   df_lease = df_from_sqlite("OK", cSQL)
   if 1 == 2:
      st.subheader("df_lease")
      st.dataframe(df_lease)
   return df_lease

   

def fig_df_summary():

   cSelect  = "SELECT L.API, L.COUNTY, L.LeaseID, L.LeaseName, "
   cSelect += "P.Year, P.Month, P.Oil, P.Gas, "

   #cSelect += " (SELECT COUNT(*) FROM LeaseProduction P WHERE P.LeaseID = L.LeaseID) AS 'PROD_PTS', "   

   #cSelect += " (SELECT COUNT(*) FROM LeaseProduction P WHERE P.LeaseID = L.LeaseID AND ( P.Oil > 0 OR P.Gas > 0 ) ) AS [PROD_PTS], "   # not working ............
   #    cSelect += "L.FirstProdDate AS [FIRST_DATE], (L.LastProdDate) AS [LAST_DATE], "
   #	        cSelect += "L.LeaseName AS [LEASENAME], MID(L.LeaseNumber,1,12) AS [LEASENO], "
   #   	cWhere += "	AND L.County IN ('Woods','Alfalfa','Grant','Major','Garfield','Blaine','Kingfisher','Logan','Canadian') "
   #   	cWhere += "	AND L.County IN ('Kay','Osage','Noble','Pawnee','Payne') "
   #  	cWhere += "	AND L.County IN (
   
   cSelect += "L.SurfaceLatitude AS 'SurfLat', L.SurfaceLongitude AS 'SurfLong', "
   cSelect += "L.BottomLatitude AS 'BotLat', L.BottomLongitude AS 'BotLong', "
   cSelect += "L.OPERATOR AS 'Operator', "
   cSelect += "L.Reservoir "
   #cSQL += "FROM Lease"
   cFrom   = " FROM Lease L LEFT OUTER JOIN LeaseProduction P ON L.LeaseID = P.LeaseID "
   cWhere  = " WHERE L.BottomLatitude > 1 AND P.Year >= 2005 AND P.Oil > 0 "
   cWhere += " AND L.COUNTY = 'OKLAHOMA' "
 
   cOrderBy = " ORDER BY L.API, P.Year, P.Month  "
 
   cSQL = cSelect + cFrom + cWhere + cOrderBy
   df_summary = df_from_sqlite("OK", cSQL)
   if 1 == 2:
      st.subheader("df_summary using ORDER BY")
 
      st.dataframe(df_summary)
   return df_summary





def fig_group_by(any_state):  ###################
   
   # GROUP BY
   #cSelect  = "SELECT P.Year, P.Month, P.Oil, P.Gas, "
   cSelect  = "SELECT P.CUMUL_MONTHS, "
   
   #cSelect += " Sum(P.Oil) AS 'OIL_SUM', "
   cSelect += " Sum(P.Oil * 4500.0 / P.LAT_LENGTH) AS 'OIL_SUM', "
  
   #cSelect += " Sum(P.Water) AS 'WATER_SUM', "
   
   #cSelect += " Sum(P.Gas) AS 'GAS_SUM', " 
   cSelect += " Sum(P.Gas * 4500.0 / P.LAT_LENGTH) AS 'GAS_SUM', " 
  
   #cSelect  = "SELECT L.API, L.COUNTY, L.LeaseID, L.LeaseName, "
   #cSelect += "P.Year, P.Month, P.Oil, P.Gas, "

   #cSelect += " (SELECT count(P.LeaseID) FROM LeaseProduction P WHERE P.LeaseID = L.LeaseID) AS 'PROD_PTS', "   
   cSelect += " (SELECT count(P.LeaseID) FROM LeaseProduction P WHERE P.LeaseID = L.LeaseID AND P.Oil > 0) AS 'OIL_PTS', "   
   cSelect += " (SELECT count(P.LeaseID) FROM LeaseProduction P WHERE P.LeaseID = L.LeaseID AND P.Gas > 0) AS 'GAS_PTS' "   

  
   #cSelect += " (SELECT count(P.LeaseID) FROM LeaseProduction P WHERE P.Oil > 0) AS 'OIL_PTS', "   
   #cSelect += " (SELECT count(P.LeaseID) FROM LeaseProduction P WHERE P.Gas > 0) AS 'GAS_PTS' "   

   #cSelect += " (SELECT COUNT(*) FROM LeaseProduction P WHERE P.LeaseID = L.LeaseID AND ( P.Oil > 0 OR P.Gas > 0 ) ) AS [PROD_PTS], "   # not working ............
   #    cSelect += "L.FirstProdDate AS [FIRST_DATE], (L.LastProdDate) AS [LAST_DATE], "
   #	        cSelect += "L.LeaseName AS [LEASENAME], MID(L.LeaseNumber,1,12) AS [LEASENO], "
   #   	cWhere += "	AND L.County IN ('Woods','Alfalfa','Grant','Major','Garfield','Blaine','Kingfisher','Logan','Canadian') "
   #   	cWhere += "	AND L.County IN ('Kay','Osage','Noble','Pawnee','Payne') "
   #  	cWhere += "	AND L.County IN (
   
   #cSelect += "L.SurfaceLatitude AS 'SurfLat', L.SurfaceLongitude AS 'SurfLong', "
   #cSelect += "L.BottomLatitude AS 'BotLat', L.BottomLongitude AS 'BotLong', "
   #cSelect += "L.OPERATOR AS 'Operator', "
   #cSelect += "L.Reservoir "
   #cSQL += "FROM Lease"
   cFrom   = " FROM Lease L LEFT OUTER JOIN LeaseProduction P ON L.LeaseID = P.LeaseID "
   cWhere  = " WHERE L.LAT_LENGTH >= 1500 AND L.MAX_MONTHS >= 12 "
   cWhere += " AND P.CUMUL_MONTHS >= 0 "
   cWhere += " AND (P.Oil > 0 OR P.Gas > 0) "
 
   #nProdPoints = 24
   #cWhere += " AND (SELECT count(*) FROM LeaseProduction PROD WHERE PROD.LeaseID = L.LeaseID) >= " + str(nProdPoints) + " "
   #cWhere += " AND (SELECT count(*) FROM LeaseProduction PROD WHERE PROD.LeaseID = L.LeaseID) >= 24 AND (P.Oil > 0 OR P.Gas > 0) "
      
   #cWhere += " AND L.COUNTY = 'OKLAHOMA' "
   #cWhere += " AND L.COUNTY = 'GRADY' "
   #cWhere += "	AND L.County IN ('OKLAHOMA', 'GRADY', 'CLEVELAND','WOODS','ALFALFA','GRANT','MAJOR','GARFIELD','BLAINE','KINGFISHER','LOGAN','CANADIAN') "
   cWhere += "	AND L.County IN ('OKLAHOMA', 'CANADIAN') "

   cOrderBy = " GROUP BY P.CUMUL_MONTHS "
 
   cSQL = cSelect + cFrom + cWhere + cOrderBy
   df = df_from_sqlite(any_state, cSQL)

   df["Ave Monthly Oil Per Well"] = df["OIL_SUM"] / df["OIL_PTS"]

   df["Ave Monthly Gas Per Well"] = df["GAS_SUM"] / df["GAS_PTS"]

   list_drop = ["OIL_SUM", "GAS_SUM"] 
   df = df.drop(list_drop, axis=1)

   df.to_csv("normalized_monthly_production.csv", index=False)
      
   if 1 == 2:
      st.subheader("df _groupby")
      st.dataframe(df)  
   return df
  








def main():
   st.title("Hyperbolic Curve Fitting")
   #st.info(
   #    """
   #    This app is maintained by Fulton Loebel
   #    """
   #)

   if 1 == 2:
      st.subheader("Distinct Query")
      cSQL = "SELECT DISTINCT Year, Month FROM LeaseProduction WHERE Year >= 2000 ORDER BY Year, Month "
      df = df_from_sqlite("OK", cSQL)
      st.dataframe(df)


   
   st.subheader("Ave Normalized Production Per Well")

   any_state = "OK"
   
   df = fig_group_by(any_state)


   #hhc_forecast = [41803, 28483, 21589, 17290, 14290, 12137, 10538, 9278, 8262, 7424, 6742, 6154, 5647, 5209, 4818]
   pin_forecast = [48270, 36000, 29500, 25070, 21940, 19560, 17550, 15910, 14640, 13540, 12600, 11770, 11070, 10440, 9900]
   #hyp_forecast = [40929, 29468, 23373, 19428, 16620, 14504, 12847, 11513, 10416, 9499, 8721, 8054, 7476, 6970, 6525]
         
   forecast_year = [2018, 2019, 2020, 2021, 2022, 2023, 2024, 2025, 2026, 2027, 2028, 2029, 2030, 2031, 2032]                

   #if 1 == 1: 
   #   STD_OR_SPECIAL = "SPECIAL"
   #   DAY_OR_MONTH = "YEAR"
   #   study_state = "??"
   #   #values = fit_hyperbolic ( hyp_forecast, forecast_year, ND_OR_LC, study_year, study_product, DAY_OR_MONTH, STD_OR_SPECIAL, study_state)    # call GEKKO
   #   #values = fit_hyperbolic_one_phase ( hyp_forecast, forecast_year)    # call GEKKO

   values = fit_hyperbolic_one_phase ( pin_forecast, forecast_year)  # FDL HYPERBOLIC   # call GEKKO

   #print()
   #print("values from fit_hyperbolic_one_phase")
   #print(values)
   #print()
  
   q_daily = values[0]
   cstr = "q_daily = " + str(q_daily)
   st.write(cstr)
   h_hyperbolic = values[1]
   cstr = "h_hyperbolic = " + str(h_hyperbolic)
   st.write(cstr)  
   d_daily = values[2]
   cstr = "d_daily = " + str(d_daily)
   st.write(cstr)  
   d_yearly = values[3]
   cstr = "d_yearly = " + str(d_yearly)
   st.write(cstr)  
   #cstr = "from oil_comparison_graph returned from GEKKO ONE PHASE ... q_daily = " + str(q_daily) + " h_hyperbolic = " + str(h_hyperbolic) + " d_yearly = " + str(d_yearly) + " d_daily = " + str(d_daily)
   #print(cstr)
   #input("Press ENTER to continue...")

   
   #df = fig_df_lease()
   #df = fig_df_summary()
   
 
   #df = query_rate_time_data()

   #df_to_webbrowser("df", df)
   
   #cSQL  = "SELECT P.LeaseIDacount(COUNTY) AS 'LEASE COUNT', COUNTY, STATE FROM Lease "
   #cSQL += "GROUP BY COUNTY ORDER BY count(COUNTY) DESC" # LIMIT 20 ASC
   # LIMIT 10
   
   #with st.spinner("Loading  ..."):
   #df_county_summary = df_from_sqlite("KS", cSQL)

   #df_county_summary = database_to_df(oENGINE, cSQL)
   #df_county_summary = df_county_summary.head(20)
     
   st.dataframe(df)

   series_time = df['CUMUL_MONTHS']

   OIL_OR_GAS = "GAS"  ######################

   if OIL_OR_GAS == "OIL":
      series_rate = df['Ave Monthly Oil Per Well']
   elif OIL_OR_GAS == "GAS":
      series_rate = df['Ave Monthly Gas Per Well']    
      
   # q = df['Ave Monthly Oil Per Well']

   qi_wt, di_wt, b_wt, RMSE_wt, np_cum_days_wt, np_cum_months_wt, np_cum_years_wt = arps_fit("TIME", "WT", series_time, series_rate, plot=False)
   cstr = "qi_wt = " + str(qi_wt)
   st.write(cstr)
   cstr = "di_wt = " + str(di_wt)
   st.write(cstr)
   cstr = "b_wt = " + str(b_wt)
   st.write(cstr)
   cstr = "RMSE_wt = " + str(RMSE_wt)
   st.write(cstr)

   qi_std, di_std, b_std, RMSE_std, np_cum_days_std, np_cum_months_std, np_cum_years_std = arps_fit("TIME", "STD", series_time, series_rate, plot=False)
   cstr = "qi_std = " + str(qi_std)
   st.write(cstr)
   cstr = "di_std = " + str(di_std)
   st.write(cstr)
   cstr = "b_std = " + str(b_std)
   st.write(cstr)
   cstr = "RMSE_std = " + str(RMSE_std)
   st.write(cstr)
         
      

   if 1 == 1:
      st.set_option('deprecation.showPyplotGlobalUse', False) 
      fig, ax = plt.subplots(figsize=(10,7))
      # fig, ax = plt.subplots() 
      #ax.set_figure(figsize=(10,7))
      #ax.step(series_time, series_rate, color='blue')
      ax.step(np_cum_days_std, series_rate, color='blue', label="Normalized Production Data")

      # Produce the hyperbolic curve (fitted)
      #tfit = np.linspace(min(np_cum_days), max(np_cum_days), 100)  # 100 ??????


      if 1 == 2:  
         tfit = np.linspace(min(np_cum_days_std), max(np_cum_days_std) * 1.50, 100)  # 100 ??????
      else:   
         #tfit = np.linspace(min(np_cum_days_std), max(np_cum_days_std), 100)  # 100 ??????
         tfit = np.linspace(0.0, max(np_cum_days_std), 100)  # 100 ??????


      if b_wt >= 0:
         fdl = 1 # logic below not needed
         tfit_wt = tfit
         qfit_wt = hyperbolic(tfit, qi_wt, di_wt, b_wt)
      else:
         tfit_wt = tfit # initialize
         qfit_wt = hyperbolic(tfit, qi_wt, di_wt, b_wt)
         nForecast = len(tfit)
         cstr = "nForecast points for weighted = " + str(nForecast)
         st.write(cstr)
         
         for i in range(nForecast):
            if i == 0:
               fdl = 1
            else:
               prev_qfit = qfit_wt[i-1]
               next_qfit = qfit_wt[i]
               if next_qfit > prev_qfit:
                  final_limit = i
                  print("Reached limit i = ", i)
                  cstr = "Reached limit at i = " + str(i) + " Prev = " + str(prev_qfit) + " Next = " + str(next_qfit)  
                  st.write(cstr)
                  max_limit = i
                  tfit_wt = tfit[0:final_limit]
                  qfit_wt = hyperbolic(tfit_wt, qi_wt, di_wt, b_wt)
                  #st.write(cstr)
                  break

               
      if b_std >= 0:
         fdl = 1 # logic below not needed
         tfit_std = tfit
         qfit_std = hyperbolic(tfit, qi_std, di_std, b_std)
      else:
         tfit_std = tfit # initialize
         qfit_std = hyperbolic(tfit, qi_std, di_std, b_std)
         nForecast = len(tfit)
         cstr = "nForecast points for standard unweighted = " + str(nForecast)
         st.write(cstr)
         
         for i in range(nForecast):
            if i == 0:
               fdl = 1
            else:
               prev_qfit = qfit_std[i-1]
               next_qfit = qfit_std[i]
               if next_qfit > prev_qfit:
                  final_limit = i
                  print("Reached limit i = ", i)
                  cstr = "Reached limit at i = " + str(i) + " Prev = " + str(prev_qfit) + " Next = " + str(next_qfit)  
                  st.write(cstr)
                  max_limit = i
                  tfit_std = tfit[0:final_limit]
                  qfit_std = hyperbolic(tfit_std, qi_std, di_std, b_std)
                  #st.write(cstr)
                  break

 
            
         
      ax.plot(tfit_wt, qfit_wt, color='red', label="Hyperbolic Curve Fit Weighted More Recent")
          
      ax.plot(tfit_std, qfit_std, color='orange', label="Hyperbolic Curve Fit Not Weighted")

      any_title = 'Normalized ' + OIL_OR_GAS + ' Production Rate vs Time Plot'
      ax.set_title(any_title, size=16, pad=15)
   
      ax.set_xlabel('Normalized Producing Days')

      if OIL_OR_GAS == "OIL":   
         ax.set_ylabel('Oil BBL Per Month')
      elif OIL_OR_GAS == "GAS":   
         ax.set_ylabel('Natural Gas MCF Per Month')    
      
      #ax.set_yscale('log')
      plt.semilogy()
      #ax.set_xlim(min(series_time), max(series_time))
      ax.set_ylim(ymin=0)
      #ax.set_ylabel('Cost'))
      #ax.set_xlim(0.0, max(np_cum_days_std) * 1.50)
      ax.set_xlim(0.0, max(np_cum_days_std))
  
      ax.set_ylim(ymin=0)
  

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

      fig, ax = plt.subplots(2,1)
    
      #ma1_checkbox = st.checkbox('Moving Average 1')
    
      #ma2_checkbox = st.checkbox('Moving Average 2')
    
      ax[0].set_title('My Title')
      ax[0].plot(df_stockdata.index, df_stockdata.values,'g-',linewidth=1.6)
      #ax[0].set_xlim(ax[0].get_xlim()[0] - 10, ax[0].get_xlim()[1] + 10)
      ax[0].grid(True)
    
      if 1 == 1: #ma1_checkbox:
         #days1 = st.slider('Business Days to roll MA1', 5, 120, 30)
         #ma1 = df_stockdata.rolling(days1).mean()
         ax[0].plot(ma1, 'b-', label = 'MA %s days'%days1)
         ax[0].legend(loc = 'best')
      if ma2_checkbox:
         days2 = st.slider('Business Days to roll MA2', 5, 120, 30)
         ma2 = df_stockdata.rolling(days2).mean()
         ax[0].plot(ma2, color = 'magenta', label = 'MA %s days'%days2)
         ax[0].legend(loc = 'best')      

      #ax[1].set_title('Daily Total Returns %s' % ticker, fontdict = {'fontsize' : 15})
      #ax[1].plot(df_stockdata.index[1:], df_stockdata.pct_change().values[1:],'r-')
      #ax[1].set_xlim(ax[1].get_xlim()[0] - 10, ax[1].get_xlim()[1] + 10)
      plt.tight_layout()
      #ax[1].grid(True)
      st.pyplot()


   

   # plot the data
   #fig_scatter = px.scatter(df_county_summary, x='LEASE COUNT', y='COUNTY', 
   #        title="MY TITLE", 
   #        color="STATE", hover_data=["COUNTY", "STATE"])
   #fig_scatter.update_layout(yaxis={'visible': True, 'showticklabels': True})
   #fig_scatter.update_layout(xaxis={'visible': True, 'showticklabels': True})
   #fig_scatter.update_traces(marker=dict(size=5, opacity=0.7, line=dict(width=1,color='DarkSlateGrey')),selector=dict(mode='markers'))
   #st.plotly_chart(fig_scatter, use_container_width=True)




   # --- PLOT PIE CHART
   #fig_pie_chart = px.pie(df_county_summary,
   #                   title='Pie Chart of Wells Per County',
   #                   values='LEASE COUNT',
   #                   names='COUNTY')

   #st.plotly_chart(fig_pie_chart)
   #st.plotly_chart(fig_pie_chart, use_container_width=True)

   #if 1 == 1:   # aggregate sales by product lines, starting point for bar chart 

   # SALES BY PRODUCT LINE [BAR CHART]
   # 'Product line' is the .index
   # 'Total' is a column
   #sales_by_product_line = (
   #   df_selection.groupby(by=["Product line"]).sum()[["Total"]].sort_values(by="Total")
   #)

   # create bar chart
   # orientation = 'h' for horizontal bar chart
   #fig_county_summary = px.bar(
   #   df_county_summary,
   #   x="LEASE COUNT",
   #   #y=sales_by_product_line.index,
   #   y="COUNTY",
   #   orientation="h",
   #   title="<b>Well Counts By County</b>",
   #   color_discrete_sequence=["#0083B8"] * len(df_county_summary),
   #   template="plotly_white",
   #)


   # remove background color
   # remove gridlines
   #fig_county_summary.update_layout(
   #   plot_bgcolor="rgba(0,0,0,0)",
   #   xaxis=(dict(showgrid=False))
   #)
   
   #st.plotly_chart(fig_county_summary)
   




   
   #ave_sepal_length = df["Sepal_Length"].mean()
   #dist_county = pd.DataFrame(df_county["Sepal_Length"].value_counts())
   #st.subheader("Wells By County Distribution Plot")
   #st.bar_chart(df_county_summary["LEASE COUNT"])
   #st.bar_chart(data = df_county_summary, x="LEASE COUNT", y="COUNTY")



   #st.subheader("Summary Plot of Lease Count By County")
   #fig = plt.figure(figsize=(10, 4))
   #sns.countplot(data = df_county_summary, y='COUNTY')
   #st.pyplot(fig)


   if 1 == 2:
      df_lease = df_from_sqlite("KS", "SELECT * FROM Lease")
      df_to_webbrowser("df_lease", df_lease)
      st.dataframe(df_prod)
      list_lease = list(df_lease.columns)
      st.write(list_lease)

   if 1 == 2:
      df_prod = df_from_sqlite("KS", "SELECT * FROM LeaseProduction")
      df_to_webbrowser("df_prod", df_prod)
      st.dataframe(df_prod)
      list_prod = list(df_prod.columns)
      st.write(list_prod)

   #sql = "UPDATE citations SET first_author = ( SELECT initial_author FROM lookups WHERE lookups.pmid = citations.pmid )"    

   #cur.execute("DROP TABLE IF EXISTS citations")

   #sql_within_database(oSQLITE, sql)


   if 1 == 2:
      cSQL  = "SELECT gsm, series_id, gpl, description, title, source_name_ch1 "
      cSQL += "FROM gsm "
      cSQL += "WHERE organism_ch1 = 'Homo sapiens' "
      cSQL += "AND description NOT LIKE '%https%' "
      cSQL += "AND description NOT LIKE 'Gene expression%' "
      cSQL += "AND description NOT LIKE 'Gene_expression%' "
      cSQL += "AND description NOT LIKE 'The collected%' "

      cSQL += "AND title NOT LIKE 'PLACENTA%' "
 
      cSQL += "AND type = 'RNA' " 
      cSQL += "AND gpl LIKE 'GPL1%' AND series_id IS NOT NULL " 
      cSQL += "AND description IS NOT NULL AND title IS NOT NULL "
      cSQL += "AND source_name_ch1 IS NOT NULL "  
      cSQL += "ORDER BY series_id, gsm LIMIT 100000 "
     
 
      cSQL = "SELECT DISTINCT series_id, gpl FROM gsm WHERE gpl LIKE 'GPL1%' AND series_id IS NOT NULL ORDER BY gpl" #  LIMIT 500"
 
      #elif one_table == "INDEX":

      #Another way to get all indexes from a database is to query from the sqlite_master table:
      sql = "SELECT type, name, tbl_name, sql FROM sqlite_master WHERE type= 'index'"
      #print("df.head(100) of INDEXES")
      #print(df.head(100))
      #input("wait")

   if 1 == 2:  # WORKS ONE FIELD AT A TIME 
      sql = "UPDATE citations SET first_author = ( SELECT initial_author FROM lookups WHERE lookups.pmid = citations.pmid )"    
      #sql_within_database(oSQLITE, sql)

      sql = "UPDATE citations SET last_author = ( SELECT final_author FROM lookups WHERE lookups.pmid = citations.pmid )"    
      #sql_within_database(oSQLITE, sql)


   if 1 == 2:
      print("df.head(100) of citations sorted by pmid, citationid ")
      print(df.head(100))
      input("wait")
      #elif one_table == "TEMP":
                         
      #sql = "INSERT OR IGNORE INTO articles SELECT pmid, pmcid, title, year, journal, xml_file, doi, abstract FROM temp" 
      sql = "INSERT OR REPLACE INTO articles SELECT pmid, pmcid, title, year, journal, xml_file, doi, abstract FROM temp" 

      print("insert or replace records from temp table to articles table")
      start_time = start_timer()
      sql_within_database(oSQLITE, sql)
      end_timer(start_time)
 
      #elif one_table == "articles":

      print("rows = ", len(df_all), "before dropping duplicates")
      start_time = start_timer()
      df_all = df_all.drop_duplicates(subset=['pmid'], keep="first")
      end_timer(start_time)
   
      print("rows = ", len(df_all), "after dropping duplicates")
   

   if 1 == 2:
      #df_all["first_author"] = ""
      #df_all["last_author"] = ""

      start_time = start_timer()
      df_all.to_sql("temp", cnx, if_exists='replace', index = False)  # if_exists='append' 'replace'   
      end_timer(start_time)

      oSQLITE.close()
      #oENGINE.close()
      print()
      print("closed connections to oSQLITE and oENGINE")
      print()


     

   
