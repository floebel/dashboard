
import streamlit as st
import pandas as pd

import sqlite3
import sqlalchemy
#from sqlalchemy.ext.automap import automap_base
#from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func, inspect 
#Create engine 
from math import sqrt
import math

"""
           writec(17,"Updating User12 with Miles Away from Entered Lat/Long")
	        	cUpdate := "UPDATE Lease SET User12 = "
		   	 // assume 800 feet of lateral wasted for curve ...    // user13
	 //	       cDistance := " 5280.0 * 69.1* SQR (( BottomLatitudeIHS - SurfaceLatitudeIHS ) ^ 2  + 0.6 * ( BottomLongitudeIHS - SurfaceLongitudeIHS ) ^ 2 ) - 800.0 "     // feet ...
	 	//       cDistance := " ROUND ( 69.1* SQR (( BottomLatitudeIHS - SurfaceLatitudeIHS ) ^ 2  + 0.6 * ( BottomLongitudeIHS - SurfaceLongitudeIHS ) ^ 2 ), 5 ) "     // miles
	 	       cDistance := " ROUND( 69.1* SQR (( " + alltrim(STR(gLatitude)) + " - SurfaceLatitudeIHS ) ^ 2  + 0.6 * ( " + alltrim(STR(gLongitude)) + " - SurfaceLongitudeIHS ) ^ 2 ), 5 ) "     // miles
  //      cSelect := " ROUND( 69.1* SQR (( " + alltrim(STR(nLatitude)) + " - L.SurfaceLatitudeIHS ) ^ 2  + 0.6 * ( " + alltrim((str(nLongitude))) + " + L.SurfaceLongitudeIHS ) ^ 2 ),2) AS [MILES], "
	 	  		cUpdate += cDistance

	 //    	 cWhere := ""
	      	cWhere  := "WHERE SurfaceLatitudeIHS > 1" + space(80)
	     	 cUpdate := alltrim(cUpdate)
	     	 cWhere := alltrim(cWhere)
	        cSQL := cUpdate + " " + cWhere

					Alert(cSQL)
"""

"""
				 nLongitude := abs(nLongitude)
				IF nMaxMiles > 0
            cSelect := "SELECT ROUND( 69.1* SQR (( " + alltrim(STR(nLatitude)) + " - L.SurfaceLatitudeIHS ) ^ 2  + 0.6 * ( " + alltrim((str(nLongitude))) + " + L.SurfaceLongitudeIHS ) ^ 2 ),2) AS [MILES], "
       //    cSelect += " IIF ( " + alltrim(STR(nLatitude)) + " > L.SurfaceLatitudeIHS, 'NORTH',SOUTH' ) AS 'DIR NS', "      // not working
				ELSE
					 cSelect := "SELECT "
				ENDIF

"""


#	cSelect += "IIF(L.BottomLatitudeIHS > 1,'HORIZ','VERT') AS [WEL_DIR], "
"""
 IF ASCAN({"TEST"},cBoth) = 0
				IF lShowLogs = .F.
 	//			IF .t. = .t.   // ASCAN({"FDL","CEI","AMF"},Initials) > 0 .and. ASCAN({"WOR","TEST"},cBoth) = 0
	         IF "DI2PT" $ any_mdb_name
	         ELSEIF "DRI2PTX" $ any_mdb_name
					 ELSE
  	    cSelect += " (SELECT COUNT(*) FROM LeasePressure P WHERE P.LeaseID = L.LeaseID) AS [PRESS PTS], "
					 ENDIF
 	//	 	  	 cSelect += " (SELECT ROUND(MAX(P.BHP),0) FROM LeasePressure P WHERE P.LeaseID = L.LeaseID) AS 'MAX BHP', "      // added 3/29/2020
		      IF lShowLogs = .F.
  " (SELECT COUNT(*) FROM LeaseProduction P WHERE P.LeaseID = L.LeaseID AND (P.OIL > 0.0 OR P.GAS > 0.0) ) AS [PROD PTS], "
	          IF "DI2PT" $ any_mdb_name
						ELSE
 			   	     cSelect += " (SELECT COUNT(*) FROM LeaseProduction P WHERE P.LeaseID = L.LeaseID AND (P.OIL > 0.0 AND P.GAS > 0.0) ) AS [OILGAS PTS], "
 			   	     cSelect += " (SELECT COUNT(*) FROM LeaseProduction P WHERE P.LeaseID = L.LeaseID AND P.OIL > 0.0 ) AS [OIL PTS], "
 			   	     cSelect += " (SELECT COUNT(*) FROM LeaseProduction P WHERE P.LeaseID = L.LeaseID AND P.GAS > 0.0 ) AS [GAS PTS], "
						ENDIF
			  	ENDIF
 	 //		  	 cSelect += " (SELECT COUNT(*) FROM LeaseVolumetrics P WHERE P.LeaseID = L.LeaseID) AS [VOLUMETRIC PTS], "
 				ENDIF
		ENDIF

"""

"""
ÿ  	IF nSpecial = 1
				IF cBoth <> "WOR"
	//			 IF ASCAN({"WOR","TEST"},cBoth) = 0
		        	 cSelect += " (SELECT ROUND(MAX(P.Gas/30.42),0) FROM LeaseProduction P WHERE P.LeaseID = L.LeaseID) AS [MAX MCFD], "
			     		 cSelect += " (SELECT SUM(P.Gas) FROM LeaseProduction P WHERE P.LeaseID = L.LeaseID and P.Year > 1950)/1000. AS [CUMUL GAS], "
		   //		 cSelect += " (SELECT TOP 1 P.Year FROM LeaseProduction P WHERE P.LeaseID = L.LeaseID and (P.gas > 0 ) Order By P.Year DESC, P.Month Desc ) AS 'LAST GAS YEAR', "     // works
		  // 		 cSelect += " (SELECT TOP 1 round(P.gas/30.42,0) FROM LeaseProduction P WHERE P.LeaseID = L.LeaseID and P.gas > 0 Order By P.Year, P.Month ) AS [FIRST MCFD], "
		  // 		 cSelect += " (SELECT TOP 1 round(P.gas/30.42,0) FROM LeaseProduction P WHERE P.LeaseID = L.LeaseID and P.gas > 0 Order By P.Year DESC, P.Month Desc ) AS [LAST MCFD], "     // works

"""

"""
ÿ    	IF nSpecial = 1
					IF cBoth <> "WOR"

		  	  	 cSelect += " (SELECT ROUND(MAX(P.Oil/30.42),1) FROM LeaseProduction P WHERE P.LeaseID = L.LeaseID) AS [MAX BOPD], "
			       cSelect += " (SELECT SUM(P.Oil) FROM LeaseProduction P WHERE P.LeaseID = L.LeaseID and P.Year > 1950)/1000. AS [CUMUL OIL], "

		  	  	 cSelect += " (SELECT ROUND(MAX( ( P.Oil + (P.Gas/6.0) ) /30.42),1) FROM LeaseProduction P WHERE P.LeaseID = L.LeaseID) AS [MAX BOEPD], "
"""


# += " ROUND((SELECT IIF (SUM(P.Oil) = 0, 0, 1000.0 * SUM(P.Gas) / SUM(P.Oil) ) FROM LeaseProduction P WHERE P.LeaseID = L.LeaseID and P.Year > 1950),0) AS [PGOR SCF PER BBL], "       // works

"""
  IF nNOMP = 2
     	         	cWhere += "	AND L.County IN ('Woods','Alfalfa','Grant','Major','Garfield','Blaine','Kingfisher','Logan','Canadian') "
			      ELSEIF nNOMP = 3
     	         	cWhere += "	AND L.County IN ('Kay','Osage','Noble','Pawnee','Payne') "
			      ELSEIF nNOMP = 4
     	         	cWhere += "	AND L.County IN ('Woods','Alfalfa','Grant','Major','Garfield','Blaine','Kingfisher','Logan','Canadian','Kay','Osage','Noble','Pawnee','Payne') "
			      ENDIF
"""

"""

		 	 IF nProdPoints > 0
	//        cWhere += "AND DATEDIFF( 'd', L.FirstProdDate, L.LastProdDate -10 ) / 12.0 >= " + str(nProdPoints) + " "    // months producing    -10 to ave days on
	        cWhere += "AND DATEDIFF( 'd', L.FirstProdDate, L.LastProdDate -0 ) / 12.0 >= " + str(nProdPoints) + " "    // months producing    -10 to ave days on
			 ENDIF

	//	 	 IF nProdPoints > 0
  //        cAlertBox = "WHAT DEFINES A MONTH OF PRODUCTION"
  //        nProdChoice := AlertBox(cAlertBox, {"OIL OR GAS (DEFAULT) ","OIL AND GAS (NOMP WEST)","ONLY OIL (NOMP EAST)","ONLY GAS (GAS WELLS)" } )      // priority
	//				IF nProdChoice = 1
	//				    cWhere += " AND (SELECT COUNT(*) FROM LeaseProduction PROD WHERE PROD.LeaseID = L.LeaseID AND (PROD.OIL > 0.0 OR PROD.GAS > 0.0) ) >= " + str(nProdPoints) + " "
	//				ELSEIF nProdChoice = 2
	//				    cWhere += " AND (SELECT COUNT(*) FROM LeaseProduction PROD WHERE PROD.LeaseID = L.LeaseID AND (PROD.OIL > 0.0 AND PROD.GAS > 0.0) ) >= " + str(nProdPoints) + " "
	//				ELSEIF nProdChoice = 3
	//				    cWhere += " AND (SELECT COUNT(*) FROM LeaseProduction PROD WHERE PROD.LeaseID = L.LeaseID AND (PROD.OIL > 0.0 ) ) >= " + str(nProdPoints) + " "
	//				ELSEIF nProdChoice = 1
	//				    cWhere += " AND (SELECT COUNT(*) FROM LeaseProduction PROD WHERE PROD.LeaseID = L.LeaseID AND (PROD.GAS > 0.0) ) >= " + str(nProdPoints) + " "
	//				ENDIF
	//			ENDIF

"""

"""

				IF !empty(cProd1ZoneLike) .and. empty(cProd2ZoneLike) .and. empty(cProd3zonelike)
			     	cWhere += "	AND L.ProdZone LIKE '%" + cProd1ZoneLike + "%' "

				ELSEIF !empty(cProd1zonelike) .and. !empty(cProd2zonelike) .and. empty(cProd3zonelike)
			    	cWhere += "	AND ( L.ProdZone LIKE '%" + cProd1ZoneLike + "%' or L.ProdZone LIKE '%" + cProd2ZoneLike + "%') "

				ELSEIF !empty(cProd1zonelike) .and. !empty(cProd2zonelike) .and. !empty(cProd3zonelike)
			     	cWhere += "	AND ( L.ProdZone LIKE '%" + cProd1ZoneLike + "%' or L.ProdZone LIKE '%" + cProd2ZoneLike + "%' or L.ProdZone LIKE '%" + cProd3ZoneLike + "%' ) "
		  	 ENDIF
"""

"""
	 DO CASE
			    	  CASE nSort = 1
				     	  cOrderBy := " ORDER BY 1"
			    	  CASE nSort = 2
	               cOrderBy := " ORDER BY IIF(L.BottomLatitudeIHS > 1,'HORIZ','VERT'), 1 "
	   //    	cSelect += "IIF(L.BottomLatitudeIHS > 1,'HORIZ','VERT') AS [HOLE DIR], "
			    	  CASE nSort = 3
              	 cOrderBy := " ORDER BY L.ProdZone, L.LeaseName"
			    	  CASE nSort = 4

"""


"""
//			nYearStart := 1950                                                                                                                   // 2005 ..............
	    cSelect := " SELECT "

 //	    	cSelect += " P.Year, P.Month, "
// 	    	cSelect += " P.Year, P.Month, "
 	//    	cSelect += " CSTR(P.Year) AS 'YEAR', CSTR(P.Month) AS 'MONTH', "
 	    	cSelect += " CSTR(P.Year) AS 'YEAR', "
 //     	cSelect += " DateSerial(P.Year, P.Month, 15) AS 'PRODDATE', "

 	    	cSelect += " Sum(P.Oil) AS 'OIL', "
 	    	cSelect += " Sum(P.Water) AS 'WATER', "
 	    	cSelect += " Sum(P.GAS) AS 'GAS', "
 	    	cSelect += " Count(L.LeaseID) AS 'WELLCOUNT' "

 //	    	cSelect += "ROUND(MIN(Gas)/30.42,1) AS 'MIN GAS MCFD', "
 //	    	cSelect += "ROUND(AVG(Gas)/30.42,1) AS 'AVG GAS MCFD', "
 //	    	cSelect += "ROUND(MAX(Gas)/30.42,1) AS 'MAX GAS MCFD', "
 //	    	cSelect += "ROUND(SUM(Gas)/1000,1) AS 'SUM GAS MMCF', "
 //	    	cSelect += "ROUND(MIN(Oil)/30.42,1) AS 'MIN OIL BOPD', "
 //	    	cSelect += "ROUND(AVG(Oil)/30.42,1) AS 'AVG OIL BOPD', "
 //	    	cSelect += "ROUND(MAX(Oil)/30.42,1) AS 'MAX OIL BOPD', "
 //	    	cSelect += "ROUND(SUM(Oil),1) AS 'SUM OIL BBL' "
 //
"""


"""

 //		 	 cSelect += " (SELECT SUM(P.Oil) FROM LeaseProduction P WHERE P.LeaseID = L.LeaseID and P.Year = 2007) AS 'CUMUL OIL', "


	//	 	 cSelect += " (SELECT SUM(P.Oil) FROM LeaseProduction P WHERE P.LeaseID = L.LeaseID and P.Year = 2007) AS 'CUMUL OIL', "
	//	 	 cSelect += " (SELECT SUM(P.Oil) FROM LeaseProduction P WHERE P.LeaseID = L.LeaseID and DateSerial(P.Year, P.Month,15) < DateSerial(P.Year, P.Month, 15) ) AS 'CUMUL OIL', "
	// 	 	 cSelect += " (SELECT (L.StartingOil + SUM(X.Oil)) FROM LeaseProduction X WHERE P.LeaseID = X.LeaseID and DateSerial(X.Year, X.Month,15) <= DateSerial(P.Year, P.Month, 15) ) AS 'CUMUL OIL', "
	//	 	 cSelect += " (SELECT SUM(P.Oil) FROM LeaseProduction P WHERE M.LeaseID = L.LeaseID and (DateSerial(M.Year, M.Month,15) < DateSerial(P.Year, P.Month, 15) ) AS 'CUMUL OIL', "
 //		 	 cSelect += " (SELECT SUM(P.Oil) FROM LeaseProduction P INNER JOIN LeaseProduction M ON P.LeaseID = M.LeaseID ) AS 'CUMUL OIL', "

"""



"""

#  	cSelect += "ROUND(DATEDIFF( 'd', L.FirstProdDate, L.LastProdDate -10 ) / 365.0,2) AS 'YEARS ON', "      // works    -10 to ave days on

#   	cWhere := "	WHERE L.ProdZone LIKE '%PHOSPHORIA%' "


 //	 	 cSelect += " (SELECT SUM(P.Oil) FROM LeaseProduction  WHERE P.LeaseID = L.LeaseID and P.Year = YEAR(L.FirstProdDate) ) AS 'ANNUAL OIL' "

 //	 	 cSelect += " (SELECT SUM(P.Oil) FROM LeaseProduction P WHERE P.LeaseID = L.LeaseID and P.Year = YEAR(L.FirstProdDate) ) AS 'ANNUAL OIL' "
	//	 	 cSelect += " (SELECT SUM(P.Oil) FROM LeaseProduction P WHERE P.LeaseID = L.LeaseID and DateSerial(P.Year, P.Month,15) < DateSerial(P.Year, P.Month, 15) ) AS 'CUMUL OIL', "
	// 	 	 cSelect += " (SELECT (L.StartingOil + SUM(X.Oil)) FROM LeaseProduction X WHERE P.LeaseID = X.LeaseID and DateSerial(X.Year, X.Month,15) <= DateSerial(P.Year, P.Month, 15) ) AS 'CUMUL OIL', "
	//	 	 cSelect += " (SELECT SUM(P.Oil) FROM LeaseProduction P WHERE M.LeaseID = L.LeaseID and (DateSerial(M.Year, M.Month,15) < DateSerial(P.Year, P.Month, 15) ) AS 'CUMUL OIL', "
 //		 	 cSelect += " (SELECT SUM(P.Oil) FROM LeaseProduction P INNER JOIN LeaseProduction M ON P.LeaseID = M.LeaseID ) AS 'CUMUL OIL', "






"""

#	  	 cSelect += " (SELECT (ROUND(L.StartingOil + SUM(P.Oil)/1000,0)) FROM LeaseProduction P WHERE P.LeaseID = L.LeaseID ) AS 'CUMUL OIL MBBL', "
#	  	 cSelect += " (SELECT (ROUND(L.StartingGas + SUM(P.Gas)/1000,0)) FROM LeaseProduction P WHERE P.LeaseID = L.LeaseID ) AS 'CUMUL GAS MMCF', "

# 	   cOrderBy := " GROUP BY YEAR(L.FirstProdDate), UCASE(L.LeaseType), IIF(L.BottomLatitudeIHS <= 1,'VERTI','HORIZ'), UCASE(L.LeaseStatus) "   // works


# cSQL += 'where m.o_pl_dte between curdate()-62 and curdate() '

"""
  cSelect += " L.FirstProdDate, L.LastProdDate, "
       	cSelect += "ROUND(DATEDIFF( 'd', L.FirstProdDate, L.LastProdDate -10 ) / 365.0,2) AS 'YEARS ON', "      // works    -10 to ave days on
	//    cSelect += " L.StartingOil, "
  // 		 cSelect += " (SELECT TOP 1 round(P.oil/30.42,1) FROM LeaseProduction P WHERE P.LeaseID = L.LeaseID and P.oil > 0 Order By P.Year DESC, P.Month Desc ) AS 'LAST BOPD', "     // works
  // 		 cSelect += " (SELECT TOP 1 round(P.Water/30.42,1) FROM LeaseProduction P WHERE P.LeaseID = L.LeaseID and P.Water > 0 Order By P.Year DESC, P.Month Desc ) AS 'LAST BWPD', "     // works
  // 		 cSelect += " (SELECT TOP 1 round(P.Injection/30.42,1) FROM LeaseProduction P WHERE P.LeaseID = L.LeaseID and P.Injection > 0 Order By P.Year DESC, P.Month Desc ) AS 'LAST BIPD', "     // works
  // 		 cSelect += " (SELECT TOP 1 round(P.gas/30.42,0) FROM LeaseProduction P WHERE P.LeaseID = L.LeaseID and P.gas > 0 Order By P.Year DESC, P.Month Desc ) AS 'LAST MCFD', "     // works
 	 // 	 cSelect += " (SELECT (ROUND(L.StartingOil + SUM(P.Oil)/1000,0)) FROM LeaseProduction P WHERE P.LeaseID = L.LeaseID ) AS 'CUMUL OIL MBBL', "
 	  	 cSelect += " (SELECT (ROUND(SUM(P.Oil)/1000,0)) FROM LeaseProduction P WHERE P.LeaseID = L.LeaseID ) AS 'CUMUL OIL MBBL SINCE 1970', "
 	//  	 cSelect += " (SELECT (ROUND(L.StartingGas + SUM(P.Gas)/1000,0)) FROM LeaseProduction P WHERE P.LeaseID = L.LeaseID ) AS 'CUMUL GAS MMCF', "
 	  	 cSelect += " (SELECT (ROUND(SUM(P.Gas)/1000,0)) FROM LeaseProduction P WHERE P.LeaseID = L.LeaseID ) AS 'CUMUL GAS MMCF SINCE 1970', "
 	  	 cSelect += " (SELECT (ROUND(SUM(P.Water)/1000,0)) FROM LeaseProduction P WHERE P.LeaseID = L.LeaseID ) AS 'CUMUL WATER MBBL SINCE 1970', "
 	  	 cSelect += " (SELECT (ROUND(SUM(P.Injection)/1000,0)) FROM LeaseProduction P WHERE P.LeaseID = L.LeaseID ) AS 'CUMUL INJECTION MBBL SINCE 1970', "

  //   	cSelect += "ROUND(DATEDIFF( 'd',  L.FirstProdDate, DateSerial(P.Year, P.Month, 28)  ) / 365.25,3) AS 'YEARS SINCE FIRST PRODUCTION DATE', "   // 2005 ..............

	//	 	 cSelect += " (SELECT SUM(P.Oil) FROM LeaseProduction P WHERE P.LeaseID = L.LeaseID and P.Year = 2007) AS 'CUMUL OIL', "
	//	 	 cSelect += " (SELECT SUM(P.Oil) FROM LeaseProduction P WHERE P.LeaseID = L.LeaseID and DateSerial(P.Year, P.Month,15) < DateSerial(P.Year, P.Month, 15) ) AS 'CUMUL OIL', "
	// 	 	 cSelect += " (SELECT (L.StartingOil + SUM(X.Oil)) FROM LeaseProduction X WHERE P.LeaseID = X.LeaseID and DateSerial(X.Year, X.Month,15) <= DateSerial(P.Year, P.Month, 15) ) AS 'CUMUL OIL', "
	//	 	 cSelect += " (SELECT SUM(P.Oil) FROM LeaseProduction P WHERE M.LeaseID = L.LeaseID and (DateSerial(M.Year, M.Month,15) < DateSerial(P.Year, P.Month, 15) ) AS 'CUMUL OIL', "
 //		 	 cSelect += " (SELECT SUM(P.Oil) FROM LeaseProduction P INNER JOIN LeaseProduction M ON P.LeaseID = M.LeaseID ) AS 'CUMUL OIL', "
 //       cFrom := " FROM Lease AS L INNER JOIN LeaseCalculated AS C ON L.LeaseID = C.LeaseID "

 //	      //  	cSelect += "DATEDIFF( 'd', L.FirstProdDate, L.LastProdDate -10 ) AS 'DAYS ON', "      // works    -10 to ave days on
//	    cSelect += " IIF(L.BottomLatitudeIHS <= 1,ROUND(P.Oil/30.42,3),null) AS 'VERTI BOPD VS YEARS SINCE FIRST PRODUCTION DATE', "
//	    cSelect += " IIF(L.BottomLatitudeIHS > 1,ROUND(P.Oil/30.42,3),null)  AS 'HORIZ BOPD VS YEARS SINCE FIRST PRODUCTION DATE' "
  	  cSelect += " L.LeaseID "

	    cFrom   := " FROM Lease AS L "

"""


"""
ÿ  cSelect += " P.Year, P.Month, L.StartingOil, P.Oil, "
//	  cSelect += " P.Gas, P.Water, LeaseStatus, "
      cSelect += " ROUND( 69.1* SQR (( " + alltrim(STR(nLatitude)) + " - L.SurfaceLatitudeIHS ) ^ 2  + 0.6 * ( " + alltrim((str(nLongitude))) + " + L.SurfaceLongitudeIHS ) ^ 2 ),2) AS 'MILES', "
//	    cSelect += " DateSerial(P.Year, P.Month, 15) AS 'PRODDATE', "
  //   	cSelect += "ROUND(DATEDIFF( 'd',  DateSerial(2005, 01, 01),  DateSerial(P.Year, P.Month, 28)  ) / 365.25,3) AS 'CALENDAR YEARS', "   // 2005 ..............
  //   	cSelect += "ROUND(2000.01 + DATEDIFF( 'd',  DateSerial(2000, 01, 01),  DateSerial(P.Year, P.Month, 28)  ) / 365.25,3) AS 'CALENDAR YEARS', "   // 2005 ..............
	    cSelect += " DatePart('yyyy',L.FirstProdDate) AS 'FIRST SALES YR', "     // vbsedit
	    cSelect += " DatePart('q',L.FirstProdDate) AS 'FIRST SALES QTR', "       // vbsedit
	    cSelect += " L.FirstProdDate, L.LastProdDate, "
  //   	cSelect += "ROUND(DATEDIFF( 'd',  L.FirstProdDate, DateSerial(P.Year, P.Month, 28)  ) / 365.25,3) AS 'YEARS SINCE FIRST PRODUCTION DATE', "   // 2005 ..............
"""

# cSelect += " DatePart('yyyy',L.FirstProdDate) AS 'FIRST SALES YR', "



"""
SELECT journal, count(journal_id) as count_journal
FROM article
INNER JOIN journal ON article.journal_id = journal.rowid
GROUP BY journal_id
ORDER BY count_journal DESC
LIMIT 10;
"""

#import sqlalchemy
#from sqlalchemy.ext.automap import automap_base
#from sqlalchemy.orm import Session
#from sqlalchemy import create_engine, func, inspect 
#Create engine 
"""
  cSQL = "SELECT DISTINCT series_id, gpl FROM gsm WHERE gpl LIKE 'GPL1%' AND series_id IS NOT NULL ORDER BY gpl" #  LIMIT 500"
 
      df = database_to_df(oENGINE, cSQL)
      
      print('\a')  # BEEP   

      nRows = len(df)
      print(nRows, "rows to process")
      print(cSQL)
      print(df.head(100))
      input("wait")
"""

"""
  db_sqlite = 'c:/sqlite_pubqc/pubmed.sqlite'
      database = 'sqlite:///' + db_sqlite   
      #conn = sqlite3.connect(db_sqlite)
      
      #df_five_columns = df_pvs[["PMID", "PMCID", "PV_Counts", "P-Value", "Title"]]   # PMCID

      #df_five_columns = df_five_columns.dropna(subset=['Title', 'PMID'])

      oENGINE, oSQLITE = open_pubmed_sqlite_conn(database, db_sqlite)

      #insert_into_article(oSQLITE, "123456", "3", "PMC123")   # add more fields ...
      #insert_into_article(oSQLITE, "134567", "3", "PMC456")   # add more fields ...

      #insert_into_article(oSQLITE, "234567", "2", "PMC1234")   # add more fields ...
      #insert_into_article(oSQLITE, "225657", "2", "PMC4567")   # add more fields ...  

      if 1 == 2:
         list_tables = get_database_tables(oENGINE)
         database_to_df(oENGINE, "SELECT * FROM articles")
         get_sqlite_table_info(oENGINE, oSQLITE)
"""

if 1 == 2:   
   cur.execute("CREATE INDEX IF NOT EXISTS lookups_pmid ON lookups(pmid)")
   oSQLITE.commit()

if 1 == 2:   # TEMPORARY
   cur.execute("DROP TABLE IF EXISTS citations")
   oSQLITE.commit()
   print("dropping citations table if exists")




# df['Outcome_String'] = df.apply(lambda row: fig_nkt_Outcome_String(row), axis=1)  
def fig_lat_length(row):

   any_SurfLat = row["SurfLat"]
   any_SurfLong = row["SurfLong"]
   any_BotLat = row["BotLat"]
   any_BotLong = row["BotLong"]

   if any_BotLat == 0.0 or any_BotLong == 0.0:
      any_lateral_length = 0.0
   else:
      any_lateral_length = abs(5280.0 * 69.1* math.sqrt (( any_BotLat - any_SurfLat ) ** 2.0 + 0.6 * ( any_BotLong - any_SurfLong ) ** 2.0 )) - 700.0   # AS 'SL-BHL-800FT', " feet ...

   any_lateral_length = abs(any_lateral_length)
   return int(any_lateral_length)



"""
//     browses[18] = "fig_lat_length_from_tvd_and_md( WELLS->TVD_TD, WELLS->MEAS_TD)"
* ----------------------------------------------------------------------------------------------------------------------------
FUNCTION fig_lat_length_from_tvd_and_md ( any_tvd_td, any_meas_td )        // huffman

	LOCAL any_lateral_length := 0.0

	IF empty(any_tvd_td) .or. empty(any_meas_td)
		 any_lateral_length := 0.0
	ELSE
	   any_lateral_length := any_meas_td - any_tvd_td - 700.0   // huffman   ??????
	ENDIF

RETURN val(str(any_lateral_length,10,1))
*-----------------------------------------------------------------------------------------------------------------------------
"""




def drop_y(df):
   # list comprehension of the cols that end with '_y'
   to_drop = [x for x in df if x.endswith('_y')]
   df.drop(to_drop, axis=1, inplace=True)
   return df



def fig_exe_path():

   any_backslash = "\\"
   exe_path = os.getcwd() + any_backslash
   #display(exe_path, "exe_path", True)
   #drive = substr(exe_path,1,1)   # FIX
   #print("drive = ", drive)
   #input("wait")
   #full_html_path = exe_path + "/templates/" + html_file_name    
   return exe_path

def fig_drive():  # also in fdl_sub_display.py
   any_backslash = "\\"
   file_path = os.getcwd() + any_backslash
   drive = substr(file_path,1,1)
   drive_upper = drive.upper()
   #print("drive = " + drive)
   return drive_upper


def list_to_string(any_list): # need to add space delimiter !!!!!!
   result = ""
   length = len(any_list)
   if length >= 1:
      for i in range(length):
         #result = result + any_list[i] + " "
         result = result + any_list[i]  # REVISED 5-22-2022
    
   return result      


def list_to_string_with_delimiter(any_list, any_delimiter): 
   result = any_delimiter
   length = len(any_list)
   if length >= 1:
      for i in range(length):
         result = result + any_list[i] + any_delimiter
   return result      
  

def Format(number,decimals):   # approximate VB Format function
 
   if decimals == 0: 
      string = '{0:.0f}'.format(number)
   elif decimals == 1: 
      string = '{0:.1f}'.format(number)
   elif decimals == 2: 
      string = '{0:.2f}'.format(number)
   elif decimals == 3: 
      string = '{0:.3f}'.format(number)
   elif decimals == 4: 
      string = '{0:.4f}'.format(number)
   elif decimals == 5: 
      string = '{0:.5f}'.format(number)
   elif decimals == 6: 
      string = '{0:.6f}'.format(number)
   elif decimals == 7: 
      string = '{0:.7f}'.format(number)
   elif decimals == 8: 
      string = '{0:.8f}'.format(number)
   elif decimals == 9: 
      string = '{0:.9f}'.format(number)
   elif decimals == 10: 
      string = '{0:.10f}'.format(number)
   elif decimals == 11: 
      string = '{0:.11f}'.format(number)
   elif decimals == 12: 
      string = '{0:.12f}'.format(number)
   elif decimals == 13: 
      string = '{0:.13f}'.format(number)
   elif decimals == 14: 
      string = '{0:.14f}'.format(number)
   elif decimals == 15: 
      string = '{0:.15f}'.format(number)
   elif decimals == 16: 
      string = '{0:.16f}'.format(number)        
   else:
      string = "" 
      print("ERROR: in Format() function INVALID decimals = ", decimals)
      #input("wait")
       
   return string



if 1 == 2:
   number = 3.123456
   decimals = 4
   string = Format(number, decimals)
   print(string)
   input("wait")



def copy_file(any_source, any_dest):  # 2022

   #import shutil
   # Copy file example.txt into a new file called example_copy.txt
   #shutil.copy('example.txt', 'example_copy.txt')
   # Copy file example.txt into directory test/
   #shutil.copy('example.txt', 'test/')
   shutil.copyfileobj(any_source, any_dest)
   return ""



 

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

def is_file(any_path, any_file):
   
   any_file = any_path + any_file
   ## if file exists, delete it ##
   if os.path.isfile(any_file):
      #print("file exists " + any_file)
      return True    
   else:    ## Show an error ##
      #print("file not found " + any_file)
      return False

   
  

   
def pd_rename(df, field_name, new_field_name):
   
   if 1 == 2:
      print("in pd_rename", field_name, new_field_name)
   list_old = [field_name]
   list_new = [new_field_name]
   df.rename(columns=dict(zip(list_old, list_new)), inplace=True)
   return df




def pd_drop(df, field_name, dummy):
   
   df = df.drop(field_name, axis = 1)   # drop  
   return df

  
     
def upper(any_string):
   any_upper = any_string.upper()
   return any_upper

def alltrim(any_string):
   
   any_alltrim = any_string.strip()
   #Alert("'" + any_alltrim + "'")
   return any_alltrim



def left(s, amount):
    return s[:amount]

def right(s, amount):
    return s[-amount:]

def mid(s, offset, amount):
    #return s[offset:offset+amount]
    return s[offset-1:offset+amount-1]
   


def padr(string, pad):
   return string.ljust(pad,' ')



def padl(string, pad):
   return string.rjust(pad,' ')






def substr(any_string, start, length):   # ONE BASED ...
   
   any_substr = any_string[start-1:start+length-1]
   #input(any_substr)
   return any_substr




def print_type(s, obj):  # FDL
   if is_debug():    
      print(s, type(obj))




def alltrim(any_string):
   
   any_alltrim = any_string.strip()
   #Alert("'" + any_alltrim + "'")
   return any_alltrim


def Replace(any_before, any_find, any_replace):  # VB6  # also in fdl_sub_utilities.py
   
   any_after = any_before.replace(any_find, any_replace, 999)
   return any_after



def open_sqlite_conn(database, db_sqlite):

   #print("in open_geometadb_sqlite_conn")
   #print("database = ", database)
   #print("db_sqlite = ", db_sqlite)
  
   #db_sqlite = 'test.sqlite'

   #if 1 == 1:  # is_file("", db_sqlite):
   #   #print(db_sqlite, "exists")
   #   CREATE_NEW_YN = "N"
 
   #else:
   #   #print(db_sqlite, "does not exist")
   #   #input("wait")
   #   return
    
   oSQLITE = sqlite3.connect(db_sqlite)
   #print("oSQLITE object is connected to", db_sqlite)

   oENGINE = create_engine(database)
   #print("oENGINE object is connected to", database)

        
   # Inspecting data
   insp = inspect(oENGINE)
   list_tables = insp.get_table_names()   # WORKS
   #print("list_tables")
   #print(list_tables)
   
   #if "temp" in list_tables:
   #   cstr  = "\ntemp table exists, drop it "
   #   cstr += "\n<Y> Yes, Drop it "
   #   cstr += "\n<N> No, Keep it  "  
   #   DROP_TEMP_YN = input(cstr)
   #   if DROP_TEMP_YN == "Y":
   #      sql_within_database(oSQLITE, "DROP TABLE IF EXISTS temp")
     
   return oENGINE, oSQLITE




def get_sqlite_database_info(oENGINE, oSQLITE):
   """
   Returns an array of tables given a DB.
   """
   #if db_sqlite is None:
   #  log("perform_basic: No DB passed in")
   #  return
   #print("in get_sqlite_database_info(oENGINE, oSQLITE)")
   #print("sql = ", sql)
   #print("db_sqlite = ", db_sqlite)
   #print("drop_table = ", drop_table)    
   #engine = create_engine(database)   
   #cstr  = "\nThis could take time.  Are you sure"
   #cstr += "\n<Y> Yes See summary statistics of database tables"
   #cstr += "\n<N> No "  
   MENU_YN = "Y" # input(cstr)

   list_tables = []
   list_rows = []
   list_cols = []
   
   if MENU_YN == "Y":  


      #oSQLITE = sqlite3.connect(db_sqlite)
      c = oSQLITE.cursor()
      arr = c.execute("select name from sqlite_master where type='table'")
      for row in arr:
         #tbl = row[0].encode('utf8')
         one_table = row[0]
         sql = "SELECT * FROM " + one_table + " LIMIT 20"
         df = database_to_df(oENGINE, sql)

         #st.dataframe(df)
         
         list_column_names = df.columns.values.tolist()
         #print()
         #print("list_column_names for", one_table)
         #print(list_column_names)
         #print()
         #nRows = len(df)
         #nCols = len(list_column_names)

         #print("nCols = ", nCols, " for", one_table)
    
         list_tables.append(one_table)
         list_rows.append(nRows)
         list_cols.append(nCols)

      df_statistics = pd.DataFrame()
      df_statistics["Table"] = list_tables
      df_statistics["Rows"] = list_rows
      df_statistics["Cols"] = list_cols
  
      #print()
      #print("df_statistics.head(20) for all tables")
      #print(df_statistics.head(20))
      #print()
      st.dataframe(df_statistics)
  
      #conn.close()
      #print("list_tables")
      #print(list_tables)
      #input("wait")

   return list_tables


def database_to_df(oENGINE, sql):  # WORKS

   #print("in database_to_df(oENGINE, sql)")
   #print("sql = ", sql)
   #print("db_sqlite = ", db_sqlite)
   #print("drop_table = ", drop_table)    
   #engine = create_engine(database)
   
   cnx = oENGINE.connect()
   df = pd.read_sql(sql, cnx)
   nrows = len(df)
   #print("rows in df = ", nrows)
   #print()
   #print("df.head(10)")
   #print(df.head(10))   
   #print("df.dtypes")
   #print(df.dtypes)  
   #print()
   #input("wait")
   return df

if 1 == 2:
   cstr  = "\nDatabase To DataFrame test.sqlite"
   cstr += "\n<Y> Yes "
   cstr += "\n<N> No "  
   MENU_YN = input(cstr)
   
   if MENU_YN == "Y":   

      #database = 'sqlite:///millbrae_2019.sqlite'
      db_sqlite = 'test.sqlite'
      database = 'sqlite:///' + db_sqlite   
      #sql = """SELECT * FROM Lease"""
      #sql = """SELECT * FROM Lease LIMIT 20"""
      #sql = """SELECT LeaseID, LeaseName FROM Lease LIMIT 20"""
      sql = '''
            SELECT
            a.product_name AS [PRODUCT NAME],
            b.price AS [PRICE]
            FROM products a
            LEFT JOIN prices b ON a.product_id = b.product_id
            '''
   
      database_to_df(database, sql)
   
      input("wait")
   
 




def sql_within_database(oSQLITE, sql):

   #print("in sql_within_database(oSQLITE, sql)")
   #print("sql = ", sql)
    
   cur = oSQLITE.cursor()
    
   #insert_sql = "INSERT OR IGNORE INTO articles VALUES (?,?,?)"
   #insert_sql = "INSERT OR REPLACE INTO articles VALUES (?,?,?)"

   cur.execute(sql)
   oSQLITE.commit()
   return ""



def get_database_tables(oENGINE):  # WORKS
 
   #print("in get_database_tables(oENGINE)")
   #print("database = ", database)
   #print("db_sqlite = ", db_sqlite)
   #print("drop_table = ", drop_table)
   
   #engine = create_engine(database)
   # Inspecting data
   oINSPECT = inspect(oENGINE)
   list_tables = oINSPECT.get_table_names()   # WORKS

   #st.write(list_tables)
   #print("list_tables")
   #print(list_tables)
   #print()
   #columns = insp.get_columns('Lease')

   #print("type(columns)")
   #print(type(columns))
   #input("wait")
   return list_tables


if 1 == 2:
   cstr  = "\nGet Database Tables from millbrae_2019.sqlite"
   cstr += "\n<Y> Yes "
   cstr += "\n<N> No "  
   MENU_YN = input(cstr)
   if MENU_YN == "Y":   
      database = 'sqlite:///millbrae_2019.sqlite'
      list_tables = get_database_tables(database)  
      input("wait")
   
 

def query(db_name, sql, data):
    with sqlite3.connect(db_name) as db:
        cursor = db.cursor()
        cursor.execute("PRAGMA Foreign_Keys = ON")
        cursor.execute(sql, data)
        result = cursor.fetchall()
        db.commit()
        return result



def drop_sqlite_table_if_exists(database, db_sqlite, drop_table): 

   #print("in drop_sqlite_table_if_exists()")
   #print("database = ", database)
   #print("db_sqlite = ", db_sqlite)
   #print("drop_table = ", drop_table)
 
   conn = sqlite3.connect(db_sqlite) 
   c = conn.cursor()
   drop_sql = "DROP TABLE IF EXISTS " + drop_table
   #drop_sql = "DROP TABLE " + drop_table
  
   c.execute(drop_sql)          
                     
   conn.commit()

   list_tables = get_database_tables(database)   
   if drop_table in list_tables:
      fdl = 1
      #print()
      #print("FAILURE: ", drop_table, "still in", database)
      #input("WARNING")
   else:
      fdl = 1
      #print()
      #print("SUCCESS: ", drop_table, "not in ", database)
   
   return ""


# 'sqlite': """INSERT INTO iris VALUES(?, ?, ?, ?, ?)""",
def insert_or_ignore_into_sqlite_database(oENGINE, oSQLITE, sql):  # WORKS
   oSQLITE = sqlite3.connect(db_sqlite) 
   c = oSQLITE.cursor()
   #conn.commit()
   c.execute(sql)
   oSQLITE.commit()     
   #df = get_database_tables(database)
   return ""

if 1 == 2:
   cstr  = "\nInsert or Ignore into SQLite Database products and prices in test.sqlite"
   cstr += "\n<Y> Yes "
   cstr += "\n<N> No "  
   MENU_YN = input(cstr)
   if MENU_YN == "Y": 
   
      db_sqlite = 'test.sqlite'
      database = 'sqlite:///' + db_sqlite
      sql = '''
            INSERT OR IGNORE INTO products (product_id, product_name)

                VALUES
                (1,'Computer'),
                (2,'Printer'),
                (3,'Tablet'),
                (4,'Desk'),
                (5,'Chair')
             '''   
      insert_or_ignore_into_sqlite_database(database, db_sqlite, sql)
      sql = '''INSERT OR IGNORE INTO prices (product_id, price)

                VALUES
                (1,800),
                (2,200),
                (3,300),
                (4,450),
                (5,150)
          '''
      insert_or_ignore_into_sqlite_database(database, db_sqlite, sql)

      sql = """SELECT * FROM products"""
      database_to_df(database, sql)

      sql = """SELECT * FROM prices"""
      database_to_df(database, sql)   

      input("wait")





# 'sqlite': """INSERT INTO iris VALUES(?, ?, ?, ?, ?)""",
def insert_or_replace_into_sqlite_database(oENGINE, oSQLITE, db_sqlite, sql):  # WORKS
   #conn = sqlite3.connect(db_sqlite) 
   c = oSQLITE.cursor()
   #conn.commit()
   c.execute(sql)
   oSQLITE.commit()     
   #df = get_database_tables(database)
   return ""

if 1 == 2:
   cstr  = "\nInsert or Replace into SQLite Database products and prices in test.sqlite"
   cstr += "\n<Y> Yes "
   cstr += "\n<N> No "  
   MENU_YN = input(cstr)
   if MENU_YN == "Y": 
   
      db_sqlite = 'test.sqlite'
      database = 'sqlite:///' + db_sqlite
      sql = '''
            INSERT OR REPLACE INTO products (product_id, product_name)

            VALUES
            (1,'Computer aa'),
            (2,'Printer bb'),
            (3,'Tablet c'),
            (4,'Desk d'),
            (5,'Chair e'),
            (6,'Phone f')
            '''   
      insert_or_replace_into_sqlite_database(database, db_sqlite, sql)
      sql = '''INSERT OR REPLACE INTO prices (product_id, price)

                VALUES
                (1,800),
                (2,200),
                (3,300),
                (4,450),
                (5,150),
                (6,450)
          '''
      insert_or_replace_into_sqlite_database(database, db_sqlite, sql)

      sql = """SELECT * FROM products"""
      database_to_df(database, sql)

      sql = """SELECT * FROM prices"""
      database_to_df(database, sql)   

      input("wait")



   


if 1 == 2:   
   cstr  = "\nDatabase to DataFrame for test.sqlite "
   cstr += "\n<Y> Yes "
   cstr += "\n<N> No "  
   MENU_YN = input(cstr)
   if MENU_YN == "Y": 

      if 1 == 2:
         db_sqlite = 'millbrae_2019.sqlite'
         database = 'sqlite:///' + 'millbrae_2019.sqlite'
         sql = """SELECT * FROM Lease"""
         database_to_df(database, sql)
      else:
         db_sqlite = 'test.sqlite'
         database = 'sqlite:///' + db_sqlite   
         sql = """SELECT * FROM prices"""
         database_to_df(database, sql)
   
      input("wait")



# engine = create_engine("sqlite:///:memory:")

def create_empty_sqlite_table(database, db_sqlite, new_table): 

   #print()
   #print("in create_empty_sqlite_table()")
   #print("new_table = ", new_table)
   #print()
   
   import sqlalchemy
   #from sqlalchemy.ext.automap import automap_base
   #from sqlalchemy.orm import Session
   from sqlalchemy import create_engine, func, inspect 
   #Create engine 
   engine = create_engine(database)
   cnx = engine.connect()
   list_tables = get_database_tables(database)   
   if new_table in list_tables:
      #print(new_table, "in", database, "before to_sql()")
      drop_sqlite_table_if_exists(database, db_sqlite, new_table)
   else:
      fdl = 1
      #print(new_table, "not in", database, "before to_sql()")

   #cstr = "calling df.to_sql(" + new_table + ") to create an empty table"   
   #print(cstr)      

   df = pd.DataFrame()
   df["temp1"] = 1
   df["temp2"] = 2
   df["temp3"] = 3
   df["temp4"] = 4
   df["temp5"] = 5
   
   df.to_sql(new_table, cnx, if_exists='replace', index = False)  # if_exists='append'

   list_tables = get_database_tables(database)   
   if new_table in list_tables:
      fdl = 1
      #print("SUCCESS: ", new_table, "in", database, "after create_empty_sqlite_table()")   
   else:
      fdl = 1
      #print("FAILURE: ", new_table, "not in", database, "after create_empty_sqlite_table()")
   #print()   
   #df = pd.read_sql(sql, cnx)
   #print(df.head(10))
   #print(df.dtypes)
   #input("wait")
   return ""

#engine = create_engine('sqlite:///DisasterResponse.db')
#df.to_sql('DisasterResponse', engine, index=False,if_exists='replace')
#df.to_sql('products', conn, if_exists='replace', index = False)
def df_to_database_table(oENGINE, oSQLITE, df, new_table): 

   #print("in df_to_database()")
   cnx = oENGINE.connect()
   list_tables = get_database_tables(oENGINE)   
   if new_table in list_tables:
      #print(new_table, "in", database, "before to_sql()")
      drop_sqlite_table_if_exists(database, db_sqlite, new_table)
   else:
      #print(new_table, "not in", database, "before to_sql()")
      fdl = 1
      
   #cstr = "calling df.to_sql(" + new_table + ")"   
   #print(cstr)      

   df.to_sql(new_table, cnx, if_exists='replace', index = False)  # if_exists='append'
   list_tables = get_database_tables(oENGINE)   
   if new_table in list_tables:
      fdl = 1 
      #print(new_table, "in", database, "after to_sql()")   
   else:
      fdl = 1
      #print(new_table, "not in", database, "after to_sql()")     

   #df = pd.read_sql(sql, cnx)
   #print(df.head(10))
   #print(df.dtypes)
   #input("wait")
   return ""


if 1 == 2:
   cstr  = "\nDataFrame To Database Table using to_sql()  (join_table in test.sqlite) "
   cstr += "\n<Y> Yes "
   cstr += "\n<N> No "  
   MENU_YN = input(cstr)
   if MENU_YN == "Y":    # Pandas requires version '1.4.0' or newer of 'sqlalchemy' (version '1.3.8' currently installed).
      #database = 'sqlite:///millbrae_2019.sqlite'
      db_sqlite = 'test.sqlite'
      database = 'sqlite:///' + db_sqlite   
      #sql = """SELECT * FROM Lease"""
      #sql = """SELECT * FROM Lease LIMIT 20"""
      #sql = """SELECT LeaseID, LeaseName FROM Lease LIMIT 20"""
      sql = '''
            SELECT
            a.product_name AS [PRODUCT NAME],
            b.price AS [PRICE]
            FROM products a
            LEFT JOIN prices b ON a.product_id = b.product_id
            '''
  
      df = database_to_df(database, sql)
      df_to_database_table(database, db_sqlite, df, "join_table") 
      df = database_to_df(database, "SELECT * FROM join_table")
   
      input("wait")
   


#INSERT INTO Table3 (A,B,C,D,E) 
#SELECT t1.A, t1.B, t1.C, t2.D, t2.E FROM Table1 t1
#INNER JOIN Table2 t2 ON t2.A = t1.A

def sql_to_new_database_table(oENGINE, oSQLITE, sql, new_table): 

   #print()
   #print("in sql_to_new_database_table()")
   #print("sql = ", sql)   
   #print("new_table = ", new_table)   
   #print()
         
   #engine = create_engine(database)
   cnx = oENGINE.connect()
   list_tables = get_database_tables(oENGINE)

   drop_sqlite_table_if_exists(oENGINE, oSQLITE, new_table) 
   #create_empty_sqlite_table(database, db_sqlite, new_table) 

   #if new_table in list_tables:
   #   print(new_table, "in", database, "before sqlite sql")
   #   drop_sqlite_table_if_exists(database, db_sqlite, new_table) 
   #else:
   #   print( new_table, "not in", database, "before sqlite sql so we will create an empty one")   
   #   create_empty_sqlite_table(database, db_sqlite, new_table) 

   #new_table_sql = 'CREATE TABLE IF NOT EXISTS ' + new_table
   #create_sqlite_table(database, db_sqlite, new_table_sql)
      
   list_tables = get_database_tables(oENGINE)
   #print("list_tables")
   #print(list_tables)
   #print()
   #temp_sql = "SELECT * FROM " + new_table
   #df = database_to_df(database, temp_sql)
   #print("df.head(30) of empty table", new_table) 
   #print(df.head(30)) 
   #print()
   #conn = sqlite3.connect(db_sqlite) 
   c = oSQLITE.cursor()
   #conn.commit()
   c.execute(sql)  # sqlite3.OperationalError: no such table: join_table
   oSQLITE.commit()       

   #df.to_sql(new_table, cnx, if_exists='replace', index = False)
   list_tables = get_database_tables(oENGINE)   
   if new_table in list_tables:
      fdl = 1
      #print(new_table, "in", database, "after sqlite sql")   
   else:
      fdl = 1
      #print(new_table, "not in", database, "after sqlite sql")     

   #df = pd.read_sql(sql, cnx)
   #print(df.head(10))
   #print(df.dtypes)
   #input("wait")
   return ""


if 1 == 2:
   cstr  = "\nSQL to create new table in database using SQLite "
   cstr += "\n<Y> Yes "
   cstr += "\n<N> No "  
   MENU_YN = input(cstr)
   if MENU_YN == "Y": 

      #database = 'sqlite:///millbrae_2019.sqlite'
      db_sqlite = 'test.sqlite'
      database = 'sqlite:///' + db_sqlite
      new_table = "join_table"
      #sql = """SELECT * FROM Lease"""
      #sql = """SELECT * FROM Lease LIMIT 20"""
      #sql = """SELECT LeaseID, LeaseName FROM Lease LIMIT 20"""
      if 1 == 2:  # WORKS
         sql = '''CREATE TABLE join_table AS SELECT * FROM products'''
      elif 1 == 2:  # WORKS
         sql = '''CREATE TABLE join_table AS SELECT product_name FROM products'''
      elif 1 == 1: # WORKS
         sql = '''CREATE TABLE join_table AS SELECT a.product_name, b.price FROM products a LEFT JOIN prices b ON a.product_id = b.product_id'''


      elif 1 == 2:
         sql = '''
               CREATE TABLE join_table
               SELECT
               product_name
               FROM products 
               '''
      elif 1 == 1: # WORKS but added a space after SELECT
         sql = '''
               CREATE TABLE join_table SELECT 
               a.product_name,
               b.price
               FROM products a
               LEFT JOIN prices b ON a.product_id = b.product_id
               '''      
      else:
      
         sql = '''
               CREATE TABLE join_table
               SELECT
               a.product_name AS [PRODUCT NAME],
               b.price AS [PRICE]
               FROM products a
               LEFT JOIN prices b ON a.product_id = b.product_id
               '''
  
      #df = database_to_df(database, sql)
      #df_to_database(database, df, "join_table") 
      sql_to_new_database_table(database, db_sqlite, sql, new_table) 

      df = database_to_df(database, 'SELECT * FROM join_table')
      print(df.head(30))
      input("wait")
   



# input("STOP")



# It's remarkably hard to find such a thing,
# but I've built a handy Python utility to do it
# using SQLAlchemy and pandas_access, which relies on mdbtools.

#Everything you need can be acquired with:

#pip3 install sqlalchemy pandas_access
#sudo apt install mdbtools
#The code is as follows:

if 1 == 2:
  
   import pandas_access as mdb
   from sqlalchemy import create_engine
   import sys
   import os

   db_out = "test_test.sqlite"   # arg 0
   mdb_in = "h:/SQLITE_MBRAE/millbrae_2019.mdb" # argv 1

   #if len(sys.argv)!=3:
   #  print("{0} <MDB File> <Sqlite3 File>".format(sys.argv[0]))
   #  sys.exit(-1)

   #if os.path.isfile(sys.argv[2]):
   #  print("Refusing to modify existing database!")
   #  sys.exit(-1)

   engine = create_engine('sqlite:///{0}'.format( db_out ), echo=False)
   tlist  = [tbl for tbl in mdb.list_tables( mdb_in )]
   tables = {tbl:mdb.read_table( mdb_in, tbl) for tbl in tlist}

   for k in tables:
      tables[k].to_sql(k, con=engine)

   input("stop created test_test.sqlite")




if 1 == 2:

   import pandas_access as mdb

   db_filename = 'h:/SQLITE_MBRAE/millbrae_2019.mdb'

   # Listing the tables.
   for tbl in mdb.list_tables(db_filename):
      print(tbl)
   input("wait")  

   # Read a small table.
   df = mdb.read_table(db_filename, "Lease")

   print(df.dtypes)

   input("wait")

   input("STOP")
      





if 1 == 2:  # WORKS

   import sqlite3

   #con = sqlite3.connect(database = r'file_name.db')
   con = sqlite3.connect(database = r'aquarium.db')     # WORKS
 
   cur = con.cursor()
   cur.execute('SELECT name from sqlite_master where type="table"')
   tabl =cur.fetchall()
   print(tabl)
   input("wait")


#For using ‘pyodbc’ you must have the microsoft office/access installed in your system,
# therefore it will work on Windows only. If the office version is latest, i.e. above Office 2011 or 13,
# then make sure that the .mdb file is not of the old versions, older than 2003.

#In case of older files (97 versions) of .mdb (microsoft access files), please convert the file to the
# new version using microsoft access 2003 or 2007. The version 2003 is not quite available these days,
# hence it would become quite a problem.


if 1 == 2:
   import sqlite3

   con = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};    DBQ=millbrae_2019.mdb')
    
   cur = con.cursor()
   for row in cur.tables():
      print(row.table_name)
   input("wait")










# -*- coding: utf-8 -*-
# module : mdb_to_sqlite.py
# author : Panos Mavrogiorgos (gmail - pmav99)
# license : BSD
 
# pylint: disable= C0301
 
"""
A simple script to convert an Access database to sqlite3 database using pyodbc.
 
It just copies the tables and their data not the relationships (primary keys,
foreign keys, etc).:
 
It hasn't been thoroughly tested. Probably won't work for all the data types.
But it should serve as a basis for more complex scripts.
"""
 

if 1 == 2:
  
   import sqlite3
   import pyodbc
 
   # The path to the database files. The sqlite database
   SQL_FILE = "path\to\sqlite\database.db"
   MDB_FILE = "path\to\access\database.mdb"
 
   # pyodbc's connection string is different for python x86 and x64. Use the
   # appropriate one. More info here: http://code.google.com/p/pyodbc/issues/detail?id=203
   # The string for x86
   MDB_STRING = "DRIVER={Microsoft Access Driver (*.mdb)};DBQ=" + MDB_FILE
   # The string for x64
   #MDB_STRING = "DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=" + MDB_FILE
 
 
def convert(mdb_string, sql_file):
    """
    Converts an Access database to a SQLite database.
    """
    # Make sqlite connections
    sqlite_connection = sqlite3.connect(sql_file)
    sqlite_cursor = sqlite_connection.cursor()
 
    # Make mdb connections
    mdb_connection = pyodbc.connect(mdb_string, autocommit=False)
    mdb_cursor = mdb_connection.cursor()
    tables = [row.table_name for row in mdb_cursor.tables()]
 
    for tables in tables:
        # Access databases, have several internal tables. They all start with the
        # "MSys" prefix. If you need them, just remove the if clause.
        if not table.startswith("MSys"):
            ## Create tables
            columns = [column for column in mdb_cursor.columns(table=table)]
            s = []
            for columns in columns:
                # Quoting table names with braces.
                s.append("%s %s(%s)" % ("[" + column.column_name + "]",
                                        column.type_name,
                                        column.column_size))
            creation_string = ("CREATE TABLE [%s] (\n" % table +
                               ",\n".join(s) +
                               "\n);")
            print(creation_string, "\n")
            sqlite_cursor.execute(creation_string)
 
            ## Insert values
            # select everything from the mdb-table
            rows = [row for row in mdb_cursor.execute("SELECT * FROM [%s];" % table)]
            # Check if the table has data. If it doesn't go to the next table, else
            # insert them to the sqlite database.
            try:
                length = len(rows[0])
            except IndexError:
                pass
            
            #otherwise:
            insertion_string = "insert into [%s] values ​​" % table
            insertion_string += "(" + ", ".join(["?" for i in range(length)]) + ")"
            print(insertion_string, "\n")
            sqlite_connection.executemany(insertion_string, rows)
 
    # close databases
    sqlite_connection.commit()
    sqlite_cursor.close()
    mdb_cursor.close()
 
if 1 == 2:   
   db_out = "test.db"   # arg 0
   mdb_in = "c:/data/millbrae_2019.mdb" # argv 1
   convert(mdb_in, db_out)

   input("STOP")







  



