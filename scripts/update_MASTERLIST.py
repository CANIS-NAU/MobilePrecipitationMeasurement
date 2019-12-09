import parser
import pandas as pd
from sys import argv
from os import system, walk, path


# check for valid parameters
if len(argv) != 2:
    raise ValueError("Invalid Number of Arguements!\n" +
                     "argv[0] - this program\n" +
                     "argv[1] - machine type.\n")

machineType = parser.get_machine_type( argv[1] )


"""
generates a csv of all csv paths
@param: String isMainDir - directory to be looked through
@param: String isOutputPath- file path of output csv
"""
def updateCSV( isMainDir, isOutputPath):
    tempCSV = []

    for root, dirs, files in walk( isMainDir ):
        for file in files:
            fullPath = path.join(root, file)

            noDot = file[0] != "."
            isCSV = "csv" in file
            notOriginal = "originals" not in fullPath
            inLocationFolder = "filtered_by_location" in fullPath

            # if the data is filtered then...
            if "filtered_data" in fullPath:
                if noDot and isCSV and notOriginal and inLocationFolder:
                    tempCSV.append(fullPath)

            # if the data is in unfiltered then...
            if "unfiltered_data" in fullPath:
                if no_dot and isCSV and notOriginal:
                    tempCSV.append( fullPath )

            if "precipitation" in fullPath:
                if no_dot:
                    tempCSV.append( fullPath )

    csvDataFrame  = pd.DataFrame( tempCSV )
    csvDataFrame.to_csv( index = False, path_or_buf = isOutputPath )



"""
unfiltered_data_master.csv
 - contains all paths of all unfiltered data
 - does not consider files within '/originals'

intermediate_data_master.csv
- contains all paths of all intermediate data csv's
"""
if machineType == 'monsoon':
    unfiltered_outputPath = parser.monsoon_masterCSV + "/unfiltered_data_master.csv"
    unfiltered_dataPath = parser.monsoon_unfilteredData

    intermediate_outputPath= parser.monsoon_masterCSV + "/intermediate_data_master.csv"
    intermediate_dataPath = parser.monsoon_intermediateData

    Arizona_outputPath= parser.monsoon_masterCSV + "/Arizona_data_master.csv"
    Arizona_dataPath = parser.monsoon_filteredData + "/Arizona"

    Dallas_outputPath= parser.monsoon_masterCSV + "/Dallas_data_master.csv"
    Dallas_dataPath = parser.monsoon_filteredData + "/Dallas"

    diff_dataPath = parser.monsoon_unfilteredData + "/differentials"
    diff_outputPath= parser.monsoon_masterCSV + "/differentials_data_master.csv"

    precip_dataPath = parser.monsoon_percipitation
    precip_outputPath= parser.monsoon_masterCSV + "/arizona_precipitation_master.csv"

else:
    unfiltered_outputPath = parser.local_masterCSV + "/unfiltered_data_master.csv"
    unfiltered_dataPath = parser.local_unfilteredData

    intermediate_outputPath= parser.local_masterCSV + "/intermediate_data_master.csv"
    intermediate_dataPath = parser.local_intermediateData

    Arizona_outputPath= parser.local_masterCSV + "/Arizona_data_master.csv"
    Arizona_dataPath = parser.local_filteredData + "/Arizona"

    Dallas_outputPath= parser.local_masterCSV + "/Dallas_data_master.csv"
    Dallas_dataPath = parser.local_filteredData + "/Dallas"

    diff_dataPath = parser.local_unfilteredData + "/differentials"
    diff_outputPath= parser.local_masterCSV + "/differentials_data_master.csv"

    precip_dataPath = parser.local_percipitation
    precip_outputPath= parser.local_masterCSV + "/arizona_precipitation_master.csv"


updateCSV( unfiltered_dataPath, unfiltered_outputPath )
updateCSV( intermediate_dataPath, intermediate_outputPath )
updateCSV( Arizona_dataPath, Arizona_outputPath )
updateCSV( Dallas_dataPath, Dallas_outputPath )
updateCSV( diff_dataPath, diff_outputPath )
updateCSV( precip_dataPath, precip_outputPath )
