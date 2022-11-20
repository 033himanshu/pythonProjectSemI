from coach import coach
class train:

    '''
        trainName
        trainNumber
        source
        destination
        trainType ex: express, Superfast
        viaCities
        Days
        Coaches
            AC
                I AC coach
                II AC coach
                III AC coach
            NON-AC
                sleeper
                sitting  
        ac=[ 
                (list of IAC coaches) : no. of available seats,
                (list of IIAC coaches) : no. of available seats,
                (list of IIIAC coaches) : no. of available seats 
           ]
        nonAc = [
                    [list of sleeper],
                    [list of sitting coaches]
                ]      

    '''
    def __init__(self,tName,tNum,tType,viaCities,days,coachesMetaData):
        self.trainName = tName
        self.trainNumber = int(tNum)
        # self.src = None
        # self.dest = None
        self.trainType = tType
        self.viaCities = viaCities
        self.days = days
        self.coachesMetaData = coachesMetaData
        self.coaches = self.createCoaches()

    def setRoute(self,*cities):
        # self.src = cities[0]
        # self.dest = cities[-1]
        self.viaCities = list(cities)

    def setDays(self,days):
        '''
            input type days should be string
            contains day num
            like
            1 -> sunday
            2 ->  monday
            ..
            7 -> saturday
            days should be like 1457
            1457 means train is running on
            sunday wednesday thursday saturday
        '''
        days = (int(x) for x in set(list(days)))

        for i in range(1,8):
            if i in days:
                self.days[i] = True
            else:
                self.days[i] = False

    def setCoaches(self):
        '''

            Coaches
            AC
                I AC coach
                II AC coach
                III AC coach
            NON-AC
                sleeper
                # sitting
        ac=[
                (list of IAC coaches) : no. of available seats,
                (list of IIAC coaches) : no. of available seats,
                (list of IIIAC coaches) : no. of available seats
           ]
        nonAc = [
                    [list of sleeper],
                    # [list of sitting coaches]
                ]

        '''
        #AC I
        ac1CoachesNum = int(input("Enter Number of ACI coaches"))
        ac1SeatPerCoach = 0
        if ac1CoachesNum > 0:
            ac1SeatPerCoach = int(input("Enter seats in ACI per coach"))
            if ac1SeatPerCoach < 1:
                ac1CoachesNum =0
                ac1SeatPerCoach = 0
        else:
            ac1CoachesNum = 0

        #AC II
        ac2CoachesNum = int(input("Enter Number of ACII coaches"))
        ac2SeatPerCoach = 0
        if ac2CoachesNum > 0:
            ac2SeatPerCoach = int(input("Enter seats in ACII per coach"))
            if ac2SeatPerCoach < 1:
                ac2CoachesNum = 0
                ac2SeatPerCoach = 0
        else:
            aciiCoachesNum = 0

        # AC III
        ac3CoachesNum = int(input("Enter Number of ACII coaches"))
        ac3SeatPerCoach = 0
        if aciiCoachesNum > 0:
            ac3SeatPerCoach = int(input("Enter seats in ACII per coach"))
            if ac3SeatPerCoach < 1:
                ac3CoachesNum = 0
                ac3SeatPerCoach = 0
        else:
            ac3CoachesNum = 0

        # sleeper
        sleeperCoachesNum = int(input("Enter Number of ACII coaches"))
        sleeperSeatPerCoach = 0
        if sleeperCoachesNum > 0:
            sleeperSeatPerCoach = int(input("Enter seats in ACII per coach"))
            if ac3SeatPerCoach < 1:
                sleeperCoachesNum = 0
                sleeperSeatPerCoach = 0
        else:
            sleeperCoachesNum = 0

        self.coachesMetaData = ((ac1CoachesNum,ac1SeatPerCoach),
                        (ac2CoachesNum,ac2SeatPerCoach),
                        (ac3CoachesNum,ac3SeatPerCoach),
                        (sleeperCoachesNum,sleeperSeatPerCoach))

        self.createCoaches()


    def createCoaches(self):
        ac1 = self.coachesMetaData[0]
        ac2 = self.coachesMetaData[1]
        ac3 = self.coachesMetaData[2]
        sleeper = self.coachesMetaData[3]

        if ac1[0]:
            self.coaches['ac1'] = self._createCoach(ac1[0],'ACI',ac1[1])


        if ac2[0]:
            self.coaches['ac2'] = self._createCoach(ac2[0],'ACII',ac2[1])


        if ac3[0]:
            self.coaches['ac3'] = self._createCoach(ac3[0],'ACIII',ac3[1])


        if sleeper:
            self.coaches['sleeper'] = self._createCoach(sleeper[0],'SLEEPER',sleeper[1])



    def _createCoach(self,numofCoaches,type,numOfSeats):
        coaches = (coach(type,numOfSeats) for i in range(numofCoaches))

    # def bookTicket(self,Type,numOfTickets):