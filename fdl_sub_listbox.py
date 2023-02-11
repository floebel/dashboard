
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

import win32com.client    # part of pypiwin32

from fdl_sub_listbox import *
from fdl_sub_plot_histogram import *

import sys
import shutil
from shutil import copyfile


xlTop = -4160        # excel constants
xlBottom = -4107 
xlLeft = -4131 
xlCenter = -4108 
xlRight = -4152

#  cIN = "'35011', '35043', '35073', '35039' "               
#  cWhere := "WHERE LEFT(L.API,5) IN (" + cIN + ") "          
#  cWhere := " WHERE 69.1* SQR (( " + alltrim(STR(nLatitude)) + " - L.SurfaceLatitudeIHS ) ^ 2  + 0.6 * ( " + alltrim((str(nLongitude))) + " + L.SurfaceLongitudeIHS ) ^ 2 ) <= " + alltrim(str(nMaxMiles)) + space(1)
# //	cWhere += " AND LOE.GL_TRN_PRODDATE BETWEEN 2012 AND 2013 "
#    // 	cWhere += "	AND P.Year IN(2000,2001,2002,2003,2004,2005,2006,2007,2008,2009) "
#	 //	 	  cWhere += "AND WELL.LR_WEL_STATE IN ('KS','OK','CO') "
#	       cWhere := "WHERE WELL.LR_WEL_STATE = 'CO' AND WELL.LR_WEL_COUNTY = 'LAS ANIMAS' "
# 	    cSelect += " (SELECT COUNT(*) FROM Well WHERE Well.LeaseID = L.LeaseID) AS [WELL_COUNT], "                    // median


def raw_input(any_message):
   # Get dir name
   #any_input = input("Enter directory name \nline2 : ")
   any_input = input(any_message)
 
   #print("any_input = " + any_input)
   #input("Press ENTER to continue")
   return any_input

def Alert(any_message):
   # Get dir name
   #any_input = input("Enter directory name \nline2 : ")
   any_input = input(any_message)
 
   #print("any_input = " + any_input)
   #input("Press ENTER to continue")
   return any_input

def AlertBox(any_message):
   # Get dir name
   #any_input = input("Enter directory name \nline2 : ")
   any_input = input(any_message)
 
   #print("any_input = " + any_input)
   #input("Press ENTER to continue")
   return any_input

def get_input(any_message):
   # Get dir name
   #any_input = input("Enter directory name \nline2 : ")
   any_input = input(any_message)
 
   #print("any_input = " + any_input)
   #input("Press ENTER to continue")
   return any_input


def delete_file(any_path, any_file):
   
   any_delete = any_path + any_file
   ## if file exists, delete it ##
   if os.path.isfile(any_delete):
      os.remove(any_delete)
   else:    ## Show an error ##
      print("Error: %s file not found" % any_delete)
   input("Press ENTER to continue...file not found to delete")


def type_sum(any_thing):
   
   #>>> x = 12L
   #>>> import numbers
   #>>> isinstance(x, numbers.Integral)
   #True
   if isinstance(any_thing, int) == True:
      return any_thing   
   elif isinstance(any_thing, float) == True:
      return any_thing
   elif isinstance(any_thing, NoneType) == True:
      return 0
   elif 1 == 1:
      any_type = type(any_thing)
      #Alert("WARNING: type = " )
      #Alert(any_type)
      return 0
   
    
def open_xls(any_path, any_xls_table):   

   any_file = any_path + any_xls_table
   iLoop = 0

   #IF !file(any_file)
   #   Alert("Error: missing excel file " + any_file)
   #   RETURN .T.
   #ENDIF

   oApp = win32com.client.Dispatch('Excel.Application')

   oApp.DisplayAlerts = False

   oApp.Visible = True

   oApp.Workbooks.Open(any_file)  

   # click on A2 window  freeze panes
   # freeze row 1
   oApp.Range("A2").Select()  # freeze first row
   oApp.ActiveWindow.FreezePanes = True
   
   #// macro for centering cell ...
   oApp.Cells.Select
   #//   Application.WindowState = xlMinimized
   #//   Application.WindowState = xlNormal
   #//   Sheets("Sheet1").Name = "Sheet1"
   #//   Cells.Select
   #//   With Selection
   oApp.Cells.HorizontalAlignment = xlCenter
   oApp.Cells.VerticalAlignment = xlBottom
   
   # ExcelApp.ActiveCell.HorizontalAlignment = Microsoft.Office.Interop.Excel.Constants.xlCenter 

  
   oApp.Cells.Select
   #//   oApp:Range("A:Z"):Columns:Autofit      // autofit
   oApp.Range("A:AZ").Columns.Autofit      # autofit
   oApp.Range("A1:A1").Select








class ListBoxChoice(object):
    def __init__(self, master=None, title=None, message=None, list=[]):
       
        self.master = master
        self.value = None
        self.list = list[:]

        nitems = len(self.list)
        if nitems >= 25:
            nitems = 25
        #cstr = "nitems = " + str(nitems)
        #print(cstr)
        
        cmaxstring = max(self.list, key=len)
        nmaxwidth = len(cmaxstring)
        #cstr = "max width = " + str(nmaxwidth)
        #print(cstr)
        
        self.modalPane = Toplevel(self.master)

        self.modalPane.transient(self.master)
        self.modalPane.grab_set()

        self.modalPane.bind("<Return>", self._choose)
        self.modalPane.bind("<Escape>", self._cancel)

        if title:
            self.modalPane.title(title)

        if message:
            Label(self.modalPane, text=message).pack(padx=5, pady=5)

        listFrame = Frame(self.modalPane)
        listFrame.pack(side=TOP, padx=5, pady=5)
        #listFrame.pack(side=TOP, padx=25, pady=25)
  
        scrollBar = Scrollbar(listFrame)
        scrollBar.pack(side=RIGHT, fill=Y)
        self.listBox = Listbox(listFrame, selectmode=SINGLE)  # original
        
        #self.listBox = Listbox(listFrame, selectmode=SINGLE, height=20,width=60) # try
        self.listBox = Listbox(listFrame, selectmode=SINGLE, height=nitems+1,width=nmaxwidth+6) # try

        #listbox1 = tk.Listbox(root, font="Helvetica 11 bold", height=3, width=10)
        
        self.listBox.pack(side=LEFT, fill=Y)
        scrollBar.config(command=self.listBox.yview)
        self.listBox.config(yscrollcommand=scrollBar.set)
        if 1 == 2:
            self.list.sort()
        for item in self.list:
            self.listBox.insert(END, item)

        buttonFrame = Frame(self.modalPane)
        buttonFrame.pack(side=BOTTOM)

        chooseButton = Button(buttonFrame, text="Select One", command=self._choose)
        chooseButton.pack()

        #cancelButton = Button(buttonFrame, text="Cancel", command=self._cancel)
        #cancelButton.pack(side=RIGHT)

    def _choose(self, event=None):
        try:
            firstIndex = self.listBox.curselection()[0]
            self.value = self.list[int(firstIndex)]
        except IndexError:
            self.value = None
        self.modalPane.destroy()

    def _cancel(self, event=None):
        self.modalPane.destroy()
        
    def returnValue(self):
        self.master.wait_window(self.modalPane)
        return self.value






"""
   win = Tk()
   lb = Listbox(win, height=3)  # how many rows to display
   lb.pack()
   lb.insert(END,"first entry")
   lb.insert(END,"second entry")
   lb.insert(END,"third entry")
   lb.insert(END,"fourth entry")
   sb = Scrollbar(win,orient=VERTICAL)
   sb.pack(side=LEFT,fill=Y)
   sb.configure(command=lb.yview)
   lb.configure(yscrollcommand=sb.set)
   choice = lb.curselection()
 
   win.mainloop()
   print (choice)
   raw_input("Press ENTER to continue...")

   # ('2',)
"""
   
"""
   win=Tk()
   b1 = Button(win,text="One")
   b2 = Button(win,text="Two")
   #b2.pack(side=LEFT)
   #b1.pack(side=LEFT)
   b1.pack(side=LEFT,padx=10)
   b2.pack(side=LEFT,padx=10)
   #b1.pack()
   #b2.pack()
"""


"""
   import Tkinter
   parent_widget = Tkinter.Tk()
   lb = Tkinter.Listbox(win, height=3)
   listbox_entries = ["Entry 1", "Entry 2",
                      "Entry 3", "Entry 4"]
   listbox_widget = Tkinter.Listbox(parent_widget)
   for entry in listbox_entries:
      listbox_widget.insert(Tkinter.END, entry)
   listbox_widget.pack()
"""

"""
   Tkinter.mainloop()
 
   master=Tk()
   master.title("Listbox")

   listbox=Listbox(master, background="Blue", fg="white",selectbackground="Red",highlightcolor="Red")
   listbox.grid(row=1, column=1)

   for x in range(1, 10):

      listbox.insert(END, x)

   master.mainloop()
"""






"""
   root = Tk()
    
   returnValue = True
   list = ['aaa','bbb','ccc', 'eee', 'ttt', 'ppp', 'dsr','gyh','gdgfg','fghjh','jgggg','gtddfgg','hfdfg','dgjg','dghj','dgygff']
   #list = [3,4,9,21,17,82]
   #list = [random.randint(1,100) for x in range(50)]
   #while returnValue:
   returnValue = ListBoxChoice(root, "Select one", "Pick one of these", list).returnValue()
   root.destroy()
   print returnValue
      
   raw_input("Press ENTER to continue...")
"""





 






