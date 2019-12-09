import parser
import pandas as pd
from sys import argv

if len( argv ) != 2:
    raise ValueError( "Invalid number of arguements!\n" +
                       "argv[0] - this program\n" +
                       "argv[1] - machine type\n" )

machine_type = parser.get_machine_type( argv[ 1 ] )

if machine_type == "monsoon":
    arizonaPercipitation = parser.monsoon_masterCSV + "/arizona_precipitation_master.csv"
    main_pathPercipitation = parser.monsoon_percipitation
else:
    arizonaPercipitation = parser.local_masterCSV + "/arizona_precipitation_master.csv"
    main_pathPercipitation = parser.local_percipitation

# change HTML data into list within a dictionary
# keys are years
percipitationDataFrame = pd.read_csv( arizonaPercipitation )[ "0" ]
mtUnion, magma, lakePleasant = dict(), dict(), dict()
for filePath in percipitationDataFrame:
    fileName, filePath = parser.split_path( filePath )
    with open( filePath, "r" ) as p:
        tempHTML = p.readlines()

    tempData = parser.getData( tempHTML )
    for dataLine in tempData:
        dataString = ""
        date, time, inches = parser.parseLine( dataLine )
        year = int( date.split( "/" )[ 2 ] )
        dataString += "{}, {}, {}".format( date, time, inches )

        if "lake" in fileName:
            try:
                lakePleasant[ year ].append( dataString )
            except KeyError:
                lakePleasant[ year ] = [ dataString ]
        elif "magma" in fileName:
            try:
                magma[ year ].append( dataString )
            except KeyError:
                magma[ year ] = [ dataString ]
        elif "mount" in fileName:
            try:
                mtUnion[ year ].append( dataString )
            except KeyError:
                mtUnion[ year ] = [ dataString ]

# push lakePleasant data to CSV
tempArr = []
for year in sorted( lakePleasant.keys() ):
    lakePleasant[ year ].sort()
    for data in lakePleasant[ year ]:
        data = data.split( ", " )
        tempArr.append( data )
toBeConcat = pd.DataFrame( tempArr )
toBeConcat.to_csv( index = False, header = [ "date", "time", "inches" ],
                   path_or_buf = main_pathPercipitation + "/lakePleasant.csv" )

# push mountUnion data to CSV
tempArr = []
for year in sorted( mtUnion.keys() ):
    mtUnion[ year ].sort()
    for data in mtUnion[ year ]:
        data = data.split( ", " )
        tempArr.append( data )
toBeConcat = pd.DataFrame( tempArr )
toBeConcat.to_csv( index = False, header = [ "date", "time", "inches" ],
                   path_or_buf = main_pathPercipitation + "/mountUnion.csv" )

# push magma data to CSV
tempArr = []
for year in sorted( magma.keys() ):
    magma[ year ].sort()
    for data in magma[ year ]:
        data = data.split( ", " )
        tempArr.append( data )
toBeConcat = pd.DataFrame( tempArr )
toBeConcat.to_csv( index = False, header = [ "date", "time", "inches" ],
                   path_or_buf = main_pathPercipitation + "/magma.csv" )
