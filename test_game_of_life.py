import game_of_life

def test_empty_generation():
    # GIVEN
    initial_generation = [
        '...',
        '...',
        '...'
    ]
    # WHEN
    actual = game_of_life.get_next_generation(
        initial_generation
    )
    # THEN
    assert actual == [
        '...',
        '...',
        '...'
    ]
    
def test_with_one_cell_generation():
    # GIVEN
    initial_generation = [
        '...',
        '.*.',
        '...'
    ]
    # WHEN
    actual = game_of_life.get_next_generation(
        initial_generation
    )
    # THEN
    assert actual == [
        '...',
        '...',
        '...'
    ]
    
def test_with_three_cells_neighbours():
    # GIVEN
    initial_generation = [
        '...',
        '.*.',
        '.**'
    ]
    # WHEN
    actual = game_of_life.get_next_generation(
        initial_generation
    )
    # THEN
    assert actual == [
        '...',
        '.**',
        '.**'
    ]
    
def test_is_cell_dead():
     # GIVEN
    initial_generation = [
        '.',
    ]
    cell_x = 0
    cell_y = 0
    # WHEN
    actual = game_of_life.is_alive_cell(
        cell_x, cell_y, initial_generation
    )
    # THEN
    assert actual == False
    
def test_is_cell_alive():
     # GIVEN
    initial_generation = [
        '*',
    ]
    cell_x = 0
    cell_y = 0
    # WHEN
    actual = game_of_life.is_alive_cell(
        cell_x, cell_y, initial_generation
    )
    # THEN
    assert actual == True
    
def test_alive_neigbhours():
    # GIVEN
    initial_generation = [
        '*..',
        '.*.',
        '...'
    ]
    cell_x = 1
    cell_y = 1
    # WHEN
    actual = game_of_life.alive_neigbhours(
        cell_x,
        cell_y,
        initial_generation
    )
    # THEN
    assert actual == 1