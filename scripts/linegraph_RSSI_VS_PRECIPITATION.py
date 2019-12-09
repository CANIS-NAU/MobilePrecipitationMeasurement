import parser
import pandas as pd
from sys import argv
# from matplotlib import rc
from datetime import datetime
import matplotlib.pyplot as plt


if len(argv) != 2:
    raise ValueError( "Invalid Number of Arguements!\n" +
                      "argv[0] - this program\n" +
                      "argv[1] - machine type\n" )

machineType = parser.getMachineType( argv[1] )

if machineType == "monsoon":
    ssCSV = parser.monsoon_filteredData + "/signal_strength_app/signal_strength.csv"
    percipCSV = parser.monsoon_filteredData + "/Percipitation/NOAA/NOAA_data_Nov13_Nov25.csv"

else:
    ssCSV = parser.local_filteredData + "/signal_strength_app/signal_strength.csv"
    percipCSV = parser.local_filteredData + "/Percipitation/NOAA/NOAA_data_Nov13_Nov25.csv"


xValues = []
yValues = []
y2Values = []


"""
load signal strength (ss) data and percipitation data into dictionary form
"""
contentDict = dict()
ssDataFrame = pd.read_csv( ssCSV )
percipDataFrame = pd.read_csv( percipCSV )
for date, time, signal in zip( ssDataFrame[ 'date' ], ssDataFrame[ 'time' ], ssDataFrame[ 'signal strength (dBM)' ] ):
    timeStamp = date + " " + time
    contentDict[ timeStamp ] = [ signal ]
for x, percip in zip( percipDataFrame[ "Observation Time" ], percipDataFrame[ "PC" ] ):
    newDate = datetime.strptime( x.split(" ")[0], "%m/%d/%y" ).strftime( "%b %d %Y" )
    newDate += " " + x.split( " " )[1]
    try:
        contentDict[ newDate ].append( percip )
    except KeyError:
        continue

"""
sort data, and append signal and percipitation data to lists
"""
sorted( contentDict )
for date in contentDict:
    dateList = contentDict[ date ]
    if len( dateList ) == 2 and dateList[0] > -105:
        # print( "{}: {}\t{}".format( date, dateList[0], dateList[1] ) )
        xValues.append( date )
        # print( dateList[0], type(dateList[0]) )
        # print( dateList[1], type(dateList[1]) )
        yValues.append( dateList[0] )
        y2Values.append( dateList[1] )


"""
since the data is accumulative, find the difference between the current point,
and the next point to determine the true amount of percipitation
"""
y3Values = [ 0.0 ]
for index, currentElement in enumerate( y2Values ):
    try:
        nextElement = y2Values[ index + 1 ]
    except IndexError:
        break

    diff = nextElement - currentElement
    y3Values.append( diff )


"""
this is the domain of the graph

in order to see all data:
    START_POINT = 0
    END_POINT = -1
"""
START_POINT = 0
END_POINT = -1

"""
display graph
"""
fig = plt.figure()
ax = fig.add_subplot( 111 )
ax2 = ax.twinx()

ssLine = ax.plot( xValues[START_POINT:END_POINT], yValues[START_POINT:END_POINT], 'g-', label = 'signal strength')
prLine = ax2.plot( xValues[START_POINT:END_POINT], y3Values[START_POINT:END_POINT], 'b-', label = 'percipitation')
plt.xticks( [] )

lines = ssLine + prLine
labels = [ l.get_label() for l in lines ]
ax.legend( lines, labels, loc=0 )

ax.set_xlabel( "Showing data from: {} to {}".format( xValues[START_POINT], xValues[END_POINT] ) )
ax.set_ylabel( "signal strength (dBM)" )
ax2.set_ylabel( "percipitation (in)" )
plt.title( "Showing data from {} to {}".format( xValues[START_POINT], xValues[END_POINT] ) )
plt.show()
