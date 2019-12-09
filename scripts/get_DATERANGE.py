import parser
import pandas as pd
from sys import argv
from time import gmtime, strftime

if len(argv) != 2:
    raise ValueError("Invalid Number of Arguements.\n" +
                     "argv[0] - this program\n" +
                     "argv[1] - machine type\n")

machineType = parser.getMachineType( argv[1] )


if machineType == "monsoon":
    arizona_masterCSV = parser.monsoon_masterCSV + "/Arizona_data_master.csv"
    dallas_masterCSV = parser.monsoon_masterCSV + "/Dallas_data_master.csv"
    filteredData = parser.monsoon_filteredData

else:
    arizona_masterCSV = parser.local_masterCSV + "/Arizona_data_master.csv"
    dallas_masterCSV = parser.local_masterCSV + "/Dallas_data_master.csv"
    filteredData = parser.local_filteredData


"""
parses through a master csv and returns the date range

@param: String isLocationChoice - 'Dallas' or 'Arizona'
@return: List createdDateArray, List updatedDateArray - Lists containing the
    date ranges of a location
"""
def get_date_range( isLocationChoice ):
    validLocation = parser.getLocation( isLocationChoice )

    if validLocation == "Dallas":
        masterCSV = dallas_masterCSV
    else:
        masterCSV = arizona_masterCSV

    createdArray = []
    createdDateArray = []
    updatedArray = []
    updatedDateArray = []
    for csv in pd.read_csv( masterCSV )[ "0" ] :
        csv = pd.read_csv( csv )
        for created, updated in zip( csv[ "created" ], csv[ "updated" ] ):
            try:
                created_time = gmtime( created )
                updated_time = gmtime( updated )
            except ValueError:
                print( "ERR: '{}', '{}'\n".format( creationIndex, updatedIndex ) )
                continue

            createdStringTime = str( strftime('%Y-%m-%d %H:%M:%S', created ) )
            updatedStringTime = str( strftime('%Y-%m-%d %H:%M:%S', updated ) )

            createdDateArray.append( createdStringTime )
            updatedDateArray.append( updatedStringTime )

    createdDateArray.sort()
    updatedDateArray.sort()
    return createdDateArray, updatedDateArray


if __name__ == '__main__':
    for location in [ "Dallas", "Arizona" ]:
        createdDateArray, updatedDateArray = get_date_range( location )

        outputFile = "{}/{}/date_range.txt".format( filteredData, location )
        with open( outputFile, "w" ) as f:
            f.writelines( "Creation Date Range:\n" )
            f.writelines( "{}\t{}\n\n".format( createdDateArray[ 0 ], createdDateArray[ -1 ] ) )
            f.writelines( "Updated Date Range:\n" )
            f.writelines( "{}\t{}\n".format( updatedDateArray[ 0 ], updatedDateArray[ -1 ] ) )
