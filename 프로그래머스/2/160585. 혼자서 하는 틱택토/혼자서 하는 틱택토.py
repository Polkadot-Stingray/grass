def solution(board):
    answer = 1
    FirstWin=False
    Ocount=0
    Xcount=0
    for i in range(3):
        for j in range(3):
            if board[i][j]=='O':
                Ocount+=1
            elif board[i][j]=='X':
                Xcount+=1
    
    for i in range(3):
        if board[i][0]==board[i][1] and board[i][1]==board[i][2] and board[i][0]=='O':
            FirstWin=True
        if board[0][i]==board[1][i] and board[0][i]==board[2][i] and board[0][i]=='O':
            FirstWin=True
    if board[0][0]==board[1][1] and board[1][1]==board[2][2] and board[0][0]=='O':
        FirstWin=True
    elif board[2][0]==board[1][1] and board[1][1]==board[0][2] and board[1][1]=='O':
        FirstWin=True
    print(FirstWin)
    
    for i in range(3):
        if board[i][0]==board[i][1] and board[i][1]==board[i][2] and board[i][0]=='X':
            if FirstWin or Xcount!=Ocount:
                print('a')
                return 0
        if board[0][i]==board[1][i] and board[0][i]==board[2][i] and board[0][i]=='X':
            if FirstWin or Xcount!=Ocount:
                print('b')
                return 0
    if board[0][0]==board[1][1] and board[1][1]==board[2][2] and board[0][0]=='X':
        if FirstWin or Xcount!=Ocount:
            print('c')
            return 0
    elif board[2][0]==board[1][1] and board[1][1]==board[0][2] and board[1][1]=='X':
        if FirstWin or Xcount!=Ocount:
            print('d')
            return 0
        
    if Xcount>Ocount or Ocount>Xcount+1:
        print('e')
        return 0
    
    if FirstWin and Ocount!=Xcount+1:
        print('f')
        return 0
    
    return answer