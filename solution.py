assignments = []





def assign_value(values, box, value):
    """
    Please use this function to update your values dictionary!
    Assigns a value to a given box. If it updates the board record it.
    """
    values[box] = value
    if len(value) == 1:
        assignments.append(values.copy())
    return values

def naked_twins(values):
    """Eliminate values using the naked twins strategy.
    Args:
        values(dict): a dictionary of the form {'box_name': '123456789', ...}

    Returns:
        the values dictionary with the naked twins eliminated from peers.
    """

    # Find all instances of naked twins
    # Eliminate the naked twins as possibilities for their peers
    for unit in unitlist:
        naked_twins_boxes = [[a, b] for a in unit for b in unit if a != b and len(values[a]) == 2 and values[a] == values[b]]
        for twin in naked_twins_boxes:
            for digit in values[twin[0]]:
                for b in unit:
                    if b not in twin:
                        values[b] = values[b].replace(digit, "")
    return values

def cross(A, B):
    "Cross product of elements in A and elements in B."
    res = [a+b for a in A for b in B]
    return res

def grid_values(grid):
    """
    Convert grid into a dict of {square: char} with '123456789' for empties.
    Args:
        grid(string) - A grid in string form.
    Returns:
        A grid in dictionary form
            Keys: The boxes, e.g., 'A1'
            Values: The value in each box, e.g., '8'. If the box has no value, then the value will be '123456789'.
    """
    chars = []
    digits = "123456789"
    for c in grid:
        if c in digits:
            chars.append(c)
        if (c == "."):
            chars.append(digits)
    assert(len(chars) == 81)
    res = dict(zip(boxes, chars))
    return res
    

def display(values):
    """
    Display the values as a 2-D grid.
    Args:
        values(dict): The sudoku in dictionary form
    """
    width = 1+max(len(values[s]) for s in boxes)
    line = '+'.join(['-'*(width*3)]*3)
    for r in rows:
        print(''.join(values[r+c].center(width)+('|' if c in '36' else '')
                      for c in cols))
        if r in 'CF': print(line)
    print

def eliminate(values):
    solved_boxes = [b for b in boxes if len(values[b]) == 1]
    for b in solved_boxes:
        digit = values[b]
        for p in peers[b]:
            values[p] = values[p].replace(digit, "")
    return values

def only_choice(values):
    for unit in unitlist:
        for digit in digits:
            b = [b for b in unit if digit in values[b]]
            if (len(b) == 1):
                values[b[0]] = digit
    return values

def reduce_puzzle(values):
    solved_boxes = [b for b in values.keys() if len(values[b]) == 1]
    stalled = False
    while not stalled:
        solved_boxes_before = [b for b in values.keys() if len(values[b]) == 1]
        # normal eliminate algorithm
        eliminate(values)

        # nake twins eliminate algorithm
        naked_twins(values)
        
        # only choice algorithm
        only_choice(values)

        solved_boxes_after = [b for b in values.keys() if len(values[b]) == 1]
        # if sudoku state doesn't change, it has been stalled, break the loop
        stalled = (solved_boxes_after == solved_boxes_before)
        if (len([b for b in values.keys() if len(values[b]) == 0])):
            return False
    return values

def search(values):
    # reduce the puzzle 
    values = reduce_puzzle(values)

    if (values == False):
        return False

    # return completed sudoku
    if (all(len(values[b]) == 1 for b in boxes)):
        return values

    # choose one of the unfilled squares with the fewest possibilities
    l, b = min((len(values[b]), b) for b in boxes if len(values[b]) > 1)

    # use recursion to solve each one of the resulting sudoku, if one returns a completed sudoku, return that one
    for digit in values[b]:
        new_values = values.copy()
        new_values[b] = digit
        res = search(new_values)
        if res:
            return res

    

def solve(grid):
    """
    Find the solution to a Sudoku grid.
    Args:
        grid(string): a string representing a sudoku grid.
            Example: '2.............62....1....7...6..8...3...9...7...6..4...4....8....52.............3'
    Returns:
        The dictionary representation of the final sudoku grid. False if no solution exists.
    """
    values = grid_values(grid)
    res = search(values)
    return res



rows = "ABCDEFGHI"
cols = "123456789"
digits = "123456789"
boxes = cross(rows, cols)

row_units = [cross(r, cols) for r in rows]
col_units = [cross(rows, c) for c in cols]
sqr_units = [cross(a, b) for a in ('ABC', 'DEF', 'GHI') for b in ('123', '456', '789')]
# 2 diagonal units
dia_unit1 = [a + b for a in rows for b in cols if ord(a) - ord(b) == 16]
dia_unit2 = [a + b for a in rows for b in cols if ord(a) + ord(b) == 122]
dia_units = [dia_unit1, dia_unit2]

unitlist = row_units + col_units + sqr_units + dia_units
units = dict((s, [u for u in unitlist if s in u]) for s in boxes)
peers = dict((s, set(sum(units[s], [])) - set([s])) for s in boxes)


if __name__ == '__main__':
    diag_sudoku_grid = '2.............62....1....7...6..8...3...9...7...6..4...4....8....52.............3'
    display(solve(diag_sudoku_grid))

    try:
        from visualize import visualize_assignments
        visualize_assignments(assignments)

    except SystemExit:
        pass
    except:
        print('We could not visualize your board due to a pygame issue. Not a problem! It is not a requirement.')



