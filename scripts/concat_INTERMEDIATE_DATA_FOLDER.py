import parser
import pandas as pd
from sys import argv

# if true, text regarding the size and process will be printed to the screen
debugBool = True


if len(argv) != 3:
    raise ValueError("Invalid Number of Arguements!\n" +
                     "argv[0] - this program\n" +
                     "argv[1] - machine type\n" +
                     "argv[2] - concat file name\n")

machineType = parser.getMachineType( argv[1] )


if __name__ == '__main__':
    Arizona = []
    Dallas = []

    if machineType == "monsoon":
        intermediate_dataPath = parser.monsoon_masterCSV + "/intermediate_data_master.csv"
        arizonaPath = parser.monsoon_filteredData + "/Arizona"
        dallasPath = parser.monsoon_filteredData + "/Dallas"

    else:
        intermediate_dataPath = parser.local_masterCSV + "/intermediate_data_master.csv"
        arizonaPath = parser.local_filteredData + "/Arizona"
        dallasPath = parser.local_filteredData + "/Dallas"

    masterCSV = pd.read_csv( intermediate_data_path )[ "0" ]
    index = 0
    for csv in masterCSV:
        dataFrame = pd.read_csv( csv )
        fileName, filePath = parser.split_path( csv )
        if "Arizona" in fileName:
            Arizona.append( dataFrame )
        elif "Dallas" in fileName:
            Dallas.append( dataFrame )
        else:
            raise ValueError( "Invalid File Name! '{}'\n".format( file_name ) )

        if debugBool:
            print("{} of {}".format( index, len( masterCSV ) - 1))
            print("Parsing:", fileName)
            print("File Size: {:,} lines\n".format( len( dataFrame ) ))

        index += 1

    if len( Arizona ) > 0:
        Arizona_concat = pd.concat( Arizona )
        output_file_path = "{}/{}.csv".format( arizonaPath, argv[2] )
        Arizona_concat.to_csv( index = False, path_or_buf = output_file_path )

    if len( Dallas ) > 0:
        Dallas_concat = pd.concat( Dallas )
        output_file_path = "{}/{}.csv".format( dallasPath, argv[2] )
        Dallas_concat.to_csv( index = False, path_or_buf = output_file_path )
