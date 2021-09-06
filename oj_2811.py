def determine_press(puzzle_, press_, r, c):
    """
    puzzle_ is a grid of size 5x6
    press_ is a grid of size 6x8
    press_[1:][1:7] correspond to puzzle_
    this function determines if row r and column
    c of press_ should be pressed
    which correspond to (r-1,c-1) of puzzle
    """
    puzzle_r = r-1
    puzzle_c = c-1
    return (puzzle_[puzzle_r-1][puzzle_c] + press_[r-2][c] +\
            + press_[r-1][c] + press_[r-1][c-1] +\
            press_[r-1][c+1]) % 2

def binary_inc(grid):
    lst = grid[1]
    inc_bit = 1
    idx = 1
    while idx < len(lst)-1:
        if inc_bit and lst[idx]:
            lst[idx] = 0
        elif inc_bit and not lst[idx]:
            lst[idx] = 1
            inc_bit = 0
            break
        idx += 1

def guess(puzzle_, press_):
    # starting from row 2, loop through each row
    # of press to determine the press
    r = 2
    while r < 6:
        for c in range(1,7):
            press_[r][c] = determine_press(puzzle_,press_,r,c)
        r += 1
    return not any([determine_press(puzzle_,press_,r,c) for c in range(1,7)])


def print_solution(press_):
    for r in range(1,6):
        row = " ".join([str(press_[r][c]) for c in range(1,7)])
        print(row)



def enumerate(puzzle_):
    press = [[0 for i in range(8)] for j in range(6)]
    found = False
    for _ in range(2**6):
        found = guess(puzzle_, press)
        if found:
            print_solution(press)
            break
        binary_inc(press)



if __name__ == "__main__":
    puzzle = []
    for k in range(5):
        x = input()
        row = [int(num) for num in x.split()]
        puzzle.append(row)
    enumerate(puzzle)

