class date:
    #date can be given in string format also
    #also handle that case
    def __init__(self, day=0, month=0, year=0):
        if day == 0 or month == 0 or year ==0:
            pass
            #set the current date
            # if date or month or year = 0 
            # set to current date or month or year respectively to date only
            # if input is (12,0,2021)
            # then month will be assign to current month

        if self.isValid(day,month,year):
            self._day = day
            self._month = month
            self._year = year

    @classmethod
    def isValidDate(cls,day,month,year):
        pass
        #Checking if date is valid or not 
        #otherwise raise exception

    def isValidYear(self,year):
        pass
        #if 0<year<=9999 then it is a valid year
    
    def isValidMonth(self,month):
        pass
        #if 1<=month<=12 then it is a valid month

    def isValidDay(self,day,month,year):
        pass
        #it checks is Year a leap year or not then month and then it validate

    def getDate(self,formate):
        pass
        #return date in given format
    
    def isLeapYear(self,year):
        pass

    def changeDay(self,day):
        if self.isValid(day,self.month,self.year):
            self.day = day
    
    def changeMonth(self,month):
        if self.isValid(self.day,month,self.year):
            self.month = month
    
    def changeYear(self,year):
        if self.isValid(self.day,self.month,year):
            self.year = year

    def getCurrentDate(self):
        pass
        #return current machine date
   
    def getAge(self):
        pass
        #return difference from current date
    
    def getDifferenceBetweenTwoDates(self,date2):
        pass
        #return difference
    
    def getDateXDaysAfter(self,x):
        pass
        #return date after x days
    
    def getDateXMonthsAfter(self,x):
        pass
        #return date after x months

    def getDateXYearsAfter(self,x):
        pass
        #return date after x years

    def getDateXDaysBefore(self,x):
        pass
        #return date before x days
    
    def getDateXMonthsBefore(self,x):
        pass
        #return date before x months

    def getDateXYearsBefore(self,x):
        pass
        #return date before x years
    
    def getDayName(self):
        pass
        #return day name like sunday, Monday
    '''
        Also overload operator
        - for difference between two dates
    '''
    

    
