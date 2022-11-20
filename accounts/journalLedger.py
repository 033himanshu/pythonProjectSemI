from date import date


class transaction:
    def __init__(self, account, date, amount, typ, note):
        self.account = account
        self.date = date
        self.amount = amount
        self.typ = typ
        self.note = note

    @classmethod
    def isAmountValid(cls, amount):
        if not amount.isnumeric():
            return False
        amount = int(amount)
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
            fullName += ' ' + self.mName
        if self.lName:
            fullName += ' ' + self.lName
        return fullName

    def __repr__(self):
        return f"account({self.getFullName()})"


# ------------------------------------------------


def createAccount(name):
    name = name.split()
    # name = (n.capitalize() for n in name)
    acnt = account(*name)
    return acnt


acc = {
    # 'name' : None
}

trans = [
    # tuple(account,transaction)
]

def beautifyName(name):
    name = name.split()
    return " ".join(n.capitalize() for n in name)

# cash = createAccount('cash')
def createEntry(name, trAcName, dt, amount, typ, note):
    global acc
    global trans

    name = beautifyName(name)
    trAcName = beautifyName(trAcName)

    acnt = acc.get(name)
    if not acnt:
        acnt = createAccount(name)
        acc[acnt.getFullName()] = acnt

    acnt1 = acc.get(trAcName)
    if not acnt1:
        acnt1 = createAccount(trAcName)
        acc[trAcName] = acnt1

    dt = date(*dt)
    tran = transaction(acnt1, dt, amount, typ, note)
    acnt._addTransaction(tran)
    return (acnt, tran)


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
        amount = input("Enter Amount of Transaction : ")
        if transaction.isAmountValid(amount):
            amount = int(amount)
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

    tran = None
    if typ == 'dr':
        tran = createEntry(name, 'cash', dt, amount, typ, note)
        createEntry('cash', name, dt, amount, 'cr', note)
    else:
        tran = createEntry('cash', name, dt, amount, 'dr', note)
        createEntry(name, 'cash', dt, amount, typ, note)

    trans.append(tran)


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
    print()
    print("1 -> insert entry ")
    print("2 -> show Journal ")
    print("3 -> show Ledger ")
    # print("4 -> Do Nothing ")


def showLedger():

    # assign data

    for acName in acc.keys():
        print()
        acnt = acc[acName]
        from tabulate import tabulate
        print(f"--------Ledger {acName} A/C--------")
        head = ["Date", "Particulars", "Debit", "", "Date", "Particulars", "Credit"]
        mydata = [
            # [f"{'cr.date'}", f"{'crAccount'}", f"{'cramount'}","", f"{'dr.date'}", f"{'drAccount'}", f"{'dramount'}"]
        ]
        trans = sorted(acnt._transaction, key=lambda tr: tr.date)

        crTrans = tuple(tran for tran in trans if tran.typ == 'cr')
        drTrans = tuple(tran for tran in trans if tran.typ == 'dr')
        drSum = crSum = 0
        for tran in drTrans:
            dt = tran.date.getDateWithDifferentFormat('%M %d , %y')
            ac = f"To {tran.account.getFullName()} A/C\n({tran.note})"
            amt = f"{tran.amount}"
            drSum += tran.amount
            mydata.append([dt, ac, amt, "", "", "", ""])

        i = 0
        while i < len(drTrans) and i < len(crTrans):
            dt = crTrans[i].date.getDateWithDifferentFormat('%M %d , %y')
            ac = f"By {crTrans[i].account.getFullName()} A/C\n({crTrans[i].note})"
            amt = f"{crTrans[i].amount}"
            crSum += crTrans[i].amount
            mydata[i][4] = dt
            mydata[i][5] = ac
            mydata[i][6] = amt
            i += 1

        while i < len(crTrans):
            dt = crTrans[i].date.getDateWithDifferentFormat('%M %d , %y')
            ac = f"By {crTrans[i].account.getFullName()} A/C"
            if crTrans[i].note:
                ac += f"\n({crTrans[i].note})"
            amt = f"{crTrans[i].amount}"
            crSum += crTrans[i].amount
            mydata.append(["", "", "", "", dt, ac, amt])
            i+=1

        mydata.append(["", "Total", f"{drSum}", "", "", "Total", f"{crSum}"])

        print(tabulate(mydata, headers=head, tablefmt="grid"))
        print()


def showJournal():
    print()
    from tabulate import tabulate
    # assign data
    head = ["Date", "Particulars", "Debit", "Credit"]
    mydata = [
        # [f"{'date'}", f"{'Purchase'} A/C DR. \n    To {'Cash'} A/C\n({'Note'})", f"{'amount'}", f"\n{'amount'}"]
    ]
    crSum = 0
    drSum = 0
    print("--------Printing Journal--------")
    for ac, tr in trans:
        # drAc,drTr = trans[i]
        # crAc,crTr = trans[i+1]
        # i+=2
        # trans ->  tuple(account,transaction)
        dt = tr.date.getDateWithDifferentFormat('%M %d , %y')
        part = f"{ac.getFullName()} A/C DR. \n    To {tr.account.getFullName()} A/C"
        if tr.note:
            part += f"\n({tr.note})"

        debit = tr.amount
        drSum += debit
        credit = tr.amount
        crSum += credit
        credit = f"\n{credit}"

        entry = [dt, part, debit, credit]

        mydata.append(entry)
    entry = ["", "Total", drSum, crSum]
    mydata.append((entry))
    # create header

    # display table
    print(tabulate(mydata, headers=head, tablefmt="grid"))
    print()