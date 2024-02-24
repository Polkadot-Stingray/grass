from queue import PriorityQueue
N=int(input())
plusPq=PriorityQueue()
minusPq=PriorityQueue()
zerocount=0
onecount=0

for i in range(N):
    data=int(input())
    if data>1:
        plusPq.put(data*-1)
    elif data==1:
        onecount+=1
    elif data==0:
        zerocount+=1
    else:
        minusPq.put(data)

total=0

while plusPq.qsize()>1: #양수처리
    data1=plusPq.get()
    data2=plusPq.get()
    total+=data1*data2
if plusPq.qsize()==1:
    total+=plusPq.get()*(-1)

while minusPq.qsize()>1:
    data1=minusPq.get()
    data2=minusPq.get()
    total+=data1*data2
    
if minusPq.qsize()==1:
    if zerocount==0:
        total+=minusPq.get()
total+=onecount
print(total)