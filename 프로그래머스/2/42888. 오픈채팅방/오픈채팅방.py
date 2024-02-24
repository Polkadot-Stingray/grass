def solution(record):
    answer = []
    dic=dict()
    for string in record:
        array=string.split()
        if len(array)==3:
    	    dic[array[1]]=array[2]
    
    for string in record:
        array=string.split()
        if array[0]=="Enter":
            answer.append("%s님이 들어왔습니다."%dic[array[1]])
        elif array[0]=="Leave":
            answer.append("%s님이 나갔습니다."%dic[array[1]])
        
    return answer