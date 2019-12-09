import parser
import pandas as pd
from sys import argv
import datetime as dt
import matplotlib.pyplot as plt


if len( argv ) != 2:
    raise parser.InvalidArguement( "Invalid number of command line arguements\n" +
                                   "argv[0] - this program\n" +
                                   "argv[1] - machine type\n")

machineType = parser.getMachineType( argv[ 1 ] )

if machineType == "monsoon":
    magma_hub = parser.monsoon_precipitation + "/Magma"
    mtUnion_hub = parser.monsoon_precipitation + "/MountUnion"
    lakePleasant_hub = parser.monsoon_precipitation + "/LakePleasant"

else:
    magma_hub = parser.local_precipitation + "/Magma"
    mtUnion_hub = parser.local_precipitation + "/MountUnion"
    lakePleasant_hub = parser.local_precipitation + "/LakePleasant"


locations = { "magma" : [ magma_hub ],
              "MountUnion" : [ mtUnion_hub ],
              "LakePleasant" : [ lakePleasant_hub ]
             }

# parse through all precip data and add it to a dictionary
# key = date; values = [ data1, data2, ... ]
for location in locations:
    print( "Location:", location )

    outputPath = locations[ location ][ 0 ] + "/{}_avg.csv".format( location )
    locationPercipData = dict()
    percipPath = locations[ location ][ 0 ] + "/{}.csv".format( location )
    percipDataFrame = pd.read_csv( percipPath )
    tempArr = []

    for date, data in zip( percipDataFrame[ 'date' ], percipDataFrame[ 'inches' ] ):
        try:
            locationPercipData[ date ].append( data )
        except KeyError:
            locationPercipData[ date ] = [ data ]

    for date in locationPercipData:
        dataArray = locationPercipData[ date ]
        average = round( sum( dataArray ) / len( dataArray ), 2 )
        tempArr.append( [ date, average ] )

    toBeConcat = pd.DataFrame( tempArr )
    toBeConcat.to_csv( index = False, header = [ "date", "avg (in)" ],
                       path_or_buf = outputPath )
