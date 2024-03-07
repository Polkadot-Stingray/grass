def time_arrange(time, term):
    hour=int(time[0:2])
    minute=int(time[3:])
    minute+=term
    
    if minute>=60:
        hour+=1
        minute-=60
            
    elif minute<0:
        hour-=1
        minute+=60
            
    if hour<10:
        hour='0'+str(hour)
    else:
        hour=str(hour)
                
    if minute<10:
        minute='0'+str(minute)
    else:
        minute=str(minute)
            
    return hour+":"+minute
    
def solution(n, t, m, timetable):
    answer = ''
    early=0
    ttak=0
    late=0
    for i in timetable:
        if(i<"09:00"):
            early+=1
        if(i>"09:00"):
            late+=1
        else:
            ttak+=1
    if n==1:
        if early<m-1:
            return "09:00"
        elif early==m-1:
            if "09:00" in timetable:
                return "08:59"
            else:
                return "09:00"
        else:
            timetable.sort()
            time=""
            while(len(timetable)>=m):
                time=timetable.pop()
            time=time_arrange(time, -1)
            return time
    else:
        timetable.sort()
        time="09:00"
        last=""
        for i in range(n-1):
            count=0
            delete=[]
            for j in timetable:
                if j<=time and count<m:
                    delete.append(j)
                    count+=1
            for k in delete:
                last=k
                timetable.remove(k)
            time=time_arrange(time, t)
        print(time)
        if len(timetable)==0:
            time=time_arrange(last, -1)
        else:    
            count=0
            for i in timetable:
                if i<=time and count<m:
                    last=i
                    count+=1
            if count>=m:
                time=time_arrange(last, -1)
            
    return time