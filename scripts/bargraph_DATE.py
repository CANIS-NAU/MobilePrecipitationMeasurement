import parser
import numpy as np
import pandas as pd
from sys import argv
import matplotlib.pyplot as plt


if len(argv) != 3:
    raise ValueError( "Invalid Number of Arguements!\n" +
                      "argv[0] - this program\n" +
                      "argv[1] - machine type\n" +
                      "argv[2] - location choice\n")

machineType = parser.getMachineType( argv[1] )

locationChoice =  parser.getLocation( argv[2] )


if machineType == "monsoon":
    arizonaTowerData = parser.monsoon_filteredData + "/Arizona/diff_updates.csv"
    dallasTowerData = parser.monsoon_filteredData + "/Dallas/diff_updates.csv"
else:
    arizonaTowerData = parser.local_filteredData + "/Arizona/diff_updates.csv"
    dallasTowerData = parser.local_filteredData + "/Dallas/diff_updates.csv"

if locationChoice == "Arizona":
    dataFrame = pd.read_csv( arizonaTowerData )
else:
    dateFrame = pd.read_csv( dallasTowerData )


dateDict = dict()
fileRoot = ""
tempSum = 0
for fileName, recordCounter in zip( dateFrame[ 'file name' ], dateFrame[ 'number of records' ] ):
    root = fileName.split( "_" )[ 0 ]
    if fileRoot == root:
        tempSum += recordCounter
    else:
        if fileRoot != "":
            dateDict[ fileRoot ] = tempSum
        tempSum = recordCounter
        fileRoot = root

dateRange = sorted( dateDict )
ref_dateDict = dict()
for date in dateRange:
    ref_dataDict[ date ] = dateDict[ date ]

xAxis = list( ref_dataDict.keys() )
yAxis = list( ref_dataDict.values() )

plt.title( "{}: Number of Records per diff files".format( locationChoice.upper() ) )
plt.xlabel( "Date Range (mm/dd/yyyy)" )
plt.ylabel( "Number of Records" )

plt.bar( xAxis, yAxis, align = 'center', alpha = 0.5 )
plt.xticks( xAxis )
plt.xticks(rotation=90)
plt.tight_layout()
plt.show()
