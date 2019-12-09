import parser
import pandas as pd
from sys import argv
from os import path, walk
from datetime import datetime
import matplotlib.pyplot as plt


if len(argv) != 2:
    raise ValueError( "Invalid Number of Arguements!\n" +
                      "argv[0] - this program\n" +
                      "argv[1] - machine type\n" )

machineType = parser.getMachineType( argv[1] )

if machineType == "monsoon":
    filteredPath = parser.monsoon_filtered_data + "/signal_strength_app"
else:
    filteredPath = parser.local_filtered_data + "/signal_strength_app"


xValues = []
yValues = []

for root, dirs, files in walk( filteredPath ):
    for file in files:
        if ".csv" in file:
            tempDataFrame = pd.read_csv( path.join( root, file ) )
            for date, time, signal in zip( tempDataFrame[ 'date' ], tempDataFrame[ 'time' ], tempDataFrame[ 'signal strength' ] ):
                xValues.append( date + time )
                yValues.append( signal.split( "dBM" )[ 0 ] )


plt.title( "Signal Strength between Nov. 13 to Nov. 20" )
plt.xlabel( "Time (15 min increments)" )
plt.ylabel( "Signal Strength (dBM)" )
plt.xticks( [] )

plt.plot( xValues, yValues )
plt.tight_layout()
plt.show()
