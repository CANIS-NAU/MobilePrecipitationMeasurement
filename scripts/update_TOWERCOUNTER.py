import parser
import pandas as pd
from sys import argv


# if True, will print out information regarding the process and status of Filtering
debugBool = True


if len(argv) != 2:
    raise ValueError( "Invalid Number of Arguements!\n" +
                     "argv[0] - this program\n" +
                     "argv[1] - machine type\n" )

machineType = parser.getMachineType( argv[1] )

if machineType == "monsoon":
    arizonaMasterCSV = parser.monsoon_masterCSV + "/Arizona_data_master.csv"
    dallasMasterCSV = parser.monsoon_masterCSV = "/Dallas_data_master.csv"
    filtered_dataPath = parser.monsoon_filteredData

else:
    arizonaMasterCSV = parser.local_masterCSV + "/Arizona_data_master.csv"
    dallasMasterCSV = parser.local_masterCSV + "/Dallas_data_master.csv"
    filtered_dataPath = parser.local_filteredData

arizona_outputPath = filtered_dataPath + "/Arizona/tower_data.csv"
dallas_outputPath = filtered_dataPath + "/Dallas/tower_data.csv"
masterCSV_array = [ arizonaMasterCSV, dallasMasterCSV ]

for csvCounter, masterCSV in enumerate( masterCSV_array ):
    towers = dict()
    masterDataFrame = pd.read_csv( masterCSV )[ "0" ]

    for csv in masterDataFrame:
        if debugBool:
            print("\n{:,} of {:,}".format( csvCounter, len( masterDataFrame ) - 1 ))
            fileName, filePath = parser.split_path( csv )
            print("Parsing:", file_name)

        dataFrame = pd.read_csv( csv )
        for cellTowerID in dataFrame[ "cell" ]:
            try:
                towers[ cellTowerID ] += 1
            except KeyError:
                towers[ cellTowerID ] = 1


    refactoredTowers = []
    for CID in towers:
        refactoredTowers.append( [ CID, towers[ CID ] ] )

    towerCSV = pd.DataFrame( refactoredTowers )
    if "Arizona" in masterCSV:
        towerCSV.to_csv( index = False, path_or_buf = arizona_outputPath, header = [ "Tower ID", "Number of Records" ] )
    elif "Dallas" in masterCSV:
        towerCSV.to_csv( index = False, path_or_buf = dallas_outputPath, header = [ "Tower ID", "Number of Records" ] )
