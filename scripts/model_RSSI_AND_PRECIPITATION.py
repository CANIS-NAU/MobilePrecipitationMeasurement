import parser
import numpy as np
import pandas as pd
from sys import argv
from sklearn import utils
from random import choice
from datetime import datetime
from sklearn import preprocessing
from sklearn.linear_model import LogisticRegression


if len(argv) != 2:
    raise ValueError( "Invalid Number of Arguements!\n" +
                      "argv[0] - this program\n" +
                      "argv[1] - machine type\n" )

machineType = parser.getMachineType( argv[1] )

if machineType == "monsoon":
    ssCSV = parser.monsoon_filteredData + "/signal_strength_app/signal_strength.csv"
    percipitationCSV = parser.monsoon_filteredData + "/Percipitation/NOAA/NOAA_data_Nov13_Nov22.csv"

else:
    ssCSV = parser.local_filteredData + "/signal_strength_app/signal_strength.csv"
    percipitationCSV = parser.local_filteredData + "/Percipitation/NOAA/NOAA_data_Nov13_Nov22.csv"


RSSI = []
percipitationData = []

"""
load signal strength (ss) data and precipitationitation data into dictionary form
"""
contentDict = dict()
ssDataFrame = pd.read_csv( ssCSV )
percipitationDataFrame = pd.read_csv( percipitationCSV )
for date, time, signal in zip( ssDataFrame[ 'date' ], ssDataFrame[ 'time' ], ssDataFrame[ 'signal strength (dBM)' ] ):
    timeStamp = date + " " + time
    contentDict[ timeStamp ] = [ signal ]
for x, percipitation in zip( percipitationDataFrame[ "Observation Time" ], percipitationDataFrame[ "PC" ] ):
    newDate = datetime.strptime( x.split(" ")[0], "%m/%d/%y" ).strftime( "%b %d %Y" )
    newDate += " " + x.split( " " )[1]
    try:
        contentDict[ newDate ].append( percipitation )
    except KeyError:
        continue

"""
sort data, and append signal and precipitationitation data to lists
"""
sorted( contentDict )
for date in contentDict:
    dateList = contentDict[ date ]
    if len( dateList ) == 2:
        # print( "{}: {}\t{}".format( date, dateList[0], dateList[1] ) )
        RSSI.append( [ dateList[0], dateList[0] ] )
        percipitationData.append( dateList[1] )

"""
classifiers
"""
predictionData = [choice(RSSI)]

percipitationEncoded = preprocessing.LabelEncoder().fit_transform( percipitationData )

algo = LogisticRegression( solver='lbfgs', multi_class='auto' )
algo.fit( RSSI, precipitationEncoded )
prediction = algo.predict( predictionData )

print("Given an RSSI of {}dBM the predicted precipitation is {}in".format(predictionData[0][0], prediction[0]))
