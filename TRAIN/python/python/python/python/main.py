import data
import important
print("******** Welcome To Railways ********")
important.initialize()
print(data.tickets)
print(data.scheduledTrains)
while True:
    important.showMenu()
    ch = int(input("Enter Your Choice : "))
    if ch == -1:
        break
    important.performOperation(ch)

print("******** Thank You ********")
