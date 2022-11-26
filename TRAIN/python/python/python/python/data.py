'''
trains
{
    date : train
}
to implement findMyTicket
tickets
{
    date(d/m/y)trainNumber : [ticket,....]
}
scheduledTrains = {
    date : ('trainNum' : trainObject ,.......)
}
'''
PNRs = dict()
# PNRs = { 'pnr' : ticket}
tickets =dict()
#tickets = {date()trainNum : [pnr]}
scheduledTrains = dict()
# trains = {
#             # 'trainNumber' : {
#             #
#             #     'trainName'       : 'trainName',
#             #     'trainType'       : 'trainType',
#             #     'viaCities'       : '(*cities)',
#             #     'days'            : '(True,False,--)',
#             #     'coachesMetaData' : '((coachType,seatsPerCoach),...)'
#             # }
#         }
trains = dict()
1


def pickleScheduledTrains():
    global scheduledTrains
    import pickle
    with open('scheduledTrains.pickle', 'wb') as file:
        pickle.dump(scheduledTrains, file)

def unpickleScheduledTrains():
    global scheduledTrains
    import pickle
    try:
        with open('scheduledTrains.pickle','rb') as file:
            scheduledTrains = pickle.load(file)
    except:
        print("Server Not Found")

def pickleTrains():
    global trains
    import pickle
    with open('trains.pickle','wb') as file:
        pickle.dump(trains,file)


def unpickleTrains():
    global trains
    import pickle
    try:
        with open('trains.pickle','rb') as file:
            trains = pickle.load(file)
    except:
        print("Server Not Found")

def pickleTickets():
    global tickets
    import pickle
    with open('tickets.pickle','wb') as file:
        pickle.dump(tickets,file)


def unpickleTickets():
    global tickets
    import pickle
    try:
        with open('tickets.pickle','rb') as file:
            tickets = pickle.load(file)
    except:
        print("Server Not Found")


def picklePNRs():
    global PNRs
    import pickle
    with open('PNRs.pickle','wb') as file:
        pickle.dump(PNRs,file)

def unpicklePNRs():
    global PNRs
    import pickle
    try:
        with open('PNRs.pickle','rb') as file:
            PNRs = pickle.load(file)
    except:
        print("Server Not Found")

def isScheduledTrainThere(date,trainNum):
    if scheduledTrains.get(date):
        if trainNum in scheduledTrains[date].keys():
            return True
    return False