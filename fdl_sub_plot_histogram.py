
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
from collections import Counter

#  cIN = "'35011', '35043', '35073', '35039' "               
#  cWhere := "WHERE LEFT(L.API,5) IN (" + cIN + ") "          
#  cWhere := " WHERE 69.1* SQR (( " + alltrim(STR(nLatitude)) + " - L.SurfaceLatitudeIHS ) ^ 2  + 0.6 * ( " + alltrim((str(nLongitude))) + " + L.SurfaceLongitudeIHS ) ^ 2 ) <= " + alltrim(str(nMaxMiles)) + space(1)
# //	cWhere += " AND LOE.GL_TRN_PRODDATE BETWEEN 2012 AND 2013 "
#    // 	cWhere += "	AND P.Year IN(2000,2001,2002,2003,2004,2005,2006,2007,2008,2009) "
#	 //	 	  cWhere += "AND WELL.LR_WEL_STATE IN ('KS','OK','CO') "
#	       cWhere := "WHERE WELL.LR_WEL_STATE = 'CO' AND WELL.LR_WEL_COUNTY = 'LAS ANIMAS' "
# 	    cSelect += " (SELECT COUNT(*) FROM Well WHERE Well.LeaseID = L.LeaseID) AS [WELL_COUNT], "                    // median






#grades = [83, 84, 91, 87, 70, 67, 23, 78, 86, 99]


# Floor division where decimal place is removed //
def decile(list_value):
   return list_value // 10 * 10


def create_df_histogram(any_df):

   """
   any_plot_df = []
   npoints = len(any_df)
   for i in range(npoints):
      any_adjusted = any_dfa[i]

      any_plot_df.append(any_rate)
   """
   
   if 1 == 1:

      #>>> np.median(a)
      
      #import statistics
      #items = [1, 2, 3, 6, 8]
      #statistics.median(items)
      #>>> 3
      
      #plt.hist(a, bins='auto')  # arguments are passed to np.histogram
      #sns.set()     # seaborn
      plt.hist(any_df, bins=30,rwidth=0.5)
      plt.xlabel("DF X LABEL")
      plt.ylabel("DF Y LABEL")
      plt.show()
   elif 1 == 1:
      #plt.hist(a, bins='auto')  # arguments are passed to np.histogram
      plt.hist(any_df, bins=30)
      plt.xlabel("DF X LABEL")
      plt.ylabel("DF Y LABEL")
      plt.show()
 
      #_  =  plt.hist(any_np_or_df)
      #_ = plt.xlabel("X LABEL")
      #_ = plt.ylabel("Y LABEL")


   elif 1 == 1:
      rng = any_np
      #rng = np.random.RandomState(10)  # deterministic random data
      a = np.hstack((rng.normal(size=1000),
                   rng.normal(loc=5, scale=2, size=1000)))
      plt.hist(a, bins='auto')  # arguments are passed to np.histogram
      plt.title("Histogram with 'auto' bins")
      plt.ylabel('Y LABEL')
      plt.xlabel('X LABEL')
  
      plt.show()


def create_numpy_histogram(any_MENU, any_np):
   
   list_plot = []
   npoints = len(any_np)
   for i in range(npoints):
      any_adjusted = any_np[i] / 1000.     # convert to MBBL or MMCF
      if any_adjusted >= 20:               # minimum EUR cutoff for Oil MBBL
         list_plot.append(any_adjusted)
         
   np_plot = np.asarray(list_plot)       # convert list to numpy array
   print("np_plot")
   print(np_plot)  

   if any_MENU == "OIL":
      cTitle = "Histogram of Oil EUR in MBBL for North Dakota\nUsing HHC Forecast From Power Tools"
      cX = "Bin for Oil EUR in MBBL"
      cY = "Frequency or Well Count in a Bin" 
   elif any_MENU == "GAS":
      cTitle = "Histogram of Gas EUR in MMCF for North Dakota\nUsing HHC Forecast From Power Tools"
      cX = "Bin for Gas EUR in MMCF"
      cY = "Frequency or Well Count in a Bin"
      
   if 1 == 1:
      hist_legend = []
      any_mean = np.mean(np_plot)
      any_median = np.median(np_plot) 
      cstr = "Mean (or Average) = " + str(any_mean)
      print(cstr)
      hist_legend.append(cstr)
      cstr = "Median (or Midpoint) = " + str(any_median)
      print(cstr)
      hist_legend.append(cstr)
      any_points = len(np_plot)
      cstr = "Wells included = " + str(any_points)
      hist_legend.append(cstr)
      print(cstr)
      cLegend = "" 
      l_rows = len(hist_legend)
      for i in range(l_rows):
         cLegend += hist_legend[i] + "\n"
         
      raw_input("Press ENTER to continue...")
 
     
      
      #import statistics
      #items = [1, 2, 3, 6, 8]
      #statistics.median(items)
      #>>> 3
      plt.figure(1)

      #plt.hist(a, bins='auto')  # arguments are passed to np.histogram
      #sns.set()     # seaborn
      plt.hist(np_plot, bins=30,rwidth=0.5)
      plt.title(cTitle)
      plt.grid(True)
      plt.legend([cLegend])

      plt.xlabel(cX)
      plt.ylabel(cY)
      plt.show()
   elif 1 == 1:
      #plt.hist(a, bins='auto')  # arguments are passed to np.histogram
      plt.hist(any_np, bins=30)
      plt.xlabel("X LABEL")
      plt.ylabel("Y LABEL")
      plt.show()
 
      #_  =  plt.hist(any_np_or_df)
      #_ = plt.xlabel("X LABEL")
      #_ = plt.ylabel("Y LABEL")


   elif 1 == 1:
      rng = any_np
      #rng = np.random.RandomState(10)  # deterministic random data
      a = np.hstack((rng.normal(size=1000),
                   rng.normal(loc=5, scale=2, size=1000)))
      plt.hist(a, bins='auto')  # arguments are passed to np.histogram
      plt.title("Histogram with 'auto' bins")
      plt.ylabel('Y LABEL')
      plt.xlabel('X LABEL')
  
      plt.show()

    
    


def create_list_histogram(any_list):

   if 1 == 1:

      # Create population of 1000 dog, 50/50 greyhound/labrador
      greyhounds = any_list
      labs = 500


      # Assume greyhounds are normally 28" tall
      # Assume labradors are normally 24" tall
      # Assume normal distribution of +/- 4"
      grey_height = 28 + 4 * np.random.randn(greyhounds)
      lab_height = 24 + 4 * np.random.randn(labs)

      # Greyounds - red, labradors - blue
      plt.hist([grey_height, lab_height], stacked=True, color=['r', 'b'])
      plt.show()

   if 1 == 1:

      # Create population of 1000 dog, 50/50 greyhound/labrador
      greyhounds = 500
      labs = 500


      # Assume greyhounds are normally 28" tall
      # Assume labradors are normally 24" tall
      # Assume normal distribution of +/- 4"
      grey_height = 28 + 4 * np.random.randn(greyhounds)
      lab_height = 24 + 4 * np.random.randn(labs)

      # Greyounds - red, labradors - blue
      plt.hist([grey_height, lab_height], stacked=True, color=['r', 'b'])
      plt.hist([grey_height, lab_height], stacked=True, color=['r', 'b'])
      plt.show()

   elif 1 == 1:


      # {80: 4, 90: 2, 70: 2, 20: 1, 60: 1}
      histogram = Counter(decile(item) for item in any_list)

      plt.bar([x - 4 for x in histogram.keys()],  # center bars by shifting left
           histogram.values(),  # height
           8)  # width of 8

      # x-axis range, y-axis range
      plt.axis([-5, 105, 0, 5])

      plt.xticks([10 * i for i in range(11)])

      plt.ylabel('Number of Students')
      plt.title('Test Scores')
      plt.show()




def eur_oil_and_gas_from_power_tools_csv():

   
   csv_file = "eur_oil_and_gas_from_power_tools.csv"   
   df_all = pd.read_csv(csv_file)
   
   #df_subset = df_all[['STATE','CASHFLOW','WELLCODE','NETOILREMMBBL','NETGASREMMMCF','WORKINGROYALTY']]      # select columns 
   df_subset = df_all[['RESV_YEAR','EUR_OIL','EUR_GAS','CASHFLOW','STATE']]      # select columns 
   #df_subset = df_all[['LEASEID','WELLNAME','STATE','COUNTY','BEST_BOPD','BEST_MCFD','PROD_PTS','ECON_LIFE', 'CASHFLOW','NETOILREM','NETGASREM','OIL_EUR','GAS_EUR']]      # select columns 
   #df_one_state = df_subset[df_all['STATE'] == 'SD']       # filter one state
   #df_one_state = df_subset[df_all['STATE'] == study_state]     # filter one state
   df_one_state = df_subset[df_all['RESV_YEAR'] >= 2007]     # filter one state

   #df = df_pre.sort_values('2')                                                        # how to sort leases............
   #df = df_pre.sort(['CASHFLOW', 'WELLCODE'], ascending=[0, 1])
   if 1 == 1:
      df = df_one_state.sort_values(by=['RESV_YEAR'], ascending=True)  # ascending
   elif 1 == 2:
      df = df_one_state.sort_values(by=['CASHFLOW'], ascending=False)  # descending
   elif study_product == "OIL":
      df = df_one_state.sort_values(by=['NETOILREM'], ascending=False)  # descending
      #df = df_one_state.sort_values(by=['BEST_BOPD'], ascending=False)  # descending
   elif study_product == "GAS":
      df = df_one_state.sort_values(by=['NETGASREM'], ascending=False)  # descending
      #df = df_one_state.sort_values(by=['BEST_MCFD'], ascending=False)  # descending
   #df = df_one_state.sort_values(by=['CASHFLOW'], ascending=False)  # descending
 
   print (df.head())
                       
   np_eur_oil = np.array(df["EUR_OIL"])
   np_eur_gas = np.array(df["EUR_GAS"])
                  
   """
   np_wellcode = np.array(df["LEASEID"])
   np_wellname = np.array(df["WELLNAME"]) 
   np_best_bopd = np.array(df["BEST_BOPD"]) 
   np_best_mcfd = np.array(df["BEST_MCFD"]) 
   np_prod_pts = np.array(df["PROD_PTS"]) 
   np_econ_life = np.array(df["ECON_LIFE"]) 
   np_cashflow = np.array(df["CASHFLOW"]) 
   np_netoilrem = np.array(df["NETOILREM"]) 
   np_netgasrem = np.array(df["NETGASREM"]) 
   np_oil_eur = np.array(df["OIL_EUR"]) 
   np_gas_eur = np.array(df["GAS_EUR"]) 
   """
                       
   if 1 == 2: 
      create_df_histogram(df["OIL_EUR"])  # under development
   elif 1 == 1:
      create_numpy_histogram("OIL", np_eur_oil)
      create_numpy_histogram("GAS", np_eur_gas)







# MAIN if NEEDED .................


# eur_oil_and_gas_from_power_tools_csv()




 






