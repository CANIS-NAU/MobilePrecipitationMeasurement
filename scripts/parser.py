"""
------[ PURPOSE ]------
This file acts as a helpful library, containing
functions and variables that have been and will be
useful through-out the data parsing process.

------[ STRUCTURE ]------
1. Exceptions
2. Paths
3. General Functions
4. CSV Parsing Functions
5. HTML Parsing Functions
6. Time/Date Parsing Functions

------[ AUTHOR INFORMATION ]------
@author: Christian "Kainoa" Boyce
@contact: ckb234 [at] nau [dot] edu
"""
import os
import pandas as pd
from time import gmtime, strftime
from joblib import Parallel, delayed
# from geopy.distance import great_circle # use format tuple(lat, long)


"""
------[ 1. EXCEPTIONS ]------
These are exceptions when specific conditions are met. These exceptions
exist to make debugging/trouble-shooting as easy as possible

* InvalidParameter: called when an arguemnt to a method/function is
                    not valid for the given situation
"""
class InvalidParameters( Exception ):
    pass

class InvalidMachineType( Exception ):
    pass

class InvaidLocationChoice( Exception ):
    pass


"""
------[ 2. PATHS ]------
This project was/is intended to be run on a local machine as well as NAU's
cluster Monsoon. If you intend on running this program on your own machine
please change the 'local_root_path' and follow the naming scheule shown below.

* root_path: path to main directory of project
* csv_files: path to main location of all csv file
* unfiltered_data: path to raw data directory
* intermediate_data: path to semi-parsed data directory
* master_csv: path to master csvs directory
* percipiation: path to all percipiation data
"""
# monsoon related paths
monsoon_rootPath = "/projects/canis/mcs_storm"
monsoon_csvFiles = monsoon_rootPath + "/csv_files"
monsoon_unfilteredData = monsoon_csvFiles + "/unfiltered_data"
monsoon_filteredData = monsoon_csvFiles + "/filtered_data"
monsoon_intermediateData = monsoon_filteredData + "/intermediate_data"
monsoon_masterCSV = monsoon_csvFiles + "/master_csv"
monsoon_unfilteredPercipitation = monsoon_filteredData + "/arizona_precipitation"
monsoon_percipitation = monsoon_unfilteredData + "/Percipitation"

# local machine related paths
local_rootPath = "/Users/kainoaboyce/Documents/NAU/FALL 2019/CS 485"
local_csvFiles = local_rootPath + "/csv_files"
local_unfilteredData = local_csvFiles + "/unfiltered_data"
local_filteredData = local_csvFiles + "/filtered_data"
local_intermediateData = local_csvFiles + "/filtered_data/intermediate_data"
local_masterCSV = local_csvFiles + "/master_csv"
local_unfilteredPercipitation = local_unfilteredData + "/arizona_precipitation"
local_percipitation = local_filteredData + "/Percipitation"

"""
------[ 3. GENERAL FUNCTIONS ]------
These are functions that are used more generally, and are
aimed at making data parsing as easy as possible.

* splitPath: splits a file path into filename and path
* getMachineType: given a string, returns a valid machine type
* getLocation: given a string, returns valid location ( Arizona, Dallas )



splits a file's full path into a file name and file path
NOTE: does not check if file exists

@param: String isFullPath - full and valid file path
@return: String fileName - name of file
@return: String filePath - path to file, not including file name
"""
def splitPath( isFullPath ):
    if "/" not in isFullPath:
        raise InvalidParameter("Not a valid path!")
    fileName = isFullPath.split("/")[ -1 ]
    filePath = isFullPath.replace( "/" + fileName, "" )
    return fileName, filePath


"""
returns a valid machine type string
@param: String isMachine - name of machine
@return: String [ 'local', 'monsoon' ]
"""
def getMachineType( isMachine ):
    if isMachine.lower() not in [ "local", "monsoon" ]:
        raise InvalidMachineType( "An invalid machine string was given!" )
    return isMachine.lower()


"""
returns a valid location string
@param location_choice
@return: String [ 'Arizona', 'Dallas' ]
"""
def getLocation( isLocation ):
    if isLocation.capitalize() not in [ "Arizona", "Dallas" ]:
        raise InvaidLocationChoice( "An invalid location string was given!" )
    return isLocation.capitalize()


"""
------[ 4. CSV PARSING FUNCTIONS ]------
These functions are aimed at reducing the overall code in
the main filtering files.

* filterByLocation: parses a DataFrame for its location information
* customFilterByLocation: parses a DataFrame for its location information


parses valid columns given their latitude and longitude
@param: pandas.core.DataFrame data_frame - a DataFrame of the csv
@param: String location_choice - location to be parsed
@return: pandas.core.DataFrame filtered_data - A DataFrame containing useful info
"""
def filterByLocation( isDataFrame, isLocation, numCores = 1 ):
    if not isinstance( isDataFrame, pd.core.frame.DataFrame ):
        raise TypeError("This function requires a pandas DataFrame as an arguement.")

    filteredDataFrame = data_frame.copy()
    dataFrameSize = len( data_frame )
    dropIndexArray = []
    longitude = data_frame[ "lon" ]
    latitude = data_frame[ "lat" ]

    def __removeIndex( isLocationChoice, isLat, isLon ,isIndex ):
        if isLocationChoice == "Arizona":
            latCondition = (31 + 1/3) < abs( isLat ) < 37
            lonCondition = 109.05 < abs( isLon ) < 114.816
            if not latCondition and not lonCondition:
                dropIndexArray.append( isIndex )

        elif isLocationChoice == "Dallas":
            position = ( isLat, isLon )
            Dallas = ( 32.7767, -96.7970 )
            distance = great_circle( Dallas, position ).miles
            if distance > 100:
                dropIndexArray.append( index )

    Parallel( n_jobs = numCores )( delayed( __removeIndex )( isLocationChoice, lat, lon, index ) for lat, lon, index in zip( latitude, longitude, range( dataFrameSize ) ) )

    for removeIndex in range( len( dropIndexArray ), 0, -1 ):
        value = drop_arr[ removeIndex - 1 ]
        filteredDataFrame = filteredDataFrame.drop( [ value ] )

    return filteredDataFrame


"""
given a dataframe and location data, returns a parsed dataframe
@param: pandas.core.DataFrame data_frame - a DataFrame of the csv
@param: float latitude - latitude of a location
@param: float longitude - longitude of a location
@return: pandas.core.DataFrame filtered_data - A DataFrame containing useful info
"""
def customFilterByLocation( isDataFrame, isLat, isLon, numCores = 1 ):
    if not isinstance( isDataFrame, pd.core.frame.DataFrame ):
        raise TypeError("This function requires a pandas DataFrame as an arguement.")

    filteredDataFrame = isDataFrame.copy()
    dataFrameSize = len( isDataFrame )
    dropIndexArray = []
    longitude = isDataFrame[ "lon" ]
    latitude = isDataFrame[ "lat" ]

    def __removeIndex( myLat, myLon , isIndex ):
        currentPos = ( myLat, myLon )
        location = ( isLat, isLon )
        distance = great_circle( location, currentPos ).miles
        if distance > 10:
            drop_arr.append( isIndex )

    Parallel( n_jobs = numCores )( delayed( __removeIndex )( lat, lon, index ) for lat, lon, index in zip( latitude, longitude, range( dataFrameSize ) ) )

    for removeIndex in range( len( dropIndexArray ), 0, -1 ):
        value = drop_arr[ removeIndex - 1 ]
        filteredDataFrame = filteredDataFrame.drop( [ value ] )

    return filteredDataFrame


"""
------[ 5. HTML PARSING FUNCTIONS ]------
Given a predetermined structure, returns the desired output

* getTitle: given a list, returns the plausable location name
* getData: given a list, returns a list of all plausable data


within a given HTML file, returns the title
@param: isHTMLContents - a list representing an HTML page
@return: A string of the title
"""
def getTitle( isHTMLContents ):
    if not isinstance( isHTMLContents, list ):
        raise TypeError( "list Needed for getTitle function" )
    for line in isHTMLContents:
        if "<h3>" in line:
            tempLine = line.replace( "\n", "" )
            return tempLine.split( "<h3><pre>" )[ -1 ]


"""
given a list of html code, returns the useable data
@param: isHTMLContents - a list representing an HTML page
@return: dataList - a list containing useful data from isHTMLContents
"""
def getData( isHTMLContents ):
    if not isinstance( isHTMLContents, list ):
        raise TypeError( "list Needed for getData function" )

    dataList = []
    dataBool = False
    for line in isHTMLContents:
        if "inches" in line and not dataBool:
            dataBool = True
            continue
        elif line == "\n" and dataBool:
            dataBool = False
        if dataBool:
            dataList.append( line )

    return dataList


"""
given a standard string, returns the useful data within the string
@param String data - a String containing spaces and data
@return: String date, String timestamp, String inches
"""
def parseLine( isData ):
    dataSplit = isData.split( " " )
    for isData in data_split:
        if isData == '':
            dataSplit.remove( isData )
    date = dataSplit[ 0 ]
    timestamp = dataSplit[ 1 ]
    inches = dataSplit[ 2 ]
    return date, timestamp, inches


"""
------[ 6. TIME/DATE PARSING FUNCTIONS ]------
These functions parse strings or integers and return
the desired result.

* getYear: given time and date stamp in seconds, returns the year
* getMonth: given time and date stamp in seconds, returns the month


given the epoch time, return the year
@param int epoch_time - time in seconds since epoch
@return int - year assosicated with epoch_time
"""
def getYear( isUnixTime ):
    if not isinstance( isUnixTime, int ):
        raise TypeError("Invalid Input, an integer is required!\n")

    timeDate = gmtime( isUnixTime )
    return int( strftime("%Y", timeDate) )


"""
given the epoch time, return the month
@param int epoch_time - time in seconds since epoch
@return String - month assosicated with epoch_time
"""
def getMonth( isUnixTime ):
    if not isinstance( isUnixTime, int ):
        raise TypeError("Invalid Input, an integer is required!\n")
    timeDate = gmtime( isUnixTime )
    return strftime("%m", timeDate)
