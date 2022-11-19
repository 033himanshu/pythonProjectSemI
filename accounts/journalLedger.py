from date import date


class transaction:
    def __init__(self, date, amount, typ, note):
        self.date = date
        self.amount = amount
        self.typ = typ
        self.note = note

    @classmethod
    def isAmountValid(cls, amount):
        if amount <= 0:
            return False
        return True

    @classmethod
    def isTypeValid(cls, typ):
        if typ == 'cr' or typ == 'dr':
            return True
        return False

    def __repr__(self):
        return f"transaction({self.date}  {self.amount} {self.typ})"


class account:

    def __init__(self, fName, lName='', mName=''):
        self.fName = fName
        self.mName = mName
        self.lName = lName
        self._transaction = []

    def _addTransaction(self, transaction):
        self._transaction.append(transaction)

    @classmethod
    def isNameValid(cls, name):
        name = name.split()
        if len(name) > 3 or len(name) == 0:
            return False
        for n in name:
            if not n.isalpha():
                return False
        return True

    def getFullName(self):
        fullName = self.fName
        if self.mName:
            fullName += ' '+ self.mName
        if self.lName:
            fullName += ' '+self.lName
        return fullName

    def __repr__(self):
        return f"account({self.getFullName()})"


#------------------------------------------------



def createAccount(name):
    name = name.split()
    name = (n.capitalize() for n in name)
    acnt = account(*name)
    return acnt

acc = {
    # 'name' : None
}

trans = [
    # tuple(account,transaction)
]
# cash = createAccount('cash')
def createEntry(name, dt, amount, typ, note):
    global acc
    global trans
    acnt = acc.get(name)
    if acnt:
        pass
    else:
        acnt = createAccount(name)
        acc[name] = acnt

    dt = date(*dt)
    tran = transaction(dt, amount, typ, note)
    acnt._addTransaction(tran)
    trans.append((acnt, tran))


def takeEntry():
    name = dt = amount = typ = None
    # name Entry
    while True:
        name = input("Enter Name of Account : ")
        name = name.lower()
        if account.isNameValid(name):
            break
        else:
            print("Please Enter a  Valid Name")

    # date Entry
    while True:
        dt = input("Enter date of Transaction formate<21/11/2022> : ")
        dt = dt.split('/')
        if date.isValidDate(*dt):
            break
        else:
            print("Please Enter a  Valid Date")

    # amount Entry
    while True:
        amount = int(input("Enter Amount of Transaction : "))
        if transaction.isAmountValid(amount):
            break
        else:
            print("Please Enter a  Valid Amount")

    # type Entry
    while True:
        typ = input("Enter Type of Transaction cr -> credit and dr -> debit: ")
        typ = typ.lower()
        if transaction.isTypeValid(typ):
            break
        else:
            print("Please Enter a  Valid Type")

    note = input("Note about transaction(optional) : ")


    if typ == 'dr':
        createEntry(name, dt, amount, typ, note)
        createEntry('case', dt, amount, 'cr', note)
    else:
        createEntry('case', dt, amount, 'dr', note)
        createEntry(name, dt, amount, typ, note)



def doOperation(ch):
    if ch == '1':
        takeEntry()

    elif ch == '2':
        showJournal()

    elif ch == '3':
        showLedger()

    else:
        print("Invalid input")


def showMenu():
    print("1 -> insert entry ")
    print("2 -> show Journal ")
    print("3 -> show Ledger ")
    # print("4 -> Do Nothing ")


def showLedger():
    print("Ledger")


def showJournal():
    from tabulate import tabulate
    # assign data
    head = ["Date", "Particulars", "Debit", "Credit"]
    mydata = [
       # [f"{'date'}", f"{'Purchase'} A/C DR. \n    To {'Cash'} A/C\n({'Note'})", f"{'amount'}", f"\n{'amount'}"]
    ]
    crSum =0
    drSum = 0
    i=0
    print("--------Printing Journal--------")
    while i<len(trans):
        drAc,drTr = trans[i]
        crAc,crTr = trans[i+1]
        i+=2
        #trans ->  tuple(account,transaction)
        dt = drTr.date.getDateWithDifferentFormat('%M %d , %y')
        part = f"{drAc.getFullName()} A/C DR. \n    To {crAc.getFullName()} A/C"
        if drTr.note:
            part += f"\n({drTr.note})"

        debit = drTr.amount
        drSum += debit
        credit = crTr.amount
        crSum += credit
        credit = f"\n{credit}"

        entry = [dt,part,debit,credit]

        mydata.append(entry)
    entry = ["","Total",drSum,crSum]
    mydata.append((entry))
    # create header


    # display table
    print(tabulate(mydata, headers=head, tablefmt="grid"))
