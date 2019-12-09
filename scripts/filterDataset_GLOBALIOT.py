import parser
import pandas as pd
from sys import argv
from time import time
from os import path, walk

if len( argv ) != 2:
    raise ValueError( "Invalid number of arguements!\n" +
                       "argv[0] - this program\n" +
                       "argv[1] - machine type\n")

machineType = parser.getMachineType( argv[ 1 ] )

if machineType == "monsoon":
    arizonaYearHub = parser.monsoon_filteredData + "/Arizona/Arizona_filtered_by_year"
    percipHub = parser.monsoon_percipitation
    magmaCSV = parser.monsoon_percipitation + "/Magma/magma.csv"
    lakePleasantCSV = parser.monsoon_percipitation + "/LakePleasant/lakePleasant.csv"
    mountUnion_csv = parser.monsoon_percipitation + "/MountUnion/mountUnion.csv"
else:
    arizonaYearHub = parser.local_filteredData + "/Arizona/Arizona_filtered_by_year"
    percipHub = parser.local_percipitation
    magmaCSV = parser.local_percipitation + "/Magma/magma.csv"
    lakePleasantCSV = parser.local_percipitation + "/LakePleasant/lakePleasant.csv"
    mountUnion_csv = parser.local_percipitation + "/MountUnion/mountUnion.csv"


dataFrameDictionary = { "Magma" : [ pd.read_csv( magmaCSV ), (33.1184, 111.4046) ],
                   "MountUnion" : [ pd.read_csv( mountUnion_csv ), ( 34.4150, 112.4043) ],
                   "LakePleasant" : [ pd.read_csv( lakePleasantCSV ), ( 33.9047, 112.2708 ) ]
                  }


"""
parse through dataFrame and find years
@param: isDataFrame - a pandas DataFrame
"""
def getYearCSV( isDataFrame ):
    yearPaths = []
    if not isinstance( isDataFrame, pd.core.frame.DataFrame ):
        raise TypeError( "A pandas dataFrame is required" )
    for dateData in isDataFrame[ "date" ]:
        year = dateData.split( "/" )[ -1 ]
        yearCSV = arizonaYearHub + "/{}.csv".format( year )
        if yearCSV not in yearPaths:
            yearPaths.append( yearCSV )
    yearPaths.sort()
    return yearPaths



if __name__ == '__main__':
    # look through each dataFrame
    for stringName in dataFrameDictionary:
        dataFrame = dataFrameDictionary[ stringName ][ 0 ]
        coordinates = dataFrameDictionary[ stringName ][ 1 ]
        print( "\nName:", stringName )
        print( "Lat:", coordinates[ 0 ], end = "\t" )
        print( "Lon:", coordinates[ 1 ] )

        # get OpenCell-ID information for the years,
        # that we have information for
        relYears = getYearCSV( dataFrame )
        for yearCSV in relYears:
            filename, filePath = parser.split_path( yearCSV )

            year_dataFrame = pd.read_csv( yearCSV )
            filtered_dataFrame = parser.custom_filter_by_location( year_dataFrame,
                                                                   coordinates[ 0 ],
                                                                   coordinates[ 1 ],
                                                                   -2 )

            outputString = percipHub + "/{0}/{0}{1}".format( stringName, filename )
            filtered_dataFrame = filtered_dataFrame.sort_values( 'created' )
            filtered_dataFrame.to_csv( index = False, path_or_buf = outputString )
