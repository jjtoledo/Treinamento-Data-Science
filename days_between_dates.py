'''
First try:

days = # of days in month1 - day1 -> 31 - 24 = 7
month1 += 1
while month1 < month2:
	days += # days of month1
	month1 += 1
days += day2
while year1 < year2:
	days += days in year1

---------------------------------------------------
Simple way:

days = 0
while date1 is before date2:
	date1 = day after date1
	days += 1
return days

---------------------------------------------------
### QUIZ nextDay:

### Define a simple nextDay procedure, that assumes
### every month has 30 days.
###
### For example:
###    nextDay(1999, 12, 30) => (2000, 1, 1)
###    nextDay(2013, 1, 30) => (2013, 2, 1)
###    nextDay(2012, 12, 30) => (2013, 1, 1)  (even though December really has 31 days)
###

def nextDay(year, month, day):
    """
    Returns the year, month, day of the next day.
    Simple version: assume every month has 30 days.
    """
    if day < 30:
        return year, month, day + 1
    else:
        if month < 12:
    		return year, month + 1, 1
	    else:        
    		return year + 1, 1, 1

print nextDay(2012, 1, 1)

---------------------------------------------------
# Including daysBetweenDates() procedure

def nextDay(year, month, day):
    """Simple version: assume every month has 30 days"""
    if day < 30:
        return year, month, day + 1
    else:
        if month == 12:
            return year + 1, 1, 1
        else:
            return year, month + 1, 1
        
def daysBetweenDates(year1, month1, day1, year2, month2, day2):
    """Returns the number of days between year1/month1/day1
       and year2/month2/day2. Assumes inputs are valid dates
       in Gregorian calendar, and the first date is not after
       the second."""
   
    days = 0
    while year1 != year2 or month1 != month2 or day1 != day2:
    	year1, month1, day1 = nextDay(year1, month1, day1)
    	#print (year1, month1, day1)
    	days += 1
    return days

def test():
    test_cases = [((2012,9,30,2012,10,30),30), 
                  ((2012,1,1,2013,1,1),360),
                  ((2012,9,1,2012,9,4),3)]
    
    for (args, answer) in test_cases:
        result = daysBetweenDates(*args)
        if result != answer:
            print "Test with data:", args, "failed"
        else:
            print "Test case passed!"

test()

'''