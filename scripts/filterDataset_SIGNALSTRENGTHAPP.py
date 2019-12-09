import parser
import pandas as pd
from sys import argv
from os import path, walk
from datetime import datetime


if len(argv) != 2:
    raise ValueError( "Invalid Number of Arguements!\n" +
                      "argv[0] - this program\n" +
                      "argv[1] - machine type\n" )

machineType = parser.getMachineType( argv[1] )

if machineType == "monsoon":
    monitorCSV = parser.monsoon_unfiltered_data + "/signal_strength_app"
    filtered_path = parser.monsoon_filtered_data + "/signal_strength_app"

else:
    monitorCSV = parser.local_unfiltered_data + "/signal_strength_app"
    filtered_path = parser.local_filtered_data + "/signal_strength_app"


def parseData( fileLine ):
    initSplit = fileLine.split( " " )
    day, month = initSplit[0].split( "/" )
    return "{} {} {}".format( month, day, year ), initSplit[1], initSplit[2]


def updateTime( time ):
    hour, minutes = time.split( ":" )
    print( "Before: {}:{}".format( hour, minutes ) )
    minutes = int( minutes )
    if minutes not in [ 0, 15, 30, 45 ]:
        if minutes < 7:
            print( "S1" )
            minutes = "00"
        elif ( 7 < minutes < 15 ) or ( 15 < minutes <= 22 ):
            print( "S2" )
            minutes = 15
        elif ( 22 < minutes < 30 ) or ( 30 < minutes <= 37 ):
            print( "S3" )
            minutes = 30
        elif ( 37 < minutes < 45 ) or ( 45 < minutes <= 52 ):
            print( "S4" )
            minutes = 45
        else:
            print( "S5" )
            hour = int(hour) + 1
            minutes = "00"

    print( "After: {}:{}\n".format( hour, minutes ) )
    return "{}:{}".format( hour, minutes )


dataArray = []
year = datetime.now().year
for root, dirs, files in walk( monitorCSV ):
    for file in files:
        if ".txt" not in file:
            continue

        with open( path.join( root, file ), "r" ) as p:
            fileContents = p.readlines()[ 2: ]

            previousDate, previousTime = "", ""
            for index, line in enumerate( fileContents ):
                if index > 0:
                    previousDate, previousTime, signal = parseData( fileContents[ index - 1 ] )

                date, time, signal = parseData( line )
                time = updateTime( time )

                if previousDate == date and previousTime == time:
                    continue

                dataArray.append( [ date, time, signal ] )

toExport = pd.DataFrame( dataArray )
toExport.to_csv( filtered_path + "/signal_strength.csv", index = False,
                 header = [ "date", "time", "signal strength (dBM)" ] )
