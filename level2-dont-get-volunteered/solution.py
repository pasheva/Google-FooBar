"""
2.1 Don't Get Volunteered!

The board for source 0.
The position of the horse has
also been denoted with 0.

The board steps away from the horse 1,2, etc.
are generated one by one. First, the blocks
which are 1 step away from the horse are found.
The the block which are 1 step away from the "1 step" block
,meaning 2 steps away from the horse and so on.

-------------------------
| 0| 3| 2| 3| 2| 3| 4| 5|
-------------------------
| 3| 4| 1| 2| 3| 4| 3| 4|
-------------------------
| 2| 1| 4| 3| 2| 3| 4| 5|
-------------------------
| 3| 2| 3| 2| 3| 4| 3| 4|
-------------------------
| 2| 3| 2| 3| 4| 3| 4| 5|
-------------------------
| 3| 4| 3| 4| 3| 4| 5| 4|
-------------------------
| 4| 3| 4| 3| 4| 5| 4| 5|
-------------------------
| 5| 4| 5| 4| 5| 4| 5| 6|
-------------------------

"""

def solution(src,dest):

    #Creating a list with the board
    board_dist = [[-1] * 8 for i in range(8)]

    #Get source and destination positions on the board (num - ((num//8)*8))
    x_cor_src = src // 8
    y_cor_src = src - (x_cor_src * 8)

    x_cor_dest = dest // 8
    y_cor_dest = dest - (x_cor_dest * 8)

    #Setting the position of the horse(source)
    board_dist[x_cor_src][y_cor_src] = 0

    #The number of blocks which positions from the horse have been generated.
    blocks_generated = 1
    #The levels are the steps away from the horse. 1 step, 2 steps, 3 steps... etc.
    level = 0
    #while all the blocks with -1 have not been filled.
    while blocks_generated != 64:
        for r in range(8):
            up_turn = r - 1
            down_turn = r + 1
            up = r - 2
            down = r + 2
            for c in range(8):
                left_turn = c -1
                right_turn = c + 1
                right = c + 2
                left = c - 2
                if board_dist[r][c] == level:
                    if(up >= 0) and (left_turn >= 0):
                        if board_dist[up][left_turn] == -1:
                            board_dist[up][left_turn] = (level + 1)
                            blocks_generated += 1
                    if(up >= 0) and (right_turn <= 7):
                        if board_dist[up][right_turn] == -1:
                            board_dist[up][right_turn] = (level + 1)
                            blocks_generated += 1
                    if (right <= 7) and (up_turn >= 0):
                        if board_dist[up_turn][right] == -1:
                            board_dist[up_turn][right] = (level + 1)
                            blocks_generated += 1
                    if (right <= 7) and (down_turn <= 7):
                        if board_dist[down_turn][right] == -1:
                            board_dist[down_turn][right] = (level + 1)
                            blocks_generated += 1
                    if (down <= 7) and (left_turn >= 0):
                        if board_dist[down][left_turn] == -1:
                            board_dist[down][left_turn] = (level + 1)
                            blocks_generated += 1
                    if (down <= 7) and (right_turn <= 7):
                        if board_dist[down][right_turn] == -1:
                            board_dist[down][right_turn] = (level + 1)
                            blocks_generated += 1
                    if (left >= 0) and (up_turn >= 0):
                        if board_dist[up_turn][left] == -1:
                            board_dist[up_turn][left] = (level + 1)
                            blocks_generated += 1
                    if (left >= 0) and (down_turn <= 7):
                        if board_dist[down_turn][left] == -1:
                            board_dist[down_turn][left] = (level + 1)
                            blocks_generated += 1
        level += 1

    #Answer
    return board_dist[x_cor_dest][y_cor_dest]





