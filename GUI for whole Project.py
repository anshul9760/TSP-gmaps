from tkinter import *

r = tk.Tk() 
r.title('TSP Timetable') 
r.geometry("400x300")
Label(r, text='Choose Preferred Mode').grid(row=1)
var1 = IntVar() 
Checkbutton(r, text='Go Offline', variable=var1).grid(row=3, sticky=W) 
var2 = IntVar() 
Checkbutton(r, text='Go Online', variable=var2).grid(row=4, sticky=W)
Label(r, text='Enter API key').grid(row=5)
e1 = Entry(r) 
e1.grid(row=5, column=1) 
ourMessage ='Make sure you are online for online mode!'
messageVar = Message(r, text = ourMessage)
messageVar.config(bg='lightgreen')
messageVar.grid(row=6)
Label(r, text='       ').grid(row=7)
button = tk.Button(r, text='Proceed', width=25, command=new_winF).grid(row=8)

def new_winF(): # new window definition
    newwin = Toplevel(r)
    display = Label(newwin, text="Humm, see a new window !")
    display.pack()  
    
r.mainloop()



from tkinter import *
s=" 0 -> 13 -> 30 -> 46 -> 43 -> 44 -> 32 -> 45 -> 33 -> 42 -> 29 -> 41 -> 28 -> 58 -> 68 -> 59 -> 60 -> 61 -> 57 -> 56 -> 67 -> 84 -> 71 -> 72 -> 77 -> 78 -> 66 -> 55 -> 35 -> 49 -> 39 -> 25 -> 26 -> 16 -> 17 -> 11 -> 4 -> 19 -> 18 -> 10 -> 20 -> 54 -> 53 -> 52 -> 50 -> 51 -> 36 -> 9 -> 21 -> 22 -> 5 -> 6 -> 7 -> 8 -> 37 -> 83 -> 79 -> 91 -> 88 -> 75 -> 87 -> 89 -> 109 -> 110 -> 101 -> 100 -> 65 -> 38 -> 64 -> 62 -> 74 -> 86 -> 85 -> 97 -> 103 -> 73 -> 96 -> 102 -> 105 -> 63 -> 124 -> 131 -> 130 -> 122 -> 24 -> 133 -> 132 -> 123 -> 114 -> 113 -> 104 -> 48 -> 95 -> 70 -> 92 -> 82 -> 93 -> 81 -> 69 -> 80 -> 94 -> 23 -> 119 -> 111 -> 126 -> 138 -> 139 -> 120 -> 125 -> 128 -> 118 -> 117 -> 121 -> 137 -> 136 -> 135 -> 134 -> 129 -> 115 -> 112 -> 98 -> 99 -> 127 -> 107 -> 108 -> 116 -> 106 -> 90 -> 76 -> 40 -> 34 -> 15 -> 27 -> 14 -> 12 -> 2 -> 3 -> 47 -> 1 -> 31 -> 0"

import pandas as pd
import datetime
lj=[]
def timek():
    day=1
    z='DAY'
    r=420
    ty="Day "+str(day)
    lj.append(ty)
    for i,e,k in zip(x[1],l,timespent):
        if r<limit:
            zk=round((r/60),2)
            if zk<12:
                a='AM'
                time=str(datetime.timedelta(hours=zk)).rsplit(':', 1)[0]
                ty=str(time)+" AM:"+str(majorlist[int(i)])
                lj.append(ty)
            else:
                a='PM'
                time=str(datetime.timedelta(hours=(zk-12))).rsplit(':', 1)[0]
                ty=str(time)+" PM:"+str(majorlist[int(i)])
                lj.append(ty)
            r=r+e+k
        else:
            r=420
            day+=1
            ty="Day "+str(day)
            lj.append(ty)
            zk=round((r/60),2)
            if zk<12:
                a='AM'
                time=str(datetime.timedelta(hours=zk)).rsplit(':', 1)[0]
                ty=str(time)+" AM:"+str(majorlist[int(i)])
                lj.append(ty)
            else:
                a='PM'
                time=str(datetime.timedelta(hours=(zk-12))).rsplit(':', 1)[0]
                ty=str(time)+" PM:"+str(majorlist[int(i)])
                lj.append(ty)
            r=r+e+k

temppath=r # Same address as before
majorlist=[]
filename1=temppath+ #original CSV file
data=pd.read_csv(filename1)
y=data.shape
z=data.columns
majorlist=[]

for i in range(y[0]):
    k=str(data.iloc[:,1][i])+" ,Maharashtra , "+str(data.iloc[:,2][i])
    majorlist.append(k)

majorlist

s=s.replace(" -> "," ")
s=s.split()


df=pd.read_csv('tq.csv')
rt=df.as_matrix()
r=list(rt)
for i in range(len(r)):
    r[i]=list(r[i])
timematrix=r

x=[]
x.append(1690)
x.append(s)

l=[]
for i in range(len(timematrix[0])-1):
    l.append(timematrix[int(x[1][i])][int(x[1][i+1])])

timespent=[]
for i in range(len(majorlist)):
    timespent.append(94)

start=7
end=9
limit=((end+12)-start)*60+480
value=sum(l)+(30*len(s))
r = Tk()
r.title('TSP Timetable') 
r.geometry("400x300")
Label(r, text='Choose Preferred Mode').grid(row=1)
var1 = IntVar() 
Checkbutton(r, text='Go Offline', variable=var1).grid(row=3, sticky=W) 
var2 = IntVar() 
Checkbutton(r, text='Go Online', variable=var2).grid(row=4, sticky=W)
Label(r, text='Enter API key').grid(row=5)
e1 = Entry(r) 
e1.grid(row=5, column=1) 
ourMessage ='Make sure you are online for online mode!'
messageVar = Message(r, text = ourMessage)
messageVar.config(bg='lightgreen')
messageVar.grid(row=6)
Label(r, text='       ').grid(row=7)
# Get majorlist from last file code
def new_winF():
    newwin = Toplevel(r)
    newwin.geometry("700x400")
    display = Label(newwin, text="Distance Matrix Formation !")
    display.grid(row=0) 
    Label(newwin, text='List of villages for travelling').grid(row=1)
    scrollbar = Scrollbar(newwin)
    Label(newwin, text=' ').grid(row=2)
    scrollbar.grid(row=4)
    mylist = Listbox(newwin, yscrollcommand = scrollbar.set,width=len(majorlist) ) 
    for line in range(len(majorlist)): 
       mylist.insert(END, majorlist[line]) 
    mylist.grid(row=5)
    scrollbar.config( command = mylist.yview , width='500') 
    Label(newwin, text=' ').grid(row=6)
    Label(newwin, text=' ').grid(row=7)
    Label(newwin, text=' ').grid(row=8)
timek()
def new_win():
    n = Toplevel(r)
    n.geometry("700x300")
    display = Label(n, text="Time Table is !")
    display.grid(row=0) 
    scrollbar = Scrollbar(n)
    Label(n, text=' ').grid(row=2)
    scrollbar.grid(row=4)
    mylist = Listbox(n, yscrollcommand = scrollbar.set ,width=len(lj)) 
    for line in range(len(lj)): 
       mylist.insert(END, lj[line]) 
    mylist.grid(row=5)
    scrollbar.config( command = mylist.yview )
    

button1 =Button(r, text ="See list of villages", command =new_winF).grid(row=10,columns=1)
button2 =Button(r, text ="Checkout Timetable", command =new_win).grid(row=11,columns=4)

r.mainloop()



