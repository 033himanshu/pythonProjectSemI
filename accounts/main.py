from journalLedger import *
initialize()
#-----------------------------------Main Starts from Here-----------------------------#
ch = "go"
while ch:
    showMenu()
    choi = input("Enter Your choice : ")
    doOperation(choi)
    ch = input("Press Any Key + Enter to continue or Press Enter to Stop : ")

showJournal()
showLedger()

 #-----------------------------------Main End Here-----------------------------#
