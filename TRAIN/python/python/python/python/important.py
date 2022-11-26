'''
{
    name
    age
    contactNo
    emailid
}
'''
from date import date
from train import train
import data
from ticket import ticket
from user import user

_admin = {'username': 'admin', 'pswd': '*****'}


def checkCredentials(usr, pswd):
    return usr == _admin['username'] and pswd == _admin['pswd']


# import data
def createTrain(usr, pswd):
    if checkCredentials(usr, pswd):
        trainName = trainNum = trainType = viaCities = days = coachMetaData = None
        while True:
            trainNum = input("Enter Train Number : ")
            if train.isTrainNumValid(trainNum):
                print(data.trains)
                if data.trains.get(trainNum):
                    print("Train already Exists with the Same Number")
                    return
                break
            else:
                print("Enter Valid Train Number")
        while True:
            trainName = input("Enter Train Name : ").lower()
            if train.isTrainNameValid(trainName):
                break
            else:
                print("Enter Valid Train Name")
        while True:
            trainType = input("Enter Train Type (Express / superfast Express) : ").lower()
            trainType = trainType.lower()
            if train.isTrainTypeValid(trainType):
                break
            else:
                print("Enter A Valid Train Type")
        while True:
            viaCities = setRoute()
            if len(viaCities) < 2:
                print("Please Enter a Valid Route")
            else:
                break

        days = setDays()
        coachMetaData = setMetaData()
        data.trains[f'{trainNum}'] = {
            'trainName': trainName,
            'trainType': trainType,
            'viaCities': viaCities,
            'days': days,
            'coachesMetaData': coachMetaData
        }
    else:
        print("Wrong Credentials")


def setRoute():
    city = input("Enter Source Station of Train : ").lower()
    cities = []
    while city:
        cities.append(city)
        city = input("Enter Another City to stop press Enter : ").lower()
    return tuple(cities)


def setDays():
    days = {'Sunday': False, 'Monday': False, 'Tuesday': False, 'Wednesday': False, 'Thursday': False, 'Friday': False,
            'Saturday': False}
    for i in days.keys():
        ch = input(f"is Train Run on {i} press (y/n) : ")
        days[i] = ch[0] in 'Yy'
    return days


def setMetaData():
    ac1 = setCoachDetail('AC-I')
    ac2 = setCoachDetail('AC-II')
    ac3 = setCoachDetail('AC-III')
    sleeper = setCoachDetail('sleeper')
    sitting = setCoachDetail('sitting')

    return (ac1, ac2, ac3, sleeper, sitting)


def setCoachDetail(coachType):
    coachNum = int(input(f"Enter Number of {coachType} coaches : "))
    seatPerCoach = 0
    if coachNum > 0:
        seatPerCoach = int(input(f"Enter seats in {coachType} per coach : s"))
        if seatPerCoach < 1:
            coachNum = 0
            seatPerCoach = 0
    else:
        coachNum = 0
    return (coachNum, seatPerCoach)


# ----------------For Main Function ------------------------#


def adminMenu():
    print("1 -> Create New Train ")
    print("2 -> Show All Trains ")
    print("-1 -> For Return to Main Menu")


def adminLogin():
    print("Enter Your Credentials Below")
    userName = input("Enter UserName : ")
    pswd = input("Enter Password : ")
    if checkCredentials(userName, pswd):
        adminMenu()
        ch = int(input("Enter Choice : "))
        if ch == -1:
            return
        elif ch == 1:
            createTrain(userName, pswd)
            data.pickleTrains()
        elif ch == 2:
            showAllTrains()
        else:
            print("Invalid Input :{")
    else:
        print("Wrong Credentials :{")


def stationIndex(trainNum, station):
    return data.trains[trainNum]['viaCities'].index(station)


def findTrain(src, dest='', availableTrains=[]):
    if not dest:
        for tNum, tr in data.trains.items():
            if src in (tr['viaCities'][0:len(tr['viaCities']) - 1]):
                availableTrains.append(tNum)
    if dest and availableTrains:
        for trn in availableTrains:
            srcIdx = stationIndex(trn, src)
            if not dest in data.trains[trn]['viaCities'][srcIdx:]:
                availableTrains.remove(trn)
    print(availableTrains)
    return availableTrains


def checkTrainForDate(availTrains, dt):
    day = dt.getDayName()
    availableWithDate = []
    for tr in availTrains:
        print(f"{tr} : {day} :{data.trains[tr]['days'][day]}")
        if data.trains[tr]['days'][day]:
            availableWithDate.append(tr)
    return availableWithDate


def route(trn, src, dest):
    srcIdx = stationIndex(trn, src)
    dest = stationIndex(trn, dest)
    return " --> ".join(data.trains[trn]['viaCities'][srcIdx:dest + 1])


def giveChoices(dt, trns, src, dest, i=0):
    if trns:
        # show avialable trains
        j = 1
        for trn in trns:
            print()
            s = f"{i}.{j}"
            if i == 0:
                s = j
            print(f"Press {s} -> {dt}\n\t{trn}: {data.trains[trn]['trainName']}\n\t\tRoute : {route(trn, src, dest)}")
            j += 1
        print()


def chooseTrain():
    src = input("Enter your Source Station : ").lower()
    availTrains = findTrain(src)
    dest = None
    if availTrains:
        dest = input("Enter Destination Station : ").lower()
        availTrains = findTrain(src, dest, availTrains)
        if not availTrains:
            print("No Train Available At destination Station")
            ch = input("Want to Try For Another (y/n) : ")
            if ch[0] in 'Yy':
                bookTicket()
            return
    else:
        print("No Train Available At Source Station")
        ch = input("Want to Try For Another (y/n) : ")
        if ch[0] in 'Yy':
            bookTicket()
        return
    dt = None
    if availTrains:
        while True:
            dt = input("Enter date formate(d/m/y) ie <23/4/2022> : ")
            dt = tuple(int(x) for x in dt.split('/'))
            if not date.isValidDate(*dt):
                print("Date is not valid Try Again")
            else:
                dt = date(*dt)
                diff = dt.getDifferenceInDays(date())
                if (diff < 0):
                    print(f"{dt} Already Passed {':{'}")
                    print(f"date set to current date")
                    ch = input("Do you Want to continue (y/n): ")
                    if not ch in "Yy":
                        return
                    dt = date()
                    break
                # check if date is not passed already
                else:
                    break
    avialTrainsWithDate = checkTrainForDate(availTrains, dt)
    print(avialTrainsWithDate)
    if not avialTrainsWithDate:
        print(f"Train is not avialable on Date: {dt.day}/{dt.month}/{dt.year} ")
        trainsInWeek = [(dt.getDateXDaysAfter(x), checkTrainForDate(availTrains, dt.getDateXDaysAfter(x))) for x in
                        range(1, 8)]
        trainsInWeek = [t for t in trainsInWeek if t[1]]
        # show available trains next 7 days
        i = 1
        for dt, trns in trainsInWeek:
            giveChoices(dt, trns, src, dest, i)
            i += 1
        while True:
            ch = input("Enter you choice : ")
            ch = [int(x) for x in ch.split('.')[:2]]
            if ch[0] > 0 and ch[0] <= len(trainsInWeek) and ch[1] > 0 and ch[1] <= len(trainsInWeek[ch[0] - 1][1]):
                return (src, dest, dt, trainsInWeek[ch[0] - 1][1][ch[1] - 1])
            else:
                print("Invalid Input :{")
    else:
        giveChoices(dt, avialTrainsWithDate, src, dest)
        while True:
            ch = int(input("Enter you choice : "))
            if ch > 0 and ch <= len(avialTrainsWithDate):
                return (src, dest, dt, avialTrainsWithDate[ch - 1])
            else:
                print("Invalid Input :{")


def newTrain(trainNum):
    # (tName, tNum, tType, viaCities, days, coachesMetaData)
    tName = data.trains[trainNum]['trainName']
    tNum = trainNum
    tType = data.trains[trainNum]['trainType']
    viaCities = data.trains[trainNum]['viaCities']
    days = data.trains[trainNum]['days']
    coachesMetaData = data.trains[trainNum]['coachesMetaData']
    return train(tName, tNum, tType, viaCities, days, coachesMetaData)


def chooseCoachType(train):
    i = 1
    print(train)
    print(train.coaches)
    for coach in train.coaches.keys():
        if type:
            print(f"{i} -> {coach}")
        i += 1
    ch = 1
    while True:
        ch = int(input("Enter Your choice : "))
        if not (ch > 0 and ch < i):
            print("Invalid Input")
        else:
            break

    return list(train.coaches.keys())[ch - 1]


def setCoachTypeAndSeats(train):
    print(train)
    coachType = chooseCoachType(train)
    while True:
        sReq = int(input("Enter No. of Seats You need : "))
        if sReq < 1:
            print("Please Enter Valid Number of Seats :{")
        avlSeats = train.findAvialableSeats(coachType)
        if avlSeats < sReq:
            print(f"only {avlSeats} are Available in {coachType} {':{'}")
            print("1 -> change Coach Type")
            print("2 -> change number of seats")
            print("else for return back to main menu")
            ch = int(input("Enter Your Choice : "))
            if ch == 1:
                coachType = chooseCoachType(train)
            elif ch == 2:
                continue
            else:
                return
        else:
            return (coachType, sReq)


def newUser(i):
    while True:
        name = input(f"Enter Name of Passenger {i + 1}: ")
        name = name.capitalize()
        if not user.isNameValid(name):
            print("Enter a Valid Name :{")
        else:
            break

    while True:
        age = int(input(f"Enter age : "))
        if not user.isAgeValid(age):
            print("Enter a Valid age :{")
        else:
            break

    return user(name, age)


def printTickets(tickets):
    i = 1
    with open('currentTicket.txt', 'w') as file:
        for pnr,ticket in tickets:
            print()
            print(f"{i}\n  PNR : {pnr}")
            print(f"\n\tName : {ticket.user.name}")
            print(f"\t{ticket.date}")
            print(f"\t{ticket.train.trainNumber} {ticket.train.trainName} {ticket.train.trainType}")
            print(f"\tSource : {ticket.src} \t Destination : {ticket.dest}")
            print(f"\t{ticket.coach.name} {ticket.seatNum}")
            file.write(f"{i}\n  PNR : {pnr}\n")
            file.write(f"\n\tName : {ticket.user.name}\n")
            file.write(f"\t{ticket.date}\n")
            file.write(f"\t{ticket.train.trainNumber} {ticket.train.trainName} {ticket.train.trainType}\n")
            file.write(f"\tSource : {ticket.src} \t Destination : {ticket.dest}\n")
            file.write(f"\t{ticket.coach.name} {ticket.seatNum}\n\n")
            i += 1
        print()

def bookTicket():
    train = chooseTrain()
    print(train)
    # (src, dest, date, trainNumber)
    myTrain = None
    isTrainScheduled = True
    if data.isScheduledTrainThere(str(train[2]), train[3]):
        myTrain = data.scheduledTrains[str(train[2])][train[3]]
    else:
        myTrain = newTrain(train[3])
        isTrainScheduled = False
    print(myTrain)
    coachTypeAndSeats = setCoachTypeAndSeats(myTrain)
    if not coachTypeAndSeats:
        return
    coachType, seats = coachTypeAndSeats
    tickets = []
    for i in range(seats):
        user = newUser(i)
        coach, seatNum = myTrain.book(coachType, user)
        tckt = ticket(train[2], myTrain, coach, seatNum, user, train[0], train[1])
        while True:
            import uuid
            pnr = str(uuid.uuid4().hex[:10])
            if not pnr in data.PNRs.keys():
                break
        tickets.append((pnr,tckt))
        data.PNRs[pnr] = tckt

    if not isTrainScheduled:
        data.scheduledTrains[str(train[2])] = dict()
        data.scheduledTrains[str(train[2])][train[3]] = myTrain

    else:
        data.scheduledTrains[str(train[2])][train[3]] = myTrain

    data.pickleScheduledTrains()
    tic = data.tickets.get(f'{str(train[2])}{train[3]}')
    if tic:
        data.tickets[f'{str(train[2])}{train[3]}'].extend([pnr for pnr,t in tickets])
    else:
        data.tickets[f'{str(train[2])}{train[3]}'] = [pnr for pnr,t in tickets]
    data.pickleTickets()
    data.picklePNRs()
    printTickets(tickets)


def searchTicket():
    pnr = input("Enter PNR No. : ")
    ticket = data.PNRs.get(pnr)
    if not ticket:
        print("PNR Not Exists")
    else:
        printTickets([(pnr,ticket)])


def showMenu():
    print("1 -> Admin Login")
    print("2 -> Book Ticket")
    print("3 -> Search For Ticket")
    print("-1 -> Close The Window")


def performOperation(ch):
    if ch == 1:
        adminLogin()
    elif ch == 2:
        bookTicket()
    elif ch == 3:
        searchTicket()

    else:
        print("Invalid Input :{")


def initialize():
    data.unpickleTrains()
    data.unpickleScheduledTrains()
    data.unpicklePNRs()
    data.unpickleTickets()


def showAllTrains():
    for trNum, trData in data.trains.items():
        print()
        print(f"{trNum} : {trData['trainName']} {trData['trainType']}")
        print(f"\tRoute : {route(trNum, trData['viaCities'][0], trData['viaCities'][-1])}")
        print(f"\tDays : {', '.join(day for day in trData['days'].keys() if trData['days'][day])}")
    print()
