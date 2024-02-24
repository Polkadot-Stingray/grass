
def solution(arr):
    answer = [0, 0]
    size=len(arr)
    def is_one(size, x, y):
        start=arr[x][y]
        for i in range(x, x+size):
            for j in range(y, y+size):
                if arr[i][j]!=start:
                    return False
        return True
    def papercut(size, x, y):
        if is_one(size,x,y):
            answer[arr[x][y]]+=1
        else:
            size//=2
            for i in range(2):
                for j in range(2):
                    papercut(size, x+size*i, y+size*j)
    papercut(size, 0, 0)
    return answer