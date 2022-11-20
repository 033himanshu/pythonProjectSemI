'''
main(){

    showTrains()
    bookTicket()

}
showTrains(){

}
bookTicket(){
    takeDate check it should be current or future date
    find train on currentDayName
    select 1 of the train
        show available seats in AC and Sleepers
    select 1 of the type from ac or sleeper or sitting
    take no. of tickets
        if seats available
            book train 1 by 1 and return a list of
            [
                 Ticket //{user : (date,train,coach,seatNo)}
                    // returning PNR

            ]

    findMyTicket(){
        date of travelling
        contact no

    }
    getDetailsUsingPNR(){

    }

}
'''




base = {1,2,3,4,5,6,7,8,9}
st = '71432'
l = ['132','195','164','285','312','396','375','465','645','714','735','798','915','936','978','825']
for i in range(len(st)-3):
    s = st[i:i+3]
    if s in l:
        t = tuple(base - {int(x) for x in st})
        st = st[:i+2]+str(t[0])+st[i+3:]
print(st)
