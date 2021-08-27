# A famous chess grandmaster was analysing one of his games in his head and he suddenly forgot his positions for two important pieces.
# However, he is sure about some facts:
# 1. The locations of first piece on board is (x1,y1) and xl1<=x1<=xr1, yl1<=y1<=yr1
# 2. The locations of second piece on board is (x2,y2) and xl2<=x2<=xr2, yl2<=y2<=yr2
# 3. The chessboard cells corresponding to the pieces are of same color
# How many placements of these two pieces are possible if he remembers correctly?

# Sample Input - 1 1 1 1 2 2 2 2
# Sample Output - 1 [(1,1),(2,2)]

# Sample Input - 1 1 1 1 1 1 2 2
# Sample Output - 0 (Different Color)

# Sample Input - 1 2 1 2 3 4 3 4
# Sample Output - 8

xl1 = 1
xr1 = 2
yl1 = 1
yr1 = 2

xl2 = 3
xr2 = 4
yl2 = 3
yr2 = 4

def square_color(x,y):
    if (x+y)%2==0:
        return 'Black'
    else:
        return 'White'

def determine_places():
    first_piece = []
    second_piece = []
    for i in range(xl1,xr1+1):
        for j in range(yl1,yr1+1):
            first_piece.append(square_color(i,j))
    for i in range(xl2,xr2+1):
        for j in range(yl2,yr2+1):
            second_piece.append(square_color(i,j))

    total_count = first_piece.count('White')*second_piece.count('White') + first_piece.count('Black')*second_piece.count('Black')
    return total_count

print(determine_places())

# [Done] exited with code=0 in 0.264 seconds