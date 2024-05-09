def check_col():
    first_list = [last_row, last_row + 1, last_row + 2, last_row + 3]
    second_list = [last_row - 1, last_row, last_row , last_row + 2]
    third_list = [last_row - 2, last_row - 1, last_row , last_row + 1]
    fourth_list = [last_row - 3, last_row - 2, last_row - 1 , last_row]
    if(first_list[0] >= 0 and first_list[0] < 6 and first_list[3] >= 0 and first_list[3] < 6):
        one = grid[first_list[0]][last_col]
        two = grid[first_list[1]][last_col]
        three = grid[first_list[2]][last_col]
        four = grid[first_list[3]][last_col]
        if one.__eq__(two) and two.__eq__(three) and three.__eq__(four):
            return True

    if(second_list[ 0] >=0 and second_list[0] <6 and second_list[3] >= 0 and second_list[3] < 6):
        one = grid[second_list[0]][last_col]
        two = grid[second_list[1]][last_col]
        three = grid[second_list[2]][last_col]
        four = grid[second_list[3]][last_col]
        if one.__eq__(two) and two.__eq__(three) and three.__eq__(four):
            return True

    if(third_list[ 0] >=0 and third_list[0] <6 and third_list[3] >= 0 and third_list[3] < 6):
        one = grid[third_list[0]][last_col]
        two = grid[third_list[1]][last_col]
        three = grid[third_list[2]][last_col]
        four = grid[third_list[3]][last_col]
        if one.__eq__(two) and two.__eq__(three) and three.__eq__(four):
            return True
 
    if(fourth_list[ 0] >=0 and fourth_list[0] <6 and fourth_list[3] >= 0 and fourth_list[3] < 6):
        one = grid[fourth_list[0]][last_col]
        two = grid[fourth_list[1]][last_col]
        three = grid[fourth_list[2]][last_col]
        four = grid[fourth_list[3]][last_col]
        if one.__eq__(two) and two.__eq__(three) and three.__eq__(four):
            return True
    return False

def check_left_diag():
    first_list_row = [last_col, last_col + 1, last_col + 2, last_col + 3]
    first_list_col = [last_row, last_row + 1, last_row + 2, last_row + 3]
    second_list_row = [last_col - 1, last_col, last_col + 1, last_col + 2]
    second_list_col = [last_row - 1, last_row, last_row + 1, last_row + 2]
    third_list_row = [last_col - 2, last_col - 1, last_col , last_col + 1]
    third_list_col = [last_row - 2, last_row - 1, last_row , last_row + 1]
    fourth_list_row = [last_col - 3, last_col - 2, last_col - 1 , last_col]
    fourth_list_col = [last_row - 3, last_row - 2, last_row - 1 , last_row]
    if(first_list_row[0] >= 0 and first_list_row[0] < 7 and first_list_row[3] >= 0 and first_list_row[3] < 7):
        if(first_list_col[0] >= 0 and first_list_col[0] < 6 and first_list_col[3] >= 0 and first_list_col[3] < 6):
            one = grid[first_list_col[0]][first_list_row[0]]
            two = grid[first_list_col[1]][first_list_row[1]]
            three = grid[first_list_col[2]][first_list_row[2]]
            four = grid[first_list_col[3]][first_list_row[3]]
            if one.__eq__(two) and two.__eq__(three) and three.__eq__(four):
                return True
    if (second_list_col[0] >= 0 and second_list_col[0] < 6 and second_list_col[3] >= 6 and second_list_col[3] < 6):
        if(second_list_row[0] >= 0 and second_list_row[0] < 7 and second_list_row[3] >= 0 and second_list_row[3] < 7):
            one = grid[second_list_col[0]][second_list_row[0]]
            two = grid[second_list_col[1]][second_list_row[1]]
            three = grid[second_list_col[2]][second_list_row[2]]
            four = grid[second_list_col[3]][second_list_row[3]]
            if one.__eq__(two) and two.__eq__(three) and three.__eq__(four):
                return True
   
    if(third_list_row[ 0] >=0 and third_list_row[0] <7 and third_list_row[3] >= 0 and third_list_row[3] < 7):
        if(third_list_col[ 0] >=0 and third_list_col[0] <6 and third_list_col[3] >= 0 and third_list_col[3] < 6):
            one = grid[third_list_col[0]][third_list_row[0]]
            two = grid[third_list_col[1]][third_list_row[1]]
            three = grid[third_list_col[2]][third_list_row[2]]
            four = grid[third_list_col[3]][third_list_row[3]]
            if one.__eq__(two) and two.__eq__(three) and three.__eq__(four):
                return True
    if(fourth_list_row[ 0] >=0 and fourth_list_row[0] <7 and fourth_list_row[3] >= 0 and fourth_list_row[3] < 7):
        if(fourth_list_col[ 0] >=0 and fourth_list_col[0] <6 and fourth_list_col[3] >= 0 and fourth_list_col[3] < 6):
            one = grid[fourth_list_col[0]][fourth_list_row[0]]
            two = grid[fourth_list_col[1]][fourth_list_row[1]]
            three = grid[fourth_list_col[2]][fourth_list_row[2]]
            four = grid[fourth_list_col[3]][fourth_list_row[3]]
            if one.__eq__(two) and two.__eq__(three) and three.__eq__(four):
                return True
    return False

def check_right_diag():
    first_list_row = [last_col, last_col - 1, last_col - 2, last_col - 3]
    first_list_col = [last_row, last_row + 1, last_row + 2, last_row + 3]
    second_list_row = [last_col + 1, last_col, last_col - 1, last_col - 2]
    second_list_col = [last_row - 1, last_row, last_row + 1, last_row + 2]
    third_list_row = [last_col + 2, last_col + 1, last_col , last_col - 1]
    third_list_col = [last_row - 2, last_row - 1, last_row , last_row + 1]
    fourth_list_row = [last_col + 3, last_col + 2, last_col + 1 , last_col]
    fourth_list_col = [last_row - 3, last_row - 2, last_row - 1 , last_row]
    if(first_list_row[0] >= 0 and first_list_row[0] < 7 and first_list_row[3] >= 0 and first_list_row[3] < 7):
        if(first_list_col[0] >= 0 and first_list_col[0] < 6 and first_list_col[3] >= 0 and first_list_col[3] < 6):
            one = grid[first_list_col[0]][first_list_row[0]]
            two = grid[first_list_col[1]][first_list_row[1]]
            three = grid[first_list_col[2]][first_list_row[2]]
            four = grid[first_list_col[3]][first_list_row[3]]
            if one.__eq__(two) and two.__eq__(three) and three.__eq__(four):
                return True
    if (second_list_col[0] >= 0 and second_list_col[0] < 6 and second_list_col[3] >= 0 and second_list_col[3] < 6):
        if(second_list_row[0] >= 0 and second_list_row[0] < 7 and second_list_row[3] >= 0 and second_list_row[3] < 7):
            one = grid[second_list_col[0]][second_list_row[0]]
            two = grid[second_list_col[1]][second_list_row[1]]
            three = grid[second_list_col[2]][second_list_row[2]]
            four = grid[second_list_col[3]][second_list_row[3]]
            if one.__eq__(two) and two.__eq__(three) and three.__eq__(four):
                return True
   
    if(third_list_row[ 0] >=0 and third_list_row[0] <7 and third_list_row[3] >= 0 and third_list_row[3] < 7):
        if(third_list_col[ 0] >=0 and third_list_col[0] <6 and third_list_col[3] >= 0 and third_list_col[3] < 6):
            one = grid[third_list_col[0]][third_list_row[0]]
            two = grid[third_list_col[1]][third_list_row[1]]
            three = grid[third_list_col[2]][third_list_row[2]]
            four = grid[third_list_col[3]][third_list_row[3]]
            if one.__eq__(two) and two.__eq__(three) and three.__eq__(four):
                return True
    if(fourth_list_row[ 0] >=0 and fourth_list_row[0] <7 and fourth_list_row[3] >= 0 and fourth_list_row[3] < 7):
        if(fourth_list_col[ 0] >=0 and fourth_list_col[0] <6 and fourth_list_col[3] >= 0 and fourth_list_col[3] < 6):
            one = grid[fourth_list_col[0]][fourth_list_row[0]]
            two = grid[fourth_list_col[1]][fourth_list_row[1]]
            three = grid[fourth_list_col[2]][fourth_list_row[2]]
            four = grid[fourth_list_col[3]][fourth_list_row[3]]
            if one.__eq__(two) and two.__eq__(three) and three.__eq__(four):
                return True
    return False