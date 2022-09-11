class Day:
    timetable: int
    holiday: str

class Day_extra:
    def __init__(self, timetable, holiday):
        self.timetable = timetable
        self.holiday = holiday

monday = Day
monday.timetable = 3
tuesday = Day_extra(
    timetable=4, 
    holiday="Christmas"
)

def function(day: Day):
    print(day.timetable)
    print(day.holiday)

function(tuesday)