from user import user
from train import train
from coach import coach
from date import date

class ticket:
     def __init__(self,date,train,coach,seatNum,user,src,dest):
         self.date = date
         self.train = train
         self.coach = coach
         self.seatNum = seatNum
         self.user = user
         self.src = src
         self.dest = dest