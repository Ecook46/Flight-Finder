# importing libraries
from bs4 import BeautifulSoup as Soup
import requests, re

# function to print flight info to console
def flightFinder(flightNum):
    print(flightCityPair(flightNum))
    return 

# Function to find an aircarriers city pairing by flight number
def flightCityPair(flightNum):

    flightList = decodeFlightNum(flightNum) # split inputted flight number

    # retrieve flight information from www.flightstats.com
    siteResponse = requests.get(f"https://www.flightstats.com/v2/flight-tracker/{flightList[0]}/{flightList[1]}")
   
    # get html from the response
    getHTML = siteResponse.text
    
    # use bs4 to search through html easier
    flightDoc = Soup(getHTML, "html.parser")  
    
    # retrieve Air carrier info for flight and format
    carrierInfo = flightDoc.find("h1").text
    carrierInfo = carrierInfo.replace(" Flight Tracker", "")
   
    # determine if flight exists, a non-existant flight XX1234 will return (XX) 1234 and a valid
    # flight YY1234 will return (YY) <Carrier Name> 1234
    if not re.search("\(\w+\) [\w\s]+ \d+",carrierInfo):
        return "\nNo Flight Found!\n"
 
    # Retrieve Airport Codes and Airport Cities from site
    cityInfo = flightDoc.findAll("a", attrs={"class": "ticket__AirportLink-sc-1rrbl5o-10 joakbA"})
    extraCity = flightDoc.findAll("div", attrs={"class":"text-helper__TextHelper-sc-8bko4a-0 efwouT"})
    
    # extract clean text from html 
    cityInfo = [[city.text for city in cityInfo],[extra.text for extra in extraCity]]
    
    # return formatted string of flight info
    return  formatter(carrierInfo, cityInfo)

# function to decode the flight number into components
def decodeFlightNum(flightNum):
    flightList = re.split('(\d+)', flightNum) # split by alphabet characters and digits
    # make all upper case to avoid issues with code share as ws1234 would return the DL321 instead of
    # WS1234 if WS1234 was operated by Delta
    flightList[0] = flightList[0].upper() 
    return flightList

# Function that formats all flight info
def formatter(carrierInfo, cityInfo):
    # pad used to center airport code pairing
    pad = int((len(carrierInfo)/2 - 7)+1)
    # size to determine box dimensions
    size = max([len(carrierInfo),len(cityInfo[1][0]), len(cityInfo[1][1])]) + 4

    # The following lines format the flight information
    line1 = ("\n" +"*"*size + "\n* " + str(carrierInfo) + " "*(size - len(carrierInfo)-3) + "*\n*" + " "*(size - 2) + "*\n*")
    line2 = ( " "*pad + str(cityInfo[0][0]) + " " + "-"*5 + "> " + str(cityInfo[0][1]) +" "*(size - pad - 16)) 
    line3 = ("*\n*" + "-"*(size-2) + "*\n* " + str(cityInfo[1][0]) +" "*(size-len(cityInfo[1][0])-3) + "*\n* to" + " "*(size-5))
    line4 = ("*\n* " + str(cityInfo[1][1]) +" "*(size-len(cityInfo[1][1])-3) +"*\n" + "*"*size +"\n")
    #return combined string
    return line1 + line2 + line3 + line4

