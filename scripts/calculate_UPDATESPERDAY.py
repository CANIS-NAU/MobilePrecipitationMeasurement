import parser
import pandas as pd
from sys import argv
from os import walk, path
import matplotlib.pyplot as plt
from time import gmtime, strftime
from progressbar import progressbar


if len( argv ) != 2:
    raise parser.InvalidArguement( "Invalid number of command line arguements\n" +
                                   "argv[0] - this program\n" +
                                   "argv[1] - machine type\n")

machineType = parser.getMachineType( argv[ 1 ] )

if machineType == "monsoon":
    magma_hub = parser.monsoon_precipitation + "/Magma"
    mtUnion_hub = parser.monsoon_precipitation + "/MountUnion"
    lakePleasant_hub = parser.monsoon_precipitation + "/LakePleasant"

else:
    magma_hub = parser.local_precipitation + "/Magma"
    mtUnion_hub = parser.local_precipitation + "/MountUnion"
    lakePleasant_hub = parser.local_precipitation + "/LakePleasant"


dateDict = dict()
locations = { "magma" : [ magma_hub ],
              "MountUnion" : [ mtUnion_hub ],
              "LakePleasant" : [ lakePleasant_hub ]
             }
for location in locations:
    hub = locations[ location ][ 0 ]
    percip_dataFrame = pd.read_csv( hub + "/{}.csv".format( location ) )
    outputPath = hub + "/{0}_cellCount.csv".format( location )

    # keep track of each day that there exists percipiation data
    for date in percip_dataFrame[ 'date' ]:
        dateDict[ date ] = 0

    # parse through all relevant cell data per location
    yearFiles = []
    for root, dirs, files in walk( hub ):
        for file in files:
            if "20" in file:
                full_path = path.join( root, file )
                dataFrame = pd.read_csv( full_path )[ 'created' ]
                print( "File:", file )
                for unixTime in progressbar( dataFrame ):
                    date = gmtime( unixTime )
                    stringTime = strftime( "%m/%d/%Y", date )
                    try:
                        dateDict[ stringTime ] += 1
                    except KeyError:
                        pass

    tempArr = []
    for date in dateDict:
        value = dateDict[ date ]
        tempArr.append( [ date, value ] )
    toBeConcat = pd.DataFrame( tempArr )
    toBeConcat.to_csv( index = False, header = [ "date", "data count" ],
                       path_or_buf = outputPath )
