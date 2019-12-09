"""
NOTE: Autodownloads the differential files within the last 8 days
      inclusive of today.
"""
import parser
from datetime import datetime, timedelta

urlBase = "https://opencellid.org/ocid/downloads?token=VALIDTOKEN"
urlBase += "&type=diff&file=OCID-diff-cell-export-2019-MONTH-DAY-T000000.csv.gz"
token = "33df4b541ecc4b" # please update token after Dec. 13 2019
print( "Available downloads..." )
for daysBack in range( 7 ):
    date = datetime.now() - timedelta( days = daysBack )
    dateMonth = date.month
    dateDay = date.day

    if dateMonth < 10:
        dateMonth = "0{}".format( dateMonth )
    if dateDay < 10:
        dateDay = "0{}".format( dateDay )

    diffURL = urlBase.replace( "VALIDTOKEN", token )
    diffURL = diffURL.replace( "MONTH", str( dateMonth ) )
    diffURL = diffURL.replace( "DAY", str( dateDay ) )

    print( diffURL )
