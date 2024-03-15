def get_next_generation(initial_generation):
    
    if 3 == (
        is_alive(0,0, initial_generation) + is_alive(0,1, initial_generation) + is_alive(0,2, initial_generation) 
        + is_alive(1,0, initial_generation) + is_alive(1,2, initial_generation) 
        + is_alive(2,0, initial_generation) + is_alive(2,1, initial_generation) + is_alive(2,2, initial_generation)
    ):
        return set_cell(1, 1, initial_generation, "o")
    
    if 3 == (
        is_alive(0,0, initial_generation) + is_alive(0,1, initial_generation)
        + is_alive(1,1, initial_generation)
        + is_alive(2,0, initial_generation) + is_alive(2,1, initial_generation)
    ):
        return set_cell(1, 0, initial_generation, "o")

    return set_cell(1, 1, initial_generation, ".")

def is_alive(row_number, col_number, cells):
    return cells[row_number][col_number] == "o" 

def set_cell(row_number, col_number, cells, value):
    cellsList = list(cells[row_number])
    cellsList[col_number] = value
    cells[row_number] = ''.join(cellsList)
    return cells
