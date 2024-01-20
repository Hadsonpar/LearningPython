def days(code):
    if (code == 1):
        day = "Sunday"
    if (code == 2):
        day = "Monday"
    if (code == 3):
        day = "Tuesday"
    if (code == 4):
        day = "Wednesday"
    if (code == 5):
        day = "Thursday"
    if (code == 6):
        day = "Friday"
    if (code == 7):
        day = "Saturday"
    return day

schedules = {
    "16": "16:00",
    "18": "18:00",
    "20": "20:00",    
    "22": "22:00"    
}

program = {
    "instructor": "Hadson Paredes",
    "program": "Learning Python benninger"
}