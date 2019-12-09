.. This file contains all documentation related to
   CANIS Lab's MCS Storm Project

.. Documentation Notes
   Triple New Line: New Section
   Single New Line: Split Sub Sections

.. role:: raw-html(raw)
   :format: html

############
Introduction
############
  | **Who is working on this:** This project is run and managed by Dr. Vigil-Hayes,
                                an assistant professor and researcher at Northern Arizona
                                University. The students on the "MCS Storm" Project include:

  ====================    ================
  **Student Name**        **Time Frame**
  Christian Boyce         Fall 2019
  ====================    ================

  | **Problem Description:** Currently, storm system monitoring relies on expensive radar
                     equipment. While detection systems are highly accurate, their
                     cost can be prohibitive to universal deployment. This project
                     aims to identify a relationship between storm systems and
                     cellular signal data that might be used as a means for
                     crowd sensing storm systems in an affordable and pervasive manner.

**********************
Background Information
**********************
  This program utilizes two main programming languages. The first being Python,
  it is used for: data parsing, web scraping, graph generation, model generation, etc.
  The second language used is Java; Java is used for Android application Development.
  This project used an app `Network Monitor <https://github.com/caarmen/network-monitor/>`_.

  This project utilizes a number of third party python applications in order to accomplished
  certain tasks:

  ==============================    =============   =========================
  **Library**                        **Version**     **Use Case**
  pandas                             0.25.3          CSV Read & Write
  matplotlib                         3.1.1           Graphing
  progressbar2                       3.47.0          Visualize Progress
  sklearn                            0.21.3          Maching Learning Modeling
  bs4                                0.0.1           Web Scraping
  joblib                             0.14.0          Concurrent Programs
  geopy                              1.20.0          Distance Calculations
  sphinx-rtd-theme                   0.4.3           Documentation
  sphinxcontrib-applehelp            1.0.1           Documentation
  sphinxcontrib-devhelp              1.0.1           Documentation
  sphinxcontrib-htmlhelp             1.0.2           Documentation
  sphinxcontrib-jsmath               1.0.1           Documentation
  sphinxcontrib-qthelp               1.0.2           Documentation
  sphinxcontrib-serializinghtml      1.1.3           Documentation
  ==============================    =============   =========================

*******************
Data Descriptions
*******************
  A significant section of this project deals with data gathering, parsing and
  drawing conclusions based on that data. In the early stages of this project,
  there were numerous sources of data in order to determine the viability of this
  concept. Some of these datasets are not useful anymore or are redundant. However,
  at one point they were a notable source of data. In the future, they may become useful again.

OpenCellid
===============
  OpenCellid is the world's largest Open Database of Cell Towers. OpenCellid allows
  its users to located devices with GPS, view mobile hotspots and analyze mobile operator
  coverage. OpenCellid was used to determine the location of mobile hot spots to find
  the best locations to set up cellphones and or base stations to record data about RSSI.

  ==================   ======================================================================             ==============================
  **Characteristic**   **Description**                                                                    **Possible Values/Value Type**
  radio                The generation of broadband cellular network technology                            LTE, GMS, CDMA, UMTS
  mcc                  Mobile Country Code                                                                001 - 999
  net/mnc              Mobile Network Code                                                                001 - 999
  area                 Location Area Code (LAC)                                                           001 - 999
  cell                 Cell tower code (CID)                                                              integer
  unit                 Unknown                                                                            0
  lon                  Approximate longitude of cell tower                                                (0, 180)
  lat                  Approximate latitude of cell tower                                                 (0, 90)
  range                Approximate area within which the cell could be. (radius in meters)                integer usually >= 1000
  samples              Number of measures processed to get this data                                      integer >= 1
  changeable           indicates whether the cell is averaged                                             0 or 1
  created              UNIX timestamp created                                                             integer >= 1136073600
  updated              UNIX timestamp updated                                                             integer >= 1136073600
  averageSignal        RSSI value of the average signal over number of samples                            0 (OpenCellid does not record)
  ==================   ======================================================================             ==============================

  There are two types of data avaiable. The first being country data, so all
  recorded data for a given country. The second type is known as a differential,
  this file contains data of any towers updated in the last 24 hours (based on UTC)


Arizona Weather Stations
=========================
  This data was gather through the `2019 Global IOT Datathon <https://iotdatathons.com/>`_.
  The data gathered was from the following weather stations in Arizona: Lake Pleasant,
  Magma, or Mount Union.
  :raw-html:`<br/>`
  The data initially came came in an HTML file which contained:

  ==================   ================================================             ==============================
  **Characteristic**   **Description**                                              **Possible Values/Value Type**
  Date                 Date in which the data is recorded                           MM/DD/YYYY
  Time                 Time in which the data is recorded                           HH:MM:SS (24-hour)
  Inches               Accumulated amount of precipitation                          floating point value
  Inches               Raw amount of precipitation at a given interval              floating point value
  ==================   ================================================             ==============================

  This data was recorded at random intervals, anywhere from once every minute to
  once a day. This purpose of this source was to determine if data from OpenCellid
  was within close proximity to the given weather stations.


National Oceanic and Atmospheric Administration (NOAA)
========================================================
  This data was gathered through NOAA, specifically `NOAA's Hydrometerological Automated
  Data System (HADS) <https://hads.ncep.noaa.gov//cgi-bin/hads/interactiveDisplays/displayMetaData.pl?table=dcp&nesdis_id=F004D1D0>`_.
  The data was collected using a precipitation Accumulator. The recording device is located
  on a runway at Flagstaff-Pulliam Airport.

  ==================   ================================================             ==============================
  **Characteristic**   **Description**                                              **Possible Values/Value Type**
  Observed Time        Time and Date that the data was recorded                     YYYY-MM-DD HH:MM (24-hour)
  PC                   Accumulated Precipitation                                    floating point value
  ==================   ================================================             ==============================

  Given that this is an on going collection, this data is used to determine the
  real-time / recent precipitation in Flagstaff.

The Arizona Meteorological Network (AZMET)
=============================================

  .. image:: AZMET.png
     :width: 300px
     :height: 300px
     :align: right

  The meteorological data collected by `AZMET <https://cals.arizona.edu/azmet/az-data.htm/>`_
  include temperature (air and soil),
  humidity, solar radiation, wind (speed and direction), and precipitation.
  AZMET also provides a variety of computed variables, including heat units
  (degree-days), chill hours, dew point and reference crop evapotranspiration (ETo).
  AZMET data are summarized in a variety of formats, including several ready-to-use
  summaries and comma-delimited (raw) ASCII text files that can be imported into
  most database and spreadsheet programs.

  AZMET records data from 41 stations. However, only 31 sites are active. Flagstaff is not
  one of those. AZMET is a would be a useful data source if we had access to RSSI data
  in those given areas.

  The data is formatted using the following key::

    DATA POINT
    NUMBERS --> 1  2  3  4    5    6  7 8  9   10   11  12  13  14 15  16  17  18
                |  |  |  |    |    |  | |  |    |    |   |   |   |  |   |   |  |
    DATA --> 2003,254,1,20.9,42.2,1.4,0,0,25.5,27.6,1.6,1.3,147,33,2.6,.05,.34,-.3

    Data
    Point    Description
    ------  ---------------------
     1   A   Year
     2   B   Day of Year (DOY)
     3   C   Hour of Day
     4   D   Air Temperature
     5   E   Rel. Humidity
     6   F   Vapor Pressure Deficit
     7   G   Solar Radiation
     8   H   Precipitation
     9   I   4 inc. Soil Temperature  ( = 2 inc. prior to 1999 )
    10   J   20 inc. Soil Temperature  ( = 4 inc. prior to 1999 )
    11   K   Wind Speed (Ave)
    12   L   Wind Vector Magnitude
    13   M   Wind Vector Direction
    14   N   Wind Direction Standard Deviation
    15   O   Max Wind Speed
    16   P   Reference Evapotranspiration (ETo) - Original AZMET
    -------------------------------------------------------------------
    17   Q   Actual Vapor Pressure        New : 2003 to Present
    18   R   Dew point, Hourly Average    New : 2003 to Present


Signal Strength (Android Application)
========================================
  This is an application used to record RSSI data in a particular area.
  The application allows the user to record numerous useful Characteristics
  related to Cell Service i.e. connected tower, RSSI and logging
  ( 15 min intervals up, max duration is 1 month ).

  This application was originally created by a user called "Lakshman", the app
  is currently againable in the `Google Play Store <https://play.google.com/store/apps/details?id=com.cls.networkwidget&hl=en_US/>`_

  ==================   ================================================             ==============================
  **Characteristic**   **Description**                                              **Possible Values/Value Type**
  Date                 Date that the data was recorded                              DD/Mon.
  Time                 Time that the data was recorded                              HHH:MM (24-hour)
  RSSI Value           Received Signal Strength Indicator                           negative integer <= -26
  Radio                The generation of broadband communication                    HSPA+[3G]
  ==================   ================================================             ==============================

  Example Log::

    Signal Strength Log
    Last 30 days
    13/Nov 10:47 -79 dBm HSPA+[3G]
    13/Nov 11:04 -81 dBm HSPA+[3G]
    13/Nov 11:19 -79 dBm HSPA+[3G]
    13/Nov 11:36 -69 dBm HSPA+[3G]
    13/Nov 11:54 -71 dBm HSPA+[3G]




:raw-html:`<br/>`
:raw-html:`<br/>`

########################
File System Structure
########################
.. note::
   Many of the programs rely on files being located in very specific areas. Therefore
   It is very important to follow this guide as much as possible.


   This is the current file Structure::

    .
    ├── csv_files
    │   ├── filtered_data
    │   │   ├── Arizona
    │   │   │   ├── Arizona_filtered_by_location_split
    │   │   │   ├── Arizona_filtered_by_radio
    │   │   │   ├── Arizona_filtered_by_year
    │   │   │   └── originals
    │   │   ├── Dallas
    │   │   │   ├── Dallas_filtered_by_location_split
    │   │   │   ├── Dallas_filtered_by_radio
    │   │   │   ├── Dallas_filtered_by_year
    │   │   │   └── originals
    │   │   ├── Percipitation
    │   │   │   ├── AZNET
    │   │   │   ├── LakePleasant
    │   │   │   ├── Magma
    │   │   │   ├── MountUnion
    │   │   │   └── NOAA
    │   │   ├── intermediate_data
    │   │   └── signal_strength_app
    │   ├── master_csv
    │   └── unfiltered_data
    │       ├── arizona_precipitation
    │       ├── differentials
    │       │   ├── 09-04-2019_split
    │       │   ├── 09-11-2019_split
    │       │   ├── 09-12-2019_split
    │       │   ├── 09-13-2019_split
    │       │   ├── 09-14-2019_split
    │       │   ├── 09-15-2019_split
    │       │   ├── 09-16-2019_split
    │       │   ├── 09-17-2019_split
    │       │   ├── 09-19-2019_split
    │       │   ├── 09-20-2019_split
    │       │   ├── 09-21-2019_split
    │       │   ├── 09-22-2019_split
    │       │   ├── 09-23-2019_split
    │       │   ├── 09-24-2019_split
    │       │   ├── 09-25-2019_split
    │       │   ├── 09-27-2019_split
    │       │   ├── 09-28-2019_split
    │       │   ├── 09-29-2019_split
    │       │   ├── 09-30-2019_split
    │       │   ├── autoDownload
    │       │   └── originals
    │       ├── signal_strength_app
    │       └── us_data
    │           ├── 302_split
    │           ├── 310_split
    │           ├── 311_split
    │           └── originals
    ├── documentation
    │   ├── build
    │   │   └── html
    │   └── source
    │       ├── _static
    │       └── _templates
    ├── network_monitor_master
    ├── other
    └── scripts

**************
Naming Scheme
**************

Folders
=========
  The naming scheme for the folder is to be specific and something that can be easily
  interpreted. The only important Characteristic for naming folders is to include underscores
  if a folder name contains multiple names.

  ==================   =======================================================================================
  **Folder Name**      **Contents**
  csv_files            A folder that contains all data containing CSV Files
  unfiltered_data      A folder containing all unfiltered data
  filtered_data        A folder that contains data filtered by some category i.e. Location, Radio, Year, etc.
  ==================   =======================================================================================

Scripts
=========
  All scripts written for this project can be categorized into a number of groups.
  These groups act as a prefix for the file. The only exception to this rule is the
  custom module / library ("parser.py") written for this project.
  The naming convention is as follows [prefix]_DATETYPE.

  ====================   ===================================================================================================
  **Scripts Prefix**     **Description**
  filterBy               filter some set of CSV's containing OpenCellid data
  [graph_type]graph      generate a graph using data associated with the following word i.e. bargraph_DATE.py
  filterDataset          either parse through a large dataset for useful data or change data from text/html to a CSV file
  generate               generate a CSV for temporary or permanent purposes.
                         :raw-html:`<br/>`
                         This type of file is usually used in conjunction with another task
  update                 update some CSV in /csv_files/master_csv or another file
                         :raw-html:`<br/>`
                         i.e. csv_files/filtered_data/Arizona/tower_data.csv
  get                    generate a conclusion about data
                         :raw-html:`<br/>`
                         i.e. get_DATERANGE.py generates a text file containing the date range of a the associated data
  ====================   ===================================================================================================





CSVs
====
  Regarding the naming scheme of CSV files, there are two main types of CSV files
  associated with this project. The first being general CSV files, these are files
  that contain data that needs to be parsed. The second type of CSV is known as
  "master" CSV, which contains a list of all CSV's per a certain category i.e.
  intermediate data, unfiltered data, filtered data, etc.

  ================    ============================   =================================
  **Type of CSV**     **Naming Scheme**              **Location**
  General CSV         See Notes Below                /csv_files
                                                     :raw-html:`<br/>`
                                                     **does not include master CSV**

  Master CSV          [data location]_master.csv     /csv_files/master_csv
  ================    ============================   =================================

    a `data location` refers to one of the following tags:

    =====================       ====================================================================
    **Data Location**           **Path**
    intermediate_data           /csv_files/filtered_data/intermediate_data
    unfiltered_data             /csv_files/unfiltered_data
    Arizona_data                /csv_files/filtered_data/Arizona/Arizona_filtered_by_location_split
    Dallas_data                 /csv_files/filtered_data/Dallas/Dallas_filtered_by_location_split
    Arizona_precipitation       /csv_files/unfiltered_data/arizona_precipitation
    differential_data           /csv_files/unfiltered_data/differentials
    =====================       ====================================================================

    ====================================================================     ====================================================================
    **Folder Location**                                                      **Naming Scheme**
    /csv_files/unfiltered_data/arizona_precipitation                         perception_[location]_YEAR_1.html
    /csv_files/unfiltered_data/differentials                                 MM-DD-2019__[alphabet char][alphabet char].csv
    /csv_files/unfiltered_data/us_data                                       [302 through 320]_[alphabet char][alphabet char].csv
    /csv_files/unfiltered_data/signal_strength_app                           [Mon.][DD]_[YYYY].csv
    /csv_files/filtered_data/Arizona                                         Arizona_filtered_by_[SPLITTYPE]_[alphabet char][alphabet char].csv
    /csv_files/filtered_data/Dallas                                          Dallas_filtered_by_[SPLITTYPE]_[alphabet char][alphabet char].csv
    /csv_files/filtered_data/intermediate_data                               N/A
    /csv_files/filtered_data/signal_strength_app                             signal_strength.csv
    /csv_files/filtered_data/Percipitation/AZNET                             [Station]YYYY.txt
    /csv_files/filtered_data/NOAA                                            NOAA_data_[Mon][DD]_[Mon][DD].csv
    /csv_files/filtered_data/[LakePleasant/Magma/MountUnion]                 [Location]_[Data of sorts].csv
    ====================================================================     ====================================================================



:raw-html:`<br/>`
:raw-html:`<br/>`

############
Scripts
############
  Since this project relies heavily on data parsing, interpretation and visualization
  there are a number of files associated with this project. Almost all of which
  contribute to the above mentioned tasks. All the code should be available either on
  Monsoon or the the CANIS lab GitHub page (TBD).

*********************************
Monsoon Compatibility
*********************************
  Given that there is a large amount of raw data that needs to be parsed, as well as
  a large amount of parsed data, sometimes a typical laptop is not able to compelte
  certain tasks in a timely manner, therfore this project has access to Northern Arizona
  University's Cluster Computer `Monsoon <https://in.nau.edu/hpc/>`_.

  In order for the code to work on a local machine, as well as monsoon,
  all python scripts are required to have some variation of the following
  code:

  .. code-block:: python

    import parser # all python scripts must contain this line
    from sys import argv

    """
    checks to determine that a machine type was given
    """
    if len(argv) != 2:
        raise ValueError("Invalid Number of Arguements!\n" +
                         "argv[0] - this program\n" +
                         "argv[1] - machine type\n")

    machineType = parser.getMachineType( argv[1] )

    if machineType == "monsoon":
        """
        VARIABLENAME = parser.monsoon[ SOME EXISTING EXTENSION ]
        """

    else:
        """
        VARIABLENAME = parser.monsoon[ SOME EXISTING EXTENSION ]
        """

    """
    NOTE: there should always be two of each variable in the
          above shown conditional statement
    """


*********************************
Custom Library: **parser.py**
*********************************
  This is a custom library that is used in all python files associated with this
  project. This library can be broken up into 6 main sections:

  * Exceptions
  * Paths
  * General Functions
  * CSV Parsing Functions
  * HTML Parsing Functions
  * Time/Date Functions

Exceptions
===========

  Exception.InvalidParameter:
    An exception raised if the given parameter
    was not of the necessary type

  Exception.InvalidMachineType:
    An exception raised if the input for
    getMachineType() is invalid

  Exception.InvaidLocationChoice:
    An exception raised if the input for
    getLocation() is invalid

Paths
======
  All paths mentioned below, have a monsoon and local value equivalent.

  rootPath
    the root path of the project

  csvFiles
    abstraction of: rootPath/csv_files

  unfilteredData
    abstraction of: rootPath/csv_files/unfiltered_data

  filteredData
    abstraction of: rootPath/csv_files/filtered_data

  intermediateData
    abstraction of: rootPath/csv_files/filtered_data/intermediate_data

  masterCSV
    abstraction of: rootPath/csv_files/master_csv

  unfilteredPercipitation
    abstraction of: rootPath/csv_files/unfiltered_data/arizona_precipitation

  percipitation
    abstraction of: rootPath/csv_files/unfiltered_data/Percipitation


General Functions
==================

  splitPath( str isFullPath )
      splits a file's full path into a file name and file path
      :raw-html:`<br/>`
      **NOTE**: does not check if file exists
      :raw-html:`<br/>`
      :raw-html:`<br/>`
      **parameter:** String isFullPath - full and valid file path
      :raw-html:`<br/>`
      **return:** String fileName - name of file
      :raw-html:`<br/>`
      **return:** String filePath - path to file, not including file name

  getMachineType( str isMachine )
      returns a valid machine type string
      :raw-html:`<br/>`
      **parameter:** String isMachine - name of machine
      :raw-html:`<br/>`
      **return:** String [ 'local', 'monsoon' ]

  getLocation( str isLocation )
      returns a valid location string
      :raw-html:`<br/>`
      **parameter:** String isLocation - the chosen location
      :raw-html:`<br/>`
      **return:** String [ 'Arizona', 'Dallas' ]


CSV Parsing Functions
======================

  filterByLocation( pandas.core.Dataframe isDataFrame, str isLocation, int numCores = 1 )
      parses valid columns given their latitude and longitude
      :raw-html:`<br/>`
      **parameter:** pandas.core.DataFrame isDataFrame - a DataFrame of the csv
      :raw-html:`<br/>`
      **parameter:** String isLocation - location to be parsed
      :raw-html:`<br/>`
      **parameter:** int numCores - number of cores used on problem
      :raw-html:`<br/>`
      **return:** pandas.core.DataFrame filteredData - A DataFrame containing useful info

  customFilterByLocation( pandas.core.Dataframe isDataFrame, str isLat, str isLon, int numCores = 1 )
    given a dataframe and location data, returns a parsed dataframe
    :raw-html:`<br/>`
    **parameter:** pandas.core.DataFrame isDataFrame - a DataFrame of the csv
    :raw-html:`<br/>`
    **parameter:** float isLat - latitude of a location
    :raw-html:`<br/>`
    **parameter:** float isLon - longitude of a location
    :raw-html:`<br/>`
    **return:** pandas.core.DataFrame filteredData - A DataFrame containing useful info


HTML Functions
===============

  getTitle( list isHTMLContents )
      within a given HTML file, returns the title
      :raw-html:`<br/>`
      **parameter:** isHTMLContents - a list representing an HTML page
      :raw-html:`<br/>`
      **return:** A string of the title

  getData( list isHTMLContents )
      given a list of html code, returns the useable data
      :raw-html:`<br/>`
      **parameter:** isHTMLContents - a list representing an HTML page
      :raw-html:`<br/>`
      **return:** dataList - a list containing useful data from isHTMLContents

  parseLine( str isData )
    given a standard string, returns the useful data within the string
    :raw-html:`<br/>`
    **parameter:** String isData - a String containing spaces and data
    :raw-html:`<br/>`
    **return:** String date, String timestamp, String inches


Time / Date Functions
=======================

  getYear( int isUnixTime )
      given the epoch time, return the year
      :raw-html:`<br/>`
      **parameter:** int isUnixTime - time in seconds since epoch
      :raw-html:`<br/>`
      **return:** int - year assosicated with isUnixTime


  getMonth( int isUnixTime )
      given the epoch time, return the year
      :raw-html:`<br/>`
      **parameter:** int isUnixTime - time in seconds since epoch
      :raw-html:`<br/>`
      **return:** String - month assosicated with isUnixTime



:raw-html:`<br/>`
:raw-html:`<br/>`

###############
Other Resources
###############
  These are other tools or notes that would prove useful for the current progress
  of this project.


**********
CSV Split
**********
  This is a bash function written by Christian Boyce to split a large CSV file into
  smaller chunks, and create a folder to store the newly split files. It should be noted that
  this will **not** remove the original.

  Example Use
    csv_split 302.csv 302

  =============  =================================================================
  **Argument**   **Description**
  File Name      The name of of the file to be split
  File Prefix    The prefix of the new set of files
                 :raw-html:`<br/>`
                 usually this should be the same as the file name without ".csv"
  =============  =================================================================

  .. code-block:: shell

    function csv_split {
      if [ "$#" -ne 2 ]; then
        printf "Invalid Args\n\tfile_name: file to be split\n\tfile_prefix: prefix of new files.\n\n"
      else
        csv_undo $2
        mkdir "$2_split"
        tail -n +2 $1 | split -l 5000 - $2_
        for file in $2_*
        do
            if [ "$file" != "$2_split" ]; then
              head -n 1 $1 > tmp_file
              cat $file >> tmp_file
              mv -f tmp_file "$2_split/$file.csv"
              rm -f $file
            else
              printf ""
            fi
        done
        cd "$2_split"
        rm -f $2_split.csv
        cd ..
      fi
    }


**********
CSV Undo
**********
  This is a bash function written by Christian Boyce to remove any files created
  as a result of the above mentioned `csv split` function. It should be noted that
  this will **not** remove the original.

  Example Use
    csv_undo 302

  =============  =================================================================
  **Argument**   **Description**
  File Prefix    The prefix of the new set of files
  =============  =================================================================

  .. code-block:: shell

    function csv_undo {
      if [ "$#" -ne 1 ]; then
        printf "Invalid Args\n\tfile_prefix: beginning of file or dir. to be removed\n\n"
      else
        cd "$1_split" || return
        rm -f * || return
        cd .. || return
        rmdir "$1_split" || return
      fi
    }


  :raw-html:`<br/>`
  :raw-html:`<br/>`

#############
Future Plans
#############
  Some tasks that could not be done due to a restriction but would be extremely beneficial
  for this project include:

  | * **Heat Map**: A map with an overlay option to Visualize perception data and amounts, as
    well as cell RSSI and sample quantities.

  | * **Machine Learn Regression Prediction**: A predictive regression model that can take in
    an RSSI value and output the possible precipitation, and vice versa.




  :raw-html:`<br/>`
  :raw-html:`<br/>`

###############
RST References
###############
  This is a box example::

    This is the first line of the box
    This is the second line of the box

  This line symbolizes the end of the box:

  * This is a bullet point
  * This is a bullet point ``with red text``

  **This sentence is bolded**
