#Import the required Libraries
from tkinter import *
from tkinter import ttk
from Airline_City_Pair import *

#Create an instance of Tkinter frame
win= Tk()
win.title("Flight Finder") # rename frame

#Set the geometry of Tkinter frame
win.geometry("450x350")

# command for button to execute to add flight info found
def displayText():
   global entry
   string= entry.get() # retrieve input
   label2.configure(text=flightCityPair(string)) # call flightCityPair to get flight info for input

# Add label with instructions for user
label1 = Label(win,text="Please Enter a Flight Number (XX1234)", font=("Courier 12"))
label1.pack(pady=15) # vertical pad

#Create an Entry widget to accept User Input
entry= Entry(win, width= 40)
entry.pack(pady=10) # vertical pad

# Button to execute displayText
ttk.Button(win, text= "Search",width= 15, command= displayText).pack(pady=20)

#Initialize a Label to display the User Input
label2=Label(win, text="", font=("Courier 12 bold"))
label2.pack()

win.mainloop()
