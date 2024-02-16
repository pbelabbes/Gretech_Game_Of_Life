def get_next_generation(initial_generation):
    return [
        '...',
        '...',
        '...'
    ]

def alive_neigbhours(cell_x, cell_y, generation):
    alive_neigbhours = 0
    
    alive_neigbhours += is_alive_cell(cell_x - 1, cell_y - 1, generation)
                
    return alive_neigbhours

def is_alive_cell(cell_x, cell_y, generation):
    return generation[cell_y][cell_x] == '*'