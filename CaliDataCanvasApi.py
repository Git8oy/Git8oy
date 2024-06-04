# Initialise an empty list to store events
canvasEvents = []

# Function to get an event by its ID
def getEventById(event_id):
    for event in canvasEvents:
        if event['myId'] == event_id:
            return event
    return None

def createEvent():
    # Getting input data for a new event from the user
    myID = float(input("Enter event ID: "))
    myDate = input("Enter date (DD/MM/YYYY): ")  # Update date format
    if not validateDate(myDate):  # Validating the date format
        print("Invalid date format or out of range.")
        return
    myStatus = input("Enter status: ")
    myEmail = input("Enter email: ")
    myRoomBooking = input("Enter room booking (Y/N): ")
    myRepeat = input("Enter repeat (Y/N): ")
    myLocation = input("Enter location: ")
    myVisibility = input("Enter visibility (Visible/Private): ")
    myTime = input("Enter time (HH:MM AM/PM): ")  # Update time format
    if not validateTime(myTime):  # Validating the time format
        print("Invalid time format or out of range.")
        return
    addEvent(myID, myDate, myStatus, myEmail, myRoomBooking, myRepeat, myLocation, myVisibility, myTime)
    print("Event created.")

# Function to add an event to the list
def addEvent(myID, myDate, myStatus, myEmail, myRoomBooking, myRepeat, myLocation, myVisibility, myTime):
    event = {
        'myId': myID, 'Date': myDate, 'Status': myStatus, 'Email': myEmail,
        'Room Booking': myRoomBooking, 'repeat': myRepeat, 'Location': myLocation,
        'Visibility': myVisibility, 'Time': myTime
    }
    canvasEvents.append(event)

# Hardcoded initial events with updated date and time formats
# (These are added automatically when the script is run)
addEvent(1.1, '27/01/2024', 'Accepted', 'bob.hardman@gmail.com', 'Y', 'Y', 'Cambridge', 'Visible', '01:00 PM')
addEvent(1.2, '28/01/2024', 'Accepted', 'dan.squire@gmail.com', 'Y', 'N', 'London', 'Private', '08:00 AM')
addEvent(1.3, '29/01/2024', 'Accepted', 'James.Michaels@gmail.co.uk', 'N', 'Y', 'Madrid', 'Visible', '09:00 AM')
addEvent(1.4, '10/01/2024', 'Rejected', 'peter.Gregs@gmail.com', 'N', 'N', 'Glasgow', 'Private', '10:30 AM')
addEvent(1.5, '07/02/2024', 'Accepted', 'Sarah.Maria@gmail.com', 'Y', 'Y', 'Reigate', 'Visible', '12:00 PM')
addEvent(1.6, '31/01/2024', 'Rejected', 'Josh.Key@gmail.com', 'Y', 'Y', 'Crawley', 'Visible', '02:00 PM')
addEvent(1.7, '30/01/2024', 'Accepted', 'stuart.jones@gmail.com', 'N', 'Y', 'London', 'Private', '03:00 PM')
addEvent(1.8, '24/01/2024', 'Rejected', 'Paul.Coffey@gmail.com', 'Y', 'N', 'London', 'Private', '04:00 PM')
addEvent(1.9, '28/01/2024', 'Accepted', 'Denise.Kent@gmail.com', 'Y', 'Y', 'Cardiff', 'Visible', '11:00 AM')
addEvent(1.10, '26/02/2024', 'Accepted', 'Steve.Trent@gmail.com', 'N', 'N', 'Paris', 'Visible', '12:00 PM')

# Function to read and print all events
def readCanvasEvents():
    for event in canvasEvents:
        print(event)

# Function to amend an existing meeting
def amendMeeting():
    eventId = float(input("Enter the event ID to amend: "))
    event = getEventById(eventId)
    if event:
        newDate = input("Enter new date (DD/MM/YYYY): ")
        if not validateDate(newDate):
            print("Invalid date format or out of range.")
            return
        newTime = input("Enter new time (HH:MM AM/PM): ")
        if not validateTime(newTime):
            print("Invalid time format or out of range.")
            return
        event['Date'] = newDate
        event['Time'] = newTime
        print("Meeting amended.")
    else:
        print("Event not found.")

# Function to delete an event
def deleteEvent():
    eventId = int(input("Enter the event ID to delete: "))
    global canvasEvents
    canvasEvents = [event for event in canvasEvents if event['myId'] != eventId]
    print("Event deleted if it existed.")

# Function to quit the application
def quitApplication():
    print("Quitting application")
    return True

# Function to validate the date format
def validateDate(dateStr):
    try:
        day, month, year = map(int, dateStr.split('/'))
        if not (1 <= month <= 12):
            return False
        if not (1 <= day <= 31):
            return False
        return True
    except ValueError:
        return False
    
from datetime import datetime  # Importing the datetime module from Python's standard library.

# Function to validate the time format
def validateTime(timeStr):
    try:
        # Using datetime.strptime to parse the time string according to the specified format ("%I:%M %p").
        # This converts the string into a datetime object if the format is correct.
        timeObj = datetime.strptime(timeStr, "%I:%M %p")
        return True  # If the parsing is successful, return True, indicating a valid time format.
    except ValueError:  # Handling a specific type of error: ValueError, which occurs if the string doesn't match the expected format.
        return False  # If ValueError is raised (indicating an invalid time format), return False.
