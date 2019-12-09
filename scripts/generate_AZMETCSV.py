import parser
import requests
import pandas as pd
from sys import argv
from bs4 import BeautifulSoup



if len(argv) != 2:
    raise ValueError( "Invalid Number of Arguements!\n" +
                      "argv[0] - this program\n" +
                      "argv[1] - machine type\n" )

machineType = parser.getMachineType( argv[1] )


if machineType == "monsoon":
    AZNET_dataPath = parser.monsoon_precipitation + "/AZNET"

else:
    AZNET_dataPath = parser.local_precipitation + "/AZNET"


hubURL = "https://cals.arizona.edu/azmet/az-data.htm"
hubContnets = BeautifulSoup( requests.get( hubURL ).text, 'html.parser' )
hyperLinks = hubContnets.findAll( "a" )
recordBool = False
stationDict = dict()
for link in hyperLinks:
    if link.text == "Aguila":
        recordBool = True
    elif link.text == "Yuma Mesa":
        recordBool = False

    if recordBool:
        stationDict[ link.text ] = "https://cals.arizona.edu/azmet/" + link[ 'href' ]


for stationID in stationDict:
    stationLink = stationDict[ stationID ]

    print( "Gathering files from:", stationLink )
    stationContent = BeautifulSoup( requests.get( stationLink ).text, 'html.parser' )
    stationLinks = stationContent.findAll( "a" )

    for stationLink in stationLinks:
        if stationLink.text == "Hourly":
            data = BeautifulSoup( requests.get( "https://cals.arizona.edu/azmet/" + stationLink[ 'href' ] ).text, 'html.parser' )
            year = list( data )[ 0 ].split( "," )[ 0 ]

            if int(year) < 2000:
                break

            saveFile = "{}/{}{}.txt".format( AZNET_dataPath, stationID, year )

            with open( saveFile, "w" ) as f:
                for line in list( data ):
                    f.write( line )
