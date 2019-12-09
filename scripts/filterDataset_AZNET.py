import parser
import requests
import pandas as pd
from sys import argv
from os import walk, path



if len(argv) != 2:
    raise ValueError( "Invalid Number of Arguements!\n" +
                      "argv[0] - this program\n" +
                      "argv[1] - machine type\n" )

machineType = parser.getMachineType( argv[1] )


if machine_type == "monsoon":
    AZNET_dataPath = parser.monsoon_percipitation + "/AZNET"
else:
    AZNET_dataPath = parser.local_percipitation + "/AZNET"


for root, dirs, files in walk( AZNET_dataPath ):
    for file in files:
        if ".txt" not in file:
            continue

        print( "\nParsing:", file )
        csvFile = AZNET_dataPath + "/" + file.split(".txt")[ 0 ] + ".csv"
        toBeCSV = []
        with open( path.join( root, file ), "r" ) as f:
            fileContents = f.readlines()
            for line in fileContents:
                tempLine = line.split( "," )
                try:
                    year = tempLine[0]
                    day = tempLine[1]
                    hour = tempLine[2]
                    percip = tempLine[7]

                    toBeCSV.append( [ day, year, hour, percip ] )
                except IndexError:
                    continue

        print( "Exporting:", csvFile )
        tempDataFrame = pd.DataFrame( toBeCSV )
        tempDataFrame.to_csv( csvFile, index = False, header = [ "Day of Year", "Year", "Hour od Day", "Precipitation" ] )
