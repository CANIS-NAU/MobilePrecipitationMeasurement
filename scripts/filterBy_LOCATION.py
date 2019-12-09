import parser
import pandas as pd
from sys import argv
from progressbar import progressbar
# if true, text regarding the size and process will be printed to the screen
debug = True


if len(argv) != 3:
    raise ValueError( "Invalid Number of Arguements!\n" +
                      "argv[0] - this program\n" +
                      "argv[1] - machine type\n" +
                      "argv[2] - location choice\n")

machineType = parser.getMachineType( argv[1] )

locationChoice =  parser.getLocation( argv[2] )


if __name__ == '__main__':
    if machineType == "monsoon":
        unfilteredMasterCSV = parser.monsoon_masterCSV + "/unfiltered_data_master.csv"
        intermediate_dataPath = parser.monsoon_intermediateData

    else:
        unfilteredMasterCSV = parser.local_masterCSV + "/unfiltered_data_master.csv"
        intermediate_dataPath = parser.local_intermediateData

    masterCSV = pd.read_csv( unfilteredMasterCSV )[ "0" ]
    for csv in progressbar( masterCSV, redirect_stdout = True ):
        dataFrame = pd.read_csv( csv )
        fileName, filePath = parser.split_path( csv )
        filtered_dataFrame = parser.filter_by_location( dataFrame, locationChoice )
        if debug:
            print("Parsing:", fileName)
            print("init. size: {:,}".format( len( dataFrame ) ))
            print("parsed size: {:,}\n".format( len( filtered_dataFrame ) ))

        if len( filtered_dataFrame ) != 0:
            output_filePath = "{}/{}_filtered_{}".format( intermediate_dataPath, argv[2], fileName )
            filtered_dataFrame.to_csv( index=False, path_or_buf = output_filePath )
