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

    def __init__(self, tName, tNum, tType, viaCities, days, coachesMetaData):
        '''
            # return train(tData['trainName'],tNum,tData['trainType'],)
        data =     ('trainNumber' , {
                'trainName'       : 'trainName',
                'trainType'       : 'trainType',
                'viaCities'       : '(*cities)',
                'days'            : '(True,False,--)',
                'coachesMetaData' : '((coachType,seatsPerCoach),...)'
            })
        '''
        self.trainName = tName
        self.trainNumber = tNum
        # self.src = None
        # self.dest = None
        self.trainType = tType
        self.viaCities = viaCities
        self.days = days
        self.coachesMetaData = coachesMetaData
        self.coaches = None
        self._createCoaches()

    def _createCoaches(self):
        print(self.coachesMetaData)
        ac1 = self.coachesMetaData[0]
        ac2 = self.coachesMetaData[1]
        ac3 = self.coachesMetaData[2]
        sleeper = self.coachesMetaData[3]
        sitting = self.coachesMetaData[4]
        self.coaches = dict()
        if ac1[0]:
            self.coaches['ac1'] = self._createCoach(ac1[0], 'ACI', ac1[1])

        if ac2[0]:
            self.coaches['ac2'] = self._createCoach(ac2[0], 'ACII', ac2[1])

        if ac3[0]:
            self.coaches['ac3'] = self._createCoach(ac3[0], 'ACIII', ac3[1])

        if sleeper:
            self.coaches['sleeper'] = self._createCoach(sleeper[0], 'SLEEPER', sleeper[1])

        if sitting:
            self.coaches['sitting'] = self._createCoach(sitting[0], 'SITTING', sitting[1])

    def _createCoach(self, numofCoaches, type, numOfSeats):
        return tuple(coach(type, numOfSeats,f"{type}{i+1}") for i in range(numofCoaches))

    @classmethod
    def isTrainNameValid(cls, name):
        for n in name.split():
            if not n.isalpha():
                return False
        return True

    @classmethod
    def isTrainNumValid(cls, trainNum):
        if len(str(trainNum)) < 5:
            return False
        return True

    @classmethod
    def isTrainTypeValid(cls, trainType):
        if trainType in ['exp', 'supexp', 'shatabdi', 'rajdhani']:
            return True
        return False

    def findAvialableSeats(self,coachType):
        return sum(sum(l for l in coch.vacantSeats) for coch in self.coaches[coachType])

    def  book(self,coachType,user):
        for coach in self.coaches[coachType]:
            if len(coach.vacantSeats):
                seatNum = coach.reserve(user)
                return (coach,seatNum)