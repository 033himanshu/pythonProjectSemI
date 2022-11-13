class date:
    #date can be given in string format also
    #also handle that case
    
    nDays = (31,28,31,30,31,30,31,31,30,31,30,31)

    def __init__(self, day=0, month=0, year=0):
            #set the current date
            # if date or month
            # set to current date or month or year respectively to date only
            # if input is (12,0,2021)
            # then month will be assign to current month
        if day == 0 or month == 0:
            cDate = self.getCurrentDate()
            #cDate[0] -> day    #cDate[1] -> month    #cDate[2] -> year
            if day == 0:
                day = cDate.day
            if month == 0:
                month == cDate.month
           

        if self.isValidDate(day,month,year):
            self.day = day
            self.month = month
            self.year = year



    @classmethod
    def isValidDate(cls,day,month,year):
        #Checking if date is valid or not 
        #otherwise raise exception
        if(type(day) != int or type(month) != int or type(year) != int):
            raise TypeError('type of day, month and year should be string')
        if (cls.isValidYear(year) and cls.isValidMonth(month) and cls.isValidDay(day,month,year)):
            return True
        else:
            raise ValueError('Date is Not Valid, "0<=year<=9999" , "1<=month<=12" , "1<=day<=31" (differ month to month)') 

    @classmethod
    def isValidYear(cls,year):
        return year>=0 and year <= 9999
        #if 0<=year<=9999 then it is a valid year
    
    @classmethod
    def isValidMonth(cls,month):
        return month>=1 and month <=12
        #if 1<=month<=12 then it is a valid month

    @classmethod
    def isValidDay(cls,day,month,year):
        return day>=1 and day<=cls.getNumberOfDaysInMonth(month,year)
        #it checks is Year a leap year or not then month and then it validate

    
    @classmethod
    def getNumberOfDaysInMonth(cls,month,year):
        
        if month == 2 and cls.isLeapYear(year):
            return 29
        return cls.nDays[month -1]


    @classmethod
    def isLeapYear(cls,year):
        #return True or False based on The year type
        if (year % 4 == 0):
            if (year % 100 == 0 and year % 400 != 0):
                return False
            else:
                return True
        else:
            return False


    def getDate(self,formate):
        pass
        #return date in given format

    
    def changeDay(self,day):
        if self.isValid(day,self.month,self.year):
            self.day = day
    
    def changeMonth(self,month):
        if self.isValid(self.day,month,self.year):
            self.month = month
    
    def changeYear(self,year):
        if self.isValid(self.day,self.month,year):
            self.year = year

         
    def _manageDate(self,day,month,year):
        pass
        

    def _countLeapYears(self):

        years = self.year

        # Check if the current year needs
        # to be considered for the count
        # of leap years or not
        if (self.month <= 2):
            years -= 1

        # An year is a leap year if it is a
        # multiple of 4, multiple of 400 and
        # not a multiple of 100.
        ans = int(years / 4)
        ans -= int(years / 100)
        ans += int(years / 400)
        return ans


    def _getNoOfDays(self):
        # COUNT TOTAL NUMBER OF DAYS

        # initialize count using years and day
        n = self.year * 365 + self.day

        # Add days for months in given date
        for i in range(0, self.month - 1):
            n += self.nDays[i]

        # Since every leap year is of 366 days,
        # Add a day for every leap year
        n += self._countLeapYears()
        return n

    def _createDateFromDays(self,days):
        year = 0
        month = 1
        day = 1
        if(days >= 146097):
            #146097 == 400 years
            year += (days // 146097)*400
            days %= 146097
        
        if(days >= 36524):
            #36524 == 100 years
            year += (days // 36524)*100
            days %= 36524
        
        if(days >= 1461):
            #1461 == 4 years
            year += (days //1461)*4
            days %= 1461

        if(days >= 365):
            #365 == 1 year
            year += days // 365
            days %= 365


        for i in range(12):
            if days >= self.nDays[i]:
                month +=1
                days -= self.nDays[i]
                if(self.isLeapYear(year)) and i == 1:
                    days -=1
                    if(days < 0):
                        month -=1
                        days = 28
            else:
                break
        
        day += days
        return date(day,month,year)
        

            




    def getDifferenceInDays(self, date1):
        # return no of Days between Two Dates
        return (self._getNoOfDays() - date1._getNoOfDays())

    
    def differenceWithCurrentDate(self):
        return self.getDifferenceWithDate(self.getCurrentDate)
        #return difference from current date
    
    def getDifferenceWithDate(self,date1):
        day = self.day - date1.day
        month = self.month  - date1.month
        year = self.year - date1.year

        diff = self._manageDate(day,month,year)
        status = 'P'
        if (diff[2]<0):
            status = 'N'
            diff = date1.getDifferenceWithDate(self)
        
        return tuple(diff[0],diff[1],diff[2],status)
        #return difference
    



    def __sub__(self,date1):
        return self.getDifferenceBetweenTwoDates(date1)


    def __LT__(self,date1):
        #returns true if d1 < d2
        diff = self.__sub__(date1)
        if (diff[3] == 'N'):
            return True
        return False
    
    def __GT__(self,date1):
        #returns true if d1 > d2
        diff = self.__sub__(date1)
        if (diff[3] == 'P'):
            return True
        return False
    
    def __EQ__(self,date1):
        #returns true if d1 == d2
        diff = self.__sub__(date1)
        if (diff[0] == 0 and diff[1] == 0 and diff[2] == 0):
            return True
        return False
    
    def __LE__(self,date1):
        #returns true if d1 <= d2
        if self.__LT__(date1) or self.__EQ__(date1):
            return True
        return False

    def __GE__(self,date1):
        #returns true if d1 >= d2
        if self.__GT__(date1) or self.__EQ__(date1):
            return True
        return False
    
    def __NE__(self,date1):
        # returns true if d1 != d2
        return not self.__EQ__(date1)

    # Comparison Operators :
    # Operator Magic Method
    # < __LT__(SELF, OTHER)
    # > __GT__(SELF, OTHER)
    # <= __LE__(SELF, OTHER)
    # >= __GE__(SELF, OTHER)
    # == __EQ__(SELF, OTHER)
    # != __NE__(SELF, OTHER)


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



    
    
    def getCurrentDate(self):
        #return current machine date obj
        from datetime import date as dt
        today = dt.today().strftime("%d/%m/%Y")
        today = tuple(int(x) for x in today.split('/'))
        return date(*today)
        # return date(day=today[0],month=today[1],year=today[2])


    def __repr__(self):
        return f"date({self.day}/{self.month}/{self.year})"

    
    
    '''
        Also overload operator
        - for difference between two dates
    '''
    

    
