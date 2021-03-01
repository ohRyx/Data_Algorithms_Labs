# this function checks if a queen can be placed in location (col,row)
def isValid(col,row,chessBoard):
    for x in range(chessBoard):
        print(chessBoard[x])

# initialize chessboard
N = 8
chessBoard = []
for i in range(N):
  chessBoard.append([])
  for j in range(N):
    chessBoard[i].append(0)

# place a queen in the upper left corner of the board
chessBoard[1][1]=1
chessBoard[0][4]=1
chessBoard[2][6]=1

columnIndex = int(input("Enter a column index:\n"))
rowIndex = int(input("Enter a row index:\n"))

print("Placing a queen at column", columnIndex,"row", rowIndex,":", isValid(columnIndex,rowIndex,chessBoard))
print(chessBoard)