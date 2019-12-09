import parser
import pandas as pd
from sys import argv


# if True, will print out information regarding the process and status of Filtering
debugBool = True

if len(argv) != 2:
    raise ValueError("Invalid Number of Arguements!\n" +
                     "argv[0] - this program\n" +
                     "argv[1] - machine type\n")

machineType = parser.getMachineType( argv[1] )

if machineType == "monsoon":
    arizona_masterCSV = parser.monsoon_masterCSV + "/Arizona_data_master.csv"
    dallas_masterCSV = parser.monsoon_masterCSV = "/Dallas_data_master.csv"
    filtered_dataPath = parser.monsoon_filteredData
    intermediate_dataPath = parser.monsoon_intermediateData

else:
    arizona_masterCSV = parser.local_masterCSV + "/Arizona_data_master.csv"
    dallas_masterCSV = parser.local_masterCSV + "/Dallas_data_master.csv"
    filtered_dataPath = parser.local_filteredData
    intermediate_dataPath = parser.local_intermediateData

"""
filters csv by a given radio type
@param: pd.core.frame.DataFrame isDataFrame - csv to be parsed
@param: String isRadioType - type of radio that will be returned
@return: pd.core.frame.DataFrame radioFrame - dataFrame containing only one radio signal
"""
def filterByRadio( isDataFrame, isRadioType ):
    if not type( isDataFrame ) == pd.core.frame.DataFrame:
        raise ValueError("Please use a pandas DataFrame.")

    dropIndexArray = []
    radioFrame = isDataFrame.copy()
    for index, radio in enumerate( isDataFrame[ "radio" ] ):
        if radio != isRadioType:
            dropIndexArray.append( index )

    for removeIndex in range( len( dropIndexArray ), 0, -1 ):
        value = dropIndexArray[ removeIndex - 1 ]
        radioFrame = radioFrame.drop( [ value ] )

    return radioFrame


if __name__ == '__main__':
    masterCSVArray = [ arizona_masterCSV, dallas_masterCSV ]
    for index, masterCSV in enumerate( masterCSVArray ):
        LTE_dataFrame = []
        GSM_dataFrame = []
        UMTS_dataFrame = []
        CDMA_dataFrame = []

        for csv in pd.read_csv( masterCSV )[ "0" ]:
            isDataFrame = pd.read_csv( csv )
            fileName, filePath = parser.split_path( csv )
            maxSize = len( pd.read_csv( masterCSV )[ "0" ] ) * 4

            for isRadioType in [ "LTE", "GSM", "UMTS", "CDMA" ]:

                if debugBool:
                    print( "\n{} of {:,}".format( index, maxSize ) )
                    print( "Parsing:", fileName )
                    print( "Radio Type:", isRadioType )

                radioFrame = filterByRadio( isDataFrame, isRadioType )

                if isRadioType == "LTE":
                    LTE_dataFrame.append( radioFrame )
                elif isRadioType == "GSM":
                    GSM_dataFrame.append( radioFrame )
                elif isRadioType == "UMTS":
                    UMTS_dataFrame.append( radioFrame )
                else:
                    CDMA_dataFrame.append( radioFrame )

        if "Arizona" in masterCSV:
            LTEoutput = intermediate_dataPath + "/Arizona_LTE.csv"
            GSMoutput = intermediate_dataPath + "/Arizona_GSM.csv"
            UMTSoutput = intermediate_dataPath + "/Arizona_UTMS.csv"
            CDMAoutput = intermediate_dataPath + "/Arizona_CDMA.csv"
        elif "Dallas" in masterCSV:
            LTEoutput = intermediate_dataPath + "/Dallas_LTE.csv"
            GSMoutput = intermediate_dataPath + "/Dallas_GSM.csv"
            UMTSoutput = intermediate_dataPath + "/Dallas_UTMS.csv"
            CDMAoutput = intermediate_dataPath + "/Dallas_CDMA.csv"

        LTE = pd.concat( LTE_dataFrame )
        LTE.to_csv( index = False, path_or_buf = LTEoutput )

        GSM = pd.concat( GSM_dataFrame )
        GSM.to_csv( index = False, path_or_buf = GSMoutput )

        UMTS = pd.concat( UMTS_dataFrame )
        UMTS.to_csv( index = False, path_or_buf = UMTSoutput )

        CDMA = pd.concat( CDMA_dataFrame )
        CDMA.to_csv( index = False, path_or_buf = CDMAoutput )
