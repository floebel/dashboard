

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
import plotly.express as px  # pip install plotly-express


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





def fig_group_by(any_state):  
   
   # GROUP BY
   #cSelect  = "SELECT P.Year, P.Month, P.Oil, P.Gas, "
   cSelect  = "SELECT P.CUMUL_MONTHS, "
   cSelect += " Sum(P.Oil) AS 'OIL_SUM', "
   #cSelect += " Sum(P.Water) AS 'WATER_SUM', " 
   cSelect += " Sum(P.Gas) AS 'GAS_SUM', " 
   
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
   cWhere  = " WHERE L.LAT_LENGTH >= 1000 AND L.MAX_MONTHS >= 72 "
   cWhere += " AND P.CUMUL_MONTHS >= 0 "
   cWhere += " AND (P.Oil > 0 OR P.Gas > 0) "
 
   #nProdPoints = 24
   #cWhere += " AND (SELECT count(*) FROM LeaseProduction PROD WHERE PROD.LeaseID = L.LeaseID) >= " + str(nProdPoints) + " "
   #cWhere += " AND (SELECT count(*) FROM LeaseProduction PROD WHERE PROD.LeaseID = L.LeaseID) >= 24 AND (P.Oil > 0 OR P.Gas > 0) "
      
   #cWhere += " AND L.COUNTY = 'OKLAHOMA' "
   #cWhere += " AND L.COUNTY = 'GRADY' "
   cWhere += "	AND L.County IN ('OKLAHOMA', 'GRADY', 'CLEVELAND','WOODS','ALFALFA','GRANT','MAJOR','GARFIELD','BLAINE','KINGFISHER','LOGAN','CANADIAN') "

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
   series_rate = df['Ave Monthly Gas Per Well']    
   # q = df['Ave Monthly Oil Per Well']

   if 1 == 2:   
      
      plt.figure(figsize=(10,7))
      plt.step(series_time, series_rate, color='blue')
      plt.title('Production Rate vs Time Plot', size=20, pad=15)
      plt.xlabel('Months')
      plt.ylabel('Volume Per Month')
      plt.xlim(min(series_time), max(series_time))
      plt.ylim(ymin=0)
      plt.grid()
      plt.show()


   qi, di, b, RMSE = arps_fit("TIME", series_time, series_rate, plot=False)
   cstr = "qi = " + str(qi)
   st.write(cstr)
   cstr = "di = " + str(di)
   st.write(cstr)
   cstr = "b = " + str(b)
   st.write(cstr)
   cstr = "RMSE = " + str(RMSE)
   st.write(cstr)
   

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


     

   
