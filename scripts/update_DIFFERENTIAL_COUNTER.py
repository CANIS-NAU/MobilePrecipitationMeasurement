import parser
import pandas as pd
from sys import argv
from progressbar import progressbar

# if true, text regarding the size and process will be printed to the screen
debugBool = True


if len(argv) != 2:
    raise ValueError( "Invalid Number of Arguements!\n" +
                      "argv[0] - this program\n" +
                      "argv[1] - machine type\n")

machine_type = parser.get_machine_type( argv[1] )

if machine_type == "monsoon":
    masterDiff = parser.monsoon_masterCSV + "/differentials_data_master.csv"
    arizonaUpdateCounter = parser.monsoon_filteredData + "/Arizona/diff_updates.csv"
    dallasUpdateCounter = parser.monsoon_filteredData + "/Dallas/diff_updates.csv"
else:
    masterDiff = parser.local_master_csv + "/differentials_data_master.csv"
    arizonaUpdateCounter = parser.local_filteredData + "/Arizona/diff_updates.csv"
    dallasUpdateCounter = parser.local_filteredData + "/Dallas/diff_updates.csv"

arizona_diffFiles = []
dallas_diffFiles = []
masterPath = pd.read_csv( master_diff_path )


for index, csv in enumerate( masterPath[ "0" ] ):
    fileName, filePath = parser.split_path( csv )

    if debugBool:
        print("\n{} of {}".format( index, len( masterPath ) - 1 ))
        print("Parsing:", fileName)

    tempDataframe = pd.read_csv( csv )
    tempAZ_dataFrame = parser.filterByLocation( tempDataframe, "Arizona" )
    tempTX_dataFrame = parser.filterByLocation( tempDataframe, "Dallas" )

    if debugBool:
        print("Arizona Datapoints:", len( tempAZ_dataFrame ))
        print("Dallas Datapoints:", len( tempTX_dataFrame ))


    arizona_diffFiles.append( [ fileName, len( tempAZ_dataFrame ) ] )
    dallas_diffFiles.append( [ fileName, len( tempTX_dataFrame ) ] )

arizona_diffDataFrame = pd.DataFrame( arizona_diffFiles )
dallas_diffDataFrame = pd.DataFrame( dallas_diffFiles )

arizona_diffDataFrame.to_csv( index = False, header = [ "file name", "number of records" ], path_or_buf = arizona_update_counter )
dallas_diffDataFrame.to_csv( index = False, header = [ "file name", "number of records" ], path_or_buf = dallas_update_counter )
