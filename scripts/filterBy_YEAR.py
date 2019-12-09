"""
NOTE: The code for this program is very long and repeatative, however this was
      the most optimized for speed, otherwise each file needs to be re-read and
      opened 13 times in comparison to 1.

CODE LIMITATIONS: As it stands, this code is not modular outside of its predicted
                  cases. This program works for the current file strucuture, as well
                  as the current locations, with the useable years of 2006 to 2019.
"""

import parser
import pandas as pd
from sys import argv
from progressbar import progressbar

# if true, text regarding the size and process will be printed to the screen
debugBool = True


if len(argv) != 3:
    raise ValueError( "Invalid Number of Arguements!\n" +
                      "argv[0] - this program\n" +
                      "argv[1] - machine type\n" +
                      "argv[2] - location choice\n")

machineType = parser.getMachineType( argv[1] )
location = parser.getLocation( argv[2] )


if machine_type == "monsoon":
    arizona_masterDataPath = parser.monsoon_masterCSV + "/Arizona_data_master.csv"
    dallas_masterDataPath = parser.monsoon_masterCSV + "/Dallas_data_master.csv"
    arizona_dataPath = parser.monsoon_filteredData + "/Arizona"
    dallas_dataPath = parser.monsoon_filteredData + "/Dallas"
else:
    arizona_masterDataPath = parser.local_masterCSV + "/Arizona_data_master.csv"
    dallas_masterDataPath = parser.local_masterCSV + "/Dallas_data_master.csv"
    arizona_dataPath = parser.local_filteredData + "/Arizona"
    dallas_dataPath = parser.local_filteredData + "/Dallas"

if location == "Arizona":
    masterCSV = arizona_masterDataPath
    master_outputPath = arizona_dataPath
else:
    masterCSV = dallas_masterDataPath
    master_outputPath = dallas_dataPath


def __removeIndex( isDataFrame, indexArray):
    for reverse_index in range( len( indexArray ), 0, -1 ):
        if reverse_index not in indexArray:
            isDataFrame = isDataFrame.drop( [ reverse_index ] )
    return isDataFrame


# DataFrame Array for Each Year
dataFrame2006 = []
dataFrame2007 = []
dataFrame2008 = []
dataFrame2009 = []
dataFrame2010 = []
dataFrame2011 = []
dataFrame2012 = []
dataFrame2013 = []
dataFrame2014 = []
dataFrame2015 = []
dataFrame2016 = []
dataFrame2017 = []
dataFrame2018 = []
dataFrame2019 = []

progress_masterCSV = pd.read_csv( masterCSV )[ "0" ]
for csv in progressbar( progress_masterCSV, redirect_stdout = True ):
    index2006 = []
    index2007 = []
    index2008 = []
    index2009 = []
    index2010 = []
    index2011 = []
    index2012 = []
    index2013 = []
    index2014 = []
    index2015 = []
    index2016 = []
    index2017 = []
    index2018 = []
    index2019 = []

    dataFrame = pd.read_csv( csv )
    fileName, filePath = parser.splitPath( csv )
    index = 0

    if debugBool:
        print( "Parsing:", fileName )

    for date in dataFrame[ "created" ]:

        year = parser.getYear( date )

        if year == 2006:
            index2006.append( index )
        elif year == 2007:
        	index2006.append( index )
        elif year == 2008:
        	index2007.append( index )
        elif year == 2009:
        	index2009.append( index )
        elif year == 2010:
        	index2010.append( index )
        elif year == 2011:
        	index2011.append( index )
        elif year == 2012:
        	index2012.append( index )
        elif year == 2013:
        	index2013.append( index )
        elif year == 2014:
        	index2014.append( index )
        elif year == 2015:
        	index2015.append( index )
        elif year == 2016:
        	index2016.append( index )
        elif year == 2017:
        	index2017.append( index )
        elif year == 2018:
        	index2018.append( index )
        elif year == 2019:
        	index2019.append( index )
        index += 1

    # generate a temporary dataFrame, to be fused at the very end
    temp2006 = __removeIndex( dataFrame, index2006 )
    temp2007 = __removeIndex( dataFrame, index2007 )
    temp2008 = __removeIndex( dataFrame, index2008 )
    temp2009 = __removeIndex( dataFrame, index2009 )
    temp2010 = __removeIndex( dataFrame, index2010 )
    temp2011 = __removeIndex( dataFrame, index2011 )
    temp2012 = __removeIndex( dataFrame, index2012 )
    temp2013 = __removeIndex( dataFrame, index2013 )
    temp2014 = __removeIndex( dataFrame, index2014 )
    temp2015 = __removeIndex( dataFrame, index2015 )
    temp2016 = __removeIndex( dataFrame, index2016 )
    temp2017 = __removeIndex( dataFrame, index2017 )
    temp2018 = __removeIndex( dataFrame, index2018 )
    temp2019 = __removeIndex( dataFrame, index2019 )

    # add to corresponding DataFrame Array
    dataFrame2006.append( temp2006 )
    dataFrame2007.append( temp2007 )
    dataFrame2008.append( temp2008 )
    dataFrame2009.append( temp2009 )
    dataFrame2010.append( temp2010 )
    dataFrame2011.append( temp2011 )
    dataFrame2012.append( temp2012 )
    dataFrame2013.append( temp2013 )
    dataFrame2014.append( temp2014 )
    dataFrame2015.append( temp2015 )
    dataFrame2016.append( temp2016 )
    dataFrame2017.append( temp2017 )
    dataFrame2018.append( temp2018 )
    dataFrame2019.append( temp2019 )


# Concatinated DataFrame per year
Master2006_DataFrame = pd.concat( dataFrame2006 )
Master2007_DataFrame = pd.concat( dataFrame2007 )
Master2008_DataFrame = pd.concat( dataFrame2008 )
Master2009_DataFrame = pd.concat( dataFrame2009 )
Master2010_DataFrame = pd.concat( dataFrame2010 )
Master2011_DataFrame = pd.concat( dataFrame2011 )
Master2012_DataFrame = pd.concat( dataFrame2012 )
Master2013_DataFrame = pd.concat( dataFrame2013 )
Master2014_DataFrame = pd.concat( dataFrame2014 )
Master2015_DataFrame = pd.concat( dataFrame2015 )
Master2016_DataFrame = pd.concat( dataFrame2016 )
Master2017_DataFrame = pd.concat( dataFrame2017 )
Master2018_DataFrame = pd.concat( dataFrame2018 )
Master2019_DataFrame = pd.concat( dataFrame2019 )

# output paths for each year
outputPath2006 = master_outputPath + "/2006.csv"
outputPath2007 = master_outputPath + "/2007.csv"
outputPath2008 = master_outputPath + "/2008.csv"
outputPath2009 = master_outputPath + "/2009.csv"
outputPath2010 = master_outputPath + "/2010.csv"
outputPath2011 = master_outputPath + "/2011.csv"
outputPath2012 = master_outputPath + "/2012.csv"
outputPath2013 = master_outputPath + "/2013.csv"
outputPath2014 = master_outputPath + "/2014.csv"
outputPath2015 = master_outputPath + "/2015.csv"
outputPath2016 = master_outputPath + "/2016.csv"
outputPath2017 = master_outputPath + "/2017.csv"
outputPath2018 = master_outputPath + "/2018.csv"
outputPath2019 = master_outputPath + "/2019.csv"

# export all to csv
Master2006_DataFrame.to_csv( index = False, path_or_buf = outputPath2006 )
Master2007_DataFrame.to_csv( index = False, path_or_buf = outputPath2007 )
Master2008_DataFrame.to_csv( index = False, path_or_buf = outputPath2008 )
Master2009_DataFrame.to_csv( index = False, path_or_buf = outputPath2009 )
Master2010_DataFrame.to_csv( index = False, path_or_buf = outputPath2010 )
Master2011_DataFrame.to_csv( index = False, path_or_buf = outputPath2011 )
Master2012_DataFrame.to_csv( index = False, path_or_buf = outputPath2012 )
Master2013_DataFrame.to_csv( index = False, path_or_buf = outputPath2013 )
Master2014_DataFrame.to_csv( index = False, path_or_buf = outputPath2014 )
Master2015_DataFrame.to_csv( index = False, path_or_buf = outputPath2015 )
Master2016_DataFrame.to_csv( index = False, path_or_buf = outputPath2016 )
Master2017_DataFrame.to_csv( index = False, path_or_buf = outputPath2017 )
Master2018_DataFrame.to_csv( index = False, path_or_buf = outputPath2018 )
Master2019_DataFrame.to_csv( index = False, path_or_buf = outputPath2019 )
