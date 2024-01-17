class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        """
        Alternative double pass:
        * once to assess each, mark it in a way that makes it known what next state is
        * assess each but ignore whatever the marking was
        * second pass updates based on marking
        """
        def getValue(posx,posy):
            if posx in range(len(board)) and posy in range(len(board[0])):
                return board[posx][posy]
            else:
                return 0

        def getNeighborValues(posx,posy):
            sum=0
            for x in [posx-1,posx,posx+1]:
                for y in [posy-1,posy,posy+1]:
                    if x==posx and y==posy:
                        continue
                    sum+=getValue(x,y)
            return sum
        out=[]
        ROWS,COLS=len(board),len(board[0])
        for x in range(ROWS):
            out.append([])
            for y in range(COLS):
                num = getNeighborValues(x,y)
                if board[x][y]==1:
                    if num<2:
                        out[x].append(0)
                    elif num==2 or num==3:
                        out[x].append(1)
                    elif num>3:
                        out[x].append(0) 
                else:
                    if num==3:
                        out[x].append(1)
                    else:
                        out[x].append(0)             
        for x in range(ROWS):
            for y in range(COLS):
                board[x][y]=out[x][y]
        #print(board)