# ***Problem Statement***:

## ***Given a cookie log file in the following format***:

### cookie,timestamp:
* AtY0laUfhglK3lC7,2018-12-09T14:19:00+00:00
* SAZuXPGUrfbcn5UA,2018-12-09T10:13:00+00:00
* 5UAVanZf6UtGyKVS,2018-12-09T07:25:00+00:00
* AtY0laUfhglK3lC7,2018-12-09T06:19:00+00:00
* SAZuXPGUrfbcn5UA,2018-12-08T22:03:00+00:00
* 4sMM2LxV07bPJzwf,2018-12-08T21:30:00+00:00
* fbcn5UAVanZf6UtG,2018-12-08T09:30:00+00:00
* 4sMM2LxV07bPJzwf,2018-12-07T23:30:00+00:00

## ***Write a command line program in your preferred language to process the log file and return the most active cookie for specified day. The example below shows how we'll execute your program.***

## ***Assumptions***:

* If multiple cookies meet that criteria, please return all of them on separate lines. 
* Please only use additional libraries for testing, logging and cli-parsing. There are libraries for most languages which make this too easy (e.g pandas) and we�d like you to show off your coding skills. 
* You can assume -d parameter takes date in UTC time zone.
* You have enough memory to store the contents of the whole file. 
* Cookies in the log file are sorted by timestamp (most recent occurrence is the first line of the file).

## ***Running Instructions***:

* Make sure python 3 is installed in your system.
* Usage $ python mostVisitedCookie.py <file_name> -d <query_date>
* For example: python mostVisitedCookie.py cookie_log.csv -d 2018-12-09 
* To run unittest cases - Usage: $ python -m unittest tests/testCookieSearch.py
* To check coverage - Usage: $ coverage run -m unittest tests/testCookieSearch.py && coverage report

## ***Code Reference***:

* ***mostVisitedCookie***: This file is the entry point for this project. For the given query date all the cookie id in the csv file is processed.
* ***cookieStore***:  Initially processed data will be written into cookie store. Then most visited cookies are retrieved for the given query date.
* ***testCookieSearch***: contains all unit test cases 
* ***htmlcov***: contains test coverage reports
* ***cookieSampleData***: This contains the data that is to be processed. 

