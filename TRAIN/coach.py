from user import user
class coach:
    '''
        type 
        no. of seats
        reservedSeats =[ 
                {seatNo : user},
              ]
        vacantSeats = [] 
    '''
    def __init__(self,type,nSeats):
        self.type = type
        self.nSeats = nSeats
        self.reservedSeats = [None for x in range(0,self.nSeats)]
        self.vacantSeats = [x for x in range(1,self.nSeats + 1)]

    def checkAvailability(self):
        if len(self.vacantSeats):
            return True
        return False
    def reserve(self,usr):
        self.reservedSeats[self.vacantSeats[0] -1] = usr
        seatNumber = self.vacantSeats[0]
        self.vacantSeats = self.vacantSeats[1:]
        return seatNumber

