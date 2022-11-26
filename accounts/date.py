class date:
    # date can be given in string format also
    # also handle that case

    nDays = (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)

    def __init__(self, day=0, month=0, year=0):
        # set the current date
        # if date or month or year = 0
        # set to current date or month or year respectively to date only
        # if input is (12,0,2021)
        # then month will be assign to current month
        if day == 0 or month == 0 or year == 0:
            cDate = self.getCurrentDate()
            # cDate[0] -> day    #cDate[1] -> month    #cDate[2] -> year
            if day == 0:
                day = cDate.day
            if month == 0:
                month = cDate.month
            if year == 0:
                year = cDate.year

        if self.isValidDate(day, month, year):
            self.day = int(day)
            self.month = int(month)
            self.year = int(year)

        else:
            raise ValueError(
                'Date is Not Valid, "0<year<=9999" , "1<=month<=12" , "1<=day<=31" (differ month to month)')

    @classmethod
    def _makeInt(cls, *dt):
        # return date in int format if not int
        return (int(x) for x in dt)

    @classmethod
    def isValidDate(cls, day, month, year):
        # Checking if date is valid or not
        # otherwise raise exception
        # if(type(day) != int or type(month) != int or type(year) != int):
        #     raise TypeError('type of day, month and year should be string')
        day, month, year = cls._makeInt(day, month, year)
        if (cls.isValidYear(year) and cls.isValidMonth(month) and cls.isValidDay(day, month, year)):
            return True
        return False

    @classmethod
    def isValidYear(cls, year):
        return year > 0 and year <= 9999
        # if 0<year<=9999 then it is a valid year

    @classmethod
    def isValidMonth(cls, month):
        return month >= 1 and month <= 12
        # if 1<=month<=12 then it is a valid month

    @classmethod
    def isValidDay(cls, day, month, year):

        return cls.isValidYear(year) and cls.isValidMonth(month) and day >= 1 and day <= cls.getNumberOfDaysInMonth(
            month, year)
        # it checks is Year a leap year or not then month and then it validate

    @classmethod
    def getNumberOfDaysInMonth(cls, month=1, year=1):
        # return no. of month in that month if month and year is valid else return None
        if cls.isValidMonth(month) and cls.isValidYear(year):
            if month == 2 and cls.isLeapYear(year):
                return 29
            return cls.nDays[month - 1]
        else:
            return None

    @classmethod
    def isLeapYear(cls, year):
        if not cls.isValidYear(year):
            return False
            # raise ValueError("Year is not valid  it should be in 0<year<=9999")
        # return True or False based on The year type
        if (year % 4 == 0):
            if (year % 100 == 0 and year % 400 != 0):
                return False
            else:
                return True
        else:
            return False

    def getDateWithDifferentFormat(self, formate='%Mn %d %y ,%wd'):
        '''
            formats

            %d - %m - %y %w  :  2 - 1 - 2002 Wed
            %m - %d - %y   :  1 - 2 - 2002
            %d %m %y       :  2 1 2002
            %d %M %y       :  2 Jan 2002
            %M %d , %y     :  Jan 2 , 2002
            %Mn %d , %y    :  January 2 , 2002
            %d %m %y ,%wd  : 2 1 2002 , Wednesday
        '''
        # return date in given format

        nMonth = (
        'January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November',
        'December')
        if '%d' in formate:
            formate = formate.replace('%d', str(self.day))
        if '%Mn' in formate:
            formate = formate.replace('%Mn', nMonth[self.month - 1])
        elif '%M' in formate:
            formate = formate.replace('%M', nMonth[self.month - 1][:3])
        elif '%m' in formate:
            formate = formate.replace('%m', str(self.month))
        if '%y' in formate:
            formate = formate.replace('%y', str(self.year))
        if '%wd' in formate:
            formate = formate.replace('%wd', self.getDayName())
        elif '%w' in formate:
            formate = formate.replace('%w', self.getDayName()[:3])

        return formate

    def changeDay(self, day):
        if self.isValidDate(day, self.month, self.year):
            self.day = day
        else:
            raise ValueError("Will become Invalid date")

    def changeMonth(self, month):
        if self.isValidDate(self.day, month, self.year):
            self.month = month
        else:
            raise ValueError("Will become Invalid date")

    def changeYear(self, year):
        if self.isValidDate(self.day, self.month, year):
            self.year = year
        else:
            raise ValueError("Will become Invalid date")

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
        n = (self.year - 1) * 365 + self.day

        # Add days for months in given date
        for i in range(0, self.month - 1):
            n += self.nDays[i]

        # Since every leap year is of 366 days,
        # Add a day for every leap year
        n += self._countLeapYears()
        return n

    def _createDateFromDays(self, days):
        year = 1
        month = 1
        day = 0
        if (days > 146097):
            # 146097 == 400 years
            year += (days // 146097) * 400
            days %= 146097

        if (days > 36524):
            # 36524 == 100 years
            year += (days // 36524) * 100
            days %= 36524

        if (days > 1461):
            # 1461 == 4 years
            year += (days // 1461) * 4
            days %= 1461

        if (days > 365):
            # 365 == 1 year
            year += days // 365
            days %= 365

        for i in range(12):
            if days > self.nDays[i]:
                month += 1
                days -= self.nDays[i]
                if (self.isLeapYear(year)) and i == 1:
                    days -= 1
                    if (days <= 0):
                        month -= 1
                        days = 29
            else:
                break

        day += days
        return date(day, month, year)

    def _manageDays(self, days):
        year = 0
        month = 0
        day = 0
        if (days > 146097):
            # 146097 == 400 years
            year += (days // 146097) * 400
            days %= 146097

        if (days > 36524):
            # 36524 == 100 years
            year += (days // 36524) * 100
            days %= 36524

        if (days > 1461):
            # 1461 == 4 years
            year += (days // 1461) * 4
            days %= 1461

        if (days > 365):
            # 365 == 1 year
            year += days // 365
            days %= 365

        for i in range(12):
            if days > self.nDays[i]:
                month += 1
                days -= self.nDays[i]
                if i == 1 and self.isLeapYear(year):
                    days -= 1
                    if (days <= 0):
                        month -= 1
                        days = 29
            else:
                break

        day += days
        return (day, month, year)

    def getDifferenceInDays(self, date1):
        # return no of Days between Two Dates
        return (self._getNoOfDays() - date1._getNoOfDays())

    def differenceWithCurrentDate(self):
        return self.getDifferenceWithDate(self.getCurrentDate())
        # return difference from current date

    def getDifferenceWithDate(self, date1):
        # returns a tuple (x days,y months, z years, status)
        # status represents difference is negative or positive
        diff = self.getDifferenceInDays(date1)
        status = 'P'
        if (diff < 0):
            status = 'N'
            diff *= -1

        tempDate = self._manageDays(diff)

        return (tempDate[0], tempDate[1], tempDate[2], status)

    # operators overloading starts here

    def __sub__(self, date1):
        return self.getDifferenceWithDate(date1)

    def __lt__(self, date1):
        # returns true if d1 < d2
        diff = self.getDifferenceInDays(date1)
        if (diff < 0):
            return True
        return False

    def __gt__(self, date1):
        # returns true if d1 > d2
        diff = self.getDifferenceInDays(date1)
        if (diff > 0):
            return True
        return False

    def __eq__(self, date1):
        # returns true if d1 == d2
        diff = self.getDifferenceInDays(date1)
        if (diff == 0):
            return True
        return False

    def __le__(self, date1):
        # returns true if d1 <= d2
        if self < date1 or self == date1:
            return True
        return False

    def __ge__(self, date1):
        # returns true if d1 >= d2
        if self > date1 or self == date1:
            return True
        return False

    def __ne__(self, date1):
        # returns true if d1 != d2
        return not self == date1

    # operators overloading ends here

    def getDateXDaysAfter(self, x):
        days = self._getNoOfDays() + x
        if (days >= 0):
            return self._createDateFromDays(days)
        else:
            raise ValueError("Invalid input")

        # return date after x days

    def getDateXDaysBefore(self, x):
        return self.getDateXDaysAfter(-1 * x)
        # return date before x days

    def getDayName(self):
        import pandas as pd
        d = pd.Timestamp(f'{self.year}-{self.month}-{self.day}')
        return d.day_name()
        # return day name like sunday, Monday

    def getCurrentDate(self):
        # return current machine date obj
        from datetime import date as dt
        today = dt.today().strftime("%d/%m/%Y")
        today = tuple(int(x) for x in today.split('/'))
        return date(*today)
        # return date(day=today[0],month=today[1],year=today[2])

    def getWeekEnd(self):
        today = self
        for i in range(0,8):
            if today.getDayName() == 'Sunday':
                return (today,)
            if today.getDayName() == 'Saturday':
                return (today,today.getDateXDaysAfter(1))
            today = today.getDateXDaysAfter(1)




    def __repr__(self):
        return f"date({self.day}/{self.month}/{self.year})"




