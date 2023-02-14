

#from fdl_sub_hyperbolic import *   # A06
from gekko_functions import *   # A06
from dca_functions import *

from fdl_sub_html_small import *

from sqlite3_functions import *

import streamlit as st
import sqlite3
import pandas as pd
import seaborn as sns
import numpy as np
#import probscale
import matplotlib.pyplot as plt
import matplotlib
import matplotlib.ticker as tick
from matplotlib import style
from matplotlib.ticker import FormatStrFormatter
import plotly.express as px  # pip install plotly-express

from scipy.optimize import curve_fit

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





def fig_group_by(any_state, any_county):  # SPECIAL ###########
   
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
   cSelect += " (SELECT count(P.LeaseID) FROM LeaseProduction P WHERE P.LeaseID = L.LeaseID AND P.Oil > 1.0) AS 'OIL_PTS', "   
   cSelect += " (SELECT count(P.LeaseID) FROM LeaseProduction P WHERE P.LeaseID = L.LeaseID AND P.Gas > 10.0) AS 'GAS_PTS' "   

  
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
   cWhere  = " WHERE L.LAT_LENGTH >= 1000 "
   cWhere += " AND L.MAX_MONTHS >= 6 AND L.MAX_MONTHS <= 36 "
   #cWhere += " AND L.MAX_MONTHS >= 12 "

   cWhere += " AND P.CUMUL_MONTHS >= 0 AND P.CUMUL_MONTHS <= 36 "  # ?????????
   #cWhere += " AND (P.Oil > 0 OR P.Gas > 0) "
   #cWhere += " AND (P.Oil > 0 OR P.Gas > 0) "
   cWhere += " AND (P.Oil > 1.0 OR P.Gas > 10.0) "

   #nProdPoints = 24
   #cWhere += " AND (SELECT count(*) FROM LeaseProduction PROD WHERE PROD.LeaseID = L.LeaseID) >= " + str(nProdPoints) + " "
   #cWhere += " AND (SELECT count(*) FROM LeaseProduction PROD WHERE PROD.LeaseID = L.LeaseID) >= 24 AND (P.Oil > 0 OR P.Gas > 0) "
      
   #cWhere += " AND L.COUNTY = 'OKLAHOMA' "
   #cWhere += " AND L.COUNTY = 'GRADY' "
   #cWhere += "	AND L.County IN ('OKLAHOMA', 'GRADY', 'CLEVELAND','WOODS','ALFALFA','GRANT','MAJOR','GARFIELD','BLAINE','KINGFISHER','LOGAN','CANADIAN') "

   if any_county == "":
      fdl = 1
   else:
      cWhere += " AND L.COUNTY = '" + any_county + "' "

   

   if 1 == 1:
      fdl = 1   
   elif any_state == "KS":
      cWhere += "AND L.County IN ('COMANCHE', 'HARPER') "
   elif any_state == "OK":
      cWhere += "AND L.County IN ('OKLAHOMA', 'CANADIAN') "
      

   cOrderBy = " GROUP BY P.CUMUL_MONTHS "
 
   cSQL = cSelect + cFrom + cWhere + cOrderBy

   if 1 == 2:
      st.write(cSQL)   
   
   df = df_from_sqlite(any_state, cSQL)

   df["Ave Monthly Oil Per Well"] = df["OIL_SUM"] / df["OIL_PTS"]
   df["Ave Monthly Gas Per Well"] = df["GAS_SUM"] / df["GAS_PTS"]

   df["CUMUL_MONTHS"] = df["CUMUL_MONTHS"] + 1.0

   df["CUMUL_YEARS"] = df["CUMUL_MONTHS"] / 12.0
   df["CUMUL_DAYS"] = df["CUMUL_YEARS"] * 365.25
  
   df["BOPD"] = df["Ave Monthly Oil Per Well"] / 30.4375
   df["MCFD"] = df["Ave Monthly Gas Per Well"] / 30.4375

   

   list_drop = ["CUMUL_YEARS", "CUMUL_MONTHS", "OIL_SUM", "GAS_SUM", "Ave Monthly Oil Per Well", "Ave Monthly Gas Per Well"] 
   df = df.drop(list_drop, axis=1)

   df.replace([np.nan, np.inf, -np.inf], 0, inplace=True)
   

   if 1 == 2:
      df.to_csv("normalized_monthly_production.csv", index=False)
      
   if 1 == 2:
      st.subheader("df _groupby")
      st.dataframe(df)  
   return df


def fig_rate_at_cum_days(q_daily, h_hyperbolic, d_daily, any_cum_days):

   any_days_plus = any_cum_days + 16.0
   any_days_minus = any_cum_days - 16.0

   any_cumul_minus = 1.0 * fig_hyperbolic_cumulative_volume (q_daily, h_hyperbolic, d_daily, any_days_minus)
   any_cumul_plus  = 1.0 * fig_hyperbolic_cumulative_volume (q_daily, h_hyperbolic, d_daily, any_days_plus)
   any_rate = (any_cumul_plus - any_cumul_minus) / 32.0
   return any_rate
 
 


def hyperbolic_equation(t, qi, b, di):
   """
   Hyperbolic decline curve equation
   Arguments:
       t: Float. Time since the well first came online, can be in various units 
       (days, months, etc) so long as they are consistent.
       qi: Float. Initial production rate when well first came online.
       b: Float. Hyperbolic decline constant
       di: Float. Nominal decline rate at time t=0
   Output: 
       Returns q, or the expected production rate at time t. Float.
   """
   #return qi/((1.0+b*di*t)**(1.0/b))
   return  qi/np.power((1+b*di*t), 1./b)
   

def scipy_curve_fit(OIL_OR_GAS, list_days, list_production):   # SPECIAL

   if 1 == 2:
      list_days = [ 30, 60, 90, 120, 150, 180, 210]
      list_production = [100, 90, 80, 70, 60, 50, 40]
      #nPoints = len(list_time)      

   if 1 == 1:   # SCIPY OPTIMIZE CURVE_FIT
            
      list_time = []
      list_rate = []

      #if OIL_OR_GAS == "OIL":
      nPoints = len(list_days)
      nMaxPoint = fig_max_point(list_production) 
      max_daily_rate = list_production[nMaxPoint]
      max_daily_days = list_days[nMaxPoint]
 
      max_production_days = list_days[nPoints - 1]
      cstr = OIL_OR_GAS + " max production days = " + str(max_production_days)
      if 1 == 1:
         print(cstr)   
         st.write(cstr)
      
      half_production_days = int(max_production_days/2.0)
      quarter_production_days = int(0.25 * max_production_days)
      last_quarter_production_days = int(0.75 * max_production_days)

      mid_adjust_days = half_production_days
  
      cstr = OIL_OR_GAS + " max daily rate = " + str(max_daily_rate) + " at point " + str(nMaxPoint)
      if 1 == 1:
         print(cstr)   
         st.write(cstr)
      cstr = OIL_OR_GAS + " max daily rate = " + str(max_daily_rate) + " at cumul days " + str(max_daily_days)
      if 1 == 1:
         print(cstr)   
         st.write(cstr)    

      mid_max_daily_rate = 0
      mid_max_daily_days = 0
      
      nIncluded = 0
      for i in range(nPoints):
         if i < nMaxPoint:  # only analyze points on or after nMaxPoint
            fdl = 1
         else:   
            next_time = list_days[i]
            #if OIL_OR_GAS == "OIL":
            next_rate = list_production[i]
              
            #if nIncluded <= 6:    # always include the first 6 points from max rate ...
            #   list_time.append(next_time)
            #   list_rate.append(next_rate)
            #   nIncluded = nIncluded + 1
            if 1 == 2:  # next_time >= quarter_production_days:  # add more weight to 2nd half of history
               list_time.append(next_time)
               list_rate.append(next_rate)
               nIncluded = nIncluded + 1  
            elif next_time >= half_production_days:  # add more weight to 2nd half of history
               if next_rate > mid_max_daily_rate:
                  mid_max_daily_rate = next_rate
                  mid_max_daily_days = next_time 
               
               list_time.append(next_time - mid_adjust_days) # ??????
               list_rate.append(next_rate)
               nIncluded = nIncluded + 1
               if next_time >= last_quarter_production_days: # more weight ....
                  list_time.append(next_time - mid_adjust_days)  # ??????
                  list_rate.append(next_rate)   

      if 1 == 2:
         st.write(list_time)
         st.write(list_rate)
       
      cstr = "mid_max_daily_rate = " + str(mid_max_daily_rate)
      st.write(cstr)
      cstr = "mid_max_daily_days = " + str(mid_max_daily_days)
      st.write(cstr)  
      
      #Hyperbolic curve fit 
      if 1 == 2:
         qi_min = max_daily_rate * 0.50
         qi_max = max_daily_rate * 1.50  # 1.10
      else:
         qi_min = mid_max_daily_rate * 0.95
         qi_max = mid_max_daily_rate * 1.05
         #mid_max_daily_rate = next_rate
         #mid_max_daily_days = next_time

      cstr = "qi_min = " + str(qi_min)
      st.write(cstr)
      cstr = "qi_max = " + str(qi_max)
      st.write(cstr)  
      
      b_min = 0.001 # -3.0 # 0.001
      #b_min = -3.0 # -3.0 # 0.001
      b_max = 3.0
      di_min = 0.00001
      di_max = 99.9999

      np_time = np.array(list_time)
      np_rate = np.array(list_rate)

      
 
   
      opt_hyp, cov_hyp = curve_fit(hyperbolic_equation,\
                                   np_time,\
                                   np_rate,\
                                   bounds=((qi_min, b_min, di_min), (qi_max, b_max, di_max)) )

      #opt_hyp = np.round(opt_hyp, decimals=5)


      #cstr = "Hyperbolic Fit Curve-fitted Variables: qi='+str(opt_hyp[0])+', b='+str(opt_hyp[1])+', di='+str(opt_hyp[2]))
      #input("wait")
      q_daily = opt_hyp[0]
      if 1 == 1:
         cstr = "Predicted Initial Rate Qi = " + str(q_daily)
         st.write(cstr)
      
      h_hyperbolic  = opt_hyp[1]
      if 1 == 1:
         cstr = "Predicted Hyperbolic bi = " + str(h_hyperbolic)
         st.write(cstr)

      d_daily = opt_hyp[2]
      if 1 == 1:
         cstr = "Predicted Daily Di = " + str(d_daily)
         st.write(cstr)

      max_plot_rate = max_daily_rate  # ????????
      if q_daily > max_plot_rate:
         max_plot_rate = q_daily
      if 1 == 1:
         cstr = "Max rate for plot = " + str(max_plot_rate)
         st.write(cstr)
         



   if 1 == 2:
      
      #def arps_hyperbolic_rate(qi, di, b, t):
      # return qi / ((1.0 + b * di * t) ** (1.0 / b))
      rate_at_60_days = hyperbolic_equation(q_daily, d_daily, h_hyperbolic, 60)
      cstr = "rate at 60 days = " + str(rate_at_60_days)
      st.write(cstr) 
 
      rate_at_120_days = hyperbolic_equation(q_daily, d_daily, h_hyperbolic, 120)
      cstr = "rate at 120 days = " + str(rate_at_120_days)
      st.write(cstr) 
  
      rate_at_180_days = hyperbolic_equation(q_daily, d_daily, h_hyperbolic, 180)
      cstr = "rate at 180 days = " + str(rate_at_180_days)  
      st.write(cstr) 

      rate_at_360_days = hyperbolic_equation(q_daily, d_daily, h_hyperbolic, 360)
      cstr = "rate at 360 days = " + str(rate_at_360_days)  
      st.write(cstr)

      rate_at_720_days = hyperbolic_equation(q_daily, d_daily, h_hyperbolic, 720)
      cstr = "rate at 720 days = " + str(rate_at_720_days)  
      st.write(cstr)    

      

   if 1 == 2:
      st.set_option('deprecation.showPyplotGlobalUse', False) 
      #fig, ax = plt.subplots(figsize=(10,7))
      
      #import matplotlib.pyplot as plt
      plt.figure(figsize=(10,7))
      #x_data = b
      #y_data = a_x_b
      #popt, pcov = curve_fit(duong, list_time, list_prod, bounds=([0, 0, 0],[10000, 2.99, 2.99]))
      #popt, pcov = curve_fit(duong, list_time, list_prod)

      #print('This is the best fit we found for well ', popt) # print Coefficients per well
      any_label = "Normalized " + OIL_OR_GAS + " Production Data"
      plt.step(list_time, list_rate, label = any_label)

      min_days = min(list_time)
      max_days = max(list_time)
      nPlot = len(list_time)
      np_xdata = np.linspace(min_days, max_days, nPlot)  # define data to predict 
      #q = duong(list_time, popt[0], popt[1], popt[2])
      
      np_time = np.array(list_time)
      np_rate = np.array(list_rate)   

      q = hyperbolic_equation(np_time, opt_hyp[0], opt_hyp[1], opt_hyp[2])
      plt.plot(np_xdata, q, '-', color = "red", label="Fitted Function" )
    
      plt.yscale('log') 
   
      #q = duong(time, popt[0], popt[1], popt[2]) 
      #plt.plot(list_time, duong(list_time, popt[0], popt[1], popt[2]), label='Fitted function')
      plt.legend(loc='best')
      #plt.show()
      st.pyplot() 

      #input("wait")   


   if 1 == 1:

      st.set_option('deprecation.showPyplotGlobalUse', False) 
      fig, ax = plt.subplots(figsize=(10,7))
      # fig, ax = plt.subplots() 
      #ax.set_figure(figsize=(10,7))
      #ax.step(series_time, series_rate, color='blue')
      #ax.step(np_cum_days_std, series_rate, color='blue', label="Normalized Production Data")      

      # list_days, list_production):   


      if OIL_OR_GAS == "OIL":
         #ax.step(xm, ym, color='green', label="Normalized Oil Rate BOPD")
         #ax.step(list_time, list_rate, color='green', label="Normalized Oil Rate BOPD")
         ax.step(list_days, list_production, color='green', label="Normalized Oil Rate BOPD")
      
      elif OIL_OR_GAS == "GAS":
         #ax.step(xm, ym, color='red', label="Normalized Gas Rate MCFD")
         #ax.step(list_time, list_rate, color='red', label="Normalized Gas Rate MCFD")
         ax.step(list_days, list_production, color='red', label="Normalized Gas Rate MCFD")

      #list_predict_days = []
      #list_predict_years = []
      #list_actual_rate = []
      #list_predict_rate = []
      #list_predict_cumul = []

      #min_time = min(list_time)
      #max_time = max(list_time)

      #np_time = np.array(list_time)
      #np_rate = np.array(list_rate)

      #nPlot = len(list_time)  

      #plt.step(list_time, list_rate, color='green', label="Normalized Oil Rate BOPD")

      #np_xdata = np.linspace(min_time, max_time, nPlot)   # define data to predict 

      #q = hyperbolic_equation(np_time, opt_hyp[0], opt_hyp[1], opt_hyp[2]) 

      #plt.plot(np_xdata, q, '-', color = "blue", label="Hyperbolic Fit" )

      #ax.plot(np_xdata, q, color='blue', linestyle = 'dashed', label = "Hyperbolic Curve Fit")

      plt.yscale('log') 


      if 1 == 2:
         #ax.plot(list_predict_years, list_predict_rate, color='blue', linestyle = 'dashed', label = "Predicted Rate From Hyperbolic Eqn")
         ax.plot(list_predict_days, list_predict_rate, color='blue', linestyle = 'dashed', label = "Predicted Rate From Hyperbolic Eqn")

      #   any_cumul_01 = 0.001 * fig_hyperbolic_cumulative_volume (q_daily, h_hyperbolic, d_daily, 1.0 * 365.25)
      #   any_cumul_01 = 0.001 * fig_hyperbolic_cumulative_volume (q_daily, h_hyperbolic, d_daily, 1.0 * 365.25)

      #max_daily_rate = list_production[nMaxPoint]
      #max_daily_days = list_days[nMaxPoint]

      list_pred_time = []
      list_pred_rate = []
      # OIL_OR_GAS, list_days, list_production): 
      #nProductionPoints = len(list_production)
      #nProductionDays = int(list_production[nProductionPoints-1])

      #cstr = "nProductionDays = " + str(nProductionDays)
      #st.write(cstr)

      # start forecast here ... mid_adjust_days = half_production_days

      nForecastPoints = int(max_production_days / 30.4375) # + 24  # extra 2 years to forecast    
      #nKeepPoints = len(list_time)
      #nKeepDays = int(list_time[nKeepPoints-1])
      adjust_days = max_daily_days 
      for i in range(nForecastPoints):
         #next_days = ((i + 1) * 30.4375) + adjust_days - 30.4375
         next_days = ((i + 1) * 30.4375) - 30.4375  # + mid_adjust_days #  - 30.4375  # ??????
 
         #st.write(next_days)
         if next_days <= max_production_days - half_production_days:  # since some points are weighted ... 
            next_rate = fig_rate_at_cum_days(q_daily, h_hyperbolic, d_daily, next_days)
            list_pred_time.append(next_days + mid_adjust_days)  # ??????
            list_pred_rate.append(next_rate)

      #st.write(list_pred_time)
      #st.write(list_pred_rate)
 
            
      ax.plot(list_pred_time, list_pred_rate, color='purple', linestyle = 'dashed', label = "Hyperbolic Curve Fit")

      if 1 == 2:
         ax.plot(xm, yp, color='blue', linestyle = 'dashed', label = "Predicted Rate From Hyperbolic Eqn")

      #plt.plot(students, marks, color = 'green',
      #linestyle = 'solid', marker = 'o',
      #markerfacecolor = 'red', markersize = 12)
      
      #ax.plot(xm, yp, color='red', label="Hyperbolic Curve Fit Weighted More Recent")
          
      #ax.plot(tfit_std, qfit_std, color='orange', label="Hyperbolic Curve Fit Not Weighted")

      any_title = 'Normalized ' + OIL_OR_GAS + ' Production Rate vs Time Plot'
      ax.set_title(any_title, size=16, weight='bold' ,pad=15)
   
      ax.set_xlabel('Normalized Producing Days', size=12, weight='bold')

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

      if 1 == 1:
         any_cumul_01 = 0.001 * fig_hyperbolic_cumulative_volume (q_daily, h_hyperbolic, d_daily, 1.0 * 365.25)
         any_cumul_02 = 0.001 * fig_hyperbolic_cumulative_volume (q_daily, h_hyperbolic, d_daily, 2.0 * 365.25)
         any_cumul_05 = 0.001 * fig_hyperbolic_cumulative_volume (q_daily, h_hyperbolic, d_daily, 5.0 * 365.25)
         any_cumul_10 = 0.001 * fig_hyperbolic_cumulative_volume (q_daily, h_hyperbolic, d_daily, 10.0 * 365.25)
         any_cumul_15 = 0.001 * fig_hyperbolic_cumulative_volume (q_daily, h_hyperbolic, d_daily, 15.0 * 365.25)
         #any_cumul_20 = 0.001 * fig_hyperbolic_cumulative_volume (q_daily, h_hyperbolic, d_daily, 20.0 * 365.25)
         #any_cumul_30 = 0.001 * fig_hyperbolic_cumulative_volume (q_daily, h_hyperbolic, d_daily, 30.0 * 365.25)
         if OIL_OR_GAS == "OIL":
            text_cumul  = "EUR  1 Year = " + str(round(any_cumul_01,0)) + " MBBL Oil"
            text_cumul += "\nEUR  2 Year = " + str(round(any_cumul_02,0)) + " MBBL Oil"
            text_cumul += "\nEUR  5 Year = " + str(round(any_cumul_05,0)) + " MBBL Oil"
            text_cumul += "\nEUR 10 Year = " + str(round(any_cumul_10,0)) + " MBBL Oil"
            text_cumul += "\nEUR 15 Year = " + str(round(any_cumul_15,0)) + " MBBL Oil"
            #text_cumul += "\nEUR 20 Year = " + str(round(any_cumul_20,0)) + " MBBL Oil"
            #text_cumul += "\nEUR 30 Year = " + str(round(any_cumul_30,0)) + " MBBL Oil"
         elif OIL_OR_GAS == "GAS":
            text_cumul  = "EUR  1 Year = " + str(round(any_cumul_01,0)) + " MMCF Gas"
            text_cumul += "\nEUR  2 Year = " + str(round(any_cumul_02,0)) + " MMCF Gas"
            text_cumul += "\nEUR  5 Year = " + str(round(any_cumul_05,0)) + " MMCF Gas"
            text_cumul += "\nEUR 10 Year = " + str(round(any_cumul_10,0)) + " MMCF Gas"
            text_cumul += "\nEUR 15 Year = " + str(round(any_cumul_15,0)) + " MMCF Gas"
            #text_cumul += "\nEUR 20 Year = " + str(round(any_cumul_20,0)) + " MMCF Gas"
            #text_cumul += "\nEUR 30 Year = " + str(round(any_cumul_30,0)) + " MMCF Gas"    


         from matplotlib.offsetbox import AnchoredText
         # anchored_text = AnchoredText(text_cumul, loc=4, prop={'weight': 'bold', 'fontsize': 12, 'color': 'black'},
         anchored_text = AnchoredText(text_cumul, loc=3, prop={'fontsize': 12, 'color': 'black'},
                                       **{'frameon': True})
         ax.add_artist(anchored_text)


      #print("max_daily_rate = ", max_daily_rate)



      if 1 == 2:
         
         ax.set_yticks([0.1, 0.3, 1, 3, 10, 30, 100, 300, 1000, 3000, 10000])
         ax.get_yaxis().set_major_formatter(matplotlib.ticker.ScalarFormatter())
         ax.yaxis.set_major_formatter(FormatStrFormatter('%.2f'))
         #ax.get_yaxis().set_major_formatter(FormatStrFormatter('%.2f')) 
         ax.set_ylim(0.1, 10000)

         
      elif max_plot_rate >= 30000:
         ax.set_yticks([1, 3, 10, 30, 50, 100, 300, 1000, 3000, 10000, 30000, 100000])
         ax.get_yaxis().set_major_formatter(matplotlib.ticker.ScalarFormatter())
         #ax.get_yaxis().set_major_formatter(FormatStrFormatter('%.1f')) 
         ax.set_ylim(1.0, 100000)
         
      elif max_plot_rate >= 10000:
         ax.set_yticks([1, 3, 10, 30, 50, 100, 300, 1000, 3000, 10000, 30000])
         ax.get_yaxis().set_major_formatter(matplotlib.ticker.ScalarFormatter())
         #ax.get_yaxis().set_major_formatter(FormatStrFormatter('%.1f')) 
         ax.set_ylim(1.0, 30000)
         
      elif max_plot_rate >= 3000:
         ax.set_yticks([1, 3, 10, 30, 50, 100, 300, 1000, 3000, 10000])
         ax.get_yaxis().set_major_formatter(matplotlib.ticker.ScalarFormatter())
         #ax.get_yaxis().set_major_formatter(FormatStrFormatter('%.1f')) 
         ax.set_ylim(1, 10000)
         
      #elif max_plot_rate >= 2000:
      #   ax.set_yticks([0.03, 0.10, 0.3, 1, 3, 10, 30, 100, 300, 1000, 3000, 10000])
      #   ax.get_yaxis().set_major_formatter(matplotlib.ticker.ScalarFormatter())
      #   #ax.get_yaxis().set_major_formatter(FormatStrFormatter('%.2f')) 
      #   ax.set_ylim(0.03, 10000)

      elif max_plot_rate >= 1000:
         ax.set_yticks([1, 3, 10, 30, 100, 300, 1000, 3000])
         ax.get_yaxis().set_major_formatter(matplotlib.ticker.ScalarFormatter())
         #ax.get_yaxis.set_major_formatter(FormatStrFormatter('%.2f')) 
         ax.set_ylim(1, 3000)

      #elif max_plot_rate >= 500:
      #   ax.set_yticks([0.01, 0.03, .1, .3, 1, 3, 10, 30, 100, 300, 1000, 3000])
      #   ax.get_yaxis().set_major_formatter(matplotlib.ticker.ScalarFormatter())
      #   #ax.get_yaxis().set_major_formatter(FormatStrFormatter('%.2f')) 
      #   ax.set_ylim(0.01, 3000)

      elif max_plot_rate >= 300:
         ax.set_yticks([1, 3, 10, 30, 100, 300, 1000])
         ax.get_yaxis().set_major_formatter(matplotlib.ticker.ScalarFormatter())
         #ax.get_yaxis().set_major_formatter(FormatStrFormatter('%.3f')) 
         ax.set_ylim(1, 1000)        
            
      elif max_plot_rate >= 100:
         ax.set_yticks([1, 3, 10, 30, 100, 300])
         ax.get_yaxis().set_major_formatter(matplotlib.ticker.ScalarFormatter())
         #ax.get_yaxis().set_major_formatter(FormatStrFormatter('%.3f')) 
         ax.set_ylim(1, 300)

      elif max_plot_rate >= 30:
         ax.set_yticks([1, 3, 10, 30, 100])
         ax.get_yaxis().set_major_formatter(matplotlib.ticker.ScalarFormatter())
         #ax.get_yaxis().set_major_formatter(FormatStrFormatter('%.3f')) 
         ax.set_ylim(1, 100)

      elif max_plot_rate >= 10:
         ax.set_yticks([1, 3, 10, 30])
         ax.get_yaxis().set_major_formatter(matplotlib.ticker.ScalarFormatter())
         #ax.get_yaxis().set_major_formatter(FormatStrFormatter('%.3f')) 
         ax.set_ylim(1, 100)        
                  
               
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
      #st.pyplot()
      st.pyplot(fig)


      #input("wait line 1118")




   
   if 1 == 2:
      
      
      st.dataframe(df)

      series_time = df['CUMUL_DAYS']

      OIL_OR_GAS = "GAS"  ######################

      if OIL_OR_GAS == "OIL":
         series_rate = df['BOPD']
      elif OIL_OR_GAS == "GAS":
         series_rate = df['MCFD']    
      
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




   # remove background color
   # remove gridlines
   #fig_county_summary.update_layout(
   #   plot_bgcolor="rgba(0,0,0,0)",
   #   xaxis=(dict(showgrid=False))
   #)
   
   #st.plotly_chart(fig_county_summary)
   

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


  
def handle_state_change():
   if st.session_state.state_picked:
      st.session_state.type = st.session_state.state_picked
      
   
def handle_county_change():
   if st.session_state.county_picked:
      st.session_state.type = st.session_state.county_picked
      
   



def main():
   st.title("Hyperbolic Curve Fitting")
   #st.info(
   #    """
   #    This app is maintained by Fulton Loebel
   #    """
   #)



   if 1 == 2:
      #st.subheader("Distinct Query")
      cSQL = "SELECT * FROM Lease LIMIT 10 "
      df = df_from_sqlite("KS", cSQL)
      list_cols = list(df.columns)
      st.write(list_cols)
      #st.dataframe(df)
      cSQL = "SELECT * FROM Lease LIMIT 10 "
      df = df_from_sqlite("OK", cSQL)
      list_cols = list(df.columns)
      st.write(list_cols)
      #st.dataframe(df)

   if 1 == 2:
      st.subheader("Distinct Query")
      cSQL = "SELECT DISTINCT Year, Month FROM LeaseProduction WHERE Year >= 2000 ORDER BY Year, Month "
      df = df_from_sqlite("OK", cSQL)
      st.dataframe(df)


   
   #st.subheader("Ave Normalized Production Per Well")

   #any_state = "OK"


   #OIL_OR_GAS = "GAS"  ######################
      

   any_state = "OK"
   state_picked = "OK"
   st.session_state['any_state'] = ""  # initialize          

   if len(st.session_state.any_state) == 0:
      any_title = "Select either KS (Kansas) or OK (Oklahoma) to analyze"
   else:  
      any_title = "Hyperbolic curve fitting in State Of " + any_state
   #st.title(any_title)
   st.subheader(any_title)
 
   #st.info(
   #    """
   #    This app is maintained by Fulton Loebel
   #    """
   #)

   list_states = ["KS", "OK"]
   
   state_picked = st.radio("Select another state", list_states,
                           on_change=handle_state_change, key='state_picked')
   if state_picked:

      any_state = state_picked
      cstr = "You currently have state " + state_picked + " selected (click above to change states)"
      st.write(cstr)
      
      st.session_state['any_state'] = state_picked

      if any_state == "KS":
         list_counties = ["COMANCHE", "HARPER", "BARBER", "SHERMAN"]
      elif any_state == "OK":   
         list_counties = ["PITTSBURG", "HUGHES", "HASKELL", "COAL", "ELLIS", "LE FLORE", "MC INTOSH", "CANADIAN", "LINCOLN", "ROGER MILLS", "ATOKA"]
      
      #county_picked = st.selectbox("Select another county ", options = list_counties, index=0)
      county_picked = st.selectbox("Select another county ", options = list_counties, index=0,
                      on_change=handle_county_change, key='county_picked')

      if county_picked:

         any_county = county_picked
         cstr = "You currently have county " + county_picked + " selected (click above to change counties)"
         st.write(cstr)
         st.write("")

         st.session_state['any_county'] = county_picked

      
      #county_picked = st.selectbox("Selectbox: ", options=["Jane", "Bob", "Alice"], index=0)     
  
   #if len(st.session_state.any_state) >= 1:
   if st.session_state['any_state'] in list_states:

      #any_county = ""
      df = fig_group_by(any_state, any_county)

      st.dataframe(df)
  
      list_days = df["CUMUL_DAYS"].values.tolist()

      list_oil_rates = df['BOPD'].values.tolist()
      list_gas_rates = df['MCFD'].values.tolist()

      df_oil = pd.DataFrame()
      df_oil["CUMUL_DAYS"] = list_days
      df_oil["BOPD"] = list_oil_rates
      df_oil = df_oil.query('BOPD > 0.0')  # drop OIL points with no production
      list_oil_days = df_oil["CUMUL_DAYS"].values.tolist()
      list_oil_rates = df_oil['BOPD'].values.tolist()
 
      df_gas = pd.DataFrame()
      df_gas["CUMUL_DAYS"] = list_days
      df_gas["MCFD"] = list_gas_rates
      df_gas = df_gas.query('MCFD > 0.0')  # drop GAS points with no production
      list_gas_days = df_gas["CUMUL_DAYS"].values.tolist()
      list_gas_rates = df_gas['MCFD'].values.tolist()

          
      #OIL_OR_GAS = "OIL"
      #values = fit_hyperbolic_two_phase ( "OIL", list_oil_rates, list_days)  
      #values = fit_hyperbolic_two_phase ( "GAS", list_gas_rates, list_days)  

      if len(list_oil_days) == 0:
         cstr = "No OIL production data points found for query in state of " + any_state
         st.write(cstr)
      else:   
         scipy_curve_fit("OIL", list_oil_days, list_oil_rates)

      if len(list_gas_days) == 0:
         cstr = "No GAS production data points found for query in state of " + any_state
         st.write(cstr)
      else:   
         scipy_curve_fit("GAS", list_gas_days, list_gas_rates)




     
