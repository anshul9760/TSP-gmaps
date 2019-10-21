# The bilow line has tsp solved ,atrix just to show example
s=" 0 -> 13 -> 30 -> 46 -> 43 -> 44 -> 32 -> 45 -> 33 -> 42 -> 29 -> 41 -> 28 -> 58 -> 68 -> 59 -> 60 -> 61 -> 57 -> 56 -> 67 -> 84 -> 71 -> 72 -> 77 -> 78 -> 66 -> 55 -> 35 -> 49 -> 39 -> 25 -> 26 -> 16 -> 17 -> 11 -> 4 -> 19 -> 18 -> 10 -> 20 -> 54 -> 53 -> 52 -> 50 -> 51 -> 36 -> 9 -> 21 -> 22 -> 5 -> 6 -> 7 -> 8 -> 37 -> 83 -> 79 -> 91 -> 88 -> 75 -> 87 -> 89 -> 109 -> 110 -> 101 -> 100 -> 65 -> 38 -> 64 -> 62 -> 74 -> 86 -> 85 -> 97 -> 103 -> 73 -> 96 -> 102 -> 105 -> 63 -> 124 -> 131 -> 130 -> 122 -> 24 -> 133 -> 132 -> 123 -> 114 -> 113 -> 104 -> 48 -> 95 -> 70 -> 92 -> 82 -> 93 -> 81 -> 69 -> 80 -> 94 -> 23 -> 119 -> 111 -> 126 -> 138 -> 139 -> 120 -> 125 -> 128 -> 118 -> 117 -> 121 -> 137 -> 136 -> 135 -> 134 -> 129 -> 115 -> 112 -> 98 -> 99 -> 127 -> 107 -> 108 -> 116 -> 106 -> 90 -> 76 -> 40 -> 34 -> 15 -> 27 -> 14 -> 12 -> 2 -> 3 -> 47 -> 1 -> 31 -> 0"

import pandas as pd
import datetime

temppath=r# address same as before
majorlist=[]
filename1=temppath+ #attach csv file here
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

for i in s:
    print(i,majorlist[int(i)])

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

x[1][0:10]

l[0:10]

majorlist[13]

majorlist[2]

filename=r# address of final file

f=open(filename,'w') #writing csv

def timek():  #Timetable function
    day=1
    z='DAY'
    r=420     #Starting at 8AM (24*60-8*60)
    print("Day ",day)
    f.write('"' + z + '","'+ str(day) + '"\n')
    for i,e,k in zip(x[1],l,timespent):
        if r<limit:
            zk=round((r/60),2)
            if zk<12:
                a='AM'
                time=str(datetime.timedelta(hours=zk)).rsplit(':', 1)[0]
                f.write('"' + time + '","'+ a + '","' + majorlist[int(i)] + '"\n')
                print(time," AM:",majorlist[int(i)])
            else:
                a='PM'
                time=str(datetime.timedelta(hours=(zk-12))).rsplit(':', 1)[0]
                f.write('"' + time + '","'+ a + '","' + majorlist[int(i)] + '"\n')
                print(time," PM:",majorlist[int(i)])
            r=r+e+k
        else:
            r=420
            day+=1
            print("Day ",day)
            f.write('"' + z + '","'+ str(day) + '"\n')
            zk=round((r/60),2)
            if zk<12:
                a='AM'
                time=str(datetime.timedelta(hours=zk)).rsplit(':', 1)[0]
                f.write('"' + time + '","'+ a + '","' + majorlist[int(i)] + '"\n')
                print(time," AM:",majorlist[int(i)])
            else:
                a='PM'
                time=str(datetime.timedelta(hours=(zk-12))).rsplit(':', 1)[0]
                f.write('"' + time + '","'+ a + '","' + majorlist[int(i)] + '"\n')
                print(time," PM:",majorlist[int(i)])
            r=r+e+k
timek()

f.close()

