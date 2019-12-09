import parser
import pandas as pd
from sys import argv
from os import walk, path
import matplotlib.pyplot as plt


if len( argv ) != 2:
    raise ValueError( "Invalid number of command line arguements\n" +
                       "argv[0] - this program\n" +
                       "argv[1] - machine type\n" )

machineType = parser.getMachineType( argv[ 1 ] )

if machineType == "monsoon":
    magmaHub = parser.monsoon_percipitation + "/Magma"
    mtUnionHub = parser.monsoon_percipitation + "/MountUnion"
    lakePleasantHub = parser.monsoon_percipitation + "/LakePleasant"

else:
    magmaHub = parser.local_percipitation + "/Magma"
    mtUnionHub = parser.local_percipitation + "/MountUnion"
    lakePleasantHub = parser.local_percipitation + "/LakePleasant"


def checkSeries( isValue, isSeries ):
    for seriesValue in isSeries:
        if isValue == seriesValue:
            return True
    return False



locations = { "magma" : magmaHub,
              "LakePleasant" : lakePleasantHub,
              "MountUnion" : mtUnionHub
             }

for location in locations:
    xValues = []
    y1Values = []
    y2Values = []
    locationHub = locations[ location ]
    avgPrecipitation = pd.read_csv( locationHub + "/{}_avg.csv".format( location ) )
    cellCount = pd.read_csv( locationHub + "/{}_cellCount.csv".format( location ) )
    cellDates = cellCount[ "date" ]

    for date, precip, count in zip( avgPrecipitation[ "date" ], avgPrecipitation[ "avg (in)" ], cellCount[ "data count" ] ):
        if not checkSeries( date, cellDates ):
            continue

        xValues.append( date )
        y1Values.append( precip )
        y2Values.append( count )

    fig, ax1 = plt.subplots()
    ax2 = ax1.twinx()

    plt.title( "{}: Precipitation vs. Number of Updates".format( location.capitalize() ) )

    ax1.set_xlabel( "01/01/2015 --> 01/01/2019" )
    ax1.set_ylabel( "Average Precipitation (inches)" )
    ax1.set_ylim( [ 0, max( y1Values ) + 2 ] )
    ax1.plot( xValues, y1Values, 'b', label = "Precipitation" )
    ax2.plot( xValues, y2Values, 'r', label = "Count" )
    ax2.set_ylim( [ 0, max( y2Values ) + 100 ] )
    ax2.set_ylabel( "Number of updates" )
    ax1.legend( loc = 2 )
    ax2.legend( loc = 1 )
    plt.autoscale()
    plt.ylim( bottom = 0 )
    plt.xticks( [], [] )
    plt.show()
