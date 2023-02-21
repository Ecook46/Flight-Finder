# Flight Finder Project
Flight Finder is a basic web-scraper designed to pull the airport pairings and city pairings provided a valid flight number. 
The project is not an in-depth application and was made to try out the basic concepts of webscraping, gui creation
as well as learning how to create executables with pyinstaller and pushing to a repo with git bash. This project was inspired by
Melanie Walsh's [Introduction to Cultural Analytics & Python](https://github.com/melaniewalsh/Intro-Cultural-Analytics) book.

### Working Principle of Airline_City_Pair.py
The website [FlightStats by Cirium](https://www.flightstats.com/v2) indexes the flights it tracks by separating the Airlines
IATA code from the flight number. EX: www<area>.flightstats.com/v2/flight-tracker/{CARRIER_CODE}/{FLIGHT_NUMBER}

Using this pattern any input of form XX9999 can be split and used to search for flights. Upon retrieving a response from
the website the HTML response is searched to find the necessary information. The response is validated to determine if a 
flight was found for a given number or not. If a valid response is received then the flight information is formatted and retuned.

### Working Principle of Flight_Finder_Script.py
Flight_Finder_Script.py utilizes the tkinter library to create a basic GUI for user input and displaying output.
Upon running the script the following window is displayed. The interface uses tkinter's labels, entry boxes and buttons.


<p align="center">
<img src="/Images/GUI_Image.png"  width="30%" height="30%">
</p>


The user can then enter a flight number and click the search button. The button will activate a command that takes the input in the entry field and
calls flightCityPair(). The returned formatted string is displayed in a new label below the search button.


<p align="center">
<img src="/Images/Result_Image.png"  width="30%" height="30%">
</p>

### Executable With pyinstaller
To allow people to use the Flight Finder program without any programming knowledge pyinstaller was used to create an executable.
The final file size is 14 mb which seems fairly large but the file was created with the --onefile command so there is probably a lot
of unnecessary code included in the file. Resource Hacker was used to add a new icon created by [Martz90](https://icon-icons.com/users/3h1L42DieiNhrev9g293n/icon-sets/)
to the file for visual appeal[^1].

<p align="center">
<img src="/Images/Icon_Image.png"  width="15%" height="15%">
</p>

### Limitations/Planned Fixes
The biggest limitation of the system is the assumption for flight numbers to be of the form XX9999. Some new carriers such as Flair Airlines has IATA code
of F8 and the website uses F8* to identify them. This makes Flair flights unreadable as the flight number is split at the 8. A potential fix for this problem
could be to compile a list of all airline codes recognized by FlightStats and split based off that but that would take time to compile and would need to be updated
to recognize new airlines. Another possible fix would be to split by " " and take inputs as "XX 9999" but this is a rather unatural way to write flight numbers.
Another limitation of the system is it only recognizes flights a few days out. If a flight is too far in the future or past FlightStats does not
track it by carrier and flight number but also includes a date field. Finally, the data provided is very basic and not useful. The tool would be more useful
if it also provided the flight times and date. These changes may be implemented to the attached code files if I feel motivated to but not to the .exe file.

[^1]:  CC Attribution-NonCommercial-NoDerivs
